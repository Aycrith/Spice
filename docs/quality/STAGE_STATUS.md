---
stage: 1
stage_name: "Stage 1 — Backtest realism + robustness"
last_reviewed: "2025-12-16"
authority: "Planning/Research Lead"
canonical_gates: "docs/quality/ACCEPTANCE_CRITERIA_v2.1.md"
constraints:
  planning_only_until_stage: 2
  allowed_paths_until_stage_2:
    - "docs/**"
    - ".github/**"
notes:
  - "This repository is planning-only until Stage 2 is passed on the main branch."
  - "Stage gates and Go/No-Go thresholds live in ACCEPTANCE_CRITERIA v2.1."
---

# Stage Status

This file is the single machine-readable place to record the current stage gate for automation and agent workflows.

- **Current stage:** 1 (Stage 1 — Backtest realism + robustness)
- **Planning-only constraint:** implementation code is not permitted in PRs to `main` until Stage 2 is passed on `main`.

## How to advance the stage

1. Demonstrate Stage gate completion against `docs/quality/ACCEPTANCE_CRITERIA_v2.1.md`.
2. Update this file in a **docs-only** PR that includes evidence links (Primary Sources) and the validation results.
3. Ensure `docs/validation/TRACEABILITY_INDEX_v2.1.md` reflects the decision to advance.
