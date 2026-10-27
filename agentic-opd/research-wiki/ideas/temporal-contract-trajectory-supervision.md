---
type: idea
node_id: idea:temporal-contract-trajectory-supervision
title: "用跨轮时序契约监督轨迹"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: ["paper:chen2026_look_ahead_before"]
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 用跨轮时序契约监督轨迹

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：S3；生成模型 `gpt-6.1-sol`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. teacher 在 student 当前状态输出少量可执行时序条件，例如先取得证据再引用、写入后验证、满足某前提后才能提交。
2. 从该状态采样 student 的短期真实轨迹，依据工具日志自动判定每条轨迹是否满足契约。
3. 用满足与违反契约的轨迹对更新 student；保留普通 OPD 作为基础监督。

更新规则：L=L_OPD+λΣ_{(y+,y-)}log(1+exp[-β(ℓ_S(y+|h)-ℓ_S(y-|h))])，其中 ℓ_S 只计算 action likelihood，y+ 与 y- 分别满足、违反 teacher 契约。没有可比较轨迹对时不产生该辅助项。

待验证假设：逐 turn KL 无法直接表达两个动作之间的必要依赖；关系监督允许多条不同操作路径满足同一个跨轮正确性条件。

查新结论（早期文献核查，不是效果验证）：C。新发现[ContrAgent](https://arxiv.org/html/2609.18128)已有工具trace、可检查时序契约、DFA监督。其主要是在线gate/离线评估；剩余为**teacher条件契约产生偏好对并训练teacher-free策略**，尚未被精确覆盖。

最小验证：在两个已有文本 agent 环境中选取自然存在的验证、引用与前置条件任务；比较 OPD、teacher continuation CE、契约偏好目标。匹配 rollout tokens，分别报告 success 与契约违规率。

同数据、同总成本的关键对照：同轨迹、同契约标签：普通成功偏好、契约偏好、continuation CE；评测时移除契约。

## Key risks
teacher 将个人操作偏好误写成必要条件，会压制正确的替代路径；正负轨迹对也可能稀缺。

评审补充：teacher偏好被误当必要条件；满足契约未必完成任务；偏好对稀缺。

证伪条件：违规率下降但 success 不变或恶化；或收益可由等量 teacher continuation 完全解释。

资源条件：独立 teacher 的结构化文本输出；短期环境分叉；可解析工具日志。契约只能依赖 student 可见信息。

估算：先做约 10^3 个状态、每状态 2–4 条短分支。契约 parser 与日志接口预计两周左右；新增环境成本与短分支数线性相关。 本轮没有GPU计时与效果数据。

## Connections
已有wiki背景：[chen2026_look_ahead_before](../papers/chen2026_look_ahead_before.md)。

最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

