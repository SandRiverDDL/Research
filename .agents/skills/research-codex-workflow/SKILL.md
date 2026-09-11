---
name: research-codex-workflow
description: Use when the user wants Codex to manage a research project, run literature/card workflows, read and compare papers, evaluate research ideas, design experiments, record runs, critique claims, or turn results into paper-ready notes.
metadata:
  origin: local-custom
  language: zh-CN
---

# Research Codex Workflow

Use Codex as a research collaborator and project memory, not as a blind batch worker. This skill covers the full research loop: literature discovery, paper reading, synthesis, idea review, experiment design, run recording, and writing support.

## Operating Model

Human owns the final research judgment:

- whether the problem matters
- whether baselines and metrics are fair
- whether a claim is true
- whether the paper story is credible

Codex owns execution and evidence hygiene:

- find and organize sources
- maintain compact project state
- read papers with bounded context
- compare methods and pressure-test ideas
- design minimal experiments
- record commands, configs, outputs, metrics, and conclusions
- surface risks before producing confident claims

## First Moves

Start from the smallest project-local context that can answer the request:

1. Read project instructions and current state/memory if they exist.
2. Read task-specific files such as queue, card template, report, comparison table, or experiment notes.
3. Read decision logs or open-question files only when historical rationale affects the task.
4. Prefer existing project-local scripts and templates over inventing a new process.

Do not rely on chat memory as the only source of truth after compaction or in a new session.

## Routing

- Literature discovery, batch cards, queue/brief/validator repair: read `references/literature-pipeline.md`.
- Single-paper reading or lightweight notes without a batch pipeline: read `references/paper-reading.md`.
- Comparison, research map, reports, novelty-risk checks, idea generation, reviewer mode: read `references/synthesis-and-ideas.md`.
- Experiment design, run records, result interpretation, paper-story iteration: read `references/experiment-design.md`.
- Project structure, durable memory, and what belongs in skill vs project docs: read `references/project-loop.md`.

Load only the reference needed for the current task.

## Global Rules

- Evidence before conclusion: facts must trace to a paper, PDF/page, source brief, Zotero entry, experiment record, or local file. Otherwise label them as interpretation, guess, or open question.
- Keep durable state in project files, not chat memory.
- Use scripts for mechanical work only: status, dedup, lookup, audit, bounded-input packing, and hygiene validation.
- Use Codex for research judgment: importance, paper type, method family, failure mode, novelty risk, idea hook, and synthesis.
- Do not feed full surveys, full PDFs, or large raw extraction dumps into context by default. Build or read bounded source briefs first.
- L1 notes are research indexes, not mini-surveys. Put deep reading, subjective verdicts, reproduction details, and experiment suggestions in L2 notes, comparison files, reports, or project memory.
- Reports are not card concatenations. Strong claims must point back to cards, source briefs, report appendices, L2 notes, experiment records, or original source anchors.
- Do not make generated artifacts mandatory if they cannot be maintained automatically.

## Research Standards

When planning, reviewing, or interpreting research:

- Do not claim improvement without baselines, ablations, and clear metrics.
- Prefer small clean controls before large sweeps.
- Actively check for data leakage, evaluator leakage, prompt-only tricks, weak baselines, and metrics that can be gamed.
- Ask whether the idea still matters if frontier models get stronger.
- Reject incremental deltas unless they remove a real bottleneck or change the evaluation story.
- Before reporting completion, state what was verified and what was not.
