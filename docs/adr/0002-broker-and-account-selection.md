# 0002: Broker and account type selection

## Status
Proposed

## Context
Broker and account type (cash vs margin) determine available order types, cutoffs, fractional share support, buying power rules, and operational constraints under T+1 settlement. citeturn1search9turn1search13

## Decision
TBD.

## Options
1. IBKR (cash)
2. IBKR (margin, no leverage policy)
3. Other broker (to be evaluated)

## Decision drivers
- Order type availability and constraints
- Operational reliability (API, stability)
- Fees, minimums, and reporting quality

## Validation
- Paper tests of the intended order policy and rejection behavior
- Documented cutoff schedule and enforcement plan

