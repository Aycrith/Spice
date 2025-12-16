# Security

This project is intended to run locally. Security here primarily means **protecting broker credentials, preserving auditability, and preventing silent failure**.

## 1) Secrets handling
- Never commit secrets. Use `.env` (excluded by `.gitignore`) and a dedicated `secrets/` directory (also ignored).
- Prefer least-privilege credentials and account-level restrictions.

## 2) Auditability and integrity
- Maintain tamper-evident logs (e.g., hash chaining) and immutable ledgers.
- Preserve decision provenance (DataSnapshot/DecisionRecord hashes) for post-incident analysis.

## 3) Incident response model
Use an incident lifecycle aligned to NIST incident response guidance (Preparation; Detection/Analysis; Containment/Eradication/Recovery; Post-Incident Activity). citeturn0search25

Trading-specific incidents include:
- data staleness / corruption
- broker outage or order rejects
- reconciliation breaks
- unexpected strategy behavior (drift vs backtest)

Runbook mapping is documented in `docs/ops/INCIDENT_RESPONSE.md`.

