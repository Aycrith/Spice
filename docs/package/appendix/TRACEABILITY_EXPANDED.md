# Expanded Traceability Mapping (Requirements → Plan → Modules → Validation)

This appendix extends the canonical `docs/validation/VALIDATION_MATRIX_v2.1.md` by providing stable requirement IDs (FR/NFR/C) and mapping them to:
- plan elements (file + section)
- proposed implementation modules
- validation artifacts (tests, drills, checklists)

> The Validation Matrix remains the *authoritative* traceability artifact. This is a convenience map for multi-agent execution.

---

## Requirements inventory (expanded)

| ID | Type | Requirement (summary) | Plan element (source) | Proposed modules | Validation artifact(s) |
|---|---|---|---|---|---|
| FR-001 | FR | Monthly decision cadence; Close→Open default | `PLAN_PROPOSAL_v2.1` §1.1, §3.1; ADR 0004 | Scheduler/Runner; Strategy; ExecutionPlanner | Runbook monthly checklist; E2E monthly run test; deterministic key test |
| FR-002 | FR | Momentum ranking (12m default) | `PLAN_PROPOSAL_v2.1` §2.2 | Strategy Engine | Unit tests for scoring; golden-file snapshots |
| FR-003 | FR | Defensive fallback | `PLAN_PROPOSAL_v2.1` §2.2; config §2.2 | Strategy; Risk | Scenario tests including empty-eligibility |
| FR-004 | FR | Data QA gates pre-decision | `PLAN_PROPOSAL_v2.1` §2.3; `RUNBOOK` §3.2 | Data QA | Stage 0 QA suite; missing-bar and jump tests |
| FR-005 | FR | Time-frontier enforcement | `PLAN_PROPOSAL_v2.1` §4.1; Acceptance invariant #1; Risk R-01 | Data; Strategy | Stage 0 availability suite; timestamp leakage tests |
| FR-006 | FR | CSCV/PBO gate | `PLAN_PROPOSAL_v2.1` §4.2; Acceptance Stage 1; ADR 0006 | Research Tools | Stage 1 PBO report; locked search-scope policy |
| FR-007 | FR | SAFE MODE/HALT state machine | config §2.5; `RUNBOOK` §2; Acceptance invariant #4 | Risk Engine; Runner | State transition tests; incident playbook drills |
| FR-008 | FR | ExecutionPlan with bounds + schedule | plan §5.1; config §2.4 | ExecutionPlanner | Unit tests for bounds; cutoff window enforcement tests |
| FR-009 | FR | Append-only ledger | plan §5.1; Validation Matrix “Ledger” | Ledger | Ledger immutability tests; event schema checks |
| FR-010 | FR | Reconciliation report pass/fail + breaks | `RUNBOOK` §3.5; Acceptance Stage 2 | Reconciliation | Break injection test; Stage 2 reconciliation pass-rate metric |
| NFR-001 | NFR | Planning-only compliance pre-Stage2 | `STAGE_STATUS`; `BRANCHING_STRATEGY` | Repo guardrails | CI guardrails workflow (already present) |
| NFR-002 | NFR | Deterministic replay | `SYSTEM_OVERVIEW`; plan §5.2; Acceptance invariants #2–#3 | Core Domain | Determinism test suite; hash repeatability |
| NFR-003 | NFR | Idempotent scheduling | `RUNBOOK` §1 | Runner | Re-run safety tests; idempotency property tests |
| NFR-004 | NFR | Audit trail | Acceptance invariant #2 | Ledger; Reporting | Trace linkage tests: order→decision→snapshot |
| NFR-005 | NFR | Secrets isolation | `SECURITY.md` | Secrets | secret scanning + rotation drill |
| NFR-006 | NFR | Local-first ops + restore drills | plan §5.2; `RUNBOOK` §5; Stage 0 | Ops | Backup/restore drill; offline restore evidence |
| NFR-007 | NFR | Observability | plan §5.2; config §2.8 | Observability | log schema tests; metrics smoke checks |
| C-001 | C | MVP locked (no drift) | `README.md`; `AGENTS.md` | Governance | ADR + Validation Matrix checks |
| C-002 | C | Strategy change classification & versioning | `GOVERNANCE.md`; config §3 | Governance | PR template enforcement; strategy_version bump checks |
| C-003 | C | No binaries in git | `BRANCHING_STRATEGY.md`; `.gitignore` | Repo hygiene | CI check + gitignore |
| C-004 | C | No-cost PoC constraint (sponsor) | sponsor instruction (2025-12-16) | Demo stack | Demo checklist; reproducible decision ledger |

---

## Multi-agent ownership boundaries (recommended)

- **Data QA Agent:** owns FR-004/FR-005/Stage 0 QA suite.
- **Research Integrity Agent:** owns FR-006 (CSCV/PBO) + Stage 1 robustness reports.
- **Execution Agent:** owns FR-008 and broker adapter contract.
- **Ledger/Reconciliation Agent:** owns FR-009/FR-010 and Stage 2 reconciliation criteria.
- **Ops Agent:** owns NFR-006 and drills.
- **Governance Agent:** owns NFR-001/C-001/C-002/C-003 plus doc coherence.
