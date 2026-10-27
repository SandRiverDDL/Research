---
type: idea
node_id: idea:effect-quotient-distillation
title: "按环境效果蒸馏行动等价类"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: ["paper:agarwal2023_onpolicy_distillation_language", "paper:liu2026_memopd_onpolicy_distillation", "paper:wang2026_cast_game_solvers"]
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 按环境效果蒸馏行动等价类

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：S1；生成模型 `gpt-6.1-sol`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. 在 student 自采样到达的状态 h，分别采样 teacher 和 student 的候选 tool actions，组成有限集合 A。
2. 在可恢复环境中执行候选，按相同工具返回与相同状态变化分成效果等价类 E；状态校验信息只用于训练标签。
3. teacher 样本频率给出类分布 q_T(E)，student 将类内所有 action 的概率相加，匹配类分布。

更新规则：令 p_S^A(a|h)=exp(log p_S(a|h))/Σ_{b∈A}exp(log p_S(b|h))，最小化 L=-Σ_E q_T(E)logΣ_{a∈E}p_S^A(a|h)。监督对象是执行效果的概率质量，而非某条命令的逐 token 概率。

待验证假设：工具调用存在大量实现相同效果的命令、参数表达与操作顺序。效果等价类允许保留 student 已会的表达，减少模仿 teacher 表面格式造成的有效行动损失。

查新结论（早期文献核查，不是效果验证）：P。与A1属**暂定同家族**，不是删除或合并结论；[semantic STOP](https://arxiv.org/abs/2609.20511)不覆盖执行验证的环境等价类。

最小验证：选择两个可恢复文本工具环境；比较 ordinary OPD、相同候选集但逐 action 蒸馏、效果类蒸馏。固定 rollout、teacher samples 和环境调用预算，报告 held-out success、有效替代动作保留率及全部成本。

同数据、同总成本的关键对照：同候选逐行动目标；除成功率，必须测候选集合的未归一化概率质量。

## Key risks
即时效果相同未必意味着后续语义相同；候选归一化也可能带来长度偏差。

评审补充：**候选内归一化对候选集合总概率质量不敏感**，训练可能只改变候选间排序而不提高自主生成。

证伪条件：等价类充分存在且标签可靠时，匹配成本后仍不优于逐 action 蒸馏；或增益全部来自候选数量。

资源条件：独立 teacher 的文本采样即可；student action likelihood；环境 snapshot/reset/branch；可审计的工具效果签名。隐藏状态若用于分组，不进入部署 student 输入。

估算：规划假设为 0.6B–1.7B student、4B–8B teacher。先做 10^3 个状态、每状态 4–8 个候选的 pilot；主要新增成本是约 4–8 次环境分叉。接口实现预计约两周，未测量训练时长。 本轮没有GPU计时与效果数据。

## Connections
已有wiki背景：[agarwal2023_onpolicy_distillation_language](../papers/agarwal2023_onpolicy_distillation_language.md)；[liu2026_memopd_onpolicy_distillation](../papers/liu2026_memopd_onpolicy_distillation.md)；[wang2026_cast_game_solvers](../papers/wang2026_cast_game_solvers.md)。

最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

