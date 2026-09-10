---
type: idea
node_id: idea:opd-20260820-c06-update-grafting
title: "Causal Update Grafting Across Objectives"
stage: proposed
outcome: pending
added: 2026-08-21T07:04:45Z
based_on: []
target_gaps: []
tags: ["opd", "off-policy-distillation", "causal-grafting", "geometry", "top-candidate", "idea-pool-2026-08-20"]
---

# Causal Update Grafting Across Objectives

**stage:** `proposed`  ·  **outcome:** `pending`

从同一 base 训练 matched OPD 与 off-policy distillation，分解其参数 delta，并把等范数组件移植回 fresh base 做功能干预。

## Thesis
OPD 的 sampling-efficiency 更新与 off-policy distillation 的 capability-expansion 更新可能由功能可分的参数成分承载。

## Key risks
Jury：Rank 1，PROCEED，主项目首选。最大风险是 delta graft 对参数基底、层选择和分解方法敏感；必须用随机子空间、符号翻转、layer shuffle 和多 seed 证明移植合法。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

