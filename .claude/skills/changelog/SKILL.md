---
name: changelog
description: Maintains CHANGELOG.md by regenerating it from git history. Invoke when the user asks to update or refresh the changelog, or proactively before a merge or release. Manual skill — only runs when invoked, nothing automatic.
---

# Changelog Skill

## What it does

Maintains `CHANGELOG.md` from `git log`. Idempotent — rerunning without new commits is a no-op.

## How to run

From the project root:

```bash
python3 .claude/skills/changelog/scripts/changelog.py
```

## Behavior

- Always regenerates `CHANGELOG.md` from the full git history, then skips writing if the result is identical to what's already on disk.
- If `CHANGELOG.md` does not exist, it is created.
- Dates use `## YYYY-MM-DD` headings, in reverse chronological order.
- Each commit becomes a bullet with the commit subject line.

## Format

```markdown
# Changelog

## 2026-04-18

- Add user search endpoint
- Fix off-by-one in pagination

## 2026-04-17

- Initial mission and tech-stack docs
```

## When to run

- Before merging a feature branch.
- Before cutting a release.
- Any time the user asks for an updated changelog.

## Constraints

- Must be run from the directory containing `.git/`.
- The script **fully regenerates** `CHANGELOG.md` from git history on every run. Manual edits to the file will be overwritten. Clean up commit subjects at commit time (via `git commit --amend` or rebase), not in `CHANGELOG.md`.
