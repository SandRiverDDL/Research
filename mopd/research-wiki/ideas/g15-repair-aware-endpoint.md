---
type: idea
node_id: idea:g15-repair-aware-endpoint
title: "对恢复算子求导的终点保护"
stage: proposed
outcome: pending
added: 2026-10-15T14:00:13Z
based_on: ["paper:zhu2026_upmopd_update_projection", "paper:liu2026_pmopd_task_ordering"]
target_gaps: ["gap:G15"]
tags: ["g15", "l5"]
---

# 对恢复算子求导的终点保护

**stage:** `proposed`  ·  **outcome:** `pending`

C07 · L5 · 来源 A7, S7；本轮推荐，待验证。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. 保存宏步起点与独立A检验集，定义一至两步A更新组成的恢复映射R_A，固定虚拟计算中的预条件器。
2. 将B位移d的目标写成恢复后B损失L_B(R_A(θ+d))，对恢复过程求导，并约束恢复后A损失不超过起点。
3. 执行B位移后刷新student轨迹，再执行A恢复；检验宏步终点，失败则回退并缩短位移。中间状态允许A暂时下降。

【待验证假设】存在可恢复的A下降路径；将恢复后的结果纳入B方向选择，可以到达逐步保护排除的能力组合。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】须胜过同修复次数、核验预算及完整成本的普通B→A修复；短展开和真实fresh rollout的动力学可能不符。

主推荐/条件推荐不是通过实验。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

