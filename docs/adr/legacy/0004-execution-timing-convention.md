# 0004: Execution timing convention (Close→Open vs MOC/LOC)

## Status
Accepted (default), with gated alternative

## Context
Closing auction participation has strict entry/modify/cancel limits that increase operational fragility near month-end. citeturn1search4turn1search8

## Decision
Default to **Close→Open** for MVP.

MOC/LOC month-end execution is allowed only as a gated extension after broker+venue cutoff validation.

## Consequences
- Reduces dependence on late-day auction cutoffs.
- Requires open-execution conformance monitoring.

## Validation
- Paper trading conformance drift thresholds
- Rejection-rate monitoring and SAFE MODE triggers

