# ACCEPTANCE_CRITERIA v2.1 — Phase Gates and Go/No-Go Rules (Planning-Only)

**Last updated:** 2025-12-15

## Cross-cutting invariants (always)
1. Time-frontier integrity: no signal uses data unavailable at decision time.
2. Traceability: every order traces to DecisionRecord + DataSnapshot hash.
3. Idempotency: rerunning month’s rebalance produces identical DecisionRecord.
4. Safety: failed invariant → SAFE MODE/HALT.

## Stage 0 — Data + operational foundation
**Pass**
- Data QA passes on ≥99% of days in 90-day sample; failures alert.
- Availability tests show no lookahead.
- Backup + restore drill reproduces hashes and reconciliation.

**No-go**
- Any unexplainable timestamp leakage
- Restore drill failure

## Stage 1 — Backtest realism + robustness
**Pass**
- Conservative cost model applied + sensitivity tested.
- Robustness across reasonable variants.
- CSCV/PBO gate passes under threshold.
- Crash-regime stress tests evaluated; risk controls tied to outcomes.

**No-go**
- PBO above threshold
- Knife-edge dependency

## Stage 2 — Paper trading conformance
**Pass**
- Reconciliation pass rate ≥99% (breaks resolved within 24h).
- Order acceptance rate ≥99% with documented cutoff compliance.
- Performance drift vs backtest within tolerance bands for ≥6 consecutive months.

**No-go**
- Repeated cutoff rejects
- Persistent unexplained drift beyond tolerance

## Stage 3 — Small-cap live readiness
**Pass**
- ≥3 consecutive live months with: zero missed rebalances, zero unresolved breaks, stable ops metrics.
- Settlement/tax workflows validated for actual account type.

**No-go**
- Any silent-failure missed-run
- Broker constraints prevent intended sequencing

## Stage 4 — Scaling
**Pass**
- Governance discipline maintained; drift monitoring stable.
- Increased notional does not degrade execution beyond modeled bands.

**No-go**
- Liquidity/slippage worsens materially with size
- Operational burden unsustainable on single workstation
