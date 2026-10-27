---
type: idea
node_id: idea:g15-function-preserving-reparameterization
title: "功能不变的可学性再参数化"
stage: archived
outcome: pending
added: 2026-10-15T14:00:13Z
based_on: ["paper:li2026_beyond_teacher_assignment", "paper:zhu2026_from_gradients_capabilities"]
target_gaps: ["gap:G15"]
tags: ["g15", "l1"]
---

# 功能不变的可学性再参数化

**stage:** `archived`  ·  **outcome:** `pending`

C01 · L1 · 来源 A1；本轮未优先，归档保留，不是负实验或永久排除。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. 利用SwiGLU中up通道乘正对角矩阵D、down对应通道乘D逆的精确对称性，改变参数尺度而保持student当前输出不变。
2. 每隔固定训练块，在缓存的A/B轨迹上虚拟执行等预算、等更新范数的短OPD；仅优化D，使两域中较小的留出集学习收益提高。
3. 将选定变换及对应梯度坐标下的optimizer moments写回同一个student，随后继续常规联合OPD；部署不增加模块。

【待验证假设】A训练可能改变因子尺度及后续B更新的有效几何，即使当前B能力相同，也形成可逆的可学性下降。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】Parameter Symmetries与COST已覆盖核心近邻；剩余双teacher目标较薄，需排除普通预条件。

归档仅表示本轮不优先，允许新证据后重审。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

