# Autoresearch Card Workflow

Deprecated compatibility reference. The canonical workflow now lives in:

```text
research-codex-workflow/references/literature-pipeline.md
```

Use this file only when a legacy project explicitly points to old autoresearch card files or commands.

## Core Card Contract

A good L1 card is a research index, not a mini-survey. It should preserve:

- **Core method**: what the method does.
- **Principle/mechanism**: why it should work.
- **Innovation**: what is actually new over immediate predecessors.
- **Decisions**: structured design choices that can be grepped or tabulated.
- **Solved problem**: failure mode or research gap addressed.
- **Lineage**: upstream, concurrent alternatives, downstream use.
- **Evidence anchors**: PDF/survey section, table, or figure references.

Move these out of L1:

- full experiment setup
- long ablation tables
- reproduction commands
- subjective verdicts
- open speculation

Those belong in L2 notes, comparison tables, or `doc/memory/STATE.md`.

## Legacy Generated Files

Prefer project-local current instructions over these legacy files. If they exist, treat them as generated state, not hand-maintained checklists.

Typical generated files:

```text
_meta/generated/manifest.jsonl          # one paper/candidate per line
_meta/generated/target-cards.md         # rewrite/rerun/keep queue
_meta/generated/card-validation.json    # machine-readable QA
_meta/generated/card-validation.md      # human-readable QA
_meta/generated/research-map.md         # compact decision index, tensions, coverage gaps
_meta/generated/idea-context.md         # compact ideation context
_meta/briefs/papers/           # bounded paper snippets
_meta/briefs/surveys/          # bounded survey mention windows
```

If these files exist, do not edit them by hand. Regenerate with the project script.

## Legacy OPD Commands

These were used by an older OPD high-throughput flow:

```bash
scripts/autoresearch.py sync
scripts/autoresearch.py build-survey-briefs
scripts/autoresearch.py build-briefs
scripts/autoresearch.py sync
```

Do not treat them as the default current workflow unless the project `AGENTS.md` says so. Current helper surfaces usually look like `status`, `validate`, `lookup`, `audit`, and `pack`.

Primary files:

```text
doc/codex-research-process.md
doc/templates/l1-card.md
doc/taxonomy/failure-modes.md
doc/memory/STATE.md
doc/memory/DECISIONS.md
doc/memory/OPEN-QUESTIONS.md
_meta/generated/manifest.jsonl
_meta/generated/target-cards.md
_meta/generated/card-validation.md
_meta/generated/research-map.md
_meta/generated/idea-context.md
```

## Model Input Budget

Target per-card model input:

- paper brief: 4-8k tokens
- survey windows: 1-3k tokens
- old card: 1-2k tokens
- template excerpt: 1-2k tokens

If the prompt exceeds this because of full PDFs, full surveys, or many old notes, stop and build a smaller brief first.

## Validation Order

Run validation before synthesis:

1. deterministic validator
2. card repair
3. deterministic validator again
4. cross-card reasoning
5. user review

This keeps the user's reading burden focused on research judgment rather than formatting, missing anchors, or schema drift.
