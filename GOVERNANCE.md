# Governance

This project is a **planning repository** for a personal, locally-run systematic trading system. Governance exists to prevent intent drift, preserve research integrity, and ensure operational realism.

## Roles (conceptual)

- **Planning / Research Lead:** owns plan coherence, evidence standards, and acceptance criteria.
- **Implementation Agents (later):** build strictly against the approved plan and stage gates.
- **Operator:** executes the monthly rebalance and incident response runbooks.

## Decision classification

### Strategy Change (requires strategy_version bump)
Any change that affects portfolio behavior or expected return distribution, including:
- universe membership
- signal definition (ranking, lookback)
- rebalance cadence
- filters/eligibility rules
- defensive asset logic
- risk policy affecting exposure

Required artifacts to update:
- `docs/plan/PLAN_PROPOSAL_*`
- `docs/config/CONFIG_SCHEMA_CONCEPTUAL_*`
- `docs/quality/ACCEPTANCE_CRITERIA_*`
- `docs/validation/VALIDATION_MATRIX_*`
- `docs/validation/TRACEABILITY_INDEX_*`
- ADR documenting the decision

### Operational Change (no strategy_version bump)
Changes that affect how the system runs but not the trading logic, including:
- scheduling times
- logging/observability settings
- backup cadence
- alerting mechanisms

Required artifacts to update:
- Runbook
- Config schema (if new settings)
- Traceability index (if material to reliability)

## Stage gate authority

No progression to the next stage is allowed unless the current stage acceptance criteria are met and recorded.

## Documentation versioning

- Plan artifacts are versioned (e.g., v2.1). A doc version bump indicates a coherent planning update.
- Strategy changes also require a strategy_version bump.

## Review discipline

Even for a solo project, treat changes as if they are reviewed:
- summarize what changed
- state the rationale
- show which acceptance criteria and validation matrix rows were affected
- record any new open questions
