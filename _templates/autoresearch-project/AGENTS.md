# Autoresearch Project Template

> Copy this folder for a new long-running literature project, then replace project-specific scope, taxonomy, and card template.

## Scope

- Define the topic boundary here.
- Queue broadly, but write formal cards only from original paper evidence.
- Keep project-specific vocabulary in `doc/triage-rules.json`.

## Required Workflow

1. Add survey-derived or search-derived candidates to `comparison/queue.md`.
2. Use `scripts/autoresearch.py lookup <query>` to avoid duplicates.
3. Use `scripts/autoresearch.py pack --limit 3` to prepare bounded inputs.
4. Let Codex decide whether to write the L1 card from the original source/brief.
5. Run `scripts/autoresearch.py validate` before reporting completion.

## Non-Negotiable Card Gate

- Queue row is not a card.
- Survey mention is recall evidence, not paper evidence.
- No original paper PDF/HTML brief, no formal L1 card.
- Do not create survey-only formal cards. If legacy survey-only notes are discovered, move or mark them outside the formal `notes/` set and do not count them as valid cards.
- Script validation only checks hygiene; Codex makes research judgments.

## Directories

- `papers/`: local PDFs or source mirrors.
- `notes/`: valid L1/L2 notes only.
- `notes/provisional-survey-derived/`: legacy cleanup quarantine only, not a normal workflow.
- `comparison/`: queues, audits, synthesis.
- `_meta/briefs/`: bounded source briefs.
- `_meta/generated/`: script outputs; do not edit manually.
