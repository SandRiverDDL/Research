---
type: idea
node_id: idea:opd-20260822-c07-equivalence-class-routes
title: "Quotient-OPD: Execution-Equivalent Route Preservation"
stage: proposed
outcome: pending
added: 2026-08-21T16:36:05Z
based_on: []
target_gaps: []
tags: ["opd", "agentic-opd", "tool-use", "route-diversity"]
---

# Quotient-OPD: Execution-Equivalent Route Preservation

**stage:** `proposed`  ·  **outcome:** `pending`

在多条工具路径到达同一环境效果时，避免 OPD 压掉备用路线。

## Thesis
标准 token OPD 可能在保持原分布成功率的同时压掉 execution-equivalent 备用工具路线；在效果等价类上蒸馏并保留类内路径比例可提高工具失效鲁棒性。

## Key risks
仅匹配类总概率不保证类内覆盖；若简单 entropy/support-union 匹配，或 effect class 需人工枚举，则停止。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

