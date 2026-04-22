# Initiatives

One folder per initiative. Each initiative folder contains a `roadmap.md` (the phases for that initiative) and a dated spec folder per phase.

## Structure

```
initiatives/
└── initiative-name/
    ├── roadmap.md
    └── 2026-04-22-phase-name/
        ├── requirements.md
        ├── plan.md
        └── validation.md
```

## Naming

Initiative folders use kebab-case: `auth-redesign`, `payment-flow`, `onboarding-v2`.

Phase folders use `YYYY-MM-DD-<phase-name>` (date in UTC) so they sort chronologically within the initiative.

## Threshold

If work needs a spec, it is an initiative. If it doesn't, it is a GitHub Issue.
