# Governance Model

This document adapts the governance framework from the original
`Aycrith/Spice` repository to the enhanced planning repository.  It defines
roles, decision classifications, stage gates and review procedures to ensure
accountability and traceability.

## 1 Roles and responsibilities

| Role | Responsibilities |
| --- | --- |
| **Planning/Research Lead** | Owns the planning process, coordinates research, maintains plan documents, chairs design reviews and stage gates.  Final authority on moving from planning to implementation. |
| **Implementation Agent(s)** | Write code only after the plan passes Stage 2 acceptance.  Responsible for implementing the strategy exactly as specified and updating documentation when changes arise. |
| **Operator** | Executes the runbook, monitors trading operations, initiates incident response and reports anomalies to the Planning/Research Lead. |

## 2 Decision classifications

Decisions fall into two broad categories:

* **Strategy changes** – modifications that alter the behaviour, risk or timing of the strategy (e.g., changing the universe, ranking methodology, holding period or risk controls).  Strategy changes require a bump to the `strategy_version` and refreshed validation artefacts.
* **Operational changes** – modifications that affect how the existing strategy is executed (e.g., changing data providers, broker APIs, or runbook procedures) but do not alter the underlying strategy.  Operational changes may not require a `strategy_version` bump but must be documented in an ADR.

## 3 Stage gates and authority

The planning process is divided into stages.  Each stage has a gate that
requires sign‑off before proceeding.

1. **Stage 1 – Initial Research:** gather primary evidence and outline the plan.  Deliverables include `PLAN_PROPOSAL_v2.1.md`, `VALIDATION_MATRIX_v2.1.md` and `TRACEABILITY_INDEX_v2.1.md` in draft form.  **Approval:** Planning/Research Lead.
2. **Stage 2 – Validation & Acceptance:** complete validation tasks, resolve open questions and meet the acceptance criteria (`ACCEPTANCE_CRITERIA_v2.1.md`).  **Approval:** Planning/Research Lead.  Once approved, implementation may commence.
3. **Stage 3 – Implementation:** write code to execute the strategy.  Any deviations from the plan must be justified in an ADR and may require returning to Stage 2.
4. **Stage 4 – Operations:** operate the strategy according to the runbook.  Monitor performance, handle incidents and perform periodic reviews.  Changes discovered during operations may trigger updates to the plan and return to earlier stages.

## 4 Versioning

Plan documents use semantic‑style versioning (e.g., `v2.1`).  The minor
version increments when research or validation updates are made without
changing the strategy’s behaviour (e.g., clarifying documentation,
additional evidence).  The major version increments when a **strategy change**
occurs (e.g., new asset class, different ranking methodology).  Implementation
code must reference the specific strategy version it implements.  Historical
versions should be retained for auditability.

## 5 Review discipline

* **Summary of change:** every pull request or ADR must include a summary of
  what changed, the rationale and the evidence supporting it.  The summary
  should link to the Validation Matrix and Traceability Index.
* **Peer review:** at least one other contributor must review the change
  before merging.  For strategy changes, an external subject matter expert
  review is recommended.
* **Evidence requirement:** changes must reference primary sources (e.g.,
  exchange rules, regulatory filings, tax statutes).  Secondary sources can
  provide context but cannot alone justify a material change.
* **Audit trail:** decisions are recorded using the [ADR](adr/) format (Status,
  Context, Decision, Consequences).  Each ADR receives an incremental
  identifier.  Closed ADRs remain in the repository for historical
  reference.

## 6 Conflict resolution

If disagreement arises over a decision, the Planning/Research Lead facilitates
discussion.  If consensus cannot be reached, the final decision rests with
the Planning/Research Lead, who must document the rationale in an ADR.
