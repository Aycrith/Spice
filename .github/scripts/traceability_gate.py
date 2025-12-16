#!/usr/bin/env python3
"""Traceability gate for planning docs.

Fail the PR if a potentially material planning artifact changes without an
accompanying update to at least one traceability artifact.

This is intentionally conservative: it nudges contributors (agents) to keep
"Finding → Risk/GAP → Evidence → Plan change → Validation" up to date.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]

TRACE_FILES = {
    "docs/validation/TRACEABILITY_INDEX_v2.1.md",
    "docs/validation/VALIDATION_MATRIX_v2.1.md",
    "docs/validation/OPEN_QUESTIONS_v2.1.md",
}

# Directories that generally represent plan/ops intent where drift is expensive.
MATERIAL_PREFIXES = (
    "docs/plan/",
    "docs/config/",
    "docs/ops/",
    "docs/risk/",
    "docs/research/",
    "docs/quality/",
    "docs/architecture/",
    "docs/adr/",
)

# Changes that should *not* require traceability updates.
EXEMPT_PREFIXES = (
    "docs/legacy/",
)

EXEMPT_FILES = {
    "docs/quality/STAGE_STATUS.md",  # stage changes are validated separately
}


def run_git(args: list[str]) -> str:
    r = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{r.stderr}")
    return r.stdout


def main() -> int:
    base = os.environ.get("BASE_SHA")
    head = os.environ.get("HEAD_SHA")

    if not base or not head:
        print("ERROR: BASE_SHA and HEAD_SHA must be set.")
        return 2

    changed = [
        line.strip()
        for line in run_git(["diff", "--name-only", base, head]).splitlines()
        if line.strip()
    ]

    if not changed:
        print("Traceability gate: no file changes detected.")
        return 0

    changed_set = set(changed)

    changed_trace = sorted(changed_set.intersection(TRACE_FILES))

    def is_material(path: str) -> bool:
        if path in EXEMPT_FILES:
            return False
        if any(path.startswith(p) for p in EXEMPT_PREFIXES):
            return False
        return any(path.startswith(p) for p in MATERIAL_PREFIXES)

    material_changes = sorted(p for p in changed if is_material(p))

    # If nothing material changed, do not require traceability updates.
    if not material_changes:
        print("Traceability gate: no material planning artifacts changed.")
        return 0

    # If a traceability artifact changed, we consider the gate satisfied.
    if changed_trace:
        print("Traceability gate: OK (traceability artifact(s) updated):")
        for p in changed_trace:
            print(f"  - {p}")
        return 0

    print("ERROR: Potentially material planning artifacts changed, but no traceability artifact was updated.")
    print("\nMaterial-ish changes detected:")
    for p in material_changes:
        print(f"  - {p}")

    print("\nUpdate at least one of:")
    for p in sorted(TRACE_FILES):
        print(f"  - {p}")

    print("\nIf the change is truly non-material, record why in OPEN_QUESTIONS or TRACEABILITY_INDEX.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
