# Research Backlog

This backlog is the planning-time queue of evidence gathering and validation tasks. Each item should map to an Open Question ID and/or a Validation Matrix row.

## High priority (execution, settlement, tax)

1. **NYSE MOC/LOC and cancellation windows**
   - Confirm entry, modification, cancellation rules and edge cases.
   - Output: Validation Matrix updates + timing convention ADR.

2. **Nasdaq open/close cross deadlines (MOO/MOC, LOO/LOC)**
   - Confirm cutoffs and reject behavior.
   - Output: Validation Matrix updates + alternative venue constraints.

3. **IBKR broker-side cutoffs and order type availability**
   - Confirm what is supported in the chosen account/channel (TWS, Client Portal, API).
   - Output: ADR: broker capability + operational constraints.

4. **T+1 cash availability constraints for retail brokerage accounts**
   - Confirm how unsettled funds affect ability to re-deploy capital in monthly rotation.
   - Output: updated cash buffer assumptions + acceptance thresholds.

5. **Wash sale risk boundaries for ETF rotations**
   - Clarify “substantially identical” risk for candidate ETFs and defensive sleeves.
   - Output: tax constraint ADR + mitigation options.

## Medium priority (research integrity)

6. **CSCV/PBO parameterization**
   - Choose partitions, metric, and rejection threshold; document rationale.
   - Output: acceptance criteria thresholds + validation row updates.

7. **Time frontier and data timestamp discipline**
   - Confirm chosen data vendor timestamps and availability; define “safe timestamp.”
   - Output: data availability assumptions + conformance thresholds.

## Medium priority (risk controls)

8. **Momentum crash stress test design**
   - Define what constitutes a crash episode and what “pass” means for the system.
   - Output: halt/SAFE MODE policy tie-in + acceptance criteria.
