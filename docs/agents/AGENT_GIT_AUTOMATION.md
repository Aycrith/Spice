# Agent Git Automation (No Human Review)

This repository is designed so that **agents** can own the full Git lifecycle:

- create branches
- commit and push
- open pull requests
- run validation/review checks
- merge to `main`

Human review is not required by default; **CI guardrails are the reviewer**.

## How it works

1. **Agents push a branch** (e.g., `docs/...`, `chore/...`).
2. GitHub Actions **auto-opens a PR** to `main` via `.github/workflows/agent-auto-pr.yml`.
3. Two CI suites act as the review gate:
   - `Guardrails (planning-only)` (stage gating, root-file/binary blocking)
   - `Docs CI (agent review)` (required artifacts, traceability gate, local link validation)
4. If the PR has label `automerge` (auto-applied), GitHub Actions **merges it automatically** once checks are green via `.github/workflows/agent-automerge.yml`.

## Agent responsibilities

Agents must:

- Preserve non-negotiables:
  - planning-first until Stage 2 (`docs/quality/STAGE_STATUS.md`)
  - no intent drift: MVP remains Cross-Asset Momentum Rotation (monthly)
  - traceability discipline
- Keep changes small and verifiable.
- If CI fails, the agent fixes the PR until green.

## Merge policy

- Merge method: **squash** (keeps history readable, reduces noise).
- Auto-merge happens only when:
  - PR targets `main`
  - PR is labeled `automerge`
  - required CI checks succeed
  - GitHub reports no merge conflicts

## If something needs manual intervention

The only acceptable reasons are external to the repo:

- missing GitHub repository permissions for Actions (rare)
- branch protection settings that explicitly require human review
- missing credentials to push branches

All of these are resolved by the one-time permissions bootstrap in `AGENT_PERMISSIONS.md`.
