#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys

VERSION_RE = re.compile(r'^v?(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)')
def parse_version(raw: str):
    m = VERSION_RE.match(raw.strip())
    return None if not m else tuple(int(m.group(n)) for n in ('major', 'minor', 'patch'))
def run(min_major: int) -> int:
    try:
        completed = subprocess.run(['node', '--version'], capture_output=True, text=True, check=True)
    except Exception:
        print('Node.js 20+ is required for markdownlint-cli2.', file=sys.stderr)
        return 1
    version = parse_version(completed.stdout)
    if version is None or version[0] < min_major:
        print('Node.js 20+ is required for markdownlint-cli2.', file=sys.stderr)
        return 1
    return 0
def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--min-major', type=int, default=20)
    args = parser.parse_args(argv)
    return run(args.min_major)
if __name__ == '__main__':
    raise SystemExit(main())
