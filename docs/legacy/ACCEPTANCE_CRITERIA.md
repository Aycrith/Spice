# ACCEPTANCE_CRITERIA.md — Gates, Tests, and “Go/No-Go” Thresholds (v2)

This document defines objective criteria for moving between phases and for pausing/retiring the system.

## 1) Global “must always hold” invariants

- **No-lookahead invariant:** all signals and features used at decision time must have `available_timestamp <= decision_timestamp`.
- **Idempotency invariant:** re-running a scheduled job must not place duplicate orders.
- **Reconciliation invariant:** after execution, holdings/cash must reconcile to the intended target within configured tolerances.
- **Auditability invariant:** every decision and order must be traceable to a config hash + code commit + data snapshot id.

---

## 2) Stage gates

### Stage 0 → Stage 1 (foundations complete)

**Required:**
- Backtest runner executes end-to-end with deterministic output.
- Data QA suite passes:
  - missing bars detection,
  - corp action consistency check,
  - cross-provider sample verification.

**Pass/Fail:**
- PASS if all required checks succeed and are logged.
- FAIL if any check is skipped or produces unresolved errors.

---

### Stage 1 → Stage 2 (research-grade validation complete)

**Required reports (must exist and be versioned):**
1. Baseline backtest report (entire sample).
2. Walk-forward report with pre-registered windows.
3. Robustness report:
   - parameter neighbor stability,
   - start-date sensitivity,
   - cost stress (2×/3×),
   - 1-day execution delay.
4. Overfitting diagnostic:
   - PBO/CSCV report and interpretation.

**Minimum acceptance expectations (conservative):**
- Not cost-fragile (edge not dependent on unrealistically low costs).
- Not isolated to a single regime.
- Not hypersensitive to small parameter changes.

**Go/No-Go:**
- GO if diagnostics and robustness are acceptable and assumptions are realistic.
- NO-GO if:
  - results collapse under modest cost assumptions,
  - performance is isolated to one regime,
  - PBO indicates high likelihood of selection bias.

---

### Stage 2 → Stage 3 (paper trading conformance complete)

**Minimum paper requirements:**
- >= 6 months paper OR one meaningful volatility spike episode.
- >= 3 executed rebalances.
- Forced drills completed:
  - broker reconnect/restart recovery,
  - reconciliation failure handling,
  - kill switch.

**Conformance criteria (hard):**
- Decision identity:
  - selected asset and targets match backtest for same dates (after rounding allowances).
- Operational reliability:
  - zero missed rebalances in final 3 rebalance opportunities.
- Reconciliation:
  - 100% reconciliation success for all executed paper rebalances.

**Go/No-Go:**
- GO if all criteria pass and deviations are explained and corrected.
- NO-GO if any unexplained drift persists.

---

### Stage 3 → Stage 4 (live stability complete)

**Minimum live requirements:**
- >= 3 months live with small capital.
- No critical incidents (unreconciled holdings, repeated order failures, data corruption).

**Cost/impact acceptance:**
- Realized slippage/spreads within expected bands from paper.
- Turnover not materially higher than modeled.
- Fixed costs do not exceed a configured % of AUM.

**Go/No-Go:**
- GO if operational and cost assumptions hold.
- NO-GO if silent erosion indicators persist for >2 cycles.

---

## 3) Pause / HALT / Retire criteria (always active)

### HALT triggers (immediate)
- Max drawdown threshold breach.
- Unreconciled mismatch persists >24 hours.
- Data integrity failures affecting correctness.
- Broker health failures near execution window preventing safe operation.

### Resume requirements
- Post-mortem completed.
- Regression test added that would have caught the issue.
- Paper replay of last rebalance passes.
- Manual approval token issued.

### RETIRE triggers
- Re-validation fails repeatedly after fixes.
- Edge exists only under unrealistic cost assumptions.
- Operational burden outweighs net returns.

---

## 4) Reference anchors

- PBO/CSCV reference: “The Probability of Backtest Overfitting” (Bailey et al.)
  https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf
- Momentum crash behavior reference: Daniel & Moskowitz (2016)
  https://www.kentdaniel.net/papers/published/jfe_16.pdf
