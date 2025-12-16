# Plan Proposal v2.1 — Integrated Plan (Planning-Only)

**Document control**
- **System:** Personal, locally-run systematic trading system
- **MVP strategy:** Cross-Asset Momentum Rotation (monthly)
- **Plan version:** v2.1
- **Status:** Planning / architecture-ready (no implementation)

---

## 1. Scope Map

### 1.1 Strategy scope
**In-scope (core)**
1. Cross-Asset Momentum Rotation (monthly): rank a small ETF universe on trailing momentum; hold the top-ranked asset (or defensive asset if risk/filters require).
2. Single decision point per month: compute signal after the last trading day close; trade next trading day open (default).
3. Basic risk controls: max drawdown halt, execution safety checks, SAFE MODE / HALT state machine.
4. Research integrity: strict time-frontier enforcement; explicit overfitting controls (CSCV/PBO); stress tests for momentum crash regimes.

**Out-of-scope (non-goals for MVP)**
- Intraday trading, HFT, market making, options, leverage targeting, portfolio optimization, ML forecasting, multi-strategy ensembles.
- Continuous daily rebalancing or discretionary overrides (except emergency HALT).

**Optional extensions (explicitly non-core)**
- Volatility scaling, multi-asset sleeves, alternative defensive overlays, additional universes, dynamic lookback selection.

### 1.2 System scope (modules and boundaries)
**Module boundaries (conceptual; no code)**
1. Data → 2. Strategy → 3. Risk → 4. Execution → 5. Reconciliation/Ledger → 6. Reporting/Observability

### 1.3 Lifecycle scope (stages and gates)
- Stage 0 → Stage 1 → Stage 2 → Stage 3 → Stage 4 (see Acceptance Criteria)

---

## 2. Strategy Specification (MVP)

### 2.1 Universe
- **Universe type:** small, stable ETF set spanning major risk premia / macro exposures (equities, bonds, gold, cash-like).
- **Constraints (must be explicit in config):**
  - symbol list is versioned
  - each symbol must pass minimum history + data quality checks
  - inception constraints enforced (no pre-inception backtest data)

### 2.2 Signal definition
**Default**
- Cross-sectional momentum score: trailing total-return proxy over **12 months** (default) computed from adjusted prices or validated total-return series.
- Rebalance frequency: monthly
- Selection: hold top-ranked eligible asset; if none eligible, rotate to defensive asset.

**Decision lock**
Changing lookback / ranking method / universe / filters / cadence is a **Strategy Change** requiring:
- strategy_version bump
- refreshed robustness tests and validation artifacts

### 2.3 Filters
**Core filters**
1. Liquidity rule (configurable; explicit threshold definition)
2. Data integrity rule (reject stale/missing last-close data)

**Optional filter (gated)**
- Trend filter (e.g., price above MA) only if robust and not overfit

---

## 3. Timing and Execution (Real-World Constraints)

### 3.1 Default timing convention: Close → Open
- Decision time: after month-end close (after data availability confirmed)
- Execution time: next trading day open

**Operational rationale**
- Closing-auction order types have strict cutoffs and late cancel/modify restrictions; using Close→Open reduces operational fragility.

### 3.2 Execution order policy (core)
- Enter orders for the next open using broker-supported order types with explicit price-protection safeguards.
- Rejections or cutoff-risk events trigger SAFE MODE / HALT per policy.

### 3.3 Gated alternative timing: MOC/LOC month-end
Allowed only if:
- broker+venue cutoffs are verified and enforceable
- system can reliably place/cancel/adjust within windows
- pre-close health checks and cutoff timers exist

---

## 4. Research Integrity and Validation Methodology

### 4.1 Anti-lookahead time-frontier discipline (core)
Rule: signals may only use data available at the stated decision timestamp.

### 4.2 Overfitting controls: CSCV / PBO (core)
Requirement: compute PBO during research iteration; reject configurations exceeding the threshold.

### 4.3 Known failure modes: momentum crashes (core)
Requirement: stress-test crash-like regimes and explicitly connect outcomes to risk controls (HALT/SAFE MODE, defensive rotation).

---

## 5. Architecture Hardening (Conceptual Contracts + NFRs)

### 5.1 Conceptual contracts (no code)
- DataSnapshot: complete, monotonic timestamps, reproducible hash
- SignalRecord: deterministic given snapshot + config
- DecisionRecord: idempotent keyed by (strategy_version, rebalance_month, snapshot_hash)
- ExecutionPlan: orders with safety bounds + cutoff schedule
- TradeLedger: immutable append-only
- ReconciliationReport: breaks categorized, pass/fail

### 5.2 Nonfunctional requirements (local-first)
- Reliability: deterministic runs, restart-safe, idempotent rebalance
- Observability: structured logs, run IDs, staleness + reconciliation metrics
- Security: secrets isolation, least privilege, tamper-evident logs
- Auditability: trade → decision → snapshot traceability
- Performance: bounded runtime on a single workstation

---

## 6. Tax, Settlement, and Cash Mechanics

- Settlement (T+1) and broker buying-power rules must be verified for the actual account type (cash vs margin).
- Wash sale exposure must be understood; at minimum flag potential 30-day windows for awareness and reporting completeness.

---

## 7. Required Embedded Traceability
The following documents are normative and must remain consistent with this plan:
- Validation Matrix: `docs/validation/VALIDATION_MATRIX_v2.1.md`
- Traceability Index: `docs/validation/TRACEABILITY_INDEX_v2.1.md`
- Open Questions: `docs/validation/OPEN_QUESTIONS_v2.1.md`
- Risk Register: `docs/risk/RISK_REGISTER_v2.1.md`

## References
- Primary operational and research sources: `docs/references/PRIMARY_SOURCES.md`
