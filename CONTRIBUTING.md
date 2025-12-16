# Contributing (Docs-as-Code)

This repository is intentionally **planning-first**. Contributions are changes to documentation, research evidence, validation criteria, and governance artifacts.

## Core workflow

1. **Start with the index:** read `docs/INDEX.md` and identify the artifact(s) you are modifying.
2. **Maintain traceability:** any material change must be reflected in:
   - `docs/validation/VALIDATION_MATRIX_v2.1.md` (or the current version), and
   - `docs/validation/TRACEABILITY_INDEX_v2.1.md`.
3. **Record significant decisions as ADRs:** add/update a file under `docs/adr/`.
4. **Update acceptance gates:** if the change affects phase readiness, update `docs/quality/ACCEPTANCE_CRITERIA_v2.1.md`.
5. **Update open questions:** if the change resolves or introduces uncertainty, update `docs/validation/OPEN_QUESTIONS_v2.1.md`.

This repo follows a **Docs-as-Code** approach (documentation is version-controlled and reviewed like code). See Write the Docs for the underlying philosophy. 

## What counts as a “material change”

A change is material if it impacts any of:
- Strategy behavior (universe, ranking, lookback, cadence, filters)
- Timing convention (Close→Open vs MOC/LOC)
- Risk policy (HALT/SAFE MODE conditions, drawdown gates)
- Validation metrics and thresholds
- Execution mechanics and broker constraints

Material changes require:
- **Strategy version bump** (recorded in Config Schema + ADR)
- Updated robustness/validation plan in Acceptance Criteria

## Evidence standards

Prefer primary/authoritative sources for operational constraints:
- Exchange auction/cutoff rules (NYSE/Nasdaq)
- Broker documentation for order types and deadlines (e.g., IBKR)
- Regulators for settlement rules (SEC T+1)
- Tax authorities for wash sales (IRS Publication 550)

Record sources in `docs/references/PRIMARY_SOURCES.md` and cite them in the affected artifacts.

## ADR format

Use the Nygard-style ADR structure (Status, Context, Decision, Consequences) as documented by Cognitect and the ADR community.
