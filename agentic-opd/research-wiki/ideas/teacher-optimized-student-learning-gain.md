---
type: idea
node_id: idea:teacher-optimized-student-learning-gain
title: "让 teacher 为 student 学会多少而优化"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: []
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 让 teacher 为 student 学会多少而优化

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：S6；生成模型 `gpt-6.1-sol`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. 在 student-visited states，teacher 采样两份候选监督 continuation。
2. 从相同 student checkpoint 各做一次等量蒸馏更新，在未参与更新的相关任务上测无 teacher 的表现变化。
3. 用学习增益偏好训练 teacher，再让该 teacher 继续提供常规 on-policy 蒸馏目标。

更新规则：对监督 d 定义 U(d)=R_probe(Update(S,d))-R_probe(S)。teacher 用 DPO 或采样策略梯度偏向较大 U 的监督；student 始终以独立 teacher 的 continuation CE/KL 更新。核心是将 teacher 目标改为 learner improvement。

待验证假设：teacher 自己最容易成功的路径未必最容易被小 student 学会；直接优化更新后的独立表现可选择更有教学价值的监督。

查新结论（早期文献核查，不是效果验证）：C。[MetaDistil](https://aclanthology.org/2022.acl-long.485/)已直接以蒸馏后student反馈训练teacher；[SCOUT](https://arxiv.org/html/2609.38360#S3.SS2)/[Prep-OPD](https://arxiv.org/html/2610.04950#S3.SS3)已适配teacher。剩余是agent自主泛化收益及离散continuation优化；不能claim首次“teacher为学习收益优化”。

最小验证：先在小 student 上比较固定 teacher、teacher 自身 reward 适配、student learning-gain 适配；每个 outer round 保持相同两份监督、student update 数与 probe budget。

同数据、同总成本的关键对照：同候选、影子更新、probe：固定teacher、teacher自身reward适配、learning-gain适配；外测任务完全隔离。

## Key risks
outer-loop reward 方差高、成本大，teacher 可能只适配一个 student checkpoint。

评审补充：高方差outer reward；teacher可适配probe或单一student checkpoint。

证伪条件：学习增益标签无法复现，或计入临时更新与 probe 成本后不优于固定 teacher。

资源条件：可训练独立 teacher；student checkpoint 临时复制或 LoRA；可验证 task reward；严格分开的 update、probe 与最终 test tasks。

估算：先做几十个 outer rounds，每 round 两次短 student 更新与固定小 probe set。预计三至四周实现；新增成本主要是临时 student 更新与评测，不给出未经测量的 GPU 小时。 本轮没有GPU计时与效果数据。

## Connections
最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

