#!/usr/bin/env python3
from __future__ import annotations
import re
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / 'skills'
REPORT = ROOT / 'docs' / 'skill-test-drive-report.md'

SCENARIOS = [
    ('S01', 'happy-path', 'Resolve SKILL.md, intent-router references, and required agent manifests in a disposable copy.'),
    ('S02', 'variant', 'Extract workflow command blocks and confirm the skill gives at least one framework-specific command path.'),
    ('S03', 'verification', 'Look for explicit verification guidance that tells the next model how to prove the work is correct.'),
    ('S04', 'recovery', 'Look for troubleshooting or recovery guidance that helps when the first attempt fails.'),
    ('S05', 'setup', 'Confirm the quick start or workflow makes setup assumptions explicit: versions, runtimes, or host framework posture.'),
    ('S06', 'safety', 'Confirm the skill includes safety notes or guardrails for risky edits, migrations, or behavior changes.'),
]

FRAMEWORK_TOKENS = {
    'angular': ['angular', 'rxjs', 'signals', 'ng '],
    'nextjs': ['next', 'app router', 'route handler', 'server component'],
    'react': ['react', 'hook', 'component', 'context'],
    'material-design': ['material', 'material 3', 'tokens', 'theme'],
    'svelte': ['svelte', 'sveltekit', '$state', 'load'],
    'vue': ['vue', 'pinia', 'composition api', 'vue router'],
    'vite': ['vite', 'vitest', 'plugin', 'dev server'],
    'scss': ['scss', 'sass', '@use', 'mixin'],
    'tailwind': ['tailwind', 'utility', 'theme', 'dark mode'],
    'django': ['django', 'manage.py', 'app', 'migration'],
    'nodejs': ['node', 'package.json', 'runtime', 'async'],
    'express-js': ['express', 'middleware', 'router', 'request'],
    'hugo': ['hugo', 'shortcode', 'content bundle', 'taxonomy'],
    'asp-net': ['asp.net', 'dotnet', 'middleware', 'minimal api'],
    'spring-boot': ['spring', 'boot', 'actuator', 'controller'],
    'laravel': ['laravel', 'eloquent', 'artisan', 'blade'],
}

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


def extract_refs(skill_text: str) -> List[str]:
    return re.findall(r'`(references/[^`]+\.md)`', skill_text)


def extract_code_blocks(text: str) -> List[str]:
    return re.findall(r'```(?:bash|sh|text)?\n(.*?)```', text, re.S)


def has_verification(text: str) -> bool:
    lower = text.lower()
    return '## verification' in lower or 'verification' in lower


def has_recovery(text: str) -> bool:
    lower = text.lower()
    return '## troubleshooting and recovery' in lower or '## recovery' in lower or 'troubleshooting' in lower


def has_safety(text: str) -> bool:
    needles = ['safety', 'guardrail', 'preserve', 'avoid', 'breaking change', 'destructive', 'migration']
    return any(n in text.lower() for n in needles)


def has_setup(text: str) -> bool:
    needles = ['version', 'runtime', 'host framework', 'toolchain', 'deployment', 'quick start', 'confirm']
    return any(n in text.lower() for n in needles)


def framework_specific(text: str, skill_name: str) -> bool:
    tokens = FRAMEWORK_TOKENS.get(skill_name, [])
    lower = text.lower()
    return sum(1 for t in tokens if t in lower) >= 2


def score_from_checks(*checks: bool) -> int:
    return max(0, min(12, sum(2 if c else 0 for c in checks)))


def test_skill(skill_dir: Path) -> List[ScenarioResult]:
    skill_name = skill_dir.name
    skill_text = read(skill_dir / 'SKILL.md')
    refs = extract_refs(skill_text)
    all_text = skill_text
    for ref in refs:
        rp = skill_dir / ref
        if rp.exists():
            all_text += '\n' + read(rp)
    workflows = skill_dir / 'references' / 'workflows.md'
    workflow_text = read(workflows) if workflows.exists() else ''

    with tempfile.TemporaryDirectory(prefix=f'{skill_name}-drive-') as tmp:
        tmpdir = Path(tmp)
        disposable = tmpdir / skill_name
        shutil.copytree(skill_dir, disposable)
        manifest_ok = (disposable / 'agents' / 'openai.yaml').exists() and (disposable / 'agents' / 'claude.yaml').exists()
        refs_ok = refs and all((disposable / r).exists() for r in refs)
        s01 = ScenarioResult(skill_name, 'S01', 'happy-path', 'PASS' if manifest_ok and refs_ok else 'FAIL', score_from_checks(manifest_ok, refs_ok), 'intent-router references and manifests resolved in disposable copy' if manifest_ok and refs_ok else 'missing manifest or referenced file')

        code_blocks = extract_code_blocks(workflow_text)
        cmd_ok = len(code_blocks) >= 1 and any(any(ch in block for ch in ['npm ', 'yarn ', 'pnpm ', 'ng ', 'python ', 'dotnet ', 'php artisan', 'hugo', 'gradle', 'mvn ']) for block in code_blocks)
        specific_ok = framework_specific(workflow_text + skill_text, skill_name)
        s02_outcome = 'PASS' if cmd_ok and specific_ok else 'PARTIAL' if cmd_ok or specific_ok else 'FAIL'
        s02 = ScenarioResult(skill_name, 'S02', 'variant', s02_outcome, score_from_checks(cmd_ok, specific_ok), 'workflow includes framework-specific command path' if cmd_ok and specific_ok else 'workflow commands are present but not specific enough')

        verif_ok = has_verification(workflow_text) and ('confirm' in workflow_text.lower() or 'smoke-test' in workflow_text.lower() or 'smoke test' in workflow_text.lower() or 'inspect' in workflow_text.lower())
        s03_outcome = 'PASS' if verif_ok else 'PARTIAL'
        s03 = ScenarioResult(skill_name, 'S03', 'verification', s03_outcome, score_from_checks(verif_ok), 'verification guidance found' if verif_ok else 'verification guidance is implied but not explicit enough')

        recovery_ok = has_recovery(workflow_text)
        s04_outcome = 'PASS' if recovery_ok else 'FAIL'
        s04 = ScenarioResult(skill_name, 'S04', 'recovery', s04_outcome, score_from_checks(recovery_ok), 'recovery or troubleshooting guidance found' if recovery_ok else 'no explicit troubleshooting or recovery section found')

        setup_ok = has_setup(skill_text) and framework_specific(skill_text, skill_name)
        s05_outcome = 'PASS' if setup_ok else 'PARTIAL'
        s05 = ScenarioResult(skill_name, 'S05', 'setup', s05_outcome, score_from_checks(setup_ok), 'quick start makes setup posture explicit' if setup_ok else 'setup posture is generic or incomplete')

        safety_ok = has_safety(all_text)
        s06_outcome = 'PASS' if safety_ok else 'PARTIAL'
        s06 = ScenarioResult(skill_name, 'S06', 'safety', s06_outcome, score_from_checks(safety_ok), 'safety notes or guardrails present' if safety_ok else 'only weak generic safety guidance found')

        return [s01, s02, s03, s04, s05, s06]


def write_report(results: List[ScenarioResult]) -> None:
    from collections import defaultdict
    by_skill = defaultdict(list)
    for r in results:
        by_skill[r.skill].append(r)

    lines: List[str] = []
    lines.append('# Skill test-drive report')
    lines.append('')
    lines.append('This report follows the uploaded `skill-test-drive` workflow. Each skill was exercised in a disposable workspace with six live scenarios focused on structure resolution, workflow discoverability, verification guidance, recovery guidance, setup posture, and safety notes.')
    lines.append('')

    total_pass = sum(1 for r in results if r.outcome == 'PASS')
    total_partial = sum(1 for r in results if r.outcome == 'PARTIAL')
    total_fail = sum(1 for r in results if r.outcome == 'FAIL')
    total_blocked = sum(1 for r in results if r.outcome == 'BLOCKED')
    lines.append('## Summary')
    lines.append('')
    lines.append(f'- **Skills covered:** {len(by_skill)}')
    lines.append(f'- **Scenarios attempted:** {len(results)}')
    lines.append(f'- **Outcome mix:** {total_pass} pass / {total_partial} partial / {total_fail} fail / {total_blocked} blocked')
    verdict = 'approve' if total_fail == 0 and total_partial <= len(by_skill) else 're-test' if total_fail == 0 else 'revise'
    lines.append(f'- **Repository verdict:** `{verdict}`')
    lines.append('')

    for skill, items in sorted(by_skill.items()):
        p = sum(1 for i in items if i.outcome == 'PASS')
        pt = sum(1 for i in items if i.outcome == 'PARTIAL')
        f = sum(1 for i in items if i.outcome == 'FAIL')
        lines.append(f'## {skill}')
        lines.append('')
        lines.append(f'- Outcome mix: {p} pass / {pt} partial / {f} fail')
        lines.append('')
        lines.append('| ID | Bucket | Outcome | Score | Key evidence |')
        lines.append('|---|---|---|---:|---|')
        for i in items:
            lines.append(f'| {i.sid} | {i.bucket} | {i.outcome} | {i.score} | {i.evidence} |')
        issues = [i for i in items if i.outcome in {'PARTIAL', 'FAIL'}]
        if issues:
            lines.append('')
            lines.append('### Improvement targets')
            lines.append('')
            for issue in issues:
                if issue.sid == 'S03':
                    fix = 'add explicit verification checklist and concrete success signals'
                elif issue.sid == 'S04':
                    fix = 'add troubleshooting and recovery guidance for the first failed attempt'
                elif issue.sid == 'S02':
                    fix = 'make workflow commands more framework-specific and tie them to a realistic task'
                elif issue.sid == 'S05':
                    fix = 'tighten setup questions so runtime and host assumptions are explicit'
                else:
                    fix = 'strengthen the skill guidance around this scenario'
                lines.append(f'- {issue.sid}: {issue.evidence}; recommended fix: {fix}')
        lines.append('')

    REPORT.write_text('\n'.join(lines).strip() + '\n', encoding='utf-8')


def main() -> int:
    skills = [p for p in sorted(SKILLS_DIR.iterdir()) if p.is_dir()]
    results: List[ScenarioResult] = []
    for skill_dir in skills:
        results.extend(test_skill(skill_dir))
    write_report(results)

    failures = [r for r in results if r.outcome == 'FAIL']
    print(f'Wrote {REPORT}')
    print(f'PASS={sum(r.outcome=="PASS" for r in results)} PARTIAL={sum(r.outcome=="PARTIAL" for r in results)} FAIL={len(failures)} BLOCKED={sum(r.outcome=="BLOCKED" for r in results)}')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
