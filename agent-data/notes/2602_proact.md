---
title: "ProAct: Agentic Lookahead in Interactive Environments"
year: 2026
venue: arxiv
paper_type: search-to-sft-distillation
lifecycle_role: frontier-candidate
boundary_risk: rl

failure_modes: [long-horizon-drift, metacognitive-switch-gap, static-data-ceiling]
data_knobs: [search-to-sft-distillation, process-supervision, environment-interface, student-feedback-loop]

agent_domain: game
data_object: trajectory
data_source: environment-generated
selection_signal: reward
adaptivity: environment-feedback
failure_use: replay
training_consumer: pre-rl
---

## 一句话

把环境搜索压缩成 lookahead SFT。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `long-horizon-drift` | LLM 内部模拟未来状态会累积错误。 | GLAD 用环境搜索轨迹蒸馏 grounded lookahead。 | 游戏环境比真实工具链更干净。 |
| `metacognitive-switch-gap` | 模型不知道何时从当前动作转向更优未来路径。 | 搜索树压缩为 causal reasoning chains。 | 还不是专门的失败-切换数据 recipe。 |

## 核心做法

ProAct 有两块：GLAD 和 MC-Critic。本项目只把 GLAD 当 data seed：它从 environment-based search 得到轨迹，再把复杂 search tree 压缩成简洁的 causal reasoning chain，用 SFT 让 agent 内化前瞻逻辑。[arXiv Abstract] MC-Critic 是用轻量环境 rollout 校准 value estimate，服务 PPO / GRPO 等策略优化，属于 RL-overlap。[Brief] 论文在 2048 / Sokoban 等交互环境上验证，报告 4B 模型超过开源 baseline 并接近闭源系统。[arXiv HTML §1]

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `search-to-sft-distillation` | MCTS / environment search -> causal reasoning SFT。 | inference-time search 或普通 expert imitation。 |
| `process-supervision` | 监督未来趋势估计和动作因果。 | 只监督最终动作。 |
| `environment-interface` | 2048 / Sokoban 提供客观状态转移和 reward。 | LLM 自我模拟未来状态。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| ReAct / CoT | 长程未来状态靠模型想象，误差累积。 | 用环境搜索生成可监督 lookahead。 | 需要可 rollout 环境。 |

## 谱系位置

- 上游：MCTS / RAP / Tree-of-Thought / VAGEN。
- 同期：daVinci-Agency、ASTRA。
- 下游：failed-loop-switch 和 planning data synthesis。

## 和 Agentic RL 的关系

- agentic_rl_overlap: true
- GLAD 是 data pipeline；MC-Critic 是 RL algorithm / value estimator。
- 需要登记到 `agentic-rl` queue，避免把 MC-Critic 误读成 agent-data core。

## 优缺点

- 优势：给“失败后换思路”提供比纯 reflection 更强的监督来源：外部环境搜索。
- 不足 / 风险：从游戏转到 SWE / docs / data-analysis，要先解决环境可执行和 reward 稀疏问题。

<!-- meta:
authors: [Yangbin Yu, et al.]
url: https://arxiv.org/abs/2602.05327
arxiv_id: 2602.05327
pdf:
brief: _meta/briefs/papers/2602.05327_proact.md
survey: user known-item
agentic_rl_overlap: true
agentic_rl_queue: pending
-->
