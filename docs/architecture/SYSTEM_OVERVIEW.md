# System Overview (Architecture, Planning-Only)

## 1) Pipeline
Data → Strategy → Risk → Execution → Ledger/Reconciliation → Reporting/Observability

## 2) Design principles
- Determinism and replayability
- Idempotency for monthly rebalances
- Strong audit trail (decision provenance)
- Fail-safe operations (SAFE MODE/HALT)

See `docs/plan/PLAN_PROPOSAL_v2.1.md` for the authoritative integrated plan.

