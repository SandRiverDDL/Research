# Stage Note Template

Use this as a light template. For model TR / open recipe stage-specific reminders, read `doc/model-tr-stage-notes.md`; its checklists are not mandatory headings.

```yaml
---
source_id: <slug>
section_type: architecture | pretraining-data-mixture | pretraining-engineering | rl-training | sft-distillation | reward-verifier | tool-agent-training | consolidation | eval | infra | safety | claims-and-gaps
stage: architecture | pretraining | post-training | eval | infra | safety | claims-and-gaps
substage: data-mixture | mid-training-long-context-yolo | rl-training | sft-distillation | reward-verifier | tool-agent-training | consolidation | none
depth: surface | working | deep
confidence: low | medium | high
need_expert_review: false
---
```

## Core Design / Innovation

- 

## Why It Matters

这部分值得学什么；哪些能培养 intuition / taste，哪些只是 lookup-only。

## Mechanism Sketch

1. 

## Details / Evidence

### <method / data / reward / sampling / eval / infra>

- 

## Method Blocks

Use only when a stage contains important mechanisms that are not yet worth separate files.

### <method name>

- 官方披露：
- 合理解释：
- 未披露 / 不能下结论：

## Gaps / Open Questions

- 

## Lookup-only

- 

## Evidence Anchors

- 12-13: short description of the page range.
- model-card:2-4: short description of the non-TR source.

## Optional Split Check

- If this file grows beyond ~220 lines or contains 3+ independent flows, split by substage.
- If a method block has its own problem, mechanism, tradeoff, evidence, gaps, and recurring comparison value, split it into a method note.
