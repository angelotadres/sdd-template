# Agentic Project Template

A GitHub template for agentic projects that use **spec-driven development (SDD)**.

Click **Use this template** to start a new project. Then:

**1. Bootstrap the constitution**

```
Bootstrap the project. My project is about: [one sentence].
```

The `bootstrap` skill will interview you and draft `specs/mission.md`, `specs/tech-stack.md`, and `specs/roadmap.md` together with you.

**2. Start a phase**

```
Start the next phase.
```

The `feature-spec` skill will pick up the next incomplete phase from the roadmap, create a branch, interview you, and produce the spec trio before any code is written.

**3. Update the changelog**

```
Update the changelog.
```

Run this before merging a branch or cutting a release. The `changelog` skill regenerates `CHANGELOG.md` from git history.

## What's in the box

- **`AGENTS.md`** — agent-agnostic workflow documentation.
- **`CLAUDE.md`** — Claude Code entry point that points at `AGENTS.md`.
- **`specs/`** — constitution trio (mission, tech stack, roadmap) with annotated scaffolds.
- **`.claude/skills/bootstrap/`** — interviews you to draft the three constitution docs on a fresh repo.
- **`.claude/skills/feature-spec/`** — automates new-feature kickoff (interview + spec trio generation).
- **`.claude/skills/changelog/`** — maintains `CHANGELOG.md` from git history.
- **`backlog/`** — options memos and research notes that inform future decisions.
- **`CHANGELOG.md`**, **`LICENSE`**, **`.gitignore`** — standard project hygiene.

## Why spec-driven

Specs are durable; code is disposable. When the agent (or the human) changes, the specs don't. This template bakes that assumption into the repo layout so any agent can pick up where another left off.

See `AGENTS.md` for the full workflow.

## Inspired by

This template is inspired by the [Spec-Driven Development files](https://github.com/https-deeplearning-ai/sc-spec-driven-development-files) from DeepLearning.AI's short-course on agentic development workflows.
