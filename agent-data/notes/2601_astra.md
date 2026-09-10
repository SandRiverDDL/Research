---
title: "ASTRA: Automated Synthesis of agentic Trajectories and Reinforcement Arenas"
year: 2026
venue: arxiv
paper_type: synthetic-verifiable-data
lifecycle_role: frontier-candidate
boundary_risk: rl

failure_modes: [coverage-gap, invalid-environment-state, tool-call-cascade]
data_knobs: [tool-call-grammar, environment-synthesis, verifier-design, trajectory-to-sft]

agent_domain: tool
data_object: tool-call
data_source: synthetic
selection_signal: verifier
adaptivity: static
failure_use: discard
training_consumer: pre-rl
---

## 一句话

工具轨迹和可验证环境双合成。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `coverage-gap` | 多工具 agent 数据难覆盖真实工具组合。 | MCP tool docs 归一化后按 tool-call graph 合成轨迹。 | 图拓扑不保证真实用户任务分布。 |
| `invalid-environment-state` | 只合成 tool traces 难接 RL，因为 reward 不可验证。 | QA-derived code-executable rule-verifiable environments。 | verifier 可能偏规则题，弱化开放式任务。 |

## 核心做法

ASTRA 是 tool-agent 的数据管线：先把 MCP / API / public dataset 中的工具文档归一成 OpenAI-style tool calling schema，再按同一 MCP server 内的工具转移图合成多步 tool-chain 和任务。[Brief] 论文报告过滤后保留 1,585 MCP servers、19,036 tool docs、41 domains，并用 dependency / task-chain coherence 做基础验证。[Brief] 第二部分把分解 QA traces 变成 code-executable、rule-verifiable environments，使 SFT 后可以接确定性多轮 RL。[arXiv HTML §2]

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `tool-call-grammar` | 从工具 schema 和 transition graph 生成链式调用。 | 人工写 tool demos。 |
| `environment-synthesis` | 生成 rule-verifiable executable environments。 | 只用静态对话 / prompt。 |
| `verifier-design` | dependency 和 task-chain coherence 过滤。 | final answer judge。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| 普通 tool-call SFT | 工具覆盖窄，无法自然接 RL。 | tool graph trajectory + executable arena。 | 合成任务可能学到 schema artifact。 |

## 谱系位置

- 上游：Toolformer / MCP-style tool calling / tool-use SFT。
- 同期：Agent Data Protocol、PC Agent-E、ProCUA-SFT。
- 下游：verifiable agent SFT -> RLVR warm start。

## 和 Agentic RL 的关系

- agentic_rl_overlap: true
- 本项目只写 SFT trajectories 和 environment synthesis；online RL 是消费者。
- 需要在 `agentic-rl` 侧登记 RL arena / trajectory-level reward 视角。

## 优缺点

- 优势：对你做 tool/skill selection 数据很有用，因为它把工具拓扑显式化。
- 不足 / 风险：规则可验证环境适合 closed-form task，不一定覆盖文档、数据分析和 artifact 质量。

<!-- meta:
authors: [Xiaoyu Tian, et al.]
url: https://arxiv.org/abs/2601.21558
arxiv_id: 2601.21558
pdf:
brief: _meta/briefs/papers/2601.21558_astra.md
survey: user known-item
agentic_rl_overlap: true
agentic_rl_queue: pending
-->
