# Research Program (Iterative, Evidence-First)

## 1) Operating method
This project uses a documentation-first operating model (“Docs as Code”), where planning artifacts are versioned and reviewed like code. citeturn0search5turn0search17

## 2) Research loop (repeatable)
1. **Select a claim** from `docs/validation/OPEN_QUESTIONS_v2.1.md` or a Validation Matrix row.
2. **Acquire primary sources** (exchange/broker/regulator/tax authority) and add them to `docs/references/PRIMARY_SOURCES.md`.
3. **Extract operational constraints** (cutoffs, order restrictions, settlement behavior, tax rules).
4. **Update traceability:**
   - Validation Matrix: evidence + limitations + risk if wrong + acceptance thresholds
   - Traceability Index: finding → evidence → plan change → validation
5. **Lock decisions via ADRs** when appropriate. citeturn0search12turn0search0

## 3) What “done” looks like for a research item
A research item is complete only when:
- evidence is primary/authoritative (or a verification experiment is defined)
- the plan is adjusted to reflect the constraint
- acceptance tests/drills are specified

