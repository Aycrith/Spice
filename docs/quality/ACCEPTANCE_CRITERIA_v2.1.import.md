# Acceptance Criteria v2.1

To progress from the planning stage to implementation, the following
quantifiable criteria must be satisfied.  These criteria form the stage gate
for **Stage 2**.  They derive from the research and controls documented in the
Plan Proposal and Validation Matrix.

## 1 Evidence and documentation completeness

| ID | Criterion | Threshold | Verification |
| --- | --- | --- | --- |
| AC1 | **Primary source coverage:** all regulatory, exchange and tax obligations affecting the strategy are documented in `docs/references/PRIMARY_SOURCES.md`. | 100 % of known obligations documented. | Conduct a checklist review; no outstanding open questions about regulations. |
| AC2 | **Plan coherence:** `PLAN_PROPOSAL_v2.1.md` covers universe, ranking, execution, risk, settlement, validation and crash mitigation. | All sections present and cross‑referenced in the Traceability Index. | Peer review; ensure each plan section has at least one citation in the index. |
| AC3 | **Validation Matrix completeness:** each risk or gap has evidence, plan linkage and validation method. | No blank cells in the matrix. | Inspect the Validation Matrix; confirm alignment with open questions list. |
| AC4 | **Traceability:** every plan assertion that constitutes a material decision is linked to evidence and a validation method. | 100 % traceability. | Random sampling audit; each assertion must cite the Validation Matrix. |

## 2 Model performance and robustness

| ID | Criterion | Threshold | Verification |
| --- | --- | --- | --- |
| AC5 | **Probability of Backtest Overfitting (PBO):** the in‑sample optimal model’s PBO must be low. | **PBO ≤ 0.05**【639029512866022†L590-L618】. | Implement CSCV; compute PBO; include results in an ADR. |
| AC6 | **Return distribution stability:** performance (CAGR, Sharpe ratio, max drawdown) is consistent across cross‑validation folds. | Relative standard deviation of metrics across folds ≤ 20 %. | Evaluate the distribution of performance metrics from CSCV. |
| AC7 | **Crash resilience:** maximum drawdown during historical crash periods does not exceed 1.5× the drawdown of the benchmark (e.g., SPY). | Drawdown ratio ≤ 1.5. | Backtest the strategy over known crash periods (e.g., 2008–09, 2020).  Document results. |

## 3 Operational readiness

| ID | Criterion | Threshold | Verification |
| --- | --- | --- | --- |
| AC8 | **Runbook completeness:** the runbook outlines pre‑trade, trade and post‑trade tasks, including funding, order submission and reconciliation. | All major steps documented with timings. | Review `RUNBOOK_v2.1.md`; ensure alignment with exchange cut‑offs【604093045262205†L93-L110】 and T+1 settlement【634620779460672†L263-L320】. |
| AC9 | **Incident response:** there is a documented incident response playbook addressing detection, containment, eradication and recovery. | Incident response document exists and covers common scenarios. | Review `INCIDENT_RESPONSE.md`; test run a tabletop exercise. |
| AC10 | **Security compliance:** no secrets are committed; local secrets management is implemented. | Zero secrets in repository; secure storage established. | Audit repository history; verify presence of a secrets management plan. |
| AC11 | **Open questions resolved:** all high‑priority open questions are addressed or deferred with justification. | No unresolved high‑priority open questions. | Review `OPEN_QUESTIONS_v2.1.md` and ADRs. |

## Process

1. The Planning/Research Lead coordinates the verification of each criterion.
2. Evidence for each criterion (e.g., PBO results, backtests, table top
   exercises) must be archived in the repository (e.g., in `docs/validation/`)
   and referenced in the relevant ADR.
3. Once all criteria are met, the Planning/Research Lead issues a Stage 2
   approval via an ADR, authorising implementation work.
