---
name: feature-spec
description: Kicks off a new feature by finding the next roadmap phase, creating a git branch, interviewing the user on scope/decisions/context, consulting the constitution, and generating the requirements.md + plan.md + validation.md trio. Trigger when the user says "start the next phase", "kick off a feature", "begin phase N", "write the spec for X", or asks to start any new roadmap item. Do not write code before this skill has produced the spec trio.
---

# Feature Spec Skill

## When to run

Trigger this skill at the start of every new feature. Do not write code or create files outside `specs/` before this skill has produced the spec trio and the user has approved it.

## Steps

### 1. Identify the next phase

Open `specs/roadmap.md`. Find the first phase with at least one unchecked task. That's your target.

If every phase is complete, stop and tell the user — they need to add new phases before starting work.

### 2. Create a branch

Create a git branch named `phase-N-<kebab-name>`, where N is the phase number and the kebab-name matches the roadmap title.

Example: Phase 2 "User Profile Page" → `phase-2-user-profile-page`.

Hold onto the kebab-name. The spec folder you create in step 5 reuses it: `specs/YYYY-MM-DD-<kebab-name>/`. This keeps branch and spec folder aligned.

### 3. Interview the user — exactly three questions

Ask these three questions, in order, one at a time, before writing any file. Do not skip. Do not combine. Wait for each answer before asking the next.

1. **Scope** — "What does this feature collect, expose, or accomplish? What's explicitly out of scope?"
2. **Decisions** — "What choices should I know about? Storage, visibility, validation, UX patterns, libraries?"
3. **Context** — "What constraints or non-functional considerations shape this? Tone, performance, accessibility, existing code patterns to follow?"

### 4. Consult the constitution

Read `specs/mission.md` and `specs/tech-stack.md`. The spec you're about to write must be consistent with them. If anything the user said conflicts, surface the conflict and ask how to resolve it — don't silently rewrite the constitution to match.

### 5. Generate the spec trio

Create `specs/YYYY-MM-DD-<feature-name>/` (date in UTC) with three files:

**`requirements.md`** — what is being built. Sections:

- **Scope** — what's in, what's out.
- **Decisions** — the choices made, each with a one-line rationale.
- **Context** — tone, constraints, non-functional considerations, patterns to follow.
- **Dependencies** — other specs, phases, or external systems this relies on.

**`plan.md`** — how it will be built. Sections:

- Numbered task groups. Common shapes: data layer → domain logic → interface (API or UI) → tests. Adapt to the project's actual stack.
- Each group contains concrete, independently implementable subtasks as checkboxes.
- Groups should be orderable — later groups can depend on earlier ones, but not vice versa.

**`validation.md`** — how we'll know it's done. Sections:

- **Automated checks** — tests to write, what they cover.
- **Manual walkthrough** — what to click, what to submit, what to observe.
- **Definition of done** — explicit checklist that maps 1:1 to the `plan.md` tasks. Always include a final item: "Mark the phase checkbox in `specs/roadmap.md` as complete."

### 6. Confirm with the user

Show the three files. Ask for approval or edits before implementation begins.

## Constraints

- Stay consistent with `specs/tech-stack.md`. Don't introduce new libraries or patterns without calling them out in `requirements.md` under Decisions.
- Keep scope narrow enough to ship in one phase. If the interview reveals the feature is bigger than one phase, stop and propose a roadmap edit.
- Three files, always. `requirements.md`, `plan.md`, `validation.md`. Same names every time.
- Never write code or edit files outside `specs/` from within this skill.
