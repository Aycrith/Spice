# Roadmap (Planning → Architecture → Implementation)

This roadmap is intentionally **planning-heavy**. The objective is to finish a research-backed, operationally realistic plan before any build work.

## Stage alignment

Stages are defined in `docs/quality/ACCEPTANCE_CRITERIA_v2.1.md`.

## Immediate focus: Research & Decision Lockdown (next iterations)

1. **Primary sources closure**
   - Verify exchange auction cutoffs and cancel/modify constraints (NYSE, Nasdaq).
   - Verify broker order type support and broker-side cutoffs (IBKR).
   - Verify settlement and funding impacts under U.S. T+1.
   - Verify wash sale mechanics that affect rotation strategies.

2. **Strategy research robustness**
   - Define CSCV/PBO methodology parameters and pass/fail thresholds.
   - Define momentum crash stress tests and HALT/SAFE MODE linkages.

3. **Architecture invariants**
   - Finalize conceptual interface contracts and ledger invariants.
   - Finalize runbooks and recovery drills for a single-machine operator model.

4. **Decision Records (ADRs)**
   - Broker choice and account type assumptions.
   - Data vendor(s) choice, adjustment policy, and timestamp discipline.
   - Timing convention: Close→Open (default) vs MOC/LOC (gated).

## Output discipline

Every roadmap item must update:
- the Validation Matrix,
- the Traceability Index,
- and (if needed) the Open Questions log.
