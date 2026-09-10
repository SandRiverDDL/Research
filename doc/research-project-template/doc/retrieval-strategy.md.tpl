# <PROJECT_TITLE> Retrieval Strategy

> This document defines how to find papers. Admission rules live in `doc/acceptance-rules.md`.

## Recall Focus

Candidates must primarily contribute to `<RESEARCH_LENS>`:

- <RECALL_FOCUS_1>
- <RECALL_FOCUS_2>
- <RECALL_FOCUS_3>

Do not default-include:

- <REJECT_FOCUS_1>
- <REJECT_FOCUS_2>

## Recall Sources

Use:

1. **Seed survey recall**: extract direct method references from relevant survey sections.
2. **Known-item recovery**: user-named or project-named papers enter queue, then source verification.
3. **Neighbor backflow**: inspect neighboring projects for overlap papers.
4. **Keyword direct search**: one-time search only when discovering a new term family or obvious coverage gap.

## Bounded Snowballing Loop

```text
seed / known-item
  -> source verification
  -> candidate classification
  -> apply doc/acceptance-rules.md
  -> collect PDF / HTML / brief
  -> write approved L1 cards
  -> validate
```

Stop recall when two consecutive rounds add <= 2 high-priority candidates.

## Batch-First Admission

Classify candidates before writing cards:

| candidate | class | reason | action |
|---|---|---|---|
| paper title | core / survey / benchmark-eval / adjacent / background / reject | 1 sentence | card / hold / ask user |

Do not write more than 3-5 L1 cards in one batch without validation.

## Candidate Log

Write candidates to `synthesis/queue.md` or a focused synthesis document. Do not leave recall state only in chat.

Each candidate row should include:

- `source`
- `recall_reason`
- `boundary_risk`
- `action`
