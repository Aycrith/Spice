# Branching Strategy (Agents + Humans)

This repository is **planning-first** until the Stage 2 gate is passed (see `docs/quality/STAGE_STATUS.md`). The branch strategy is designed to prevent accidental implementation work, preserve provenance, and keep traceability tight.

## Core rules

1. **No direct pushes to `main`.** All changes land via pull request.
2. **No repo-root edits by default.** Do not modify root governance files (`README.md`, `ROADMAP.md`, etc.) unless explicitly authorized.
3. **Planning-only until Stage 2:** PRs to `main` must only change:
   - `docs/**`
   - `.github/**` (templates + guardrails)
4. **No large binaries:** archives and PDFs must not be committed (see `.gitignore`).
5. **No silent overwrites:** when importing external artifacts, stage them and avoid overwriting existing files.

## Branch naming

Use short, intention-revealing prefixes:

- `docs/<topic>` — documentation updates (most PRs)
- `adr/<decision>` — new or updated ADRs
- `research/<topic>` — research backlog/program updates
- `chore/<task>` — repo hygiene, guardrails, templates
- `fix/<topic>` — fix incorrect docs, broken links, or validation mistakes

Implementation branches are **not allowed** until Stage 2 is passed on `main`:

- `feat/<capability>`
- `refactor/<area>`

## Pull request discipline (Docs-as-Code)

Each PR must include:

- **What changed** (file list + sections)
- **Why** (risk/gap)
- **Evidence** (link into `docs/references/PRIMARY_SOURCES.md`)
- **Validation method + thresholds** (reference `docs/validation/VALIDATION_MATRIX_v2.1.md`)
- **Traceability Index update** (`docs/validation/TRACEABILITY_INDEX_v2.1.md`) for any material change

 A PR template in `.github/PULL_REQUEST_TEMPLATE.md` standardizes this.

## Import workflow (safe, non-overwriting)

When importing artifacts (e.g., tarballs):

1. Extract into a temp folder (e.g., `.tmp_import_*`).
2. Run a collision scan before copying.
3. Copy only non-colliding files.
4. For collisions, copy the incoming version as `*.import.md` (or `*.imported_vX.Y.md`) and merge manually.

## Release / milestone semantics

This repo’s “releases” are documentation readiness milestones:

- **Stage 0**: data/ops foundations planned + validated
- **Stage 1**: backtest realism + robustness validated
- **Stage 2**: paper trading conformance validated (implementation allowed afterward)

Stage status is recorded in `docs/quality/STAGE_STATUS.md`.
