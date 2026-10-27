---
type: idea
node_id: idea:g15-target-tangent-plasticity
title: "目标相关切向可学性保护"
stage: archived
outcome: pending
added: 2026-10-15T14:00:14Z
based_on: ["paper:liu2026_pmopd_task_ordering", "paper:zhu2026_from_gradients_capabilities"]
target_gaps: ["gap:G15"]
tags: ["g15", "l1"]
---

# 目标相关切向可学性保护

**stage:** `archived`  ·  **outcome:** `pending`

C11 · L1 · 来源 S2；本轮未优先，归档保留，不是负实验或永久排除。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. 在常规B监督batch上，用teacher–student残差选定输出方向，构造student输出Jacobian的低秩随机sketch，估计这些方向对应的局部学习核。
2. 执行A更新时，对B目标相关学习核的显著谱塌缩加入正则；约束按残差与更新尺度归一化，允许B当前预测随A变化。
3. 交换A/B轮流维护参考；每个短训练块重新估计sketch，所有正则仅在训练使用，部署保留一个student。

【待验证假设】即使B当前表现相同，A训练也可能压缩B目标残差可被参数更新修正的方向，使后续相同B监督更难转化为能力。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】目标相关传输退化已有近邻证据；raw核谱不是Adam有效学习核，保谱不等于真实能力收益。

归档仅表示本轮不优先，允许新证据后重审。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

