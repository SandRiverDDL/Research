---
type: idea
node_id: idea:opd-20260820-c15-checkpoint-subspace
title: "Checkpoint-Invariant Delta-Subspace Distillation"
stage: archived
outcome: unknown
added: 2026-08-21T07:04:46Z
based_on: []
target_gaps: []
tags: ["opd", "checkpoint-chain", "subspace", "abandoned", "idea-pool-2026-08-20"]
---

# Checkpoint-Invariant Delta-Subspace Distillation

**stage:** `archived`  ·  **outcome:** `unknown`

从 compatible teacher checkpoint chain 的相邻 activation deltas 中估计稳定低秩子空间，并分别蒸馏共享与残差成分。

## Thesis
跨 base、instruction-tuned 与 reasoning-post-trained checkpoints 稳定的 teacher-change 成分可能比 checkpoint-specific residual 更可复用。

## Key risks
Jury：Abandon。Checkpoint distillation、OPD²、representation distillation 和 subspace 的组合过重，缺乏独特结论。未运行实验。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

