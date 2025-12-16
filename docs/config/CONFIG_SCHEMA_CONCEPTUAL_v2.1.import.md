# Conceptual Configuration Schema v2.1

This document captures the tunable parameters and configuration fields for the
cross‑asset momentum rotation strategy.  It is **conceptual**: no code is
present.  When parameters change, update this schema and bump the
`strategy_version` accordingly.

## 1 Metadata

| Field | Description | Type | Default |
| --- | --- | --- | --- |
| `strategy_version` | Semantic version of the strategy definition (e.g. `2.1`) | string | required |
| `rebalance_frequency` | Frequency of rebalancing (`monthly`, `quarterly`, etc.) | enum | `monthly` |
| `rebalance_day` | Which business day of the rebalance month (e.g. `second_last`) | enum | `second_last` |
| `data_provider` | Identifier for price data source | string | none |

## 2 Universe

```yaml
universe:
  - symbol: SPY
    asset_class: equities
    description: S&P 500 ETF
  - symbol: TLT
    asset_class: bonds
    description: 20+ Year U.S. Treasury ETF
  - symbol: DBC
    asset_class: commodities
    description: Diversified commodity futures ETF
  - symbol: GLD
    asset_class: gold
    description: Gold trust ETF
  - symbol: SHV
    asset_class: cash
    description: Short‑term Treasury ETF for cash parking
```

*Add additional assets by appending to the list.  Each asset must include a
symbol, asset class and description.*

## 3 Ranking and selection

```yaml
ranking:
  lookback_months: 12      # number of months used for momentum calculation
  skip_months: 1           # number of most recent months skipped (12‑1 momentum)
  select_top_n: 2          # number of assets to go long on
  weighting_method: equal  # `equal` or `risk_parity`
```

## 4 Execution

```yaml
execution:
  order_type: MOC          # `MOC` (Market‑on‑Close) or `LOC` (Limit‑on‑Close)
  order_entry_cutoff: "15:50"  # 24h time; ensure order entry before 3:50 PM ET
  broker: TBD              # broker name (e.g., IBKR)
```

## 5 Risk controls

```yaml
risk_controls:
  max_asset_weight: 0.60   # maximum fraction of portfolio allocated to a single asset
  max_portfolio_drawdown: 0.15 # triggers capital preservation mode
  volatility_threshold: 0.30   # realised volatility threshold to scale down positions
```

## 6 Tax considerations

```yaml
tax:
  wash_sale_window_days: 30 # avoid repurchasing substantially identical securities within 30 days before or after a sale at a loss
  track_basis: true        # maintain cost basis to compute disallowed losses
```

## 7 Logging & audit

```yaml
logging:
  enable_detailed_logs: true
  log_retention_months: 24
  encrypt_logs: true
```

### Notes

*Values are placeholders and must be tailored to the actual implementation.*
 The above schema should be serialised into a configuration file (e.g. JSON or
 YAML) once the system is implemented.  Until then, maintain this
 conceptual schema as a living document to capture design decisions.
