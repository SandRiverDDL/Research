---
name: autoresearch
description: Compatibility entrypoint for automated literature research, paper-card workflows, queue/brief/validator repair, and legacy autoresearch prompts. For current behavior, route to research-codex-workflow literature pipeline.
---

# Autoresearch

This skill is a compatibility wrapper. The canonical research workflow now lives in `research-codex-workflow`.

When a user asks for:

- autoresearch
- automatic paper discovery or summarization
- batch paper cards
- survey processing
- queue, brief, or validator repair
- L1/L2 paper-card workflows
- migrating older Claude/cc-internal autoresearch processes back to Codex

use `research-codex-workflow` and read:

```text
research-codex-workflow/references/literature-pipeline.md
```

## Compatibility Rules

- Do not maintain a second independent workflow here.
- Prefer project-local instructions, templates, and helper scripts.
- Treat survey-only formal cards as legacy errors to clean up, not as a normal workflow.
- Keep generated artifacts and project-specific vocab in project docs, not in this skill.

If a project still has legacy autoresearch files such as manifest, target-card lists, old validation reports, or `references/card-workflow.md`, use them only as project history unless the project `AGENTS.md` says they remain current.
