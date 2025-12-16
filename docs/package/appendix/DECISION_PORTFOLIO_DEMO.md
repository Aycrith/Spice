# Decision Portfolio Demo (No-cost Proof of Concept)

This appendix defines the **Decision Portfolio Demo** path introduced by ADR 0007.

## Purpose

Demonstrate that the system can:
- ingest market data (free/legal sources or local CSVs)
- compute deterministic signals
- produce deterministic, replayable **DecisionRecords**
- generate an **ExecutionPlan**
- simulate execution (SimBroker) and maintain an append-only ledger
- reconcile and report pass/fail

This provides **real value** (repeatable decision sessions + traceable artifacts) without requiring a funded brokerage account or paid services.

## What it is / is not

- **Is:** a deterministic decision + evidence pipeline; a portfolio of decisions with simulated execution and an equity curve.
- **Is not:** proof of real broker cutoffs, order acceptance rates, or real-world slippage. Those remain Stage 2+ concerns.

## Where the demo lives

Implementation is intentionally **not committed** in this planning repository while Stage < 2.

A local sandbox reference implementation is placed under:

- `tmp/spice-impl/`

This folder is ignored by git (see `.gitignore`) and is safe for local iteration.

## Expected outputs

For each monthly decision session:
- `config.json` (config used)
- `snapshot.json` (snapshot hash + metadata)
- `signal.json` (momentum scores)
- `decision.json` (DecisionRecord + decision key)
- `execution_plan.json`
- `ledger.jsonl` (append-only events)
- `reconciliation.json` (pass/fail)

For a backtest run:
- `run_config.json` (range + config hash)
- `summary.json` (equity curve + final equity)
- `ledger.jsonl` (events)

## Demo acceptance checks (POC quality gate)

A demo run is acceptable if:
1. **Determinism:** same inputs → identical DecisionRecord key.
2. **Idempotency:** rerunning the same month does not append duplicate ledger events.
3. **Traceability:** each ledger run references `config_hash` + `snapshot_hash`.
4. **Reconciliation:** report is generated and is `ok=true` under nominal simulation.

## Linkage to the plan

- Plan invariants: `docs/quality/ACCEPTANCE_CRITERIA_v2.1.md`
- Contracts: `docs/plan/PLAN_PROPOSAL_v2.1.md` §5.1
- Demo decision: `docs/adr/0007-no-cost-proof-of-concept-demo-path.md`
