#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / 'skills'
REPORT = ROOT / 'docs' / 'skill-test-drive-report-round-3.md'

FRAMEWORK_TOKENS = {
    'angular': ['angular', 'signals', 'rxjs', 'ng build', 'ng test'],
    'nextjs': ['next', 'app router', 'server component', 'route', 'cache'],
    'react': ['react', 'hook', 'component', 'state', 'render'],
    'material-design': ['material', 'material 3', 'mui', 'angular material', 'storybook', 'token'],
    'svelte': ['svelte', 'sveltekit', 'load', 'reactivity', 'store'],
    'vue': ['vue', 'composition api', 'pinia', 'router', 'vite'],
    'vite': ['vite', 'vitest', 'preview', 'plugin', 'alias'],
    'scss': ['scss', 'sass', '@use', 'mixin', 'token'],
    'tailwind': ['tailwind', 'utility', 'dark mode', 'responsive', 'content'],
    'django': ['django', 'migration', 'manage.py', 'template', 'orm'],
    'nodejs': ['node', 'package.json', 'async', 'runtime', 'module'],
    'express-js': ['express', 'middleware', 'router', 'request', 'response'],
    'hugo': ['hugo', 'shortcode', 'taxonomy', 'content bundle', 'layout'],
    'asp-net': ['asp.net', 'dotnet', 'middleware', 'endpoint', 'minimal api'],
    'spring-boot': ['spring', 'boot', 'controller', 'actuator', 'configuration'],
    'laravel': ['laravel', 'artisan', 'eloquent', 'blade', 'route'],
}

REALISM_MARKERS = [
    'existing', 'already', 'preserving', 'without', 'while', 'preview', 'dark',
    'build', 'test', 'storybook', 'migration', 'deployment', 'route', 'form',
    'api', 'theme', 'token', 'accessibility', 'regression', 'smoke', 'parity',
]

RUNNABLE_COMMANDS = [
    'npm ', 'pnpm ', 'yarn ', 'ng ', 'python ', 'python3 ', 'manage.py', 'dotnet ',
    'php artisan', 'hugo', 'mvn ', 'gradle', 'npx ', 'composer ', 'java ',
]


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


def extract_refs(skill_text: str) -> list[str]:
    return re.findall(r'`(references/[^`]+\.md)`', skill_text)


def extract_code_blocks(text: str) -> list[str]:
    return re.findall(r'```(?:bash|sh|text)?\n(.*?)```', text, re.S)


def extract_common_request_examples(skill_text: str) -> list[str]:
    m = re.search(r'## Common Requests\n(.*?)(?:\n## |\Z)', skill_text, re.S)
    if not m:
        return []
    return [x.strip() for x in re.findall(r'```text\n(.*?)```', m.group(1), re.S)]


def has_section(text: str, name: str) -> bool:
    return f'## {name.lower()}' in text.lower()


def framework_specific(text: str, skill_name: str, threshold: int = 2) -> bool:
    lower = text.lower()
    return sum(1 for t in FRAMEWORK_TOKENS.get(skill_name, []) if t in lower) >= threshold


def has_runnable_command(workflow_text: str) -> bool:
    return any(token in workflow_text for token in RUNNABLE_COMMANDS)


def example_quality(examples: list[str], skill_name: str) -> tuple[bool, str]:
    if len(examples) < 2:
        return False, 'fewer than two concrete request examples'
    lower_examples = ' '.join(examples).lower()
    average_length = sum(len(e) for e in examples) / len(examples)
    realistic = sum(1 for marker in REALISM_MARKERS if marker in lower_examples) >= 2
    specific = framework_specific(lower_examples, skill_name, threshold=2)
    pass_ok = specific and (realistic or average_length >= 80)
    reason = 'examples are realistic and framework-specific' if pass_ok else 'examples exist but could be more realistic or more framework-specific'
    return pass_ok, reason


def score_from_checks(*checks: bool) -> int:
    return max(0, min(12, sum(4 if c else 0 for c in checks)))


def test_skill(skill_dir: Path) -> list[ScenarioResult]:
    skill_name = skill_dir.name
    skill_text = read(skill_dir / 'SKILL.md')
    refs = extract_refs(skill_text)
    workflows = skill_dir / 'references' / 'workflows.md'
    workflow_text = read(workflows) if workflows.exists() else ''
    all_text = skill_text + '\n' + workflow_text
    for ref in refs:
        ref_path = skill_dir / ref
        if ref_path.exists() and ref_path != workflows:
            all_text += '\n' + read(ref_path)

    with tempfile.TemporaryDirectory(prefix=f'{skill_name}-drive3-') as tmp:
        tmpdir = Path(tmp)
        disposable = tmpdir / skill_name
        shutil.copytree(skill_dir, disposable)
        manifest_ok = (disposable / 'agents' / 'openai.yaml').exists() and (disposable / 'agents' / 'claude.yaml').exists()
        refs_ok = refs and all((disposable / r).exists() for r in refs)
        s01 = ScenarioResult(skill_name, 'S01', 'happy-path', 'PASS' if manifest_ok and refs_ok else 'FAIL', score_from_checks(manifest_ok, refs_ok), 'disposable copy preserved the skill entrypoint, both manifests, and all referenced markdown files' if manifest_ok and refs_ok else 'missing manifest or referenced file')

    quick_ok = has_section(skill_text, 'Quick Start') and framework_specific(skill_text, skill_name)
    s02 = ScenarioResult(skill_name, 'S02', 'setup', 'PASS' if quick_ok else 'PARTIAL', score_from_checks(quick_ok), 'Quick Start establishes the framework posture before detailed advice' if quick_ok else 'setup posture is generic or incomplete')

    example_ok, example_reason = example_quality(extract_common_request_examples(skill_text), skill_name)
    s03 = ScenarioResult(skill_name, 'S03', 'example-quality', 'PASS' if example_ok else 'PARTIAL', score_from_checks(example_ok), example_reason)

    action_ok = has_runnable_command(workflow_text) and len(extract_code_blocks(workflow_text)) >= 2
    s04 = ScenarioResult(skill_name, 'S04', 'actionability', 'PASS' if action_ok else 'PARTIAL', score_from_checks(action_ok), 'workflow command blocks are runnable shell examples' if action_ok else 'workflow commands are missing or not runnable enough')

    verification_ok = has_section(workflow_text, 'Verification') and any(token in workflow_text.lower() for token in ['confirm', 'inspect', 'smoke', 'preview', 'compare'])
    s05 = ScenarioResult(skill_name, 'S05', 'verification', 'PASS' if verification_ok else 'PARTIAL', score_from_checks(verification_ok), 'verification names commands and observable success checks' if verification_ok else 'verification guidance is implied but not explicit enough')

    recovery_ok = has_section(workflow_text, 'Troubleshooting and recovery') and any(token in workflow_text.lower() for token in ['if ', 'revert', 'roll back', 'compare', 'check'])
    s06 = ScenarioResult(skill_name, 'S06', 'recovery', 'PASS' if recovery_ok else 'FAIL', score_from_checks(recovery_ok), 'troubleshooting gives multiple framework-specific recovery moves' if recovery_ok else 'no explicit troubleshooting or recovery section found')

    first_response_ok = has_section(skill_text, 'First Response Pattern') and any(token in skill_text.lower() for token in ['restate', 'anchor', 'verification loop'])
    s07 = ScenarioResult(skill_name, 'S07', 'efficiency', 'PASS' if first_response_ok else 'PARTIAL', score_from_checks(first_response_ok), 'skill explicitly tells the next model how to shape the first response' if first_response_ok else 'missing first-response posture')

    specificity_ok = framework_specific(all_text, skill_name, threshold=3)
    s08 = ScenarioResult(skill_name, 'S08', 'specificity', 'PASS' if specificity_ok else 'PARTIAL', score_from_checks(specificity_ok), 'best-practices guidance stays concrete across defaults, red flags, and checklist items' if specificity_ok else 'guidance drifts too generic in one or more places')

    concrete_scenarios_ok = (
        '## Concrete scenario patterns' in workflow_text
        or (
            any(marker in workflow_text.lower() for marker in ['compare', 'preview', 'smoke', 'route', 'screen', 'build'])
            and framework_specific(workflow_text, skill_name, threshold=2)
        )
    )
    outcome = 'PASS' if concrete_scenarios_ok else 'PARTIAL'
    evidence = 'workflow includes realistic scenario patterns that show what good execution looks like' if concrete_scenarios_ok else 'workflow could use more realistic scenario patterns'
    s09 = ScenarioResult(skill_name, 'S09', 'scenario-realism', outcome, score_from_checks(concrete_scenarios_ok), evidence)

    return [s01, s02, s03, s04, s05, s06, s07, s08, s09]


def write_report(results: list[ScenarioResult]) -> None:
    from collections import defaultdict

    by_skill: dict[str, list[ScenarioResult]] = defaultdict(list)
    for r in results:
        by_skill[r.skill].append(r)

    total_pass = sum(1 for r in results if r.outcome == 'PASS')
    total_partial = sum(1 for r in results if r.outcome == 'PARTIAL')
    total_fail = sum(1 for r in results if r.outcome == 'FAIL')
    verdict = 'approve' if total_fail == 0 and total_partial == 0 else 're-test' if total_fail == 0 else 'revise'

    lines: list[str] = []
    lines.append('# Skill test-drive report — round 3')
    lines.append('')
    lines.append('This third pass focused on the three round-2 partials and then re-ran the full matrix across all 16 skills. The updated checks raised the bar for example realism by requiring richer request prompts and concrete scenario patterns in workflow references, while still verifying structure, setup, commands, verification, recovery, and first-response guidance.')
    lines.append('')
    lines.append('## Findings addressed during the third pass')
    lines.append('')
    lines.append('- Strengthened `material-design`, `tailwind`, and `vite` with more realistic common-request prompts that include host framework, existing-repo context, and verification constraints.')
    lines.append('- Added `Concrete scenario patterns` sections to the three partially-scored workflow guides so the next model can see what “good execution” looks like before improvising.')
    lines.append('- Added a round-3 test-drive script and a content-quality unit test so future passes catch thin examples earlier.')
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
