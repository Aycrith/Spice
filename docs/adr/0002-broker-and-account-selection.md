# 0002: Broker and account selection

- **Status:** Proposed
- **Date:** 2025-12-15

## Context
The plan requires a broker that supports:
- ETF trading
- reliable API or automation interface
- sufficient order types for safety (e.g., market-with-protection, limit orders)
- operational transparency for fills, rejections, and account state

Broker choice constrains execution mechanics, data access, reconciliation, and security controls.

## Decision (pending)
Select the brokerage and account type that will be used for MVP live trading.

## Options (non-exhaustive)
1. **Interactive Brokers (IBKR)**
   - Pros: broad order types, mature APIs, wide market access.
   - Cons: operational complexity; account permissions and platform constraints to verify.
2. **Other U.S. retail brokers**
   - Pros: simpler UX.
   - Cons: limited automation and order-type constraints; often weaker audit/reconciliation hooks.

## Decision drivers
- API capability and stability
- Order type availability and cutoff behavior
- Fees and constraints relevant to small AUM
- Security posture (2FA, token management)

## What would change the decision
- Evidence that the selected broker cannot meet required order safety / automation constraints.

## Validation
- Confirm broker documentation for order types and any relevant cutoffs.
- Paper trading conformance tests must demonstrate acceptable drift vs backtest.

## References
- IBKR Order Types overview: https://www.interactivebrokers.com/en/trading/ordertypes.php
- IBKR API order types reference: https://www.interactivebrokers.com/campus/ibkr-api-page/order-types/
