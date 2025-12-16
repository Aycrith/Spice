# RUNBOOK.md — Operations, Incidents, and Maintenance (v2)

## 1) Operating principles

- **Correctness > uptime.** If the system is uncertain, it must enter SAFE MODE or HALT rather than “try anyway.”
- **Deterministic + auditable.** Every action must be reproducible from the ledger + config + code version.
- **Idempotent scheduling.** Jobs must be safe to run multiple times without double-trading.

---

## 2) System states and what to do

### RUN
- Normal operations.
- Rebalance job executes if scheduled.

### DEGRADED_DATA
Triggered by:
- stale/missing bars,
- corporate action inconsistencies,
- checksum/provenance mismatch.

Action:
1. Enter SAFE MODE (no new trades).
2. Run Data QA suite.
3. If cannot restore data correctness, HALT.

### BROKER_DOWN
Triggered by:
- API authentication failure,
- disconnected sessions,
- repeated order rejections.

Action:
1. Enter SAFE MODE.
2. Retry connectivity per policy.
3. If still failing and close/open window approaches, HALT and alert.

### SAFE_MODE
- No new discretionary orders.
- Reconciliation and risk-off actions only.

Exit SAFE_MODE:
- After integrity checks pass and manual approval token issued.

### HALT
- Trading disabled until manual review is completed.
- Required after max drawdown breach or unresolved reconciliation issues.

---

## 3) Monthly rebalance operational procedure

### 3.1 Pre-rebalance (T-1 day through rebalance day)

1. Confirm system clock sync (NTP) and timezone correctness.
2. Confirm market calendar for:
   - last trading day of month,
   - early close days.
3. Run “data freshness” check:
   - all universe symbols updated through prior close.
4. Confirm broker session healthy:
   - authentication valid,
   - account permissions intact,
   - paper/live mode correct.
5. Confirm `strategy_version` and config hash are unchanged from validated baseline.

### 3.2 Decision and order placement (default Close→Open convention)

1. After official close is finalized, compute:
   - momentum scores,
   - selected asset,
   - target allocation.
2. Persist Decision Record:
   - decision timestamp,
   - prices used (with provenance),
   - targets,
   - config hash,
   - code commit hash.
3. Generate Execution Plan:
   - MOO (or market-at-open) order set for next session open.
4. Place orders and record broker order ids in the ledger.

### 3.3 Post-open reconciliation

1. Fetch fills and current positions.
2. Reconcile:
   - target vs filled,
   - residual cash and rounding,
   - unexpected partial fills.
3. If reconciliation fails:
   - enter SAFE MODE,
   - halt further actions,
   - notify.

---

## 4) Incident response

### 4.1 Immediate actions (always)

1. Enter SAFE MODE.
2. Snapshot:
   - positions, cash, open orders,
   - latest ledger entries,
   - config hash, code commit hash,
   - broker connectivity status.
3. Classify incident:
   - Data, Broker/API, Scheduler, Strategy logic, Market anomaly.

### 4.2 Common incident playbooks

#### A) Rebalance job missed
- Detection: job not completed by configured deadline after close.
- Action:
  1. SAFE MODE.
  2. Determine if decision can be recomputed safely.
  3. If decision time is missed (e.g., post-open), do not “catch up” without explicit policy; HALT if unsure.

#### B) Reconciliation mismatch
- Detection: holdings differ from expected after execution.
- Action:
  1. SAFE MODE.
  2. Pull broker statements and fills.
  3. If mismatch persists, HALT until corrected.

#### C) Data integrity failure
- Detection: missing bars, suspicious jumps, corp action mismatch.
- Action:
  1. SAFE MODE.
  2. Re-fetch data from primary and secondary provider.
  3. If cannot fix, HALT.

#### D) Max drawdown breach
- Detection: drawdown > threshold.
- Action:
  1. HALT immediately.
  2. Risk-off per policy at next safe window.
  3. Post-mortem required before resumption.

---

## 5) Kill switch

### Manual
- Create the kill switch file / set kill flag:
  - `./ops/KILL_SWITCH` (example)
- Next orchestrator tick must:
  - cancel pending orders where possible,
  - prevent new order submission,
  - transition to HALT.

### Automatic (policy)
- Max drawdown breach.
- Unreconciled mismatch beyond time threshold.

---

## 6) Maintenance cadence

### Daily (automated)
- Data freshness check
- Broker health check
- Scheduler “heartbeat” check

### Weekly
- Full reconciliation audit
- Backup ledger and configs
- Dependency vulnerability scan (optional)

### Monthly
- Rebalance replay (simulate last rebalance using stored snapshots)
- Slippage and spread report vs expected bands

### Quarterly
- Disaster recovery drill:
  - restore from backup,
  - run in paper mode,
  - verify idempotency and reconciliation.

---

## 7) References (operationally relevant)

- NYSE auction timelines and MOC/LOC restrictions:
  https://www.nyse.com/publicdocs/nyse/markets/nyse/NYSE_Opening_and_Closing_Auctions_Fact_Sheet.pdf
- SEC statement on T+1 settlement (cash/ops implications):
  https://www.sec.gov/newsroom/press-releases/2024-62
