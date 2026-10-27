---
type: idea
node_id: idea:g15-learning-response-transport
title: "跨teacher学习方向输运"
stage: proposed
outcome: pending
added: 2026-10-15T14:00:13Z
based_on: ["paper:liu2026_pmopd_task_ordering", "paper:zhu2026_from_gradients_capabilities"]
target_gaps: ["gap:G15"]
tags: ["g15", "l1"]
---

# 跨teacher学习方向输运

**stage:** `proposed`  ·  **outcome:** `pending`

C03 · L1 · 来源 A3；本轮推荐，待验证。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. 在B能够有效学习的checkpoint，保存少量成功B更新方向及其在固定B锚点上的logit变化，作为B的低秩学习响应基；A对称保存。
2. 经历A训练后，用当前student的JVP与小型正则最小二乘，重新寻找能产生相同响应的参数方向，将旧学习方向输运到当前参数位置。
3. 用输运后的方向构造B梯度的低秩预条件器，基外仍做常规更新；按固定间隔刷新，同一student持续吸收两个teacher。

【待验证假设】A可能扭曲B原本有效的学习方向，使相同B监督难以转化成有效功能变化；这种下降可以通过方向输运部分逆转。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】旧成功功能响应可能过时；必须在重建成功后仍改善真实B学习，并胜过当前方向重算和一般预条件。

主推荐/条件推荐不是通过实验。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

