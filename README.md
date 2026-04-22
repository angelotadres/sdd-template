# Agentic Project Template

A GitHub template for agentic projects that use **spec-driven development (SDD)**.

## Prerequisites

- [GitHub CLI](https://cli.github.com/) (`gh`) — required for issue tracking. Run `gh auth login` after installing.

## Quick start

Click **Use this template** to start a new project. Then:

**1. Bootstrap the constitution**

```
Bootstrap the project. My project is about: [one sentence].
```

The `bootstrap` skill will interview you and draft `specs/mission.md`, `specs/tech-stack.md`, and the first initiative under `specs/initiatives/` together with you.

**2. Start a phase**

```
Start the next phase of [initiative name].
```

The `feature-spec` skill will read the initiative's roadmap, consult the constitution, fill any gaps with you, and produce the spec trio before any code is written.

**3. Update the changelog**

```
Update the changelog.
```

Run this before merging a branch or cutting a release. The `changelog` skill regenerates `CHANGELOG.md` from git history.

## What's in the box

- **`AGENTS.md`** — agent-agnostic workflow documentation.
- **`CLAUDE.md`** — Claude Code entry point that points at `AGENTS.md`.
- **`specs/`** — constitution files (mission, tech stack) plus `initiatives/` and `research/`.
- **`.claude/skills/bootstrap/`** — interviews you to draft the constitution and first initiative on a fresh repo.
- **`.claude/skills/feature-spec/`** — automates new-phase kickoff (constitution consult + spec trio generation).
- **`.claude/skills/changelog/`** — maintains `CHANGELOG.md` from git history.
- **`CHANGELOG.md`**, **`LICENSE`**, **`.gitignore`** — standard project hygiene.

## Who this is for

This template is designed for a solo developer, or a small team working on one active initiative at a time, coordinating with one or more agents. The documentation is written primarily for agents to consume — humans benefit from it too, but the structure is deliberately machine-readable so agents can pick up context without being told what to read.

It is not a team coordination tool, a project management system, or a replacement for a task tracker. It is an opinionated repo layout that keeps specs and code honest with each other.

## Assumptions

The template is designed around three assumptions. When they hold, the workflow is frictionless. When they don't, you will feel friction:

1. **Phases within an initiative are sequential.** One phase completes before the next starts.
2. **One person owns the constitution.** Someone has final authority over `specs/mission.md` and `specs/tech-stack.md`. Changes to those files should be deliberate and visible to everyone.
3. **Parallel initiatives are possible, but the workflow is optimized for one active initiative at a time.** Multiple people can work on different initiatives simultaneously — each initiative lives in its own folder, so there is no file overlap. However, there is no built-in assignment or coordination mechanism beyond git branches and PRs.

## By design

These are deliberate constraints, not gaps:

**Parallel multi-person work causes merge friction.** The constitution files (`mission.md`, `tech-stack.md`) are shared. Changes to them from multiple branches will require merge resolution. This is intentional — constitution changes are significant and should be visible, not silently merged.

**Team coordination relies on git and PRs.** There is no assignment mechanism, no phase lock, no spec review gate beyond what GitHub PRs provide. For a small team, that is enough. Branch creation signals that someone has claimed a phase; the PR is the review gate.

**The SDD workflow is not a bug tracker.** Simple bugs and polish items belong in GitHub Issues, not in specs. The only exception: a bug that requires a multi-phase redesign should be treated as a new initiative.

## Issue tracking

Non-blocking bugs, polish, and small improvements that surface during implementation go to **GitHub Issues**, not into the spec workflow. The convention:

- The agent notices something worth tracking and surfaces it ("I noticed X — should I file an issue?")
- The human authorizes
- The agent creates it: `gh issue create --label bug` or `--label enhancement`

Before starting a new phase, the agent runs `gh issue list` to surface any open issues relevant to the current initiative.

## Why spec-driven

Specs are durable; code is disposable. When the agent (or the human) changes, the specs don't. This template bakes that assumption into the repo layout so any agent can pick up where another left off.

See `AGENTS.md` for the full workflow.

## Inspired by

This template began as an implementation of the spec-driven development workflow introduced in [DeepLearning.AI's short course on agentic development](https://github.com/https-deeplearning-ai/sc-spec-driven-development-files). The course established the core idea: write specs before code, keep them in the repo, let agents read them.

This template extends that foundation substantially for real-project use: automated skills (`bootstrap`, `feature-spec`, `changelog`) that run the workflow without manual steps; an agent-agnostic `AGENTS.md` that any agent can follow, not just Claude; an initiative and phase structure that scales beyond a single flat roadmap; a `research/` folder for investigations that inform decisions; a GitHub Issues convention for non-spec work; and annotated constitution scaffolds that guide the bootstrap interview.
