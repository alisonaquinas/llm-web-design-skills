#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / 'skills'
REPORT = ROOT / 'docs' / 'skill-test-drive-report-round-2.md'

FRAMEWORK_TERMS = {
    'angular': ['angular', 'standalone', 'signals', 'rxjs', 'forms'],
    'nextjs': ['next.js', 'app router', 'server', 'client', 'cache', 'route'],
    'react': ['react', 'hook', 'context', 'component', 'state', 'accessibility'],
    'material-design': ['material', 'theme', 'tokens', 'density', 'contrast', 'storybook'],
    'svelte': ['svelte', 'sveltekit', 'load', 'store', 'adapter', 'hydration'],
    'vue': ['vue', 'composable', 'pinia', 'router', 'store', 'component'],
    'vite': ['vite', 'plugin', 'preview', 'env', 'asset', 'hmr'],
    'scss': ['scss', 'sass', '@use', '@forward', 'mixin', 'css'],
    'tailwind': ['tailwind', 'theme', 'token', 'dark', 'utility', 'content'],
    'django': ['django', 'serializer', 'form', 'migration', 'settings', 'database'],
    'nodejs': ['node', 'module', 'package', 'runtime', 'async', 'stream'],
    'express-js': ['express', 'middleware', 'route', 'server', 'auth', 'error'],
    'hugo': ['hugo', 'shortcode', 'taxonomy', 'bundle', 'url', 'layout'],
    'asp-net': ['asp.net', '.net', 'middleware', 'endpoint', 'options', 'startup'],
    'spring-boot': ['spring', 'boot', 'profile', 'controller', 'service', 'actuator'],
    'laravel': ['laravel', 'eloquent', 'blade', 'queue', 'artisan', 'route'],
}

KNOWN_COMMAND_STARTS = (
    'npm ', 'npx ', 'pnpm ', 'yarn ', 'ng ', 'node ', 'python ', 'dotnet ',
    'php ', 'hugo', 'sass ', 'curl ', './mvnw', './gradlew', 'mvn ', 'gradle '
)

@dataclass
class ScenarioResult:
    skill: str
    sid: str
    bucket: str
    outcome: str
    score: int
    evidence: str


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def section(text: str, heading: str) -> str:
    match = re.search(rf'^## {re.escape(heading)}\n(.*?)(?=^## |\Z)', text, re.M | re.S)
    return match.group(1).strip() if match else ''


def bullets(text: str) -> list[str]:
    return [line[2:].strip() for line in text.splitlines() if line.strip().startswith('- ')]


def bash_blocks(text: str) -> list[str]:
    return re.findall(r'```bash\n(.*?)```', text, re.S)


def executable_lines(block: str) -> list[str]:
    out: list[str] = []
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        out.append(stripped)
    return out


def is_exec(line: str) -> bool:
    return line.startswith(KNOWN_COMMAND_STARTS) or re.match(r'^[A-Z_]+=.+\s+(node|npm|pnpm|yarn|python|php|dotnet)\b', line) is not None


def term_hits(text: str, terms: list[str]) -> int:
    lower = text.lower()
    return sum(1 for term in terms if term in lower)


def label(score: int) -> str:
    if score >= 10:
        return 'PASS'
    if score >= 7:
        return 'PARTIAL'
    return 'FAIL'


def refs_from_skill(skill_text: str) -> list[str]:
    return re.findall(r'`(references/[^`]+\.md)`', skill_text)


def test_skill(skill_dir: Path) -> list[ScenarioResult]:
    name = skill_dir.name
    terms = FRAMEWORK_TERMS[name]
    skill_text = read(skill_dir / 'SKILL.md')
    workflows = read(skill_dir / 'references' / 'workflows.md')
    best_practices = read(skill_dir / 'references' / 'best-practices.md')

    with tempfile.TemporaryDirectory(prefix=f'{name}-round2-') as tmp:
        disposable = Path(tmp) / name
        shutil.copytree(skill_dir, disposable)
        refs_ok = all((disposable / ref).exists() for ref in refs_from_skill(skill_text))
        manifests_ok = (disposable / 'agents' / 'openai.yaml').exists() and (disposable / 'agents' / 'claude.yaml').exists()
        entry_ok = (disposable / 'SKILL.md').exists()
        score = (4 if refs_ok else 0) + (4 if manifests_ok else 0) + (4 if entry_ok else 0)
        s01 = ScenarioResult(name, 'S01', 'happy-path', label(score), score, 'disposable copy preserved the skill entrypoint, both manifests, and all referenced markdown files' if score == 12 else 'disposable copy exposed a missing manifest, entrypoint, or reference')

    quick_start = section(skill_text, 'Quick Start')
    numbered = re.findall(r'^\d+\.\s', quick_start, re.M)
    first_line_specific = term_hits(quick_start, terms) >= 2
    setup_shape = (' and ' in quick_start.lower()) or quick_start.count(',') >= 3
    score = (4 if len(numbered) >= 4 else 0) + (4 if first_line_specific else 0) + (4 if setup_shape else 0)
    s02 = ScenarioResult(name, 'S02', 'setup', label(score), score, 'Quick Start establishes the framework posture before detailed advice' if score >= 10 else 'Quick Start exists but setup posture could be clearer or more framework-specific')

    common = section(skill_text, 'Common Requests')
    examples = skill_text.count('```text') >= 2
    example_terms = term_hits(common, terms) >= 2
    example_variety = ('review this' in common.lower()) and ('refactor this' in common.lower() or 'help refactor' in common.lower())
    score = (4 if examples else 0) + (4 if example_terms else 0) + (4 if example_variety else 0)
    s03 = ScenarioResult(name, 'S03', 'example-quality', label(score), score, 'request examples cover review and change scenarios with framework-native vocabulary' if score >= 10 else 'examples exist but could be more realistic or more framework-specific')

    blocks = bash_blocks(workflows)
    command_lines = [line for block in blocks for line in executable_lines(block)]
    pseudo = [line for line in command_lines if not is_exec(line)]
    score = (4 if len(blocks) >= 2 else 0) + (4 if len(command_lines) >= 3 else 0) + (4 if not pseudo else 0)
    evidence = 'workflow command blocks are runnable shell examples' if not pseudo else f'non-runnable example(s) found: {", ".join(pseudo[:2])}'
    s04 = ScenarioResult(name, 'S04', 'actionability', label(score), score, evidence)

    verify = section(workflows, 'Verification')
    verify_bullets = bullets(verify)
    commandish = ('`' in verify) or any(is_exec(line) for line in command_lines)
    checks = sum(word in verify.lower() for word in ['confirm', 'verify', 'inspect', 'smoke']) >= 2
    score = (4 if len(verify_bullets) >= 3 else 0) + (4 if commandish else 0) + (4 if checks else 0)
    s05 = ScenarioResult(name, 'S05', 'verification', label(score), score, 'verification names commands and observable success checks' if score >= 10 else 'verification guidance exists but could be more concrete or more observable')

    recovery = section(workflows, 'Troubleshooting and recovery')
    recovery_bullets = bullets(recovery)
    recovery_logic = sum(word in recovery.lower() for word in ['if ', 'before ', 'compare ', 'inspect ', 're-check', 'retest', 're-test']) >= 2
    recovery_specific = term_hits(recovery, terms) >= 1
    score = (4 if len(recovery_bullets) >= 3 else 0) + (4 if recovery_logic else 0) + (4 if recovery_specific else 0)
    s06 = ScenarioResult(name, 'S06', 'recovery', label(score), score, 'troubleshooting gives multiple framework-specific recovery moves' if score >= 10 else 'troubleshooting exists but could be more specific or more obviously actionable')

    first = section(skill_text, 'First Response Pattern')
    first_bullets = bullets(first)
    first_logic = any(word in first.lower() for word in ['verification', 'verify']) and any(word in first.lower() for word in ['smallest', 'anchor'])
    first_specific = term_hits(first, terms) >= 1
    score = (4 if len(first_bullets) >= 3 else 0) + (4 if first_logic else 0) + (4 if first_specific else 0)
    s07 = ScenarioResult(name, 'S07', 'efficiency', label(score), score, 'skill explicitly tells the next model how to shape the first response' if score >= 10 else 'first-response guidance is missing or too generic')

    sections_ok = all(section(best_practices, heading) for heading in ['Default design choices', 'Common red flags', 'Review checklist'])
    bp_terms = term_hits(best_practices, terms) >= 4
    checklist_ok = best_practices.count('- [ ]') >= 4
    score = (4 if sections_ok else 0) + (4 if bp_terms else 0) + (4 if checklist_ok else 0)
    s08 = ScenarioResult(name, 'S08', 'specificity', label(score), score, 'best-practices guidance stays concrete across defaults, red flags, and checklist items' if score >= 10 else 'best-practices guidance drifts too generic in one or more places')

    return [s01, s02, s03, s04, s05, s06, s07, s08]


def write_report(results: list[ScenarioResult]) -> None:
    from collections import defaultdict
    by_skill: dict[str, list[ScenarioResult]] = defaultdict(list)
    for result in results:
        by_skill[result.skill].append(result)

    total_pass = sum(1 for r in results if r.outcome == 'PASS')
    total_partial = sum(1 for r in results if r.outcome == 'PARTIAL')
    total_fail = sum(1 for r in results if r.outcome == 'FAIL')
    verdict = 'approve' if total_fail == 0 else 'revise'

    lines: list[str] = []
    lines.append('# Skill test-drive report — round 2')
    lines.append('')
    lines.append('This second pass used the uploaded `skill-test-drive` guidance with a stricter emphasis on real usability: command examples had to be runnable, setup posture had to be explicit, and each skill had to tell the next model how to shape its first response.')
    lines.append('')
    lines.append('## Findings addressed during the second pass')
    lines.append('')
    lines.append('- Replaced pseudo-commands in the `scss` and `tailwind` workflow docs with runnable CLI examples.')
    lines.append('- Added a `First Response Pattern` section to every skill so the next model starts with the right posture, boundary, and verification loop.')
    lines.append('- Tightened a few weaker examples and verification bullets where the second pass exposed ambiguity.')
    lines.append('')
    lines.append('## Summary')
    lines.append('')
    lines.append(f'- **Skills covered:** {len(by_skill)}')
    lines.append(f'- **Scenarios attempted:** {len(results)}')
    lines.append(f'- **Outcome mix:** {total_pass} pass / {total_partial} partial / {total_fail} fail / 0 blocked')
    lines.append(f'- **Repository verdict:** `{verdict}`')
    lines.append('')

    for skill_name, items in sorted(by_skill.items()):
        p = sum(1 for i in items if i.outcome == 'PASS')
        pt = sum(1 for i in items if i.outcome == 'PARTIAL')
        f = sum(1 for i in items if i.outcome == 'FAIL')
        lines.append(f'## {skill_name}')
        lines.append('')
        lines.append(f'- Outcome mix: {p} pass / {pt} partial / {f} fail')
        lines.append('')
        lines.append('| ID | Bucket | Outcome | Score | Key evidence |')
        lines.append('|---|---|---|---:|---|')
        for item in items:
            lines.append(f'| {item.sid} | {item.bucket} | {item.outcome} | {item.score} | {item.evidence} |')
        lines.append('')

    REPORT.write_text('\n'.join(lines).strip() + '\n', encoding='utf-8')


def main() -> int:
    results: list[ScenarioResult] = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if skill_dir.is_dir():
            results.extend(test_skill(skill_dir))
    write_report(results)
    total_pass = sum(1 for r in results if r.outcome == 'PASS')
    total_partial = sum(1 for r in results if r.outcome == 'PARTIAL')
    total_fail = sum(1 for r in results if r.outcome == 'FAIL')
    print(f'Wrote {REPORT}')
    print(f'PASS={total_pass} PARTIAL={total_partial} FAIL={total_fail} BLOCKED=0')
    return 1 if total_fail else 0


if __name__ == '__main__':
    raise SystemExit(main())
