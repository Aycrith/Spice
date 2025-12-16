# Integration Guide — Mapping v2.1 Artifacts Into the Existing Plan Set

**Last updated:** 2025-12-15

## 1. Current files detected (legacy inputs preserved)
The following source plan files were imported into `docs/legacy/` for provenance:
- `planproposal.md`
- `planproposal_v2.md`
- `RUNBOOK.md`
- `ACCEPTANCE_CRITERIA.md`
- `CONFIG_SCHEMA.md`

## 2. New canonical documents (v2.1)
These are the documents implementation agents should treat as the current source of truth:

| Canonical purpose | New file | Notes |
|---|---|---|
| Integrated plan | `docs/plan/PLAN_PROPOSAL_v2.1.md` | Consolidates strategy+architecture+validation requirements |
| Runbook | `docs/ops/RUNBOOK_v2.1.md` | SAFE MODE/HALT + monthly ops |
| Config schema | `docs/config/CONFIG_SCHEMA_CONCEPTUAL_v2.1.md` | Change classification + invariants |
| Acceptance criteria | `docs/quality/ACCEPTANCE_CRITERIA_v2.1.md` | Stage gates + go/no-go |
| Risk register | `docs/risk/RISK_REGISTER_v2.1.md` | Likelihood/impact + drills |
| Validation matrix | `docs/validation/VALIDATION_MATRIX_v2.1.md` | Primary traceability mechanism |
| Open questions | `docs/validation/OPEN_QUESTIONS_v2.1.md` | Resolution paths |
| Traceability index | `docs/validation/TRACEABILITY_INDEX_v2.1.md` | Change log backbone |
| ADR template | `docs/adr/0000-adr-template.md` | Governs decision capture |

## 3. How v2.1 integrates with your existing plan structure
1. **Plan proposal evolution**
   - Your `planproposal.md` (candidate strategy shortlist and broader exploration) remains useful as *ideation and provenance*.
   - Your `planproposal_v2.md` represents an intermediate hardening pass.
   - **v2.1 becomes the canonical “architecture-ready” plan** with explicit gates, risks, and traceability.

2. **Runbook / Acceptance / Config alignment**
   - The v2.1 runbook, acceptance criteria, and config schema are aligned as a “triad”:
     - Acceptance defines *what must be true to advance*
     - Runbook defines *how the system is operated safely*
     - Config schema defines *what is allowed to change and how changes are governed*
   - Implementation agents should treat contradictions between these as defects to log and resolve via ADR.

3. **Traceability as the repo’s spine**
   - The Validation Matrix is the primary mapping from plan elements to evidence, risk, and validation thresholds.
   - The Traceability Index functions as a lightweight change log tied to concrete validation.

## 4. Practical governance workflow (planning-only)
- Add an ADR when you lock:
  - timing convention (Close→Open vs MOC/LOC)
  - broker/account type choice
  - universe symbol set and defensive asset
  - PBO threshold and search scope
- Update Validation Matrix rows impacted by each ADR.
- Ensure the Risk Register contains a validation drill for each High-impact risk.
