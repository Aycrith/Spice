#!/usr/bin/env python3
"""Ensure required planning artifacts exist.

Keeps the repo usable for agents by ensuring the expected entrypoints and
traceability artifacts are present.
"""

from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]

REQUIRED = [
    "docs/INDEX.md",
    "docs/plan/PLAN_PROPOSAL_v2.1.md",
    "docs/validation/VALIDATION_MATRIX_v2.1.md",
    "docs/validation/TRACEABILITY_INDEX_v2.1.md",
    "docs/validation/OPEN_QUESTIONS_v2.1.md",
    "docs/quality/ACCEPTANCE_CRITERIA_v2.1.md",
    "docs/ops/RUNBOOK_v2.1.md",
    "docs/references/PRIMARY_SOURCES.md",
    "docs/quality/STAGE_STATUS.md",
]


def main() -> int:
    missing = [p for p in REQUIRED if not (REPO_ROOT / p).exists()]
    if missing:
        print("ERROR: Required artifacts missing:")
        for p in missing:
            print(f"- {p}")
        return 1

    print("Required artifacts: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
