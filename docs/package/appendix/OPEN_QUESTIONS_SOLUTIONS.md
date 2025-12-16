# Open Questions v2.1 — Solutions Playbook (Low/No-Cost Proof of Concept)

This document proposes **legal, low/no-cost** resolution paths for the blockers in `docs/validation/OPEN_QUESTIONS_v2.1.md`.

**Important constraint:** The repo sponsor requested a proof-of-concept with **no paid services** and **no injected trading funds**. This can support a strong “Decision Portfolio Demo” (deterministic decisions + simulated execution), but may not satisfy Stage 2/3 criteria that require real broker conformance.

**Important compliance note:** This project will not use piracy, stolen credentials, or ToS-violating scraping. The goal is “free and open” via **lawful** sources and replaceable adapters.

---

## P0-1 Broker / account type (cash vs margin)

### Decision needed
- Select broker *for Stage 2+ conformance* and decide account type.

### Low/no-cost solution paths
1. **Path A (POC now): SimBroker (no external broker)**
   - Implement a broker adapter that simulates:
     - order submission and acceptance/rejection
     - fills at next-open with configurable slippage/spread model
     - account state snapshots (positions/cash) derived from fills
   - What it achieves: end-to-end “live-action” decision sessions and an auditable ledger **without funding**.
   - What it does *not* achieve: Stage 2 metrics that depend on real broker reject codes/cutoffs and reconciliation against real broker reports.

2. **Path B (later): real broker paper account (free if available)**
   - Candidate brokers that might offer free paper trading APIs exist, but **must be verified** via primary sources before lock-in.
   - Verification method: broker docs + account creation test + test orders; then lock via ADR 0002.

### Recommended action (stage-consistent)
- Treat **SimBroker as an Operational tooling choice** to unblock the demo while keeping ADR 0002 “Broker selection” open.

### Validation
- Demo acceptance: deterministic ledger generation and reproducible reports.
- Stage 2 acceptance (future): order acceptance ≥99% and reconciliation ≥99% (Acceptance Criteria Stage 2).

---

## P0-2 Data provider (adjusted prices + timestamp semantics)

### Decision needed
- Choose a primary data source and define:
  - adjustment policy (splits/dividends)
  - time-frontier / availability semantics

### Low/no-cost solution paths (legal)
1. **Free EOD market data feeds (CSV/API) + multi-source QA**
   - Use a free source for daily OHLCV (and adjusted close if provided).
   - Add a second free “reference” source for spot checks on corporate actions and large return jumps.
   - Critical: record *availability time* separately from bar timestamp to prevent lookahead (Plan §4.1; Risk R‑01).

2. **Operator-maintained dataset (“vendorless mode”)**
   - Acquire daily bars manually from lawful sources, store locally, and run the system offline.
   - Pros: no service dependency.
   - Cons: operational overhead; must maintain provenance.

### Recommended action
- Implement the Data subsystem to accept **multiple providers** and enforce the Stage 0 availability suite regardless of provider.

### Validation
- Stage 0: availability tests pass; no timestamp leakage; data QA passes ≥99% of days in 90-day sample (Acceptance Stage 0).

---

## P0-3 Venue + broker cutoffs for chosen order types

### Decision needed
- Confirm cutoffs and enforceability for the intended order types.

### Low/no-cost solution paths
1. **POC now:** keep Close→Open (default) and implement cutoff windows as configuration.
   - Cutoffs are still relevant in “demo” to ensure the scheduler is designed correctly.

2. **Paper/live:** verify cutoffs using the primary sources already indexed (`docs/references/PRIMARY_SOURCES.md`) and paper tests.

### Validation
- Demo: scheduler enforces the configured submission window and records “would-have-missed” events.
- Stage 2: order acceptance ≥99% with documented cutoff compliance.

---

## P0-4 Exact ETF universe + minimum history

### Decision needed
- Lock the MVP ETF universe list and eligibility rules.

### Low/no-cost solution approach
- Choose a **small, stable ETF set** with:
  - long history (supports 12-month lookback)
  - high liquidity
  - broad macro exposure coverage (equities, duration, gold, cash-like)
- **Do not assume** specific tickers are acceptable until you verify inception dates and data availability.

### Verification method
- Produce a universe dossier:
  - inception dates
  - liquidity metrics
  - data coverage results under the chosen provider
- Lock via ADR 0005.

---

## P1 Defensive asset and fallback behavior

### Decision needed
- Define the defensive asset and the fallback behavior under stress (rotate to defensive vs hold prior vs HALT).

### Low/no-cost solution approach
- Keep the decision logic as a config parameter and validate via crash-regime stress tests.

### Validation
- Stage 1: crash-stress evaluation includes defensive logic and ties to SAFE MODE/HALT policy.

---

## P1 PBO threshold and search scope

### Decision needed
- Set CSCV/PBO configuration and PBO rejection threshold.

### Low/no-cost solution approach
- Implement CSCV/PBO locally (no services needed) and lock:
  - the parameter search space
  - number of trials
  - partitions
  - threshold

### Verification method
- Run pilot CSCV/PBO across a small set of candidate parameterizations and record results in the Stage 1 PBO report.
- Lock via ADR 0006.

---

## P1 Account context + wash-sale posture

### Decision needed
- Decide whether the intended account is taxable or IRA and what minimum tax reporting/flagging is required.

### Low/no-cost solution approach
- For the demo: implement **wash-sale flagging as optional** (config toggle) and treat it as informational.
- For live: finalize account context and required reporting.

### Verification method
- Review IRS Pub 550 (already indexed in PRIMARY_SOURCES) and define a minimal, testable reporting output.

---

## P2 Conformance drift thresholds

### Decision needed
- Define numeric tolerance bands for “paper/live vs backtest drift.”

### Low/no-cost solution approach
- For the demo: define drift measures for the simulated execution model (slippage model vs backtest assumptions).
- For Stage 2: empirically set thresholds from paper results and document in Acceptance Criteria.

---

## Summary recommendation

- **Unblock the proof-of-concept immediately** with a SimBroker + free/legal data adapters while preserving the plan’s intent and keeping P0 broker selection open for Stage 2.
- Continue to treat broker/data/cutoff decisions as ADR-governed lock-ins backed by primary sources.
