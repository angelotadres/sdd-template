# AGENTS.md

This repository follows a **spec-driven development (SDD)** workflow. Every feature starts as a spec, not code. These instructions apply to any agent working in this repository.

## Mental model

SDD organizes work into three durable layers:

1. **The Constitution** (`specs/mission.md`, `specs/tech-stack.md`, `specs/roadmap.md`) — the long-lived "why, how, and when" of the project. Edit rarely and deliberately.
2. **Feature specs** (`specs/YYYY-MM-DD-<feature-name>/`) — per-feature trio of `requirements.md`, `plan.md`, `validation.md`. One folder per feature.
3. **Agent skills** (`.claude/skills/`) — reusable procedures. `bootstrap` drafts the constitution on a fresh repo; `feature-spec` kicks off new features; `changelog` maintains `CHANGELOG.md`.

The pattern is deliberately agent-agnostic. Claude Code picks up `.claude/skills/` natively; other agents can read this file and follow the workflow manually.

## Starting a new project

If the constitution files (`specs/mission.md`, `specs/tech-stack.md`, `specs/roadmap.md`) are still the stock scaffolds — only HTML comments and section headers, no real content — the repo has just been cloned from the template. Before any other work, invoke the `bootstrap` skill to draft them together with the user, even if the user hasn't asked for it by name.

The bootstrap skill runs a three-part interview (mission → tech-stack → roadmap) and produces the filled-in constitution. Only after all three are approved does the workflow below apply.

## Starting a new feature

Do not write code before the spec exists. The ritual:

1. **Find the next phase.** Open `specs/roadmap.md`. The next incomplete phase is the one to pick up.
2. **Branch.** Create a git branch named `phase-N-<kebab-name>` matching the roadmap entry.
3. **Consult the constitution first.** Read `specs/mission.md`, `specs/tech-stack.md`, and the target phase entry in `specs/roadmap.md`. Extract everything already known about scope, decisions, and context. Surface any conflicts between them before proceeding.
4. **Fill gaps with the user — only what the constitution doesn't already answer.** Present a pre-filled summary of what you know across the three dimensions (scope, decisions, context) and ask the user to confirm, correct, or add to it. Only ask open-ended questions for dimensions that have no coverage in the constitution docs. If all three are fully covered, skip interviewing entirely and proceed.
5. **Generate the spec trio** in `specs/YYYY-MM-DD-<feature-name>/`:
   - `requirements.md` — scope boundaries, decision rationale, context/tone rules.
   - `plan.md` — numbered task groups, each independently implementable.
   - `validation.md` — automated checks, manual walkthrough, definition of done.
6. **Show the user.** Get approval before coding.

## Implementing a feature

Work task group by task group from `plan.md`. Commit in small increments tied to task groups. When the group is done, run the checks in `validation.md`.

A feature is *done* when:

- Every task in `plan.md` is checked off.
- Every automated check in `validation.md` passes.
- The manual walkthrough in `validation.md` has been performed.
- The roadmap entry in `specs/roadmap.md` is checked off.

## Conventions

- **Feature folder names:** `YYYY-MM-DD-<feature-name>` (date in UTC, kebab-case name).
- **Branch names:** `phase-N-<kebab-name>` — matches the roadmap phase number.
- **Phase sizing:** Each roadmap phase should fit in one focused working session. If it doesn't, split it.
- **Backlog memos:** Research notes and options memos live in `backlog/YYYY-MM-DD-<topic>.md`. They inform decisions before a feature is scoped; they are not features.
- **Changelog:** `CHANGELOG.md` is maintained by the `changelog` skill from git history. Don't hand-edit it.
- **`.gitignore`:** Always kept in sync with `specs/tech-stack.md`. When the stack changes — or is first approved during bootstrap — update `.gitignore` in the same commit.
- **Diagrams:** Use Mermaid (fenced ` ```mermaid ` blocks) for all architecture, flow, and sequence diagrams. They render natively on GitHub and in most AI-assisted editors. Never use ASCII art diagrams.
- **Markdown style:** Use heading levels (`#`, `##`, `###`) to divide documents into sections — never horizontal rules (`---`) for structure. No emojis unless the content explicitly calls for one. Write in plain prose; avoid bullet-point-heavy writing where paragraphs would read better.

## Replanning

The roadmap is not immutable. When you learn something important mid-build — a decision was wrong, a dependency surfaced, priorities shifted — stop, update `roadmap.md`, and (if needed) revise `mission.md` or `tech-stack.md`. Replanning is cheap when the specs are small.

## Files an agent should read first

1. `specs/mission.md` — what we're building and why.
2. `specs/tech-stack.md` — how we're building it.
3. `specs/roadmap.md` — what's next.
4. The active feature folder under `specs/` (if any).
