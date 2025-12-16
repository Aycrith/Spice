# Agent Permissions (One-time bootstrap)

Goal: future agents can operate without repeated human intervention.

## What needs permission

Agents need two capability buckets:

1. **Local push permission** (from the IDE environment)
   - Agents must be able to `git push` branches to `origin`.
   - This is the only capability required locally.

2. **PR/merge permission** (inside GitHub)
   - Handled by GitHub Actions using the repository `GITHUB_TOKEN`.
   - This repo provides workflows to open PRs and merge PRs automatically (no PAT required).

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

If you don't see this, make sure you're in the repository (not your user settings), and that your account has admin access to the repo.

These permissions allow the automation workflows to:

- create PRs
- apply labels
- merge PRs

### C) Secrets (optional)

This repository is designed to work **without any PAT/App token** by using the built-in `GITHUB_TOKEN`.

If you previously created an `AGENT_GH_TOKEN` secret and it's not a valid token, remove it to avoid confusion.

Where to manage secrets:

- Settings → Secrets and variables → Actions → **Secrets** tab
   - New repository secret

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

### Security note: treat tokens as compromised if pasted

If a token is ever pasted into chat, an issue, a PR description, or any log output:

- Assume it is compromised.
- Revoke/rotate it immediately.
- Update the repository secret (for example `AGENT_GH_TOKEN`) to the rotated value.

If an admin token is ever required, store it as a GitHub Secret in repo settings.
