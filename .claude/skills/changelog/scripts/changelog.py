#!/usr/bin/env python3
"""Maintain CHANGELOG.md from git log.

Always regenerates from the full git history, then only writes the file if
the result differs from what's on disk. Run from the project root (must
contain .git/).

Design note: manual edits to CHANGELOG.md will be overwritten on the next
run. Clean up commit subjects at commit time, not in this file.
"""

from __future__ import annotations

import subprocess
import sys
from collections import defaultdict
from pathlib import Path

CHANGELOG = Path("CHANGELOG.md")


def git_log_all() -> list[tuple[str, str]]:
    """Return [(YYYY-MM-DD, subject)] for all commits, oldest -> newest."""
    cmd = ["git", "log", "--reverse", "--date=short", "--pretty=format:%ad%x09%s"]
    out = subprocess.check_output(cmd, text=True).strip()
    if not out:
        return []
    return [tuple(line.split("\t", 1)) for line in out.splitlines()]


def render(commits_by_date: dict[str, list[str]]) -> str:
    lines: list[str] = ["# Changelog", ""]
    for day in sorted(commits_by_date.keys(), reverse=True):
        lines.append(f"## {day}")
        lines.append("")
        for subject in commits_by_date[day]:
            lines.append(f"- {subject}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    if not Path(".git").is_dir():
        print("error: run from the project root (no .git/ here)", file=sys.stderr)
        return 2

    commits = git_log_all()
    if not commits:
        new_text = "# Changelog\n\n<!-- No commits yet. -->\n"
    else:
        grouped: dict[str, list[str]] = defaultdict(list)
        for day, subject in commits:
            grouped[day].append(subject)
        new_text = render(grouped)

    current = CHANGELOG.read_text() if CHANGELOG.exists() else ""
    if current == new_text:
        print("changelog up to date; no changes")
        return 0

    CHANGELOG.write_text(new_text)
    print(f"changelog regenerated from {len(commits)} commit(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
