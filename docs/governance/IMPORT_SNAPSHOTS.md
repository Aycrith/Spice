# Import snapshots (`*.import.md`)

This repository may contain files ending in `*.import.md`.

## What they are

- **Non-authoritative snapshots** of externally imported artifacts.
- They are intentionally kept side-by-side with the canonical documents to prevent accidental overwrites and preserve provenance.

## What they are not

- They are **not** the canonical plan.
- They should **not** be used as the “source of truth” for agent execution.

The canonical plan remains the non-suffixed files referenced by `docs/INDEX.md`.

## How to resolve an import snapshot

For each `*.import.md` file:

1. Compare it to the canonical file (same name without `.import`).
2. Decide one of:
   - **Manual merge** into the canonical file (preferred)
   - **Discard** the snapshot if it provides no value
   - **Keep** the snapshot temporarily as audit/provenance support (with a note in the PR)
3. If the merge is material (strategy/timing/risk/validation thresholds), update:
   - `docs/validation/TRACEABILITY_INDEX_v2.1.md`
   - `docs/validation/VALIDATION_MATRIX_v2.1.md`
   - `docs/validation/OPEN_QUESTIONS_v2.1.md` (if uncertainty remains)

## Safety rule

Never overwrite canonical files silently during imports. Always stage imports and merge deliberately.
