# Local Artifacts Policy (No Binaries in Git)

This repository is **planning-only** until Stage 2 and explicitly prohibits committing large binaries such as PDFs and archives (`docs/governance/BRANCHING_STRATEGY.md`).

## Policy

1. **Do not commit PDFs/archives** to git.
   - Rationale: prevents repo bloat and accidental inclusion of sensitive broker statements or account artifacts.
2. **Cite authoritative sources by URL** in `docs/references/PRIMARY_SOURCES.md`.
   - If a source is critical, prefer linking to the authoritative publisher (exchange, broker, regulator, IRS, publisher site).
3. **If you need offline copies**, store them locally **outside version control**.

## Recommended local storage layout (non-versioned)

- Create a local folder that is ignored by git (this repo already ignores `*.pdf`, `*.gz`, etc. in `.gitignore`).
- Suggested folder names (pick one and stick to it):
  - `C:\Dev\ACMEoutLand\Spice\.local_refs\`
  - `C:\Dev\ACMEoutLand\Spice\tmp\refs\`

## Evidence capture without committing binaries

For each researched source, record in the relevant planning artifact (Validation Matrix / ADR / Open Questions):
- URL
- date accessed
- short paraphrase of the binding constraints
- how it changes assumptions
- falsifiers / edge cases

This keeps the repo “docs-as-code” while remaining lightweight and safe.
