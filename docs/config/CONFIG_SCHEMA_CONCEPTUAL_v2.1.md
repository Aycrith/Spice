# CONFIG_SCHEMA v2.1 — Conceptual Model (Planning-Only)

**Last updated:** 2025-12-15

## 1. Configuration principles
- Reproducibility: every run references immutable config hash + strategy_version.
- Change classification: label each change as Strategy or Operational.
- Idempotency: rebalance decisions keyed by (strategy_version, rebalance_month, snapshot_hash).

## 2. Conceptual configuration model

### 2.1 Meta
- plan_version
- config_id / config_hash
- strategy_version
- change_classification: strategy | operational
- change_reason (required)
- approval_record (required for strategy changes)

### 2.2 Strategy
- universe: [symbols]
- lookback_months (default 12)
- rebalance_frequency: monthly
- ranking_method: trailing_return
- defensive_asset_symbol
- eligibility_filters:
  - min_history_days
  - liquidity_threshold (explicit definition)
  - data_quality_required: true/false

### 2.3 Timing model
- timezone: America/New_York
- decision_time_policy:
  - decision_reference: last_trading_day_close
  - decision_time: after_close + data_available_delay
- execution_time_policy:
  - execution_reference: next_trading_day_open
  - order_submission_window: [start, end] (must respect cutoffs)
- calendar_source (validated)

### 2.4 Broker & execution
- broker: name, account_type (cash|margin), fractional_shares, order_types_allowed
- order_policy:
  - primary: open-auction participation type (as supported)
  - fallback: market/limit with bounds
  - max_spread_bps
  - max_price_deviation_bps
  - reject_on_cutoff_risk: true

### 2.5 Risk policy
- state_machine_enabled: true
- max_drawdown_pct
- halt_conditions: drawdown_breach, severe_reconciliation_break, repeated_rejects
- safe_mode_conditions: data_QA_fail, stale_data, cutoff_miss_risk

### 2.6 Data policy
- data_provider
- bar_type: daily
- adjustment_policy: adjusted_close_required
- availability_policy: must_confirm_end_time_delivery
- QA thresholds: missing bars, return jump sigma

### 2.7 Reconciliation & ledger
- ledger_mode: append_only
- reconciliation_tolerances: position, cash, fees
- tax_lot_tracking: enabled/disabled
- wash_sale_flagging: enabled/disabled

### 2.8 Observability
- run_id_format
- logging_level
- metrics_enabled
- alert_channels (local-only)

## 3. Change management rules
- Strategy Change → strategy_version bump + Stage 1 re-validation.
- Operational Change → no strategy_version bump, but must pass relevant operational checks.
