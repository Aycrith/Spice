# Security

This project is intended to run on a **single workstation** and interact with brokerage infrastructure. Security requirements are therefore practical and operational.

## Secrets handling

- **Never commit secrets** (API keys, tokens, session cookies, account numbers, statements). See `.gitignore`.
- Store secrets locally in one of the following:
  - OS credential store, or
  - encrypted secret file (local-only), or
  - environment variables loaded at runtime (later),
  - with strict access controls.

## Auditability and tamper evidence

- All trading decisions must be traceable to immutable inputs (snapshot hash + decision record).
- Logs should be treated as evidence; tamper-evidence (hash chaining) is recommended once implementation begins.

## Incident response alignment

Operational incident response should follow a structured lifecycle (Preparation; Detection/Analysis; Containment/Eradication/Recovery; Post-Incident Activity), consistent with NIST incident response guidance.

See `docs/ops/INCIDENT_RESPONSE.md` for trading-specific incident playbooks.
