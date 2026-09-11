# Project Loop

## What Belongs Where

Skill files hold cross-project behavior:

- stable research methods
- Codex operating rules
- evidence and validation standards
- routing between literature, synthesis, idea review, and experiments

Workspace or project `AGENTS.md` files hold local contracts:

- directory layout and startup files
- environment commands and hard boundaries
- topic scope and exclusions
- project-local helper commands
- card schema, taxonomy, vocab, and acceptance rules

Project memory files hold durable state:

- `STATE.md`: short current state, next actions, reliable findings, and open risks
- `DECISIONS.md`: stable decisions and historical reasons
- `OPEN-QUESTIONS.md`: unresolved questions that should not be forgotten

Do not move project-specific vocabulary, survey cutoff assumptions, or temporary triage rules into the global skill.

## Startup Pattern

For an existing project:

1. Read the smallest local instruction/state set needed for the request.
2. Identify current artifacts: notes, queue, comparison, reports, source briefs, experiment records, and helper scripts.
3. If there are multiple plausible workflows, state the assumption before acting.
4. If a pipeline is broken, find the root cause and minimal reproduction before patching.

For a new long-running research topic, create only the minimum structure:

```text
AGENTS.md
papers/
notes/
comparison/
doc/memory/STATE.md
```

Add templates, validators, queues, and generated artifacts only when the project is expected to manage enough papers or runs to justify them.

## Simplicity Rule

Prefer the smallest durable process that answers the research question. A process is worth adding only if it prevents repeated mistakes, reduces manual bookkeeping, or protects evidence integrity.
