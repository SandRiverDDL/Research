---
type: idea
node_id: idea:teacher-selected-environment-counterexample
title: "让 teacher 用真实反例训练 student 应变"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: ["paper:chen2026_look_ahead_before"]
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 让 teacher 用真实反例训练 student 应变

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：S7；生成模型 `gpt-6.1-sol`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. student 在其访问状态提交下一步 action 及短期后续意图。
2. teacher 从环境允许的少量反馈分支中选择一个会暴露该意图缺陷的真实反例，例如合法空结果或暂时失败。
3. student 在该分支继续执行；teacher 对这些 student 实际访问的新状态提供正确 action 标签。

更新规则：teacher 选择 c*=argmax_{c∈C_legal} violation(a_student,c)，student 最小化真实反例分支上的 L=Σ_t -log p_S(a_T,t|h_S,t)。teacher 改变交互问题，独立 teacher action 仍是训练监督；不把 teacher 变成部署执行者。

待验证假设：随机工具失败训练浪费大量无关分支；针对 student 当前意图构造合法反例，可集中教会何时放弃、重试或重新验证。

查新结论（早期文献核查，不是效果验证）：P。[PAIRED](https://arxiv.org/abs/2012.02096)已有对抗环境设计，[BranchOPD](https://arxiv.org/abs/2610.13481)已有student分叉；这里是**独立teacher依据当前意图选择合法反馈反例，并监督新student状态**。未见精确覆盖。

最小验证：在具有原生异常分支的两个文本环境中，比较普通 OPD、随机分支 OPD、teacher-selected 分支 OPD；保持分支集合与调用数一致，同时评测正常和自然异常任务。

同数据、同总成本的关键对照：同一合法分支池、调用数及teacher标签：随机选择与teacher选择；外测自然异常和正常任务。

## Key risks
teacher 可能偏爱不现实的罕见异常，牺牲正常任务性能。

评审补充：`violation`评分尚未具体化；可能集中训练不自然异常，牺牲正常任务。

证伪条件：只适用于 teacher 选择的训练扰动，不能改善自然异常；或随机分支效果相同。

资源条件：独立 teacher；合法环境分支选择接口；snapshot/reset；分支后 teacher action 标注。环境不可支持的假反馈不纳入训练。

估算：先做约 10^3 个状态、每状态最多 2–3 个合法短分支；约两周接口工作。新增 teacher 判断与环境分叉成本必须分别统计。 本轮没有GPU计时与效果数据。

## Connections
已有wiki背景：[chen2026_look_ahead_before](../papers/chen2026_look_ahead_before.md)。

最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

