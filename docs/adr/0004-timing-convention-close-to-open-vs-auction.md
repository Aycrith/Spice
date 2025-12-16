# 0004: Timing convention (Close→Open vs Auction)

- **Status:** Proposed (default: Close→Open)
- **Date:** 2025-12-15

## Context
Month-end execution can be performed either:
1) by computing signals after the close and trading at the next open (Close→Open), or
2) by targeting the closing auction (MOC/LOC).

Auction participation introduces strict cutoffs and cancellation restrictions, increasing operational fragility.

## Decision (pending)
Adopt Close→Open as the MVP convention; treat MOC/LOC as gated and optional.

## Rationale
Close→Open reduces dependency on minute-level cutoff handling and late cancel/modify rules.

## What would falsify this decision
If evidence shows that Close→Open materially worsens tracking/slippage beyond tolerance and the system can reliably satisfy auction cutoffs.

## Validation
- Demonstrate that Close→Open conformance drift (paper/live vs backtest) stays within defined thresholds.
- If auction is considered: verify exchange cutoffs and broker enforceability.

## References
- NYSE Closing Process fact sheet: https://www.nyse.com/publicdocs/nyse/NYSE_Auctions_Closing_Process_Fact_Sheet.pdf
- Nasdaq Opening/Closing Crosses quick guide: https://www.nasdaqtrader.com/content/technicalsupport/specifications/TradingProducts/openclosequickguide.pdf
