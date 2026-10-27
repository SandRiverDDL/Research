---
type: idea
node_id: idea:counterfactual-observation-action-contrast
title: "蒸馏工具反馈改变行动的条件差异"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: ["paper:chen2026_look_ahead_before"]
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 蒸馏工具反馈改变行动的条件差异

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：S4；生成模型 `gpt-6.1-sol`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. 在 student 发起工具调用的状态，取得两种可实际产生的返回，例如成功与可恢复失败。
2. teacher 为两种 observation 分别指定下一行动 a1、a2，并明确反馈变化是否应引起行动切换。
3. student 学习同一前缀下 observation 与 action 的匹配关系。

更新规则：对于应切换的反馈对，L_pair=-logσ(ℓ_S(a1|h,o1)-ℓ_S(a2|h,o1))-logσ(ℓ_S(a2|h,o2)-ℓ_S(a1|h,o2))，与普通 OPD 相加。监督对象是反馈引起的行动差异，不是某条完整 teacher 路径。

待验证假设：agent 容易延续已计划的操作而忽略新工具反馈。成对条件差异监督可迫使 student 使用 observation 中真正改变决策的信息。

查新结论（早期文献核查，不是效果验证）：C。与A4属**暂定同家族**；[CROP](https://arxiv.org/abs/2608.13387)非直接覆盖。但现公式可分解为**两个独立状态的pairwise分类loss**，没有显式跨状态关系约束，关系claim偏薄。

最小验证：使用允许真实成功/失败分支的两个工具环境；比较独立 CE、成对反馈对比、普通 OPD。匹配 teacher 标注与分支数，测成功率和反馈被忽略的比例。

同数据、同总成本的关键对照：同反馈对与行动标签，直接比较独立CE、逐状态pairwise与所提目标，测完整生成。

## Key risks
工具分支缺少现实可比性；有限候选 action 可能让 student 学会局部辨别而不改善完整执行。

评审补充：可能仅训练局部二选一；提高判别不保证生成正确action。

证伪条件：成对目标不优于相同样本的独立 CE，或仅适用于训练时的返回字符串。

资源条件：独立 text teacher；student action likelihood；可控制合法工具返回分支的 resettable 环境。不得伪造不可能的世界状态。

估算：先做 10^3 个反馈对，每对两次短环境执行与两份 teacher action 标签；预计一至两周实现，训练成本接近等量 pairwise action supervision。 本轮没有GPU计时与效果数据。

## Connections
已有wiki背景：[chen2026_look_ahead_before](../papers/chen2026_look_ahead_before.md)。

最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

