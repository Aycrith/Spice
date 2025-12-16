#!/usr/bin/env python3
"""Validate local Markdown links (best-effort).

- Checks that relative file links in docs exist.
- Ignores http(s) links.
- Ignores pure anchors (#foo).

This is intentionally simple and offline.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]

MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def run_git(args: list[str]) -> str:
    r = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{r.stderr}")
    return r.stdout


def iter_markdown_files(base: str, head: str) -> list[Path]:
    changed = [
        line.strip()
        for line in run_git(["diff", "--name-only", base, head]).splitlines()
        if line.strip()
    ]
    # Always include docs/INDEX.md because it's the entrypoint.
    candidates = set(changed)
    candidates.add("docs/INDEX.md")

    md_files: list[Path] = []
    for rel in sorted(candidates):
        if not rel.lower().endswith(".md"):
            continue
        p = REPO_ROOT / rel
        if p.exists() and p.is_file():
            md_files.append(p)
    return md_files


def normalize_target(raw: str) -> str:
    # Strip surrounding whitespace
    raw = raw.strip()

    # Drop title fragments "file.md 'title'" (rare), keep before whitespace.
    raw = raw.split()[0]

    # Split anchor
    target = raw.split("#", 1)[0]
    return target


def main() -> int:
    base = os.environ.get("BASE_SHA")
    head = os.environ.get("HEAD_SHA")

    if not base or not head:
        print("ERROR: BASE_SHA and HEAD_SHA must be set.")
        return 2

    failures: list[str] = []

    for md_path in iter_markdown_files(base, head):
        text = md_path.read_text(encoding="utf-8", errors="replace")
        for match in MD_LINK_RE.finditer(text):
            raw = match.group(1).strip()

            if not raw or raw.startswith("#"):
                continue
            if raw.startswith("http://") or raw.startswith("https://"):
                continue
            if raw.startswith("mailto:"):
                continue

            target = normalize_target(raw)
            if not target:
                continue

            # Ignore absolute-path links
            if target.startswith("/"):
                continue

            # Resolve relative to file
            resolved = (md_path.parent / target).resolve()

            try:
                resolved.relative_to(REPO_ROOT)
            except ValueError:
                failures.append(f"{md_path.relative_to(REPO_ROOT)} links outside repo: {raw}")
                continue

            if not resolved.exists():
                failures.append(f"{md_path.relative_to(REPO_ROOT)} broken link: {raw}")

    if failures:
        print("ERROR: Broken local Markdown links detected:")
        for f in failures:
            print(f"- {f}")
        return 1

    print("Markdown link check: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
