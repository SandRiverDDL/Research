# Research Project Template

> Template version: 2026-07-28.
> This template is the default scaffold for new long-running research topics under `/Users/chy/Research/`.

## Purpose

This directory captures the reusable project layer that was previously implicit in mature projects such as `agentic-rl/`:

- local `AGENTS.md` scope contract
- hot memory files
- queue / acceptance / retrieval rules
- L1 card template
- stable taxonomy files
- lightweight `scripts/autoresearch.py` helper for status, validation, lookup, audit, and bounded packs

Skills provide the methodology. This template provides the file contract. A topic project provides the scope, taxonomy, seeds, and decisions.

## New Project Workflow

For a new long-running research topic:

1. Create the topic directory under `/Users/chy/Research/<topic>/`.
2. Copy this template contents into the topic directory.
3. Rename `*.tpl` files by removing `.tpl`.
4. Replace placeholders such as `<PROJECT_TITLE>`, `<PROJECT_SLUG>`, `<RESEARCH_LENS>`, and `<NEIGHBOR_PROJECTS>`.
5. Fill the project-specific parts:
   - scope and boundary
   - `paper_type` taxonomy
   - `failure_modes`
   - `design_knobs`
   - initial seed / queue rows
   - lifecycle roles and acceptance exceptions
6. Run:

```bash
python3 scripts/autoresearch.py status
python3 scripts/autoresearch.py validate
```

Do not write formal L1 cards until the project has an original paper PDF / HTML / bounded brief source.

## Existing Project Policy

Template changes do **not** automatically migrate existing projects.

Existing projects keep their local contract until the user explicitly asks for migration. This avoids silent breakage in old notes, queues, validators, or synthesis reports.

When the template changes:

- Add or update files in this template.
- If the change is breaking, document the migration path in this README.
- Do not bulk-edit existing projects.
- To migrate one project, compare its local files against the template, make a narrow migration plan, then run that project's `scripts/autoresearch.py validate`.

### Migration: `comparison/` → `synthesis/`

The template now uses `synthesis/` for comparisons, bottleneck reconstruction, idea generation, and other cross-paper judgments. Existing projects migrate by renaming the directory, replacing path references, updating the helper's canonical queue path, and running `validate`; no compatibility directory is required.

## Change Classes

- **Patch**: typo, explanation, non-behavioral wording. Template only.
- **Additive**: new optional field, optional taxonomy tag, new helper command. Template only; old projects may adopt later.
- **Breaking**: required frontmatter changes, queue schema changes, validator behavior changes. Requires explicit per-project migration.

## Minimal Project-Specific Surface

A new topic should only need project-specific edits in:

- `AGENTS.md`
- `doc/memory/STATE.md`
- `doc/acceptance-rules.md`
- `doc/retrieval-strategy.md`
- `doc/triage-rules.json`
- `doc/templates/l1-card.md`
- `doc/taxonomy/failure-modes.md`
- `doc/taxonomy/design-knobs.md`
- `synthesis/queue.md`
- `synthesis/seed-sources.md`

The helper scripts should stay generic unless a project genuinely needs custom mechanical checks.
