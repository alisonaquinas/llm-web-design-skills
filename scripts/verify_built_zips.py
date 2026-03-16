#!/usr/bin/env python3
from __future__ import annotations
import argparse
import zipfile
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[1]
def discover(skills_root: Path): return sorted(p.parent.name for p in skills_root.glob('*/SKILL.md'))
def verify_zip(path: Path):
    if not path.exists(): return False, 'missing'
    try:
        with zipfile.ZipFile(path, 'r') as zf: bad = zf.testzip()
    except zipfile.BadZipFile:
        return False, 'invalid zip'
    return (False, f'corrupt member: {bad}') if bad else (True, 'valid')
def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument('--build-dir', default='built'); ap.add_argument('--skills-dir', default='skills'); args = ap.parse_args(argv)
    build_dir = (REPO_ROOT / args.build_dir).resolve(); skills_root = (REPO_ROOT / args.skills_dir).resolve()
    if not build_dir.exists():
        print(f"Error: {build_dir} does not exist. Run 'make build' first."); return 1
    failures = 0
    for skill in discover(skills_root):
        ok, detail = verify_zip(build_dir / f'{skill}-skill.zip')
        print(f"[{'OK' if ok else 'MISSING'}] {(build_dir / f'{skill}-skill.zip').as_posix()} ({detail})")
        failures += 0 if ok else 1
    return 1 if failures else 0
if __name__ == '__main__':
    raise SystemExit(main())
