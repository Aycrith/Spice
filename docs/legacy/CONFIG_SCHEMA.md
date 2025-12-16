# CONFIG_SCHEMA.md — Configuration Contract (v2)

This document defines the configuration structure for the MVP strategy and the system. It is intended to be implemented as a versioned JSON or YAML file (plus environment variables for secrets).

## 1) Design rules

- **Everything deterministic:** all values used for decisions must be explicitly configurable and logged.
- **Secrets are never in config files:** broker keys/passwords must come from environment variables or OS keychain.
- **Config changes are strategy changes** unless explicitly marked “operational only.”

---

## 2) Top-level config layout (conceptual)

```yaml
meta:
  system_name: "personal-trading-system"
  environment: "backtest|paper|live"
  strategy_version: "v1.0.0"           # increments on any strategy rule change
  config_version: "2025-12-15"         # increments on any config file change
  code_commit: "<git hash optional>"
  timezone: "America/New_York"

universe:
  symbols:
    - "SPY"
    - "IEF"
    - "GLD"
    - "EFA"
    - "SHY"
  eligibility:
    min_adv_usd: 50000000
    max_median_spread_bps: 5
    require_unlevered: true
    require_post_inception_only: true

strategy:
  type: "cross_asset_momentum_rotation"
  rebalance:
    frequency: "monthly"
    day_rule: "last_trading_day"
    decision_time: "after_close"       # default Close→Open convention
    execution_time: "next_open"
  momentum:
    lookback_months: 12                 # freeze after validation
    use_total_return: true
  selection:
    top_n: 1
    absolute_momentum_threshold: 0.0
  defensive_asset: "SHY"

execution:
  policy: "close_to_open"               # must match backtest assumptions
  order_style: "MOO_or_market_at_open"
  allow_fractional: false
  cash_buffer_pct: 0.5                  # avoid over-allocation due to rounding
  max_order_retries: 2

cost_model:
  commission_per_trade_usd: 0.0
  slippage:
    model: "max(half_spread, bps_floor)"
    bps_floor: 2
    spread_source: "broker|data_provider"
  fee_overrides:
    enabled: true

risk:
  state_machine:
    enabled: true
  precedence:
    - "KILL_SWITCH"
    - "MAX_DRAWDOWN_HALT"
    - "DATA_INTEGRITY"
    - "BROKER_HEALTH"
    - "DAILY_LOSS_LIMIT"
    - "STOP_FAILSAFE"
    - "STRATEGY_REBALANCE"
  max_drawdown:
    enabled: true
    threshold_pct: 20
    action: "HALT_AND_RISK_OFF"
  daily_loss_limit:
    enabled: false
    threshold_pct: 3
  stop_failsafe:
    enabled: false
    threshold_pct: 10
    evaluation: "EOD_only"
    exit: "next_open"

data:
  providers:
    primary: "provider_name"
    secondary: "provider_name"
  storage:
    sqlite_path: "./data/system.db"
    bars_path: "./data/bars/"
  integrity:
    require_checksums: true
    max_staleness_hours: 36
    random_crosscheck_pct: 2

scheduler:
  engine: "apscheduler"
  heartbeat_seconds: 60
  missed_job_policy: "SAFE_MODE_AND_ALERT"
  calendar_source: "exchange_calendar"
  early_close_awareness: true

observability:
  logging:
    level: "INFO"
    json_logs: true
    path: "./logs/"
  alerts:
    email:
      enabled: true
      recipients:
        - "you@example.com"
    sms:
      enabled: false
  dashboard:
    enabled: false

secrets:
  broker:
    env:
      IBKR_USERNAME: "ENV:IBKR_USERNAME"
      IBKR_PASSWORD: "ENV:IBKR_PASSWORD"
      IBKR_TOTP_SECRET: "ENV:IBKR_TOTP_SECRET"
```

---

## 3) JSON Schema (minimal starting point)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["meta", "universe", "strategy", "execution", "risk", "data", "scheduler", "observability"],
  "properties": {
    "meta": {
      "type": "object",
      "required": ["environment", "strategy_version", "timezone"],
      "properties": {
        "environment": { "enum": ["backtest", "paper", "live"] },
        "strategy_version": { "type": "string" },
        "timezone": { "type": "string" }
      }
    },
    "strategy": {
      "type": "object",
      "required": ["type", "rebalance", "momentum", "defensive_asset"],
      "properties": {
        "type": { "const": "cross_asset_momentum_rotation" },
        "defensive_asset": { "type": "string" }
      }
    }
  }
}
```

---

## 4) Change management rules

Treat the following as **strategy changes** (requires re-validation and strategy_version bump):
- Universe symbols or eligibility thresholds
- Momentum lookback
- Rebalance schedule or timing convention
- Risk thresholds or precedence ordering
- Any execution policy that changes fills/timing assumptions

Treat the following as **operational-only changes** (no strategy_version bump, but config_version bump):
- Alert recipients
- Logging verbosity
- Storage paths
- Retry counts (if they do not alter fills)

---

## 5) Reference anchors

- NYSE auction cutoffs (for later MOC/LOC variants):
  https://www.nyse.com/publicdocs/nyse/markets/nyse/NYSE_Opening_and_Closing_Auctions_Fact_Sheet.pdf
- SEC settlement cycle change (T+1):
  https://www.sec.gov/newsroom/press-releases/2024-62
