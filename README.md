# Agentic Project Template

A GitHub template for agentic projects that use **spec-driven development (SDD)**.

## Prerequisites

- [GitHub CLI](https://cli.github.com/) (`gh`) — required for issue tracking. Run `gh auth login` after installing.

To enable automatic changelog updates on every push, run once after cloning:

```bash
git config core.hooksPath .githooks
```

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

**3. Changelog**

`CHANGELOG.md` is regenerated automatically on every push via the `.githooks/pre-push` hook (requires the one-time setup above). To regenerate it manually at any time:

```bash
python3 .claude/skills/changelog/scripts/changelog.py
```

## What's in the box

- **`AGENTS.md`** — agent-agnostic workflow documentation.
- **`CLAUDE.md`** — Claude Code entry point that points at `AGENTS.md`.
- **`specs/`** — constitution files (mission, tech stack) plus `initiatives/` and `research/`.
- **`.claude/skills/bootstrap/`** — interviews you to draft the constitution and first initiative on a fresh repo.
- **`.claude/skills/feature-spec/`** — automates new-phase kickoff (constitution consult + spec trio generation).
- **`.claude/skills/changelog/`** — maintains `CHANGELOG.md` from git history.
- **`CHANGELOG.md`**, **`LICENSE`**, **`.gitignore`** — standard project hygiene.

## Who this is for

This template is designed for a solo developer or a small team coordinating with one or more agents. The documentation is written primarily for agents to consume — humans benefit from it too, but the structure is deliberately machine-readable so agents can pick up context without being told what to read.

It is not a team coordination tool, a project management system, or a replacement for a task tracker. It is an opinionated repo layout that keeps specs and code honest with each other.

## Assumptions

The template is designed around two assumptions. When they hold, the workflow is frictionless. When they don't, you will feel friction:

1. **Phases within an initiative are sequential.** One phase completes before the next starts. Different people (or agents) can work on different initiatives simultaneously — each initiative lives in its own folder with no file overlap.
2. **One person owns the constitution.** Someone has final authority over `specs/mission.md` and `specs/tech-stack.md`. Changes to those files should be deliberate and visible to everyone, not silently merged from a feature branch.

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

## Motivation

This template started from the spec-driven development workflow introduced in [DeepLearning.AI's short course on agentic development](https://github.com/https-deeplearning-ai/sc-spec-driven-development-files). The course made a correct and important point: write specs before code, keep them in the repo, let agents read them.

In practice, the course material had significant gaps that made it hard to use on a real project. The workflow was entirely manual — no automation for the bootstrap interview, the spec kickoff, or the changelog. The "roadmap" was a single flat file with a global phase queue, meaning a small team working in parallel would immediately hit merge conflicts and have no clear place to put new work that emerged mid-project. The terminology conflated "features" and "phases." There was no guidance on what to do with bugs, research notes, or the dozens of small items that surface during real development but don't warrant a full spec.

This template addresses those gaps directly: automated skills that run the workflow end-to-end; an initiative and phase structure that lets multiple people work in parallel without colliding; per-initiative roadmaps instead of a global queue; a `research/` folder for investigations that is explicitly not a task backlog; a GitHub Issues convention for non-spec work with agent-assisted creation; a pre-push hook so the changelog updates without anyone remembering to run it; and clear documentation of what the template is for, what it assumes, and what it deliberately does not solve.
