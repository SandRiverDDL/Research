---
type: idea
node_id: idea:g15-reciprocal-meta-distillation
title: "互惠可学性元蒸馏"
stage: archived
outcome: pending
added: 2026-10-15T14:00:13Z
based_on: ["paper:sun2026_d³mopd_dynamic_domain", "paper:zhu2026_upmopd_update_projection"]
target_gaps: ["gap:G15"]
tags: ["g15", "l1"]
---

# 互惠可学性元蒸馏

**stage:** `archived`  ·  **outcome:** `pending`

C02 · L1 · 来源 A2；本轮未优先，归档保留，不是负实验或永久排除。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. 在普通A更新后的student上，用固定B support轨迹虚拟训练k步，计算独立query上的增益G_B=L_B(训练前)−L_B(训练后)；teacher评分在该episode内固定。
2. 对G_B反传得到可学性元梯度，并去掉其沿当前B query梯度的分量，避免通过一阶恶化起点loss制造虚假学习增益。
3. 将限幅后的元梯度作为实际A更新的附加修正；训练B时对称处理A，虚拟权重丢弃，最终仍只有一个student。

【待验证假设】A的可行更新方向对未来B学习效率具有不同影响，而普通A loss下降及梯度夹角无法充分区分它们。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】投影学习增益可能精确等价于投影终点loss；需排除起点恶化与一般meta-learning。

归档仅表示本轮不优先，允许新证据后重审。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

