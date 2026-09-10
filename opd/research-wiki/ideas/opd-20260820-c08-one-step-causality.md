---
type: idea
node_id: idea:opd-20260820-c08-one-step-causality
title: "One-Step Gradient Causality Matrix"
stage: archived
outcome: unknown
added: 2026-08-21T07:04:45Z
based_on: []
target_gaps: []
tags: ["opd", "gradient-analysis", "causal-probe", "abandoned", "idea-pool-2026-08-20"]
---

# One-Step Gradient Causality Matrix

**stage:** `archived`  ·  **outcome:** `unknown`

在早中晚 checkpoint 克隆上分别施加等范数 teacher-matching、verifier、反向和随机单步更新，并测量即时行为变化。

## Thesis
同一 student states 上，teacher-matching 与 verifier-outcome 梯度可能产生方向相反的即时因果效果，即使 cosine 看似正常。

## Key risks
Jury：Abandon。Unmasking OPD 已定义 success gradient 并做细粒度 alignment；若只做 measurement matrix，新增空间有限。未运行实验。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

