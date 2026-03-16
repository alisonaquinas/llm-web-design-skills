#!/usr/bin/env bash
set -euo pipefail
repo_root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_root"
if [ "$#" -eq 0 ]; then
  python3 scripts/validate_skills.py
else
  python3 scripts/validate_skills.py "$(basename "$1")"
fi
