# 0007: No-cost proof-of-concept demo path (SimBroker + free/legal data)

- **Status:** Proposed
- **Date:** 2025-12-16

## Context

The v2.1 plan defines stage gates that eventually require **paper trading conformance** against a real broker (Acceptance Criteria Stage 2). However, the sponsor/operator has introduced an additional constraint for the proof-of-concept phase:

- **No paid external services** for data/brokerage
- **No injected trading funds**

This constraint is compatible with demonstrating deterministic decision-making and safe operations, but may not satisfy Stage 2 broker conformance criteria.

Separately, the planning repository is constrained to **docs-only changes** until Stage 2 on `main` (`docs/quality/STAGE_STATUS.md`).

## Decision (pending)

Adopt a two-path approach:

1. **Decision Portfolio Demo path (no-cost):**
   - Use a **SimBroker** adapter and free/legal EOD data to run monthly decision sessions.
   - Output DecisionRecords, ExecutionPlans, a ledger of simulated fills, and reconciliation reports.
   - Purpose: demonstrate end-to-end decision provenance, determinism, and operational safety without external costs.

2. **Paper/Live conformance path (Stage 2+):**
   - Keep broker selection and account type as a P0 open question (ADR 0002).
   - When funds/constraints permit, implement a real broker adapter and meet Stage 2 criteria.

Implementation work for the demo will occur in a **separate implementation repository** to maintain planning-only compliance in this repo.

## Consequences

### Positive
- Unblocks parallel implementation and demonstration without waiting for broker funding.
- Preserves the plan’s intent and stage-gate integrity (Stage 2 remains the real conformance proof).
- Enables multi-agent work with clear module boundaries (broker adapter is replaceable).

### Negative / risks
- Demo results are not proof of real-world order acceptance/cutoff behavior.
- Execution realism must be explicitly labeled “simulated” to avoid overstating evidence.

## Validation

- Demo validation:
  - deterministic replay (same inputs → identical DecisionRecord key and hashes)
  - idempotent monthly run (no duplicate ledger events)
  - SAFE MODE/HALT triggers covered via simulated rejects/staleness scenarios
- Stage-gate integrity:
  - no changes to Acceptance Criteria Stage 2 conformance requirements

## References

- `docs/validation/OPEN_QUESTIONS_v2.1.md`
- `docs/quality/ACCEPTANCE_CRITERIA_v2.1.md`
- `docs/package/appendix/OPEN_QUESTIONS_SOLUTIONS.md`
