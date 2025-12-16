# Incident Response (Trading Operations)

This document defines incident handling for the locally-run trading system. It adapts a standard incident-response lifecycle (Preparation; Detection & Analysis; Containment/Eradication/Recovery; Post-Incident) to trading automation.

Reference lifecycle: NIST SP 800-61r3 (Incident Response Recommendations and Considerations for Cyber Risk Management, Apr 2025).
- Source: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf

## 1. Incident categories

1. **Operational scheduling**
   - Missed monthly rebalance run
   - Clock/timezone mismatch
2. **Data integrity**
   - Stale last-close data
   - Corporate action adjustment anomalies
   - Symbol/inception data violations
3. **Execution and brokerage**
   - Order rejected
   - Partial fills beyond tolerance
   - Unexpected order type behavior
4. **Cash/settlement**
   - Insufficient settled cash under T+1
   - Unexpected margin usage
5. **Security**
   - Credential exposure or suspected compromise
   - Unauthorized login/connected device

## 2. Severity levels

- **SEV-1 (Critical):** any condition that could place or keep the system in an unintended market exposure state, or indicates credential compromise.
- **SEV-2 (High):** material reconciliation breaks, repeated order rejects, or data staleness that would invalidate the run.
- **SEV-3 (Medium):** non-material deviations (e.g., reporting lag) with no exposure impact.

## 3. Lifecycle playbook

### 3.1 Preparation
- Ensure the Runbook checklists are current.
- Confirm backup/restore drills are within cadence.
- Confirm SAFE MODE / HALT semantics are understood and tested as drills.

### 3.2 Detection & Analysis
For each incident:
- Capture **Run ID**, timestamp, and last known system state.
- Identify whether the system is in **SAFE MODE**, **HALT**, or active trading mode.
- Determine scope:
  - affected symbol(s)
  - affected decision month
  - affected broker account(s)

### 3.3 Containment / Eradication / Recovery
- If exposure is uncertain or uncontrolled: **HALT immediately**.
- If data integrity is uncertain: **SAFE MODE** (no new orders) until validated.
- Recovery requires a documented decision on whether to:
  - retry the run (idempotent),
  - defer execution to next eligible time,
  - or exit to cash/defensive asset (if permitted by policy).

### 3.4 Post-incident activity
- Record a brief incident report:
  - timeline
  - root cause hypothesis
  - corrective action
  - validation test/drill added
- Update the Risk Register and Traceability Index.

## 4. Category-specific response checklists

### 4.1 Missed rebalance run (SEV-1/2 depending on exposure)
**Detection signals**
- No completed run record for the scheduled window
- Staleness alarms

**Immediate actions**
1. Enter SAFE MODE.
2. Determine current holdings vs intended holdings.
3. Decide whether a late run is allowed (per Runbook cutoffs).
4. If late execution is not allowed: document defer decision and lock.

**Validation after recovery**
- Add/verify a missed-run detection test and a “late-run policy” acceptance threshold.

### 4.2 Data staleness or adjustment anomaly (SEV-2)
**Immediate actions**
1. SAFE MODE.
2. Compare last-close timestamp against expected market close.
3. Cross-check against an independent reference (second data source or broker quotes).
4. If mismatch exceeds tolerance: block signals and log reconciliation break.

### 4.3 Order rejected (SEV-2)
**Immediate actions**
1. SAFE MODE.
2. Capture broker rejection reason and order parameters.
3. Confirm the order type is supported for the instrument.
4. Decide whether to resubmit with an allowed alternative order type.

**Post-actions**
- Open an ADR if this reveals a broker constraint not captured in planning.

### 4.4 Settlement / cash shortfall under T+1 (SEV-2)
**Immediate actions**
1. SAFE MODE.
2. Confirm settled cash vs required cash.
3. If shortfall persists: defer trade or reduce trade size per policy.

**Post-actions**
- Update cash buffer assumptions and validation criteria.

### 4.5 Credential compromise (SEV-1)
**Immediate actions**
1. HALT.
2. Revoke/rotate credentials.
3. Review broker login history and device authorizations.
4. Treat all recent runs as untrusted until verified.

**Post-actions**
- Add a security drill for credential rotation.
