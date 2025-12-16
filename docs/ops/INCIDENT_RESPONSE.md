# Incident Response (Trading Operations)

This document maps trading-system incidents to an incident lifecycle aligned with NIST guidance. citeturn0search25

## 1) Preparation
- Define SAFE MODE / HALT semantics in the Runbook.
- Ensure backups + restore drills are scheduled.
- Ensure monitoring/alerts exist for: missed runs, stale data, order rejects, reconciliation breaks.

## 2) Detection and analysis
**Signals**
- data staleness flags
- broker reject codes
- reconciliation breaks
- conformance drift beyond thresholds

**First questions**
- Is this a data issue, broker issue, or logic issue?
- Is there risk exposure that must be reduced immediately?

## 3) Containment, eradication, and recovery
- Enter SAFE MODE or HALT as appropriate.
- Stop opening new positions until invariants are restored.
- Recover by replaying the last run deterministically from stored inputs.

## 4) Post-incident activity
- Record a short incident report (what happened, why, how prevented).
- Update Validation Matrix and (if needed) an ADR.

