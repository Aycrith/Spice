# VALIDATION_MATRIX v2.1 (Traceability Core)

**Last updated:** 2025-12-15

| Plan Element | Claim / Decision | Assumptions | Evidence / Example | Relevance + Limitations | Risk if wrong | Proposed plan adjustment | Validation method + acceptance threshold |
|---|---|---|---|---|---|---|---|
| Strategy choice | Cross-asset momentum rotation is viable MVP | Momentum persists; ETFs tradable | Momentum documented in equities; cross-asset/time-series momentum literature | Academic settings may differ from ETF execution | Deploying non-robust edge | Tighten scope; require stronger OOS | Stage 1 robustness + OOS stability gates |
| Timing | Default Close→Open | EOD data available; open orders feasible | Exchange/broker cutoff constraints (must be verified for actual venues) | Venue-specific; broker can be earlier | Operational failure; rejects | Keep Close→Open default; gate MOC/LOC | Paper conformance within drift thresholds |
| Execution policy | Open orders with safeguards | Broker supports order types | Venue rulebooks and broker order specs | Depends on broker/venue | Order rejects, bad fills | Add fallback policy; SAFE MODE on rejects | Paper: ≥99% acceptance; bounds enforced |
| Lookahead prevention | Time-frontier enforcement mandatory | Data timestamps can leak | Known failure pattern in bar data timestamping | Provider-specific | Inflated backtest | Provider qualification + tests | Stage 0: availability tests pass |
| Overfitting control | CSCV/PBO gating | Sufficient samples; controlled search | PBO methodology literature | Requires disciplined search scope | False discovery | Freeze params; reduce DoF | Stage 1: PBO ≤ threshold |
| Regime risk | Momentum crashes must be stress-tested | Crash proxies measurable | Momentum crash literature | Implementation details vary | Tail drawdowns | HALT/defensive rules | Stress: tail loss bounded; kill-switch drills pass |
| Settlement | T+1 affects cash availability | Account rules compatible | SEC settlement cycle guidance; broker rules | Broker-specific | Buy rejects, violations | Cash buffer; sequencing rules | Paper: no settlement rejects |
| Tax | Wash sale risk exists | Taxable account; re-entries possible | IRS/Investor.gov wash sale guidance | “Substantially identical” facts-based | Disallowed losses | Wash-sale flagging; lot tracking | Reporting completeness + flags generated |
| Ledger | Append-only ledger + reconciliation | Broker data sufficient | Best practice for auditability | Must be proven via outcomes | Undetected breaks | Strong reconciliation + alerts | Stage 2: reconciliation pass rate ≥ threshold |
| Local ops | Single workstation reliability | Scheduler/backups work | Ops best practices | Must be proven empirically | Missed rebalance | Heartbeats; restore drills | Stage 2: missed-job rate below threshold |
