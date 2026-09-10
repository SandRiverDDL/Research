---
type: idea
node_id: idea:opd-20260820-c12-amortized-frontier
title: "Amortized Compute Frontier for OPD"
stage: archived
outcome: unknown
added: 2026-08-21T07:04:45Z
based_on: []
target_gaps: []
tags: ["opd", "compute-allocation", "test-time-scaling", "parked", "idea-pool-2026-08-20"]
---

# Amortized Compute Frontier for OPD

**stage:** `archived`  ·  **outcome:** `unknown`

统一计算 OPD 训练、teacher scoring、rollout 与部署推理成本，并与相同总预算下的 base test-time scaling 比较。

## Thesis
OPD 是否优于直接增加 base-model test-time samples，取决于部署查询量和 amortized break-even point。

## Key risks
Jury：Park。若没有稳定的 ranking reversal 或 OPD-specific scaling law，容易退化成硬件相关 accounting。未运行实验。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

