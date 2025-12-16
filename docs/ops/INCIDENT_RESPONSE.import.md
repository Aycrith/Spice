# Incident Response Playbook

This playbook outlines procedures for detecting, containing, eradicating and
recovering from incidents that may occur during the operation of the trading
system.  It is aligned with the **NIST Computer Security Incident Handling
Guide** and the security principles in `SECURITY.md`【813758299569681†L4-L22】.  The
goal is to ensure rapid response and minimise impact on capital and data.

## 1 Incident definition

An **incident** is any event that threatens the confidentiality, integrity or
availability of the trading system or results in unexpected financial loss.  Examples:

* Compromise of account credentials or API keys
* Execution of incorrect orders or double executions
* Failure to settle trades due to funding shortfall
* Data corruption or loss (e.g., price feed outage)
* Regulatory or tax compliance breach

## 2 Roles

| Role | Responsibility |
| --- | --- |
| **Operator** | Primary on‑call responder; executes the runbook and monitors the system. |
| **Planning/Research Lead** | Coordinates analysis, approves remediation decisions, updates ADRs and documentation. |
| **Security Officer** (optional) | Manages secrets, verifies logs, and liaises with external parties (broker, bank). |

## 3 Response stages

1. **Preparation** – maintain up‑to‑date documentation, backups, and contact information.  Conduct periodic training and tabletop exercises.
2. **Detection & analysis** – identify the incident via monitoring alerts, broker messages or manual observation.  Gather evidence (logs, screenshots, broker communications).  Classify the incident (e.g., security breach, operational error, regulatory issue).
3. **Containment** – take immediate steps to limit damage.  Examples:
   * Disable compromised accounts; reset credentials.
   * Cancel erroneous orders or halt trading.
   * Place the portfolio into capital preservation mode if drawdown triggers are met.
4. **Eradication & recovery** – remove the root cause (e.g., malware, misconfiguration).  Restore data from backups if necessary.  Resume normal trading only after verifying that the system is secure and compliant.
5. **Post‑incident activities** – conduct a post‑mortem to analyse the cause, impact and response effectiveness.  Document findings in an ADR and update the runbook, security procedures and training.

## 4 Communication plan

* Maintain a list of contact methods for the broker, bank, data provider and any advisors.
* During an incident, promptly communicate the situation and mitigation steps to all stakeholders.  Use secure channels (e.g., encrypted email, phone).
* If sensitive data may have been exposed, follow breach notification requirements in applicable jurisdictions.

## 5 Record keeping

* Retain all logs and incident artefacts (e.g., order confirmations, error messages) for at least 24 months.
* Record every action taken during the incident with timestamps.  Use immutable, time‑stamped logs.
* Ensure that secrets (e.g., API keys) are never included in incident documentation【813758299569681†L4-L22】.

## 6 Review and updates

This playbook should be reviewed at least annually or after any significant
incident.  Updates may be required when regulations change, new tools are
introduced or lessons are learned from tabletop exercises.  All updates must
be captured in an ADR and summarised in the Validation Matrix and
Traceability Index.
