---
type: idea
node_id: idea:contingent-controller-distillation
title: "蒸馏能够分支执行的短程条件控制器"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: ["paper:wang2026_tcod_exploring_temporal"]
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "shortlist-rank-2"]
---

# 蒸馏能够分支执行的短程条件控制器

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：A2；生成模型 `gpt-6-astra`；首轮推荐第2项。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. 在 student 访问的 h，请 teacher 生成最多两层的条件控制器：工具调用、对返回字段的条件判断、分支行动。
2. 采用受限 DSL 和确定性解释器；在具有有限 outcome schema 的环境中核验分支是否合法。
3. student 学习生成控制器，并自主执行到控制器结束；后续 teacher 监督继续发生在 student 实际到达的状态。

更新规则：L = −log πθ(AST(CT)|h)，监督对象是规范化的控制器 AST。部署时 student 生成控制器，解释器根据实际工具返回执行分支。

待验证假设：单条 continuation 只展示实际发生的一条路径；条件控制器同时传递面对工具失败、空结果或冲突返回时的响应策略。

查新结论（早期文献核查，不是效果验证）：P。[Skill-DisCo](https://arxiv.org/html/2606.26669)已有可执行条件控制流，但从成功trace离线编译外部技能；这里将**student状态上的teacher条件控制器训练进student生成策略**。

最小验证：选择有 success/empty/error 等有限返回类型的文本 API 环境；比较单轨迹 CE、所有分支展开 CE、控制器蒸馏。严格匹配 teacher 输出量和部署总推理预算，测试训练未见的返回分支组合。

同数据、同总成本的关键对照：同一控制器全部分支展开后的action CE，与AST CE比较；部署计算量相同。

## Key risks
DSL 限制了开放任务表达；teacher 生成的条件可能遗漏关键情况，分支核验成本也可能迅速增长。

评审补充：DSL解释器可能贡献主要能力；未发生分支的teacher标签未必正确。

证伪条件：展开全部分支后的普通 CE 达到同等表现；或者收益完全来自解释器提供的手写策略。

资源条件：Black-box teacher；工具 schema；受限 DSL 解释器；可控制并验证分支的文本环境。控制器只能读取部署可见的工具返回。

估算：条件估算：DSL 和环境适配约 2–3 人周；每状态一个 teacher 控制器，深度 2、最多 4 条验证路径，环境调用需完整计入。 本轮没有GPU计时与效果数据。

## Connections
已有wiki背景：[wang2026_tcod_exploring_temporal](../papers/wang2026_tcod_exploring_temporal.md)。

最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

