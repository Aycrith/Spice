# Agent Permissions (One-time bootstrap)

Goal: future agents can operate without repeated human intervention.

## What needs permission

Agents need two capability buckets:

1. **Local push permission** (from the IDE environment)
   - Agents must be able to `git push` branches to `origin`.
   - This is the only capability required locally.

2. **PR/merge permission** (inside GitHub)
   - Handled by GitHub Actions using the repository `GITHUB_TOKEN`.
   - This repo provides workflows to open PRs and merge PRs automatically.

## One-time setup (recommended)

### A) Configure push credentials once

Use one of:

- SSH key authenticated against GitHub for the agent identity, or
- GitHub Credential Manager (HTTPS) for the agent identity.

After setup, verify agents can:

- `git fetch`
- `git push` to `https://github.com/Aycrith/Spice.git`

### B) Ensure GitHub Actions has sufficient permissions

Repository setting (GitHub UI):

- Settings → Actions → General → Workflow permissions
  - Select **Read and write permissions**
  - (Optional) allow Actions to create and approve pull requests

These permissions allow the automation workflows to:

- create PRs
- apply labels
- merge PRs

## Branch protection / rulesets

To keep the process agent-only, configure `main` so that merges require:

- required status checks (CI)
- **no mandatory human reviews**

Recommended required checks:

- Guardrails (planning-only)
- Docs CI (agent review)

If you *do* require reviews, you must either:

- allow Actions/bot approvals to count, or
- introduce a dedicated reviewer-bot identity.

## Never store credentials in the repo

- Do not commit PATs, SSH keys, or tokens.
- Do not add secrets to `.env` for this repository.

If an admin token is ever required, store it as a GitHub Secret in repo settings.
