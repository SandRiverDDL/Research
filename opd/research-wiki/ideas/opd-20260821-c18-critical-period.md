---
type: idea
node_id: idea:opd-20260821-c18-critical-period
title: "Critical Period for OPD"
stage: archived
outcome: pending
added: 2026-08-21T08:50:57Z
based_on: []
target_gaps: []
tags: ["opd", "idea-pool-2026-08-21"]
---

# Critical Period for OPD

**stage:** `archived`  ·  **outcome:** `pending`

在不同 pretraining checkpoints 插入相同 OPD pulse，再继续相同 future stream。

## Thesis
OPD 可能存在不同于 RL/offline KD 的持久性或反转窗口。

## Key risks
训练时点定位与 front-loading/RL-excursion 工作重叠，且接近用户不看好的旧方向。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

