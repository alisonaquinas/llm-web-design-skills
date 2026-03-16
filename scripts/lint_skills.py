#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / 'skills'
REQUIRED_FILES = ['SKILL.md', 'agents/claude.yaml', 'agents/openai.yaml']
AGENT_REQUIRED_FIELDS = ['display_name', 'short_description', 'default_prompt']
FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---', re.DOTALL)
REFERENCES_LINK_RE = re.compile(r'`(references/[^`]+\.md)`')
KEBAB_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
FAIL = 'FAIL'
WARN = 'WARN'
PASS = 'PASS'


def result(level: str, rule: str, message: str) -> dict:
    return {'level': level, 'rule': rule, 'message': message}


def parse_frontmatter(path: Path):
    m = FRONTMATTER_RE.match(path.read_text(encoding='utf-8'))
    if not m:
        return None
    fields = {}
    current = None
    for line in m.group(1).splitlines():
        if line.startswith(('  ', '\t')) and current:
            fields[current] = f"{fields[current]} {line.strip()}".strip()
            continue
        if ':' in line:
            key, _, val = line.partition(':')
            current = key.strip()
            fields[current] = '' if val.strip() in {'>', '|'} else val.strip()
    return fields


def lint_skill(skill_dir: Path):
    findings = []
    skill_md = skill_dir / 'SKILL.md'
    fm = parse_frontmatter(skill_md) if skill_md.exists() else None

    for rel in REQUIRED_FILES:
        if not (skill_dir / rel).exists():
            findings.append(result(FAIL, 'L03', f'Missing required file: {rel}'))

    if fm is None:
        findings.append(result(FAIL, 'L01', 'SKILL.md has no YAML frontmatter block'))
    else:
        keys = set(fm)
        if keys != {'name', 'description'}:
            findings.append(result(FAIL, 'L01', f'Frontmatter keys must be name and description, got {sorted(keys)}'))
        name = fm.get('name', '').strip('"').strip("'")
        if name and (not KEBAB_RE.match(name) or name != skill_dir.name):
            findings.append(result(FAIL, 'L02', f'Invalid or mismatched skill name: {name!r}'))

    for yaml_name in ('claude.yaml', 'openai.yaml'):
        path = skill_dir / 'agents' / yaml_name
        if path.exists():
            text = path.read_text(encoding='utf-8')
            for field in AGENT_REQUIRED_FIELDS:
                if field not in text:
                    findings.append(result(FAIL, 'L04', f'agents/{yaml_name} missing {field}'))

    if skill_md.exists():
        content = skill_md.read_text(encoding='utf-8')
        for match in REFERENCES_LINK_RE.finditer(content):
            if not (skill_dir / match.group(1)).exists():
                findings.append(result(FAIL, 'L07', f'Dangling reference: {match.group(1)}'))

    return findings


def main(argv=None):
    args = argv if argv is not None else sys.argv[1:]
    skill_dirs = [SKILLS_ROOT / a for a in args] if args else sorted(p.parent for p in SKILLS_ROOT.glob('*/SKILL.md'))
    any_fail = False
    for skill_dir in skill_dirs:
        findings = lint_skill(skill_dir)
        fails = [f for f in findings if f['level'] == FAIL]
        warns = [f for f in findings if f['level'] == WARN]
        header = FAIL if fails else (WARN if warns else PASS)
        print(f"{header}  {skill_dir.name}  {len(findings)} finding(s)")
        for finding in findings:
            print(f"       [{finding['rule']}] {finding['level']}: {finding['message']}")
        any_fail = any_fail or bool(fails)
    return 1 if any_fail else 0


if __name__ == '__main__':
    raise SystemExit(main())
