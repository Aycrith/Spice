# RISK_REGISTER v2.1 (Planning-Only)

**Last updated:** 2025-12-15

| Risk ID | Category | Risk | Likelihood | Impact | Mitigation | Validation test / drill | Monitoring signals |
|---|---|---|---|---|---|---|---|
| R-01 | Research integrity | Lookahead bias from timestamped daily bars | Med | High | Time-frontier enforcement; availability tests | Stage 0 availability suite | Signal computed before data availability |
| R-02 | Research | Overfitting from parameter search | Med | High | CSCV/PBO gating | Stage 1 PBO report | PBO > threshold; unstable OOS |
| R-03 | Market/regime | Momentum crash regime losses | Med | High | Stress tests; HALT/defensive logic | Crash scenario stress + kill-switch drills | Drawdown acceleration, vol spikes |
| R-04 | Execution | Cutoff misses / order rejects | Low–Med | High | Verified cutoffs; SAFE MODE on rejects; avoid close-auction default | Late submission simulation | Reject codes; repeated late events |
| R-05 | Execution | Poor fills at open (gaps/spreads) | Med | Med–High | Price bounds; fallback policies | Paper vs reference cost analysis | Slippage beyond modeled band |
| R-06 | Ops | Missed rebalance due to workstation downtime | Med | High | Heartbeat; missed-run alerts; restart safety | Outage simulation | Missed-job counter |
| R-07 | Ops | Data provider outage on month-end | Med | Med | Alternate validation source; skip if unverified | Month-end outage drill | Stale close prices |
| R-08 | Reconciliation | Ledger/broker mismatch undetected | Low–Med | High | Append-only ledger; daily reconciliation | Break injection test | Unexplained deltas |
| R-09 | Settlement | T+1 cash constraints cause rejects | Low–Med | Med | Verify account rules; cash buffer | Paper constraints test | Buy rejects; warnings |
| R-10 | Tax ops | Wash sale exposure | Med | Med | Lot awareness; wash-sale flagging | Detection simulation | Loss sale + repurchase window |
| R-11 | Security | Credential leakage | Low | High | Secret isolation; least privilege; audit logs | Secret rotation drill | Unexpected logins |
| R-12 | Governance | Uncontrolled strategy drift | Med | High | Strategy_version locks; approvals; re-validation | Change audit | Unapproved config diffs |
