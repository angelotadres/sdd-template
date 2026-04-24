# Agentic Project Template

A GitHub template for agentic projects that use **spec-driven development (SDD)**.

## Prerequisites

- [GitHub CLI](https://cli.github.com/) (`gh`) — required for issue tracking. Run `gh auth login` after installing.

## Quick start

### Greenfield project

Click **Use this template** on GitHub to create a new repo with this structure already in place. Then:

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

### Brownfield project

To adopt this workflow in an existing repo:

1. Copy the following into your project root: `AGENTS.md`, `CLAUDE.md`, `.claude/`, and the `specs/` folder (without the scaffold content — just the structure).
2. Run `gh auth login` if needed.
3. Run the bootstrap skill — it will interview you about your existing project and fill in the constitution based on what's already built, not what you're starting from scratch.

The bootstrap skill is designed to document reality, not invent it. Point it at an existing codebase and it will produce a constitution that reflects what's there.

## What's in the box

- **`AGENTS.md`** — agent-agnostic workflow documentation.
- **`CLAUDE.md`** — Claude Code entry point that points at `AGENTS.md`.
- **`specs/`** — constitution files (mission, tech stack) plus `initiatives/` and `research/`.
- **`.claude/skills/bootstrap/`** — interviews you to draft the constitution and first initiative on a fresh repo.
- **`.claude/skills/feature-spec/`** — automates new-phase kickoff (constitution consult + spec trio generation).
- **`LICENSE`**, **`.gitignore`** — standard project hygiene.

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

This template started from the spec-driven development workflow introduced in [DeepLearning.AI's short course on agentic development](https://github.com/https-deeplearning-ai/sc-spec-driven-development-files). The course teaches the right ideas: write specs before code, keep them in the repo, let agents read them. It introduced the constitution (mission, tech-stack, roadmap), the spec trio (requirements, plan, validation), and the backlog folder — all of which carry over here.

The course is designed around building a single specific project to illustrate the concepts, not around shipping a reusable template. Taking those ideas and making them work as a general-purpose starting point required a few concrete changes:

- **Constitution-first ordering.** The original `feature-spec` skill interviewed the user before reading `mission.md` and `tech-stack.md`, which meant asking questions already answered in the docs. We flipped that order.
- **Bootstrap skill.** There was no automated way to draft the constitution on a fresh repo — it was built manually following per-video prompts. The `bootstrap` skill automates that interview.
- **Agent-agnostic instructions.** The course used `prompts.md` files tied to specific videos. `AGENTS.md` replaces that with durable instructions any agent can follow without knowing which video they're on.
- **Initiative and phase structure.** The roadmap was a single flat file with a global phase queue. That works for one person on one track but creates merge conflicts and has no natural home for new work when a team runs multiple things in parallel. Per-initiative roadmaps under `specs/initiatives/` replace it.
- **Research folder.** The `backlog/` folder sat at the project root with no clear scope. We moved it to `specs/research/` and defined it as research documents only — bugs and task ideas go to GitHub Issues instead.

None of this diminishes the course — the conceptual foundation is sound and worth taking. This template is what you reach for when you want those concepts running on day one without the manual setup.
