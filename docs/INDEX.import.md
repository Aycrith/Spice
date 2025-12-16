# Documentation Index

This index guides contributors through the planning artifacts in this repository.  The documents are
organized by purpose (plan, validation, operations, references, governance).  Read them in the order
listed below to understand the proposed strategy and the evidence supporting it.

## 1. Plan

| Document | Purpose |
| --- | --- |
| `docs/plan/PLAN_PROPOSAL_v2.1.md` | Integrated proposal for the cross‑asset momentum rotation strategy.  Defines the universe, ranking rules, timing convention, risk policy and monthly rebalance procedure. |
| `docs/config/CONFIG_SCHEMA_CONCEPTUAL_v2.1.md` | Conceptual configuration schema capturing all tunable parameters (universe, lookback windows, filters).  Used to document any strategy changes and version bumps. |

## 2. Validation & Traceability

| Document | Purpose |
| --- | --- |
| `docs/validation/VALIDATION_MATRIX_v2.1.md` | Matrix linking findings (risks/gaps) to evidence sources, plan changes and validation methods.  Use this to trace every material change. |
| `docs/validation/TRACEABILITY_INDEX_v2.1.md` | Index mapping plan sections to evidence and validation methods.  Serves as a cross‑reference between the plan and supporting research. |
| `docs/validation/OPEN_QUESTIONS_v2.1.md` | Log of unresolved questions with proposed research paths and responsible parties. |

## 3. Quality & Acceptance

| Document | Purpose |
| --- | --- |
| `docs/quality/ACCEPTANCE_CRITERIA_v2.1.md` | Defines the stage gate criteria for progressing from planning to implementation.  Each gate includes measurable thresholds derived from validation. |

## 4. Operations

| Document | Purpose |
| --- | --- |
| `docs/ops/RUNBOOK_v2.1.md` | Operational runbook for the monthly rebalance process, including order preparation, funding, execution, and post‑trade checks. |
| `docs/ops/INCIDENT_RESPONSE.md` | Incident response playbook aligned with the NIST lifecycle for handling trading incidents, including detection, containment, and recovery. |

## 5. Governance

| Document | Purpose |
| --- | --- |
| `docs/adr/` | Architectural Decision Records (ADRs).  Each material decision must be captured using a Nygard‑style ADR (Status, Context, Decision, Consequences). |
| `docs/governance.md` | Overview of roles, decision classifications, stage gate authority, versioning rules, and review discipline.  Adopted from the original governance document. |

## 6. References

| Document | Purpose |
| --- | --- |
| `docs/references/PRIMARY_SOURCES.md` | Curated list of primary evidence (exchange auction rules, broker order deadlines, SEC/FINRA regulations, tax publications, academic papers).  Each source includes a citation with context lines. |
| `docs/references/SECONDARY_SOURCES.md` | Secondary references (blog posts, articles) used for context but not authoritative. |

Please refer to `AGENTS.md` in the root directory for the agent operating contract.  Contributions must
follow the docs‑as‑code workflow described in `CONTRIBUTING.md` and respect the security guidelines
in `SECURITY.md`.