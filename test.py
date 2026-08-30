#!/usr/bin/env python3
"""Run all .py files under a directory and summarize pass/fail results with optional coverage.

This improved runner supports:
- --root <dir> : directory to search (default: pythonstart)
- --coverage   : run each script under coverage (requires 'coverage' package)
- --exclude    : glob pattern to exclude files or directories (can be repeated)
- --show-output: show stdout/stderr for passing scripts as well

Behavior notes:
- Each Python file is executed as a standalone script via subprocess to avoid import-time side effects.
- Coverage: when --coverage is used, each script is run with ``coverage run --source=<root>`` so the
  coverage measurement is limited to the chosen root. After all runs the script attempts to
  combine parallel data files and print a consolidated report plus HTML report (htmlcov/).
- Excludes are matched against file paths relative to the root using ``fnmatch``.

Security reminder: this will execute code in the target directory. Only run it on trusted code or in
an isolated environment.
"""
from __future__ import annotations

import argparse
import fnmatch
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


def find_py_files(root: Path, excludes: List[str]) -> List[Path]:
    if not root.exists():
        print(f"Path not found: {root}", file=sys.stderr)
        return []

    all_files = sorted(root.rglob("*.py"))
    if not excludes:
        return [p for p in all_files if p.is_file()]

    # Normalize excludes: match against path relative to root, POSIX style
    rel_paths = []
    results: List[Path] = []
    for p in all_files:
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        s = rel.as_posix()
        skip = False
        for pat in excludes:
            if fnmatch.fnmatch(s, pat):
                skip = True
                break
            # Also allow matching against parent directory patterns
            # e.g., exclude 'tests/*' or '*/migrations/*'
            if fnmatch.fnmatch(p.as_posix(), pat):
                skip = True
                break
        if not skip:
            results.append(p)
    return results


def run_script(path: Path, use_coverage: bool, coverage_source: str) -> subprocess.CompletedProcess:
    if use_coverage:
        cmd = [sys.executable, "-m", "coverage", "run", "--source", coverage_source, str(path)]
    else:
        cmd = [sys.executable, str(path)]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run .py files under a directory and report pass/fail and optional coverage")
    parser.add_argument("--root", default="pythonstart", help="Root directory to search for .py files")
    parser.add_argument("--coverage", action="store_true", help="Run each script under coverage (requires 'coverage' package)")
    parser.add_argument("--exclude", action="append", default=[], help="Glob pattern to exclude (relative to root). Can be repeated.")
    parser.add_argument("--show-output", action="store_true", help="Show stdout/stderr for passing scripts too")
    args = parser.parse_args(argv)

    root = Path(args.root)

    files = find_py_files(root, args.exclude)
    if not files:
        print("No Python files found.")
        return 0

    results: List[Tuple[Path, bool, subprocess.CompletedProcess]] = []

    print(f"Found {len(files)} .py files under {root}\n")

    for f in files:
        print(f"Running {f}...")
        proc = run_script(f, args.coverage, str(root))
        ok = proc.returncode == 0
        results.append((f, ok, proc))

        status = "PASS" if ok else "FAIL"
        print(f"  {status} (exit={proc.returncode})")
        if not ok or args.show_output:
            if proc.stdout:
                print("--- stdout ---")
                print(proc.stdout)
            if proc.stderr:
                print("--- stderr ---")
                print(proc.stderr)
        print()

    passed = [r for r in results if r[1]]
    failed = [r for r in results if not r[1]]

    print("Summary:")
    print(f"  Total: {len(results)}")
    print(f"  Passed: {len(passed)}")
    print(f"  Failed: {len(failed)}")

    if failed:
        print("\nFailed files:")
        for f, _, proc in failed:
            print(f"- {f} (exit={proc.returncode})")

    # Coverage report
    if args.coverage:
        try:
            # Combine parallel data files and show report
            subprocess.run([sys.executable, "-m", "coverage", "combine"], check=False)
            subprocess.run([sys.executable, "-m", "coverage", "report", "-m"], check=False)
            subprocess.run([sys.executable, "-m", "coverage", "html"], check=False)
            print("\nHTML coverage report written to htmlcov/index.html")
        except FileNotFoundError:
            print("coverage package not found; install it with 'pip install coverage' to enable coverage reports.")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
