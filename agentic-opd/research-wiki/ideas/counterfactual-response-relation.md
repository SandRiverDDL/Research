---
type: idea
node_id: idea:counterfactual-response-relation
title: "蒸馏工具反馈改变时的决策响应关系"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: ["paper:agarwal2023_onpolicy_distillation_language"]
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 蒸馏工具反馈改变时的决策响应关系

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：A4；生成模型 `gpt-6-astra`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. 以 student 实际访问的 h 为锚点，通过环境合法分叉得到只改变一个工具反馈因素的 h′。
2. 对两个完整候选行动 a、b，查询独立 teacher 在 h 与 h′ 下的相对偏好。
3. 在普通 OPD 上加入成对响应关系监督，要求 student 对反馈变化产生相同方向和幅度的决策变化。

更新规则：定义 ℓM(h)=log πM(a|h)−log πM(b|h)。L = LOPD + λ[(ℓθ(h′)−ℓθ(h))−(ℓT(h′)−ℓT(h))]²。保留 OPD anchor，因为响应差本身不能确定绝对行动偏好。

待验证假设：工具 agent 必须理解反馈如何改变决策，例如请求失败后重试还是换策略；显式传递这种响应关系有助于避免忽略工具返回或错误坚持原计划。

查新结论（早期文献核查，不是效果验证）：P。[CROP](https://arxiv.org/abs/2608.13387)用counterfactual sensitivity选择token；关系蒸馏已有先例。这里直接转移**合法工具反馈干预引起的teacher行动log-odds变化**。

最小验证：在可控 success/failure、empty/nonempty、版本冲突环境上构造合法分叉；比较普通 OPD、两状态独立 OPD、成对关系目标，完全共享查询与训练数据。

同数据、同总成本的关键对照：同一 \(h,h′\)、候选及teacher logprob，比较独立KL与差分关系项。

## Key risks
关系目标没有增加标签信息，可能只是低效重复逐状态 KL；长行动 log-odds 的尺度也可能不稳定。

评审补充：两状态KL已包含关系标签；关系项可能只是重新加权，长行动尺度不稳。

证伪条件：两状态独立 KL 达到相同表现；或者收益仅存在于人为不一致的 observation 扰动。

资源条件：Teacher 与 student 对完整候选行动的 logprob；环境合法干预和分叉能力。不得直接伪造与历史矛盾的工具输出。

估算：条件估算：环境可分叉时约 1–2 人周；每锚点至少两个 teacher scoring context 和两条对应分叉，训练成本约随成对状态数增长。 本轮没有GPU计时与效果数据。

## Connections
已有wiki背景：[agarwal2023_onpolicy_distillation_language](../papers/agarwal2023_onpolicy_distillation_language.md)。

最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

