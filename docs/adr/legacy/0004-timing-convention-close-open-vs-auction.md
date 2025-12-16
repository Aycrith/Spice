# 0004: Timing convention (Close→Open vs MOC/LOC)

- **Status:** Proposed
- **Date:** 2025-12-15

## Context
Monthly rotation can be executed using:
- **Close→Open (default):** compute signal after month-end close, trade next open.
- **Auction participation:** use Market-on-Close / Limit-on-Close orders on month-end.

Auction participation introduces strict cutoff windows and cancellation restrictions.

## Decision (pending)
Confirm the default timing convention and define gating criteria for auction execution.

## Options
1. **Close→Open (default)**
   - Pros: less operational fragility.
   - Cons: overnight gap risk.
2. **Month-end MOC/LOC (gated)**
   - Pros: tighter tracking to month-end signal definition.
   - Cons: cutoff and cancel restrictions; higher operational burden.

## Validation
- Verify exchange cutoff and cancellation rules for the chosen venue.
- Demonstrate reliability of scheduled placement within the cutoff window.

## References
- NYSE Closing Process fact sheet: https://www.nyse.com/publicdocs/nyse/NYSE_Auctions_Closing_Process_Fact_Sheet.pdf
- Nasdaq opening/closing cross quick guide: https://www.nasdaqtrader.com/content/technicalsupport/specifications/TradingProducts/openclosequickguide.pdf
