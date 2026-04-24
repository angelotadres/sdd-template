# AGENTS.md

This repository follows a **spec-driven development (SDD)** workflow. Every initiative starts as a spec, not code. These instructions apply to any agent working in this repository.

## Mental model

SDD organizes work into three durable layers:

1. **The Constitution** (`specs/mission.md`, `specs/tech-stack.md`) — the long-lived "why and how" of the project. Edit rarely and deliberately. Changes here affect every initiative.
2. **Initiatives** (`specs/initiatives/<initiative-name>/`) — one folder per initiative. Each contains a `roadmap.md` (the phases for that initiative) and a dated spec folder per phase (`YYYY-MM-DD-<phase-name>/` with `requirements.md`, `plan.md`, `validation.md`).
3. **Agent skills** (`.claude/skills/`) — reusable procedures. `bootstrap` drafts the constitution and first initiative on a fresh repo; `feature-spec` kicks off new phases.

Multiple initiatives can be active simultaneously — different people or agents work on different initiatives without file overlap. Within a single initiative, phases are sequential.

The pattern is deliberately agent-agnostic. Claude Code picks up `.claude/skills/` natively; other agents can read this file and follow the workflow manually.

## Starting a new project

If the constitution files (`specs/mission.md`, `specs/tech-stack.md`) are still the stock scaffolds — only HTML comments and section headers, no real content — the repo has just been cloned from the template. Before any other work, invoke the `bootstrap` skill to draft them together with the user, even if the user hasn't asked for it by name.

The bootstrap skill runs a three-part interview (mission → tech-stack → first initiative) and produces the filled-in constitution plus the first initiative folder. Only after all three are approved does the workflow below apply.

## Starting a new phase

Do not write code before the spec exists. The ritual:

1. **Identify the initiative.** Ask the user which initiative they are working on. Read `specs/initiatives/<initiative-name>/roadmap.md` to find the first incomplete phase. That is the target.
2. **Branch.** Create a git branch named `<initiative-name>/<phase-name>` — for example, `auth-redesign/login-flow`.
3. **Consult the constitution first.** Read `specs/mission.md`, `specs/tech-stack.md`, the initiative's `roadmap.md`, and any memos in `specs/research/` relevant to this initiative. Extract everything already known about scope, decisions, and context. Surface any conflicts before proceeding.
4. **Fill gaps with the user — only what the constitution doesn't already answer.** Present a pre-filled summary of what you know and ask the user to confirm, correct, or add to it. Only ask open questions for dimensions that have no coverage. If all three are fully covered, skip interviewing entirely.
5. **Generate the spec trio** in `specs/initiatives/<initiative-name>/YYYY-MM-DD-<phase-name>/`:
   - `requirements.md` — scope boundaries, decision rationale, context/tone rules.
   - `plan.md` — numbered task groups, each independently implementable.
   - `validation.md` — automated checks (agent runs), human validation (agent cannot), and definition of done.
6. **Show the user.** Get approval before coding.

## Implementing a phase

Work task group by task group from `plan.md`. Commit in small increments tied to task groups. When a group is done, run the checks in `validation.md`.

**Validation principle:** The agent runs every automated check it can — tests, lint, type checks, CLI smoke tests — and reports the results. Only after exhausting automated validation does it ask the human to step in. The human's role is to review the agent's report, perform the checks only a human can (visual UI, business logic judgment, accessibility), and then authorize the commit or PR push. That authorization is the explicit gate.

A phase is *done* when:

- Every task in `plan.md` is checked off.
- Every automated check in `validation.md` passes.
- The human walkthrough in `validation.md` has been performed and authorized.
- The phase checkbox in the initiative's `roadmap.md` is checked off.

## Conventions

- **Initiative folder names:** `<kebab-case-name>` under `specs/initiatives/`.
- **Phase folder names:** `YYYY-MM-DD-<phase-name>` (date in UTC, kebab-case) inside the initiative folder.
- **Branch names:** `<initiative-name>/<phase-name>` — maps directly to the folder structure.
- **Phase sizing:** Each phase should fit in one focused working session. If it doesn't, split it.
- **Research memos:** Investigations, comparisons, and technical memos live in `specs/research/YYYY-MM-DD-<topic>.md`. These are documents, not tasks — they inform decisions before a phase is scoped.
- **Issue tracking:** Non-blocking bugs, polish, and small improvements go to GitHub Issues, not into specs. The threshold: if it needs a spec, it is an initiative; if it doesn't, it is an issue. When the agent notices something worth tracking, it surfaces the suggestion and waits for the user to authorize before running `gh issue create`. Before starting a new phase, the agent runs `gh issue list` to surface any open issues relevant to the current initiative.
- **`.gitignore`:** Always kept in sync with `specs/tech-stack.md`. When the stack changes — or is first approved during bootstrap — update `.gitignore` in the same commit.
- **Diagrams:** Use Mermaid (fenced ` ```mermaid ` blocks) for all architecture, flow, and sequence diagrams. They render natively on GitHub and in most AI-assisted editors. Never use ASCII art diagrams.
- **Markdown style:** Use heading levels (`#`, `##`, `###`) to divide documents into sections — never horizontal rules (`---`) for structure. No emojis unless the content explicitly calls for one. Write in plain prose; avoid bullet-point-heavy writing where paragraphs would read better.

## Replanning

An initiative's roadmap is not immutable. When you learn something important mid-build — a decision was wrong, a dependency surfaced, priorities shifted — stop, update the initiative's `roadmap.md`, and (if needed) revise `mission.md` or `tech-stack.md`. Replanning is cheap when the specs are small. Constitution changes should be surfaced to the user and committed deliberately, not silently folded into a phase branch.

## Files an agent should read first

1. `specs/mission.md` — what we're building and why.
2. `specs/tech-stack.md` — how we're building it.
3. `specs/initiatives/<active-initiative>/roadmap.md` — what's next for the current initiative.
4. The active phase folder inside that initiative (if any).
5. Any relevant memos in `specs/research/`.
