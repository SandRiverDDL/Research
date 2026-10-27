---
type: idea
node_id: idea:g15-cross-learning-metric
title: "交叉学习收益的共享塑性度量"
stage: archived
outcome: pending
added: 2026-10-15T14:00:14Z
based_on: ["paper:li2026_beyond_teacher_assignment", "paper:zhu2026_from_gradients_capabilities"]
target_gaps: ["gap:G15"]
tags: ["g15", "l1"]
---

# 交叉学习收益的共享塑性度量

**stage:** `archived`  ·  **outcome:** `pending`

C10 · L1 · 来源 S1；本轮未优先，归档保留，不是负实验或永久排除。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. 在共享LoRA坐标中学习低秩正定更新度量P；所有teacher共用P，将变换后更新重新归一到原更新范数，保持监督预算与步长尺度。
2. 周期性使用同一组固定student prefixes建立短虚拟分支：B连续学习、A后接相同步数B，并交换A/B；记录held-out B的有限步收益。
3. 按B起点loss分桶校正剩余学习空间，用交叉学习收益差反向更新P；常规训练继续执行teacher监督，结束后合并LoRA。

【待验证假设】A可能改变B所需方向的条件数，而当前梯度夹角与信号尺度不足以描述这种变化；共享塑性度量能够改善这一条件。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】GAP、La-MAML已有元预条件；配对交叉收益目标需证明超过一般学习加速。

归档仅表示本轮不优先，允许新证据后重审。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

