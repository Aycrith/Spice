# Contributing (Docs-as-Code)

This repository is a **planning and architecture** repo for a locally-run systematic trading system. It follows a **docs-as-code** model: documentation is versioned, reviewed, and tested for internal consistency the same way code would be. See the Write the Docs overview of “Docs as Code” for the underlying philosophy. citeturn0search5

## 1) Golden rules
1. **No implementation content** in core planning documents. (No code, no commit plans, no “build steps.”)
2. **Traceability is mandatory:** every material change must be traceable through:
   - `docs/validation/VALIDATION_MATRIX_v2.1.md`
   - `docs/validation/TRACEABILITY_INDEX_v2.1.md`
3. **No intent drift:** MVP remains **Cross-Asset Momentum Rotation (monthly)**.

## 2) How to propose a change
1. Identify the **Finding** and document it in the Validation Matrix (new row or updated row).
2. Update the plan/runbook/config/acceptance criteria as needed.
3. Add/Update an ADR if the change alters architecture, interfaces, NFRs, or strategy semantics.

## 3) ADR process
We use the ADR format introduced by Michael Nygard (“Documenting Architecture Decisions”) and common ADR templates. citeturn0search12turn0search4turn0search0

- ADRs live in: `docs/adr/`
- Each ADR must state:
  - Context
  - Decision
  - Alternatives considered
  - Consequences
  - Validation / what would falsify the decision

## 4) Documentation versioning
- The canonical planning artifacts are versioned (e.g., `v2.1`).
- **Strategy changes** require a `strategy_version` bump and refreshed validation artifacts.
- **Operational changes** require updated runbooks and operational acceptance checks.

