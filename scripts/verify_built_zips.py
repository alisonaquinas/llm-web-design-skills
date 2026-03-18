#!/usr/bin/env python3
"""Verify built skill ZIPs exist and open cleanly."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = ["SKILL.md", "agents/claude.yaml", "agents/openai.yaml"]


def discover(skills_root: Path) -> list[str]:
    return sorted(path.parent.name for path in skills_root.glob("*/SKILL.md"))


def verify_zip(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, "missing"
    try:
        with zipfile.ZipFile(path, "r") as zf:
            bad_member = zf.testzip()
            names = {name.replace("\\", "/") for name in zf.namelist()}
    except zipfile.BadZipFile:
        return False, "invalid zip"
    if bad_member is not None:
        return False, f"corrupt member: {bad_member}"
    if not names:
        return False, "empty zip"

    repo_name = path.parent.parent.name
    skill_name = path.stem.replace("-skill", "")
    missing = []
    for rel_path in REQUIRED_FILES:
        expected = f"{repo_name}/skills/{skill_name}/{rel_path}"
        if expected not in names:
            missing.append(expected)
    if missing:
        return False, "missing members: " + ", ".join(sorted(missing))
    return True, "valid"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Verify llm-web-design-skills ZIP artifacts.")
    ap.add_argument("--build-dir", default="built", help="Build directory containing *-skill.zip files")
    ap.add_argument("--skills-dir", default="skills", help="Directory containing skill folders")
    args = ap.parse_args(argv)

    build_dir = (REPO_ROOT / args.build_dir).resolve()
    skills_root = (REPO_ROOT / args.skills_dir).resolve()

    if not build_dir.exists():
        print(f"Error: {build_dir} does not exist. Run 'make build' first.")
        return 1

    failures = 0
    for skill in discover(skills_root):
        zip_path = build_dir / f"{skill}-skill.zip"
        ok, detail = verify_zip(zip_path)
        print(f"[{'OK' if ok else 'MISSING'}] {zip_path.as_posix()} ({detail})")
        failures += 0 if ok else 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
