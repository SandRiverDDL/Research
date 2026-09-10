---
type: idea
node_id: idea:opd-20260820-c03-rare-solution-replay
title: "Rare-Solution Replay OPD"
stage: archived
outcome: unknown
added: 2026-08-21T07:04:45Z
based_on: []
target_gaps: []
tags: ["opd", "replay", "retention", "abandoned", "idea-pool-2026-08-20"]
---

# Rare-Solution Replay OPD

**stage:** `archived`  ·  **outcome:** `unknown`

把低频但正确的 base trajectories 作为普通监督批次，与等预算 OPD 交替训练。

## Thesis
均匀回放稀有正确解可能保留 base capability boundary，同时维持 OPD 的采样效率增益。

## Key risks
Jury：Abandon。本质接近 replay 加 rare-positive heuristic；On-Policy Replay 使其更适合作为 baseline。未运行实验。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

