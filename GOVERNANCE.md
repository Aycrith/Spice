# Governance and Change Control

## 1) Purpose
This file defines how the planning repository is managed so that future implementation agents can proceed deterministically and safely.

## 2) Roles (conceptual)
- **Research + Systems Planning Lead:** maintains strategy validity, research integrity, and traceability.
- **Implementation Agents (future):** build only what is specified and gated by acceptance criteria.
- **Reviewer (optional):** sanity-checks risk, execution realism, and documentation coherence.

## 3) Change classification
### Strategy Change (requires strategy_version bump)
Any modification that changes expected returns/risk profile or the semantics of trading decisions, including:
- universe membership
- signal definition / lookback
- ranking/selection rules
- rebalance cadence
- core risk controls that alter exposure

### Operational Change (no strategy_version bump, but still governed)
Any modification that changes operations but not strategy semantics, including:
- scheduling, logging, alerting
- backup cadence
- broker connectivity/retry policy (unless it changes execution timing semantics)

## 4) Decision locks
Decisions that are “locked” must be captured in ADRs. Changing a locked decision requires:
- explicit rationale
- updated Validation Matrix rows
- re-validation per Acceptance Criteria

## 5) Documentation authority
- Canonical plan: `docs/plan/PLAN_PROPOSAL_v2.1.md`
- Canonical gates: `docs/quality/ACCEPTANCE_CRITERIA_v2.1.md`
- Canonical traceability: `docs/validation/VALIDATION_MATRIX_v2.1.md` + `TRACEABILITY_INDEX_v2.1.md`

