# planproposal_v2.md — Safe & Scalable Personal Trading System Plan (v2)

## Document control

- **Intent and scope (unchanged):** Build a locally-run, personal systematic trading system that starts with an MVP **Cross-Asset Momentum Rotation** strategy, deployed via phased de-risking (backtest → paper → small live → scale).
- **Primary objective (unchanged):** Survivability and capital preservation first; returns second; minimal operational burden.
- **Non-goals (explicit):**
  - No high-frequency trading.
  - No discretionary “screen time” dependency.
  - No leverage requirement for MVP.
  - No cloud dependency; must run on a single workstation.

---

## 1) Summary of improvements integrated (items 1–8)

This revision strengthens the original plan without changing goals or strategy direction:

1. **Signal/execution timing made implementable** with a single, auditable convention used in backtest, paper, and live.
2. **Strategy rules fully specified** (math, timestamps, investability constraints, edge cases).
3. **Risk controls formalized as policies + a state machine** (halts, resumes, precedence, incident handling).
4. **Validation upgraded to decision-grade** (anti-lookahead, investable history, robustness checks, overfitting diagnostics, conformance testing).
5. **Execution realism tightened** (auction cutoffs awareness, slippage/cost modeling, reconciliation, restart-safe behavior).
6. **Architecture hardened** (modular contracts, idempotency, persistent ledger, observability, testing pyramid).
7. **Economic viability made measurable** (fixed-cost drag, turnover and tax friction controls, “silent erosion” monitoring).
8. **Operational survivability elevated** (runbooks, disaster recovery, maintenance cadence, retirement criteria).

---

## 2) Strategy selection framework (unchanged; clarified)

Strategies are evaluated on: implementability, robustness to regime change, low monitoring needs, and survival under realistic costs/taxes at small capital.

**Shortlisted classes (unchanged):**
- Cross-Asset Momentum Rotation (**selected MVP**)
- Trend following (time-series momentum variants; future extension)
- Mean reversion (higher fragility; later only)
- Pairs/stat-arb (higher complexity; later only)
- Crypto momentum (optional extension; higher ops risk)

---

## 3) MVP Strategy — Cross-Asset Momentum Rotation (fully specified)

### 3.1 High-level logic (unchanged)

At each rebalance:
- Compute momentum scores for a fixed, liquid universe.
- Allocate to the top-ranked asset **only if** its momentum is positive (“absolute momentum” filter).
- If no asset has positive momentum, allocate to a defensive/cash proxy.

### 3.2 Universe governance (investability + change control)

**Universe eligibility rules (MVP):**
- Highly liquid, unlevered ETFs only.
- Must have:
  - Sufficient ADV and tight spreads.
  - Clean, auditable price history since inception.
  - No synthetic pre-inception backfills for live decision rules.

**Change control:**
- Any universe change increments `strategy_version` and triggers re-validation (mini walk-forward + paper conformance).

### 3.3 Data definition and anti-lookahead discipline

**Price series:**
- Use split/dividend-adjusted **total-return** (preferred) or adjusted close consistently.
- Store both raw and adjusted series; document which is used for signals and which for accounting.

**Time discipline:**
- Every feature and price used for a decision must record:
  - `asof_timestamp` (timestamp it refers to)
  - `available_timestamp` (timestamp it becomes known/usable)
- A backtest run is invalid if it consumes data with `available_timestamp > decision_timestamp`.

### 3.4 Signal construction (explicit)

Let:
- `t` be the decision timestamp for the rebalance.
- `P_i(t)` be the adjusted/total-return price for asset `i` at `t`.

**Momentum score:**
- Choose a lookback `L` months (default candidate set: 3, 6, 12).
- Define:
  - `m_i(t) = P_i(t) / P_i(t-L) - 1`
- Rank assets by `m_i(t)` descending.

**Selection rule:**
- If `max_i m_i(t) > 0`, choose the top asset `argmax_i m_i(t)`.
- Else choose the defensive asset/cash proxy.

**Parameter governance:**
- Select `L` once for MVP using pre-registered validation rules (Section 4) and freeze it.
- Do not “adapt L” month-to-month.

### 3.5 Execution timing convention (item 1 — resolved)

To prevent silent backtest/live divergence, this plan adopts a single implementable convention:

**Default convention (“Close→Open”):**
- **Decision time:** after the final close price is known for the last trading day of the month.
- **Execution:** trade at the **next session open** using Market-on-Open (MOO) where available; otherwise trade as close to the open as practical (market order at open with conservative slippage model).

This convention is used identically in:
- backtesting fill assumptions,
- paper trading,
- live trading.

**Optional extension (not required for MVP):**
- If you later choose Market-on-Close (MOC), you must:
  - compute the signal using a pre-close snapshot that is available before the broker’s MOC cutoff, and
  - model that snapshot identically in backtests.
  NYSE MOC/LOC cutoffs and cancellation restrictions are documented in the NYSE auction fact sheets (see References).

### 3.6 Portfolio construction (MVP)

- **Fully invested in a single chosen asset** (or defensive/cash proxy).
- No leverage.
- Fractional shares allowed only if broker supports and accounting is consistent.
- Rounding rules must be deterministic and logged.

### 3.7 Risk management (policy-driven; stateful)

Risk controls are implemented as **policies with explicit precedence** and **state transitions**.

**State machine (minimum):**
- `RUN`: normal operation.
- `DEGRADED_DATA`: data staleness/quality failure detected.
- `BROKER_DOWN`: broker unavailable/unhealthy.
- `SAFE_MODE`: no new orders; only reconciliation and risk-off actions permitted.
- `HALT`: trading stopped; manual review required.

**Policy precedence (highest to lowest):**
1. **KILL_SWITCH** (manual or automatic)
2. **MAX_DRAWDOWN_HALT**
3. **DATA_INTEGRITY / BROKER_HEALTH**
4. **DAILY_LOSS_LIMIT** (if implemented)
5. **STOP_FAILSAFE** (if implemented; controlled cadence)
6. **STRATEGY_REBALANCE**

**Max drawdown halt (primary survival control):**
- Define max allowed drawdown (e.g., 20% or as configured).
- If breached:
  - enter `HALT`,
  - cancel orders where possible,
  - move to defensive/cash at the next safe execution window,
  - require a post-mortem + explicit resume token.

**Stop-loss (secondary; fail-safe only):**
- If used, it is a “break glass” policy:
  - evaluated at a defined cadence (e.g., end-of-day only),
  - exits at next open,
  - triggers an incident and review.

**Whipsaw limiter:**
- Minimum holding period of one full rebalance interval unless a high-precedence policy triggers exit.

---

## 4) Backtesting & validation (decision-grade; locally feasible)

### 4.1 Data integrity & bias controls (must-pass)

- No pre-inception trading.
- Corporate actions handled consistently (splits/dividends).
- Missing data detection and cross-check against a secondary provider for random samples.
- Strict time-frontier enforcement: no lookahead.

### 4.2 Execution realism & costs

**Fill assumptions (default convention):**
- Fill at next open (MOO / market-at-open) + conservative slippage.
- Slippage model should include:
  - half-spread floor and/or bps floor,
  - volatility scaling (optional),
  - explicit fees (even if “$0 commission,” record platform/broker fees if any).

**Stress tests:**
- Multiply costs 2× and 3× to test fragility.
- Add 1-day execution delay to quantify sensitivity to timing.

### 4.3 Robustness checks (required)

- Regime slices (dot-com bust, GFC, post-GFC, 2020, 2022 rates shock, recent years).
- Start-date sensitivity analysis (many rolling start dates).
- Parameter stability (neighboring lookbacks should not radically change outcomes).
- Crash window focus for momentum (report drawdowns and recovery dynamics).

### 4.4 Overfitting defense

- Parameter freeze before out-of-sample evaluation.
- Walk-forward protocol with pre-registered windows.
- Probability of Backtest Overfitting (PBO) style diagnostics (CSCV) used to detect overfitting risk.

### 4.5 Paper trading gate (event-based; not time-only)

Paper trading must demonstrate both correctness and operational reliability.

**Minimum gate:**
- >= 6 months paper OR at least one volatility spike episode, AND
- >= 3 executed rebalances, AND
- >= 1 forced drill of:
  - broker reconnect/restart recovery,
  - reconciliation failure handling,
  - kill switch.

**Conformance requirements:**
- Signals and targets match backtest decisions for the same dates (allowing rounding).
- Deviations must be explained and fixed; repeated unexplained drift is a no-go.

---

## 5) Software architecture (local, modular) — build specification

### 5.1 Modules and responsibilities

1. **Data Service**
   - Historical ingestion + live updates
   - QA checks + provenance + checksums
   - Local storage (SQLite for metadata/ledger; Parquet/CSV for bars)

2. **Strategy Engine**
   - Pure function: (data snapshot, config) → (targets, decision metadata)

3. **Risk Engine**
   - Applies policies and state machine
   - Produces approved orders or state transition

4. **Execution Engine**
   - Broker adapter boundary
   - Order lifecycle state machine
   - Reconciliation loop (positions/cash/orders)

5. **Portfolio Accounting**
   - Positions, PnL, fees
   - Tax lots (at least FIFO lots tracked for exports)

6. **Monitoring & Observability**
   - Structured logs, metrics, alerts (email/SMS)
   - Optional local dashboard

7. **Scheduler/Orchestrator**
   - Calendar-aware (holidays/early closes)
   - Idempotent jobs + retries

### 5.2 Reliability primitives (must-have)

- **Persistent trading ledger** (SQLite):
  - decisions, targets, orders, fills, positions, cash, state transitions
- **Idempotency keys**:
  - derived from (strategy_version, job_date, job_type)
- **Kill switch**:
  - file flag or CLI command that forces `HALT`
- **Audit manifest per run**:
  - git commit hash, config hash, data snapshot hash, timestamps

### 5.3 Testing pyramid

- Unit: momentum calc, ranking, thresholds, drawdown, state transitions
- Integration: broker paper API, order placement, reconciliation, restart recovery
- Invariants: buy-and-hold sanity checks; no-lookahead assertions

---

## 6) Phased roadmap (same stages; clearer exit criteria)

### Stage 0 — Environment & foundations
**Done when:**
- Reproducible local env.
- Data ingestion + QA scripts run.
- Scheduler skeleton runs with market calendar awareness.

### Stage 1 — Research-grade backtesting
**Done when:**
- Event-driven backtester with time discipline.
- Walk-forward + robustness + cost stress reports.
- Overfitting diagnostic report.
- Frozen MVP config candidate identified.

### Stage 2 — Paper trading (conformance + ops)
**Done when:**
- End-to-end paper execution with reconciliation.
- Paper gate requirements met (Section 4.5).
- Zero “missed rebalance” incidents in the final 3 rebalances.

### Stage 3 — Live small capital
**Done when:**
- >= 3 months live operation with no critical incidents.
- Costs/slippage within expected bounds.
- All exports (ledger, tax lots) work.

### Stage 4 — Scale cautiously
- Only increase scale after:
  - persistent stability,
  - costs remain controlled,
  - no operational debt accumulation.

---

## 7) Economics, taxes, and sustainability controls

- Track performance **net of**:
  - slippage/fees,
  - fixed operational costs,
  - tax estimates (for awareness).
- Monitor “silent erosion” indicators:
  - spreads widen, slippage rises, turnover increases, drift vs expectations grows.
- Settlement cycle awareness: U.S. markets moved to T+1 (operational implications for cash availability; see References).
- Wash sale awareness: frequent re-entry can affect realized loss accounting (see References).

---

## 8) Stop/Revise/Retire criteria (operationalized)

**HALT + review triggers:**
- Max drawdown threshold breach.
- Unreconciled position/order mismatch persists beyond 24 hours.
- Data integrity failures or broker health failures that affect correctness.
- Performance deviates beyond pre-specified tracking bands for a full review window.

**RETIRE triggers:**
- Re-validation fails repeatedly after fixes.
- Edge exists only under unrealistic cost assumptions.
- Operational burden outweighs net returns.

---

## Appendix A — Pre-live checklist (short)

- Time frontier / anti-lookahead checks pass.
- PBO/overfitting diagnostics acceptable.
- Calendar early-close handling validated.
- Reconciliation pass rate 100% for last 3 rebalances.
- Kill switch drill successful.
- Backup/restore drill successful.

## References (primary / high-quality)

Execution & market microstructure
- NYSE Opening and Closing Auctions Fact Sheet (order entry cutoffs and cancellation rules): https://www.nyse.com/publicdocs/nyse/markets/nyse/NYSE_Opening_and_Closing_Auctions_Fact_Sheet.pdf
- NYSE Auctions Closing Process Fact Sheet (MOC/LOC mechanics): https://www.nyse.com/publicdocs/nyse/NYSE_Auctions_Closing_Process_Fact_Sheet.pdf
- Interactive Brokers glossary: Market-on-Close (MOC) order overview: https://www.interactivebrokers.com/campus/glossary-terms/market-on-close-order/

Settlement, taxes, compliance (operational awareness; not legal/tax advice)
- SEC statement on T+1 implementation (May 28, 2024): https://www.sec.gov/newsroom/press-releases/2024-62
- SEC small-entity compliance guide: shortened settlement cycle (Rule 15c6-1): https://www.sec.gov/investment/settlement-cycle-small-entity-compliance-guide-15c6-1-15c6-2-204-2
- IRS Publication 550 (Investment Income and Expenses), wash sales: https://www.irs.gov/pub/irs-pdf/p550.pdf
- Investor.gov wash sale definition: https://www.investor.gov/introduction-investing/investing-basics/glossary/wash-sales

Research foundations (context; not a guarantee of future returns)
- Daniel & Moskowitz, “Momentum Crashes,” Journal of Financial Economics (2016): https://www.kentdaniel.net/papers/published/jfe_16.pdf
- Bailey et al., “The Probability of Backtest Overfitting” (CSCV/PBO): https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf
- QuantConnect docs on time modeling / time frontier (anti-lookahead mental model): https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/time-modeling/timeslices

