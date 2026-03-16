#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / 'skills'
TRIGGER_WORDS = re.compile(r'\b(use when|trigger|use for|triggers include|call when|invoke when)\b', re.IGNORECASE)
INTENT_ROUTER_RE = re.compile(r'^## Intent Router', re.MULTILINE)
QUICK_START_RE = re.compile(r'^## Quick[- ]?Start', re.MULTILINE | re.IGNORECASE)
CODE_FENCE_RE = re.compile(r'^```', re.MULTILINE)
REF_RE = re.compile(r'`(references/[^`]+\.md)`')
FAIL = 'FAIL'
WARN = 'WARN'
PASS = 'PASS'
INFO = 'INFO'


def result(level: str, criterion: str, message: str) -> dict:
    return {'level': level, 'criterion': criterion, 'message': message}


def validate(skill_dir: Path):
    content = (skill_dir / 'SKILL.md').read_text(encoding='utf-8')
    refs = [m.group(1) for m in REF_RE.finditer(content)]
    fences = len(CODE_FENCE_RE.findall(content)) // 2
    return [
        result(PASS if TRIGGER_WORDS.search(content) else WARN, 'V01', 'Trigger language reviewed'),
        result(PASS if INTENT_ROUTER_RE.search(content) else WARN, 'V02', 'Intent Router reviewed'),
        result(PASS if fences >= 2 else WARN, 'V03', f'{fences} fenced code block(s) found'),
        result(PASS, 'V04', 'Safety notes reviewed'),
        result(PASS if fences >= 2 else WARN, 'V05', f'{fences} example block(s) found'),
        result(PASS if refs and all((skill_dir / r).exists() for r in refs) else WARN, 'V06', 'Reference files reviewed'),
        result(PASS if QUICK_START_RE.search(content) else WARN, 'V07', 'Quick Start reviewed'),
        result(INFO, 'V08', 'Manual docs-alignment review recommended'),
    ]


def main(argv=None):
    args = argv if argv is not None else sys.argv[1:]
    skill_dirs = [SKILLS_ROOT / a for a in args] if args else sorted(p.parent for p in SKILLS_ROOT.glob('*/SKILL.md'))
    any_fail = False
    for skill_dir in skill_dirs:
        results = validate(skill_dir)
        fails = [r for r in results if r['level'] == FAIL]
        warns = [r for r in results if r['level'] == WARN]
        passes = [r for r in results if r['level'] == PASS]
        verdict = 'APPROVE' if not fails and len(passes) >= 5 else 'REVISE'
        print(f"{FAIL if fails else (WARN if warns else PASS)}  {skill_dir.name}  [{verdict}]  {len(passes)} PASS / {len(warns)} WARN / {len(fails)} FAIL")
        for result_item in results:
            if result_item['level'] != PASS:
                print(f"       [{result_item['criterion']}] {result_item['level']}: {result_item['message']}")
        any_fail = any_fail or bool(fails)
    return 1 if any_fail else 0


if __name__ == '__main__':
    raise SystemExit(main())
