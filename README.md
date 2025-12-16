# Local Systematic Trading System — Planning Repository

This repository contains **planning-only** artifacts for a personal, locally-run systematic trading system.

## Operating rules (non-negotiable)
- **Planning-first:** no implementation steps or code in these documents.
- **Traceability:** every material change must be traceable via the Validation Matrix and Traceability Index.
- **No intent drift:** MVP strategy remains **Cross-Asset Momentum Rotation** (monthly).

## How to use this repo (agent-friendly)
1. Start with: `docs/INDEX.md`
2. Read the integrated plan: `docs/plan/PLAN_PROPOSAL_v2.1.md`
3. Use traceability to drive work: `docs/validation/VALIDATION_MATRIX_v2.1.md`
4. Govern changes via ADRs: `docs/adr/`
5. Operate safely via the runbook: `docs/ops/RUNBOOK_v2.1.md`

## Versioning
- Plan versions use semantic-ish doc versions (e.g., v2.1).
- **Strategy changes require** a `strategy_version` bump and refreshed validation artifacts.

## License / disclaimer
This is not financial advice. Trading involves risk.
