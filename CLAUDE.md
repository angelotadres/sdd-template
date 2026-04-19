# CLAUDE.md

This project follows a spec-driven development workflow defined in [`AGENTS.md`](./AGENTS.md). Read it first — it describes the constitution, the per-feature spec trio, and the kickoff ritual.

## Claude-specific notes

- Skills live in `.claude/skills/`. The `bootstrap` skill drafts the constitution on a fresh repo; the `feature-spec` skill automates the new-feature kickoff ritual from `AGENTS.md`; the `changelog` skill maintains `CHANGELOG.md`.
- Before starting any work, read `specs/mission.md`, `specs/tech-stack.md`, and `specs/roadmap.md`. They are the source of truth for the project. **If they are still empty scaffolds (HTML comments only), invoke the `bootstrap` skill first — even if the user hasn't asked for it by name.**
- Do not hand-edit `CHANGELOG.md` — invoke the `changelog` skill.
- Do not write code for a feature before its spec trio exists under `specs/YYYY-MM-DD-<feature-name>/`.
