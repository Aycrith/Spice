# RUNBOOK v2.1 — Operations, Incidents, and Maintenance (Planning-Only)

**Last updated:** 2025-12-15

## 1. Operating principles
- Correctness > uptime: uncertainty triggers SAFE MODE/HALT.
- Deterministic + auditable: every action reproducible from ledger + config + version.
- Idempotent scheduling: safe to re-run jobs without double trading.

## 2. System states
### RUN
Normal operations.

### SAFE MODE
- No new risk positions.
- Closing trades only (if policy allows).
- Investigation and reconciliation continue.

### HALT
- All trading disabled until human clears incident and records a restart decision.

## 3. Monthly rebalance checklist (core)
### 3.1 Pre-rebalance (T-5 to T-1 trading days)
1. Confirm trading calendar (holidays/early closes).
2. Confirm data provider health (no staleness; adjustment pipeline OK).
3. Confirm broker connectivity and account status (buying power, restrictions).
4. Confirm config integrity (strategy_version; no unapproved changes).

### 3.2 Decision (month-end, after close)
1. Create DataSnapshot (record hash).
2. Run data QA gates (missing bars, abnormal returns, timestamp integrity).
3. Compute signal and DecisionRecord.
4. Run risk gates (drawdown, crash-stress flags, cash/settlement feasibility).

### 3.3 Order staging (before next open)
1. Produce ExecutionPlan with order types, bounds, and cutoff schedule.
2. Human review checkpoint (“two-person rule” conceptually).

### 3.4 Execution (next open)
1. Submit orders within verified cutoffs.
2. Monitor rejects/partials.
3. If invariant breaks → SAFE MODE/HALT.

### 3.5 Post-trade (same day)
1. Ingest fills/fees; append to TradeLedger.
2. Reconcile vs broker positions/cash.
3. Generate Rebalance Report (pass/fail + anomalies).

## 4. Incident response playbooks
### 4.1 Data staleness / missing close
- Block rebalance; verify provider vs ingestion.
- If unverified by deadline → SAFE MODE and skip rebalance (explicitly logged).

### 4.2 Broker outage / order rejects
- Capture reject codes and timestamps.
- Do not retry blindly.
- Use fallback policy only if explicitly permitted; otherwise SAFE MODE.

### 4.3 Partial fills / protection breaches
- Follow policy: complete with fallback or unwind to neutrality.
- Record as conformance event.

### 4.4 Reconciliation break
- SAFE MODE.
- Triage source: missing fill, corporate action, cash movement, fees.
- Require resolution before next decision cycle.

## 5. Backup / restore / disaster recovery
- Daily backups: config, ledger, decision records and hashes.
- Off-machine copy required.
- Quarterly restore drill required; must reproduce hashes and reconciliation outputs.

## 6. Change management (ops workflow)
- Strategy Changes require: strategy_version bump + refreshed validation artifacts.
- Operational Changes require: targeted smoke checks and recorded rationale.
