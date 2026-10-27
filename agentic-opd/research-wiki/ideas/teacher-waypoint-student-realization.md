---
type: idea
node_id: idea:teacher-waypoint-student-realization
title: "teacher 给出可见里程碑，student 自己实现到达路径"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: ["paper:chen2026_look_ahead_before", "paper:wang2026_tcod_exploring_temporal"]
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# teacher 给出可见里程碑，student 自己实现到达路径

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：A7；生成模型 `gpt-6-astra`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. 在 student 访问的 h，teacher 于副本短程推进，提取一个任务可见、可验证的 waypoint gT，例如获得指定证据或完成某项文件修改。
2. 保持真实训练轨迹从原 h 出发，让 student 自己实现 gT；teacher 只在这些真实 student 状态上提供 goal-conditioned 行动监督。
3. 同时训练 student 从 h 预测 waypoint，部署时由 student 预测并执行，不需要 teacher 在线给目标。

更新规则：L = −log πθ(gT|h) + Σt KL[πT(·|ht,gT) || πθ(·|ht,gT)]，其中 ht 来自 student 对 waypoint 的实际尝试；black-box teacher 时可改为 teacher action CE。

待验证假设：长程任务中可迁移的是阶段性状态推进，而 teacher 的具体路径未必适合 student；保留 waypoint、让 student 生成实现路径可能缩小这种落差。

查新结论（早期文献核查，不是效果验证）：C。[Sub-goal Distillation](https://proceedings.mlr.press/v274/hashemzadeh25a.html)已覆盖teacher subgoal→planner/executor→无teacher部署。剩余只在**student实际实现路径上的在线goal-conditioned监督**，须证明贡献超过数据分布改变。

最小验证：选择存在多条实现路径的检索加编辑任务；比较普通 OPD、teacher bridge 交接、waypoint 加 student realization。分别报告 oracle waypoint 与预测 waypoint，匹配全部 teacher 和环境预算。

同数据、同总成本的关键对照：相同waypoint/行动标签，oracle-path训练与student-path训练；oracle/预测waypoint分别报告。

## Key risks
teacher 选出的 waypoint 可能超出 student 能力；目标预测与目标执行的误差会相互放大。

评审补充：waypoint可达性、预测与执行误差相乘；不能把层级结构本身claim新颖。

证伪条件：只有部署时提供 oracle waypoint 才有效；或者相同长度 teacher continuation CE 已达到同等结果。

资源条件：Teacher rollout 分叉；文本或工具可见的 waypoint 表示和完成检测；student 在线访问状态的 teacher 标注。不得把部署不可见的隐藏 state 当 waypoint。

估算：条件估算：约 2–3 人周；每 waypoint 增加 H 次 teacher 工具推进，以及 student 实现路径上的标注。需同时计算失败尝试成本。 本轮没有GPU计时与效果数据。

## Connections
已有wiki背景：[chen2026_look_ahead_before](../papers/chen2026_look_ahead_before.md)；[wang2026_tcod_exploring_temporal](../papers/wang2026_tcod_exploring_temporal.md)。

最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

