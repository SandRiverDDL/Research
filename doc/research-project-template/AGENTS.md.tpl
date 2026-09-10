# <PROJECT_TITLE> Research Workspace

> This file narrows `/Users/chy/Research/AGENTS.md`.
> Current directory is for **<PROJECT_TITLE>**: <ONE_SENTENCE_SCOPE>.

## Current Goal

Build a source-backed literature map for `<RESEARCH_LENS>`, prioritizing:

- <CORE_QUESTION_1>
- <CORE_QUESTION_2>
- <CORE_QUESTION_3>
- <CORE_QUESTION_4>

This project is a research lens, not necessarily a mature community survey category. Do not force papers into this project if their core contribution belongs elsewhere.

## Boundary

Include:

- <IN_SCOPE_1>
- <IN_SCOPE_2>
- <IN_SCOPE_3>

Move or cross-link to neighboring projects:

- `<NEIGHBOR_PROJECT_1>/`: <BOUNDARY_RULE_1>
- `<NEIGHBOR_PROJECT_2>/`: <BOUNDARY_RULE_2>

Mixed papers:

- If this project's mechanism is the core contribution, write this project's perspective card.
- If another project owns the core contribution, only add a queue / cross-link row here.
- If both are substantial, dual-register and write separate perspective cards.

## Entry Points

Read in this order:

1. `doc/memory/STATE.md` — hot state and next actions.
2. `synthesis/queue.md` — canonical script queue.
3. `doc/acceptance-rules.md` — what can enter queue / formal L1.
4. `doc/retrieval-strategy.md` — how to recall papers.
5. `doc/templates/l1-card.md` — L1 card template.
6. `doc/taxonomy/failure-modes.md` and `doc/taxonomy/design-knobs.md` — stable tag vocabulary.
7. `doc/memory/DECISIONS.md` and `doc/memory/OPEN-QUESTIONS.md` when scope or unresolved issues matter.

## Literature Pipeline Hard Gates

- Queue row is not a card.
- Survey mention is recall signal, not paper evidence.
- No original paper PDF / HTML / bounded brief, no formal L1 card.
- `notes/` root only contains formal L1/L2 notes.
- Run `scripts/autoresearch.py validate` before reporting completed cards.
- `scripts/autoresearch.py` handles hygiene / lookup / audit / pack only; Codex makes research judgments.

## Directory Contract

- `doc/`: topic rules, templates, taxonomy, memory.
- `notes/`: formal L1/L2 paper notes.
- `synthesis/`: queue, seed sources, structured comparisons, bottleneck reconstruction, and idea synthesis.
- `papers/`: PDF mirrors or temporary downloads.
- `_meta/`: generated or bounded source artifacts; do not manually maintain generated files.
- `scripts/autoresearch.py`: project-local helper.

## L1 Card Metadata

New L1 cards use short YAML plus a trailing `<!-- meta: ... -->` block.

Required frontmatter is defined in `doc/triage-rules.json`. Keep human-useful, Obsidian-filterable fields in YAML; put low-frequency source metadata such as authors, URL, PDF, and brief paths in the trailing meta block.

## Constraints

- L1 is a research index, not a full paper summary.
- Strong claims require source anchors.
- Reports must label fact / interpretation / conjecture / open question.
- Do not add new workflow fields unless they can be validated or maintained.
