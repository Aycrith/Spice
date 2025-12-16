# 0003: Data provider and adjustment policy

- **Status:** Proposed
- **Date:** 2025-12-15

## Context
Momentum signals require total-return-consistent historical data. The plan assumes either:
- adjusted prices that correctly reflect splits/dividends, or
- a validated total-return series.

Data must also enforce time-frontier discipline (no lookahead) and inception constraints.

## Decision (pending)
Select the primary data provider(s) and define a formal adjustment/timestamp policy.

## Options (illustrative)
1. Paid market data API + corporate actions feed
2. Broker-provided historical data (if suitable)
3. Hybrid: primary provider + secondary reference for QA

## Decision drivers
- Adjustment correctness (splits/dividends)
- Timestamp semantics and availability timing
- Cost and local-only constraints
- Reliability and historical depth

## Validation
- Data QA checks on corporate action events
- Cross-source reconciliation sampling
- Explicit tests for timestamp discipline (daily bars delivered only after close)

## References
- Time frontier / bar availability concepts (reference model):
  - https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/time-modeling/timeslices
  - https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/time-modeling/periods
