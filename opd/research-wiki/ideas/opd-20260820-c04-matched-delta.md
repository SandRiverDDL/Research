---
type: idea
node_id: idea:opd-20260820-c04-matched-delta
title: "Matched-Delta Causal Control"
stage: proposed
outcome: pending
added: 2026-08-21T07:04:45Z
based_on: []
target_gaps: []
tags: ["opd", "causal-control", "teacher-delta", "reasoning-style", "idea-pool-2026-08-20"]
---

# Matched-Delta Causal Control

**stage:** `proposed`  ·  **outcome:** `pending`

构造 reasoning × style 的 matched-ancestry factorial，再以相同 student、prompts 和预算蒸馏各 teacher-minus-base delta。

## Thesis
Teacher-minus-base delta 只有在来源确实是 reasoning acquisition 时才会向 student 转移新能力；否则主要传递 style 或一般 policy shaping。

## Key risks
Jury：Rank 2，谨慎推进。Lightning OPD 2.0 已压缩“delta 含 style”的空间；style-only 干预难以识别，且需要至少两套可信 ancestry。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

