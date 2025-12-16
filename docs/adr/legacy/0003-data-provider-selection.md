# 0003: Data provider selection and timestamp semantics

## Status
Proposed

## Context
Lookahead bias can occur when bars are timestamped at the start time while including the close price. A time-frontier discipline must be enforceable using the chosen provider’s semantics. citeturn2search5turn2search1

## Decision
TBD.

## Options
- Paid EOD provider with explicit corporate action adjustments
- Multiple-source validation approach

## Validation
- Provider documentation review
- Empirical availability tests (what time is close data actually available?)

