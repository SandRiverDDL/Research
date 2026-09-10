---
type: idea
node_id: idea:opd-20260820-c01-decoder-envelope
title: "Decoder-Envelope Capability Audit"
stage: proposed
outcome: pending
added: 2026-08-21T07:04:45Z
based_on: []
target_gaps: []
tags: ["opd", "capability-audit", "test-time-scaling", "idea-pool-2026-08-20"]
---

# Decoder-Envelope Capability Audit

**stage:** `proposed`  ·  **outcome:** `pending`

在等生成 token 预算下，用预注册 decoder grid 比较 fixed-decoder 与 envelope-level 的 retained/learned/forgotten 集合。

## Thesis
OPD 的一部分 large-K capability loss 可能来自后训练概率几何与单一固定 decoder 的失配，而非正确轨迹从模型 support 中消失。

## Key risks
Jury：Rank 4，建议先做低成本 probe；若 held-out decoder envelope 下差距不变则停止。单纯 decoder sweep 不足以支撑顶会论文。来源：idea-stage/IDEA_REPORT_20260820-234115.md。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

