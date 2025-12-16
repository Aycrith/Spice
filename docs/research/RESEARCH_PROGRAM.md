# Research Program (Iterative)

This document defines how we will use targeted web research + structured validation to harden the plan before implementation.

The program is designed to keep documentation in version control and evolve it like code (Docs-as-Code). For background on the philosophy, see Write the Docs.
- Reference: https://www.writethedocs.org/guide/docs-as-code.html

## 1. Research loop (repeatable)

Each iteration ("research sprint") follows the same steps:

1. **Pick targets**
   - Select 1–3 items from `docs/validation/OPEN_QUESTIONS_v2.1.md` or from failed validation thresholds.
2. **Acquire evidence**
   - Prefer primary sources (exchange/broker/regulator/tax authority) over secondary write-ups.
3. **Extract constraints**
   - Convert evidence into explicit assumptions, cutoffs, and invariants.
4. **Update traceability**
   - Add/modify rows in the Validation Matrix.
   - Add entries to the Traceability Index.
5. **Lock decisions (if warranted)**
   - If evidence is sufficient, create/update an ADR and mark it Accepted.
6. **Strengthen validation**
   - Define or refine acceptance thresholds and drills.

## 2. Evidence capture standard

For each researched topic, capture:
- What was asked (question)
- Source(s) (link + date accessed)
- What the source *actually* says (short paraphrase)
- How it affects the plan (assumption update / rule / new risk)
- What would invalidate it (exceptions, boundary conditions)

## 3. Prioritized research lanes

1. **Execution realism**
   - Exchange cutoffs, order restrictions, broker cutoffs.
2. **Settlement and cash**
   - T+1 implications for cash availability and rotation timing.
3. **Tax mechanics**
   - Wash sale risks in rotation strategies.
4. **Research integrity**
   - PBO/CSCV configuration choices; time-frontier enforcement.
5. **Failure modes**
   - Momentum crash regime characterization and stress test design.

## 4. Required outputs per sprint

A sprint is only “done” if it produces at least one of:
- New/updated ADR
- Updated Validation Matrix row(s)
- Updated Acceptance Criteria threshold(s)
- New/updated Risk Register mitigation + drill

