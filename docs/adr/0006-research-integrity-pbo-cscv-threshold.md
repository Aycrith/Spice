# 0006: Research integrity (PBO/CSCV threshold)

- **Status:** Proposed
- **Date:** 2025-12-15

## Context
Backtests are susceptible to overfitting. The plan requires explicit methodology to detect and limit overfitting during strategy selection and parameter tuning.

## Decision (pending)
Define the CSCV/PBO procedure parameters and the rejection threshold.

## Options
- Conservative PBO threshold (lower allowed PBO) to reduce risk of selecting overfit strategies.
- More permissive threshold (higher allowed PBO) to allow exploration at the cost of higher selection risk.

## Validation
- Implement CSCV/PBO in research and record results per candidate configuration.
- Reject configurations exceeding the chosen PBO threshold.

## References
- Bailey et al., The Probability of Backtest Overfitting (PDF): https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf
