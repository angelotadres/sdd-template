---
name: feature-spec
description: Kicks off a new phase within an initiative. Reads the initiative's roadmap, runs the two-way-door test to size the work, and either takes the light path (record intent, build) or the escalated path (consult the constitution, generate the requirements.md + plan.md + validation.md trio, gate on approval). Trigger when the user says "start the next phase", "kick off a phase", "begin the next phase of [initiative]", "write the spec for X", or asks to start any new phase of work.
---

# Feature Spec Skill

## When to run

Trigger this skill at the start of every new phase. It first sizes the work, then routes to the light or escalated path. On the escalated path, do not write code before the spec trio exists and the user has approved it.

## 1. Identify the initiative and next phase

Ask the user which initiative they are working on. Then read `specs/initiatives/<initiative-name>/roadmap.md` and find the first phase with at least one unchecked task. That is your target.

If every phase in the initiative is complete, stop and tell the user — they need to add new phases to the roadmap before starting work.

## 2. Run the two-way-door test

Apply the two-way-door test in `AGENTS.md` to the target phase. State your recommendation in one line — "Reversible, internal-only — going light. Say 'spec it' to escalate." — naming the trigger if you're escalating. Default to light; escalate only when you can name a trigger. The user can force either direction with one word.

Then take the matching path below.

## Light path (two-way door)

1. **Record intent.** Add a couple of bullets under the phase in the initiative's `roadmap.md` — what and why. That is the whole spec; no trio, no separate file.
2. **Branch from a clean tree.** Commit or stash pending changes first (the clean-tree rule in `AGENTS.md`), then create `<initiative-name>/<phase-name>`.
3. **Hand off to implementation.** Build per the "Implementing a phase" and coding-discipline guidance in `AGENTS.md`. There is no spec-approval gate — the door-test call already was it. Stop here; this skill is done.

## Escalated path (one-way door)

### E1. Prompt the user to clear context

Escalated phases warrant a clean session. Tell the user:

> "This is a one-way-door phase, so let's spec it properly. Consider running `/clear` (or `/compact`) first — spec sessions work best with a clean slate. Let me know when you're ready and I'll pick up from the roadmap."

Wait for confirmation before proceeding.

### E2. Create a branch

Ensure the working tree is clean — commit or stash pending changes per the clean-tree rule in `AGENTS.md`. Then create `<initiative-name>/<phase-name>` (kebab-case, matching the initiative folder and phase goal). Example: initiative "auth-redesign", phase "Login Flow" -> `auth-redesign/login-flow`. Hold onto the phase kebab-name; the spec folder in E5 reuses it exactly.

### E3. Consult the constitution first

Read `specs/mission.md`, `specs/tech-stack.md`, the initiative's `roadmap.md`, and any relevant memos in `specs/research/`. Extract everything already stated across the three spec dimensions:

- **Scope** — what the phase's goal and task list imply; what mission.md says is in/out of scope.
- **Decisions** — stack choices, libraries, patterns, and data model details from tech-stack.md.
- **Context** — constraints, tone, non-functional requirements, and philosophy from mission.md.

Also run `gh issue list` and surface any open issues relevant to this phase. If anything conflicts with the constitution, surface the conflict explicitly — don't silently resolve it.

### E4. Fill gaps with the user — only what's missing

Present a concise pre-filled summary across all three dimensions, then ask only about parts with no coverage in the constitution:

- If scope is clear from the phase goal, state it and ask the user to confirm — don't re-ask as an open question.
- If decisions are fully specified in tech-stack.md, list the relevant ones as already decided — don't ask again.
- If context is fully covered by mission.md, summarize it — don't ask.

If all three are fully covered, skip interviewing and proceed to E5.

### E5. Generate the spec trio

Create `specs/initiatives/<initiative-name>/<phase-name>/` with three files. Apply the spec-brevity convention in `AGENTS.md`: reference the constitution instead of restating it, and keep each file short enough that the user will genuinely read every line in E6.

**`requirements.md`** — what is being built:

- **Scope** — what's in, what's out.
- **Decisions** — the choices made, each with a one-line rationale.
- **Context** — tone, constraints, non-functional considerations, patterns to follow.
- **Dependencies** — other specs, phases, or external systems this relies on.

**`plan.md`** — how it will be built:

- Numbered task groups. Common shape: data layer -> domain logic -> interface (API or UI). Adapt to the project's actual stack.
- Each group contains concrete, independently implementable subtasks as checkboxes.
- Tests live inside the group that introduces the behavior they cover — never as a trailing "tests" group. See the testing convention in `AGENTS.md`.
- Groups should be orderable — later groups can depend on earlier ones, not vice versa.

**`validation.md`** — how we'll know it's done:

- **Agent validates** — everything the agent can run or observe autonomously: automated tests, lint, type checks, CLI smoke tests, API response checks. Name the tests this phase adds or updates (per the testing convention in `AGENTS.md`); if the phase needs none, say why in one line.
- **Human validates** — only what requires human judgment: visual UI correctness, business logic that can't be asserted programmatically, accessibility, UX feel. Keep it short — if the agent can check it, it belongs above.
- **Definition of done** — checklist that maps 1:1 to `plan.md` tasks. Always end with: "Mark the phase checkbox in the initiative's `roadmap.md` as complete."

### E6. Confirm with the user

Show the three files. Then, separately, call out the decisions and assumptions most likely to be wrong — anything you inferred without constitution backing, any new dependency or pattern, any scope judgment call. Keep it to the genuinely risky items (typically 3-5). Approval of that list is the real gate — don't accept a bare "looks good" if the user hasn't addressed them.

## Constraints

- Default to the light path. Escalate only when you can name a two-way-door trigger from `AGENTS.md`.
- On the escalated path: stay consistent with `specs/tech-stack.md` — don't introduce new libraries or patterns without calling them out in `requirements.md` under Decisions.
- Enforce the phase-sizing rule in `AGENTS.md`. If the phase fails either test, stop and propose a roadmap split — and refuse splits that create stub-then-finish pairs.
- Escalated spec is always three files: `requirements.md`, `plan.md`, `validation.md`. Same names every time.
- Never write code or edit files outside `specs/` and the initiative `roadmap.md` from within this skill.
