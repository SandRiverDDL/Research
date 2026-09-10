---
type: idea
node_id: idea:opd-20260820-c09-plan-lattice
title: "Plan-Lattice OPD"
stage: proposed
outcome: pending
added: 2026-08-21T07:04:45Z
based_on: []
target_gaps: []
tags: ["opd", "state-coverage", "planning", "multi-rollout", "idea-pool-2026-08-20"]
---

# Plan-Lattice OPD

**stage:** `proposed`  ·  **outcome:** `pending`

让 student 为每题生成多个互异高层 plan，再分别自行 rollout；teacher 只在这些 student-visited states 上执行普通 OPD。

## Thesis
OPD 难以获得新能力的瓶颈可能是 student 访问的策略集合过窄；多计划可打开未访问但可局部纠正的状态。

## Key risks
Jury：Rank 3，谨慎推进。必须在等 rollout/teacher-token 预算下击败普通多采样、prompt paraphrase 和 diversity-constrained plan，否则只是 multi-rollout 加 planning prompt。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

