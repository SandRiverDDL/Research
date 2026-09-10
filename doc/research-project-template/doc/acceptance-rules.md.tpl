# <PROJECT_TITLE> Acceptance Rules

> This document defines what can enter queue / formal L1. Retrieval rules live in `doc/retrieval-strategy.md`.

## Basic Principles

- Queue can be broad; formal L1 must be strict.
- Application domain alone does not determine inclusion.
- Judge by the reusable contribution to `<RESEARCH_LENS>`.
- When unsure, use `queue / review` rather than writing a formal card.

## Hard Gates

Formal L1 cards require:

- Original paper PDF / HTML / source brief.
- A clear mechanism relevant to `<RESEARCH_LENS>`.
- At least one reusable design knob from `doc/taxonomy/design-knobs.md`.

## Time / Venue Gate

Prioritize:

- <TIME_WINDOW_OR_RECENCY_RULE>
- strong venue / strong lab / code / data / project page
- papers that directly affect current novelty risk

Older papers enter only if they are canonical anchors, repeated baselines, or unavoidable for comparison.

## Core Mechanism Gate

Include if the core contribution changes:

- <CORE_MECHANISM_1>
- <CORE_MECHANISM_2>
- <CORE_MECHANISM_3>

Do not automatically include:

- <OUT_OF_SCOPE_1>
- <OUT_OF_SCOPE_2>

## Boundary Handling

Common boundary risks:

- `boundary_risk: none`
- `boundary_risk: adjacent`
- `boundary_risk: eval`
- `boundary_risk: recipe`
- `boundary_risk: infra`

For each boundary item, write why it may belong here, why it may belong elsewhere, and what evidence would decide.

## Queue vs Card

Queue row minimum:

- verifiable source
- one-sentence `recall_reason`
- initial `paper_type` and `boundary_risk`

Formal L1 minimum:

- passes hard gates
- passes time / venue gate or has an exception
- has bounded original source input
- passes `scripts/autoresearch.py validate`
