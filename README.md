# Agentic Project Template

A GitHub template for **developers working with agents**, built around **spec-driven development (SDD)** — kept light by default so it speeds you up instead of slowing you down.

- **Light by default, escalate on risk** — most work is a two-way door: reversible, so the agent just builds it and leaves a breadcrumb. Only one-way-door changes (migrations, auth, public APIs, constitution edits) get the full spec trio. Ceremony scales with the cost of being wrong.
- **Bootstrap skill** — drafts the project's constitution (mission, tech stack, first initiative) on a fresh repo, or documents an existing one.
- **Per-initiative roadmaps** — multiple people, each driving their own agent, can work in parallel without colliding on the constitution.
- **Phase-sized work** — phases are closed increments that fit one agent context window; no stub-then-finish pairs.
- **Agent-agnostic workflow** — the rules live in `AGENTS.md`, so any agent or IDE that reads it (Claude Code, Cursor, Codex, etc.) can follow the same workflow. The automation ships as Claude Code skills (`bootstrap`, `feature-spec`, `coding-discipline`); other agents run the same steps by reading those skill files directly — each is written as a plain procedure, not Claude-specific magic.

## Prerequisites

- [GitHub CLI](https://cli.github.com/) (`gh`) — required for issue tracking. Run `gh auth login` after installing.
- **MCP servers** (optional) — `.mcp.json` pre-wires Context7 (live library docs), the GitHub server, and Playwright. Claude Code auto-loads it; the GitHub server needs a `GITHUB_PAT` in your environment. Remove any server a project doesn't need.

## Quick start

### Greenfield project

Click **Use this template** on GitHub to create a new repo with this structure already in place. Then:

#### 1. Bootstrap the constitution

```text
Bootstrap the project. My project is about: [one sentence].
```

The `bootstrap` skill will interview you and draft `specs/mission.md`, `specs/tech-stack.md`, and the first initiative under `specs/initiatives/` together with you.

#### 2. Start a phase

```text
Start the next phase of [initiative name].
```

The `feature-spec` skill reads the initiative's roadmap and runs the **two-way-door test** to size the phase. If it's reversible, it goes light — records intent on the roadmap and builds. If it's a one-way door, it consults the constitution, fills gaps with you, and produces the spec trio before any code is written. The agent states which path in one line; one word overrides it.

### Brownfield project

To adopt this workflow in an existing repo:

1. Copy the following into your project root: `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.mcp.json`, and the `specs/` folder (without the scaffold content — just the structure).
2. Run `gh auth login` if needed.
3. Run the bootstrap skill — it will interview you about your existing project and fill in the constitution based on what's already built, not what you're starting from scratch.

The bootstrap skill is designed to document reality, not invent it. Point it at an existing codebase and it will produce a constitution that reflects what's there.

## What bootstrap produces

Running the `bootstrap` skill on a fresh template fills in the constitution and creates the first initiative. A typical post-bootstrap repo looks like this:

```text
my-project/
├── AGENTS.md
├── CLAUDE.md
├── README.md
└── specs/
    ├── mission.md          ← what the project does, who uses it, success criteria
    ├── tech-stack.md       ← architecture, stack choices, interfaces, testing
    ├── initiatives/
    │   └── <first-initiative>/
    │       └── roadmap.md  ← phases for this initiative
    └── research/
```

From there, `Start the next phase of <initiative>` runs the `feature-spec` skill, which produces the spec trio (requirements, plan, validation) for the next phase before any code is written.

## What's in the box

- **`AGENTS.md`** — agent-agnostic workflow documentation.
- **`CLAUDE.md`** — Claude Code entry point that points at `AGENTS.md`.
- **`specs/`** — constitution files (mission, tech stack) plus `initiatives/` and `research/`.
- **`.claude/skills/bootstrap/`** — interviews you to draft the constitution and first initiative on a fresh repo.
- **`.claude/skills/feature-spec/`** — automates new-phase kickoff (constitution consult + spec trio generation).
- **`.claude/skills/coding-discipline/`** — behavioral guardrails applied while implementing a phase (think before coding, simplicity first, surgical changes, verifiable goals), derived from [Andrej Karpathy's observations on LLM coding pitfalls](https://x.com/karpathy/status/2015883857489522876).
- **`.mcp.json`** — pre-wired MCP servers (Context7, GitHub, Playwright); edit to taste.
- **`LICENSE`**, **`.gitignore`** — standard project hygiene.

## Who this is for

For developers who build with agents — one person per feature, driving an agent, solo or alongside others. Sharing the repo works, but there's no team-coordination machinery beyond git and PRs. The docs are written primarily for agents to consume, so they can pick up context without being told what to read. It is not a team coordination tool, a project management system, or a task-tracker replacement — it is an opinionated repo layout that keeps specs and code honest with each other.

## Design assumptions & constraints

The workflow is frictionless when two assumptions hold, and deliberately constrained where they meet multi-person work:

1. **Phases within an initiative are sequential** — one completes before the next starts. Different people or agents can work different initiatives simultaneously, since each lives in its own folder with no file overlap.
2. **One person owns the constitution** — someone has final authority over `specs/mission.md` and `specs/tech-stack.md`. Because those files are shared, edits from multiple branches will need merge resolution. That friction is intentional: constitution changes are significant and should be visible, not silently merged.

Coordination relies on git and PRs — no assignment mechanism, no phase lock, no review gate beyond what a PR provides. Branch creation claims a phase; the PR is the gate. For a small team, that's enough.

## Issue tracking

Non-blocking bugs and polish go to **GitHub Issues**, not the spec workflow — if it needs a spec it's an initiative, if it doesn't it's an issue. The agent surfaces the suggestion, you authorize, and it files with `--label bug` or `--label enhancement`. See `AGENTS.md` for the full convention.

## Why spec-driven

Specs are durable; code is disposable. When the agent (or the human) changes, the specs don't — so any agent can pick up where another left off. They're also deliberately short and deliberately rare: a spec too long to read gets rubber-stamped, which is worse than no spec, so the template writes a full trio only for one-way-door work and leaves a one-line breadcrumb for everything else.

See `AGENTS.md` for the full workflow.

## Acknowledgements

The conceptual core of this workflow — write specs before code, keep them in the repo, organize them as a constitution plus a per-phase spec trio — comes from [DeepLearning.AI's short course on Spec-Driven Development with Coding Agents](https://www.deeplearning.ai/short-courses/spec-driven-development-with-coding-agents/). This template builds on those ideas and adds what a reusable starting point needs: the bootstrap skill, per-initiative roadmaps, phase-sizing and closure rules, agent-agnostic instructions, and the brevity, testing, and coding-discipline conventions.

## License

MIT — see [LICENSE](LICENSE).
