---
name: bootstrap
description: Interviews the user to draft the project constitution — mission.md, tech-stack.md, and roadmap.md — in that order. Trigger on a fresh clone of the template when the user says things like "bootstrap the project", "set up the constitution", "fill in mission/tech-stack/roadmap", "this is a fresh repo — let's start", "help me write the mission", or asks for help writing any of the three constitution docs. Can target one doc at a time or run all three back-to-back.
---

# Bootstrap Skill

## When to run

Trigger on a fresh clone, before any feature work. The three constitution docs (`specs/mission.md`, `specs/tech-stack.md`, `specs/roadmap.md`) must be meaningfully filled in before the `feature-spec` skill can do useful work.

If the user asks to fill in only one doc, do just that one. Otherwise run all three in order: mission → tech-stack → roadmap. The order matters — each doc builds on the previous.

## Before you start

Check the current state of each target file:

- If the file still contains only HTML-comment scaffolding (no real prose), it's safe to replace.
- If the file has real content already, stop and ask: revise, append, or leave alone? Don't silently overwrite the user's work.

## Part 1 — Mission

Ask exactly three questions, one at a time, waiting for each answer before the next:

1. **Purpose & users** — "In one or two paragraphs: what does this project do, who uses it, and what problem does it solve?"
2. **Capabilities & success** — "What are the top 3–7 things the system must do, and how will you know it's working? Prefer measurable criteria."
3. **Scope & philosophy** — "What's explicitly in scope for the first version, what are you deferring (and why), and what non-negotiables shape every downstream decision?"

Synthesize the answers into `specs/mission.md`, preserving the section structure from the scaffold (Core Purpose, Users, Problems Solved, Key Capabilities, Success Metrics, Scope: Included, Scope: Deferred, Design Philosophy). Remove the HTML-comment guidance from sections you've filled in.

Show the draft. Get explicit approval before moving on.

## Part 2 — Tech Stack

Only start after `mission.md` is approved.

Ask exactly three questions, one at a time:

1. **Architecture** — "What's the high-level architecture? Major components and how they talk to each other."
2. **Choices & rationale** — "Language, framework, database, key libraries — each with a one-line reason."
3. **Interfaces, config & testing** — "What are the entry points (API, CLI, UI)? Key environment variables? How will you verify correctness?"

Synthesize into `specs/tech-stack.md`, preserving the scaffold's section structure (System Design, Stack Choices, Data Model Overview, Interfaces, Configuration, Testing Strategy, Dependencies, Open Questions). If the user has unresolved decisions, put them in Open Questions rather than inventing answers.

Show the draft. Get approval.

**After approval:** update `.gitignore` with stack-specific entries derived from the approved stack choices. The commented section at the bottom of `.gitignore` has examples. Add entries there, then show the diff to the user for confirmation before moving on to Part 3.

## Part 3 — Roadmap

Only start after `tech-stack.md` is approved.

Ask exactly three questions, one at a time:

1. **Phase 1** — "What's the smallest thing you could ship that shows the system exists? One focused session's worth of work."
2. **Near-term phases** — "What comes next, in rough order? Each phase must fit one focused session — if it needs more, split it."
3. **Horizon** — "Any later phases you can sketch in a single line? Don't over-plan — roadmap is a living document."

Synthesize into `specs/roadmap.md` using the phase template in the scaffold. Every phase gets a one-sentence **Goal** and a checkbox task list. Enforce the one-session rule: if any phase has 10+ tasks or sounds like two sessions of work, split it before writing.

Show the draft. Get approval.

## Finish

Once all three docs are approved:

- Confirm the constitution is in place.
- Tell the user the next step: start Phase 1 by saying something like *"start the next phase"* or *"kick off Phase 1"* — which will invoke the `feature-spec` skill.

## Constraints

- Three questions per part, always. No mechanical question lists — each question is a macro prompt that invites a rich answer. If an answer is thin, ask a follow-up before moving on.
- Preserve the scaffold's section structure. Don't invent new top-level sections.
- Remove the HTML-comment guidance from sections you fill in — it served its purpose.
- Write specifically. Abstract constitution docs are useless to agents.
- Only edit `specs/` files and `.gitignore`. Don't touch any other files.
- Don't skip parts. If running all three, mission → tech-stack → roadmap in that order. If one fails approval, stop there.
