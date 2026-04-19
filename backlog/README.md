# Backlog

Options memos and research notes that inform decisions *before* a feature is scoped.

## What goes here

- Comparisons between possible approaches ("Postgres vs. SQLite for persistence").
- Research on external services, libraries, or APIs we might use.
- Cost, performance, or compliance investigations.
- Any writeup that will influence a future `specs/YYYY-MM-DD-<feature>/requirements.md` decision.

## What does not go here

- Active feature specs — those live in `specs/YYYY-MM-DD-<feature>/`.
- Decisions already made — those live in `specs/tech-stack.md` (or `mission.md`).
- Raw feature ideas — those live in `specs/roadmap.md` or a personal TODO.

## Naming

`YYYY-MM-DD-<topic>.md` — date first so files sort chronologically.

Example: `2026-04-18-postgres-vs-sqlite.md`.

## Lifecycle

When an options memo produces a decision, the decision is promoted to `specs/tech-stack.md` (or whichever constitution doc is relevant). The memo stays here as the audit trail — don't delete, archive in place.
