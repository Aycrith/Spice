# Agent Workflow (VS Code / GitHub Copilot)

This file is a practical checklist for agents iterating in this repository.

## Required reading order

1. `docs/INDEX.md`
2. `docs/plan/PLAN_PROPOSAL_v2.1.md`
3. `docs/validation/VALIDATION_MATRIX_v2.1.md`
4. `docs/quality/ACCEPTANCE_CRITERIA_v2.1.md`
5. `docs/ops/RUNBOOK_v2.1.md`

## Before you change anything

- Confirm current stage in `docs/quality/STAGE_STATUS.md`.
- If `stage < 2`, treat the repo as **planning-only**:
  - Allowed changes: `docs/**`, `.github/**`
  - Disallowed: implementation code, binaries, datasets, broker exports
- Create a feature branch (never work directly on `main`).

## During changes (Docs-as-Code)

- Do not introduce intent drift: MVP remains **Cross-Asset Momentum Rotation (monthly)**.
- Keep traceability: for any material change, update:
  - `docs/validation/TRACEABILITY_INDEX_v2.1.md`
  - `docs/validation/VALIDATION_MATRIX_v2.1.md`
  - `docs/validation/OPEN_QUESTIONS_v2.1.md` (if unresolved)
- Prefer ADRs for decisions (`docs/adr/`).

## Import / merge safety

If you are importing artifacts:

- Extract into a staging directory (e.g., `.tmp_import_*`).
- Run a collision scan.
- Never overwrite existing files.
- Use `*.import.md` naming for incoming versions and merge manually.

## Pull request requirements

Follow `.github/pull_request_template.md`.

Minimum acceptance checks per PR:

- No secrets or large binaries committed.
- No repo-root governance files modified.
- `docs/INDEX.md` remains the “start here” entrypoint.
- Evidence is linked in `docs/references/PRIMARY_SOURCES.md`.
- Validation method + thresholds stated.
