---
type: idea
node_id: idea:opd-20260820-c13-fresh-state-rehearsal
title: "Fresh-State Rehearsal for Continual OPD"
stage: archived
outcome: unknown
added: 2026-08-21T07:04:45Z
based_on: []
target_gaps: []
tags: ["opd", "continual-learning", "rehearsal", "abandoned", "idea-pool-2026-08-20"]
---

# Fresh-State Rehearsal for Continual OPD

**stage:** `archived`  ·  **outcome:** `unknown`

只保存历史 prompts，训练时由当前 student 在旧新任务上重新生成 states，再用固定 teacher 做普通 OPD。

## Thesis
Sequential OPD forgetting 可能部分来自不再访问旧任务 prefix states；fresh current-policy rehearsal 可能优于答案回放。

## Key risks
Jury：Abandon。Continual Prompt Replay 几乎正面覆盖这一数据源逻辑，teacher-scored OPD 区别可能只是增量。未运行实验。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

