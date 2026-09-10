---
title: "Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic Reinforcement Learning"
year: 2026
venue: icml-2026
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: data

failure_modes: [action-space-fragility, reward-hacking, rollout-cost]
design_knobs: [reward-shaping, prompt-action-interface, rollout-source]

rl_env: mixed
rl_interaction: online
rl_reward: dense
rl_credit: step
---

## 一句话定位

用 RL 学自适应省略 thought/observation。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `rollout-cost` | agent 生成冗余 thought，并累积过多 observations。 | omission reward 按 saved tokens 奖励效率。 | token saving 可能牺牲任务信息。 |
| `reward-hacking` | agent 可能通过省略关键信息拿效率 reward。 | task reward 为 0 时 omission reward 也置 0。[PDF §4.2] | reward 权重仍需调。 |
| `action-space-fragility` | omission 后上下文改变，agent 可能不会继续推理。 | dual sampling：full trajectory + omission partial trajectories。 | 需要 cold-start omission data。 |

## 方法机制

Agent-Omit 先合成 omission cold-start data，让 agent 学会 thought/observation omission 格式；随后用 omit-aware GRPO-style RL 训练自适应 omission policy。RL 部分包含 dual sampling、task reward + omission reward 的多目标优化，并用“task fail 则 omission reward 为 0”抑制省 token reward hacking。[PDF §4.1-4.2] 机制增量是 **把 context management 变成 agent action/reward 设计问题**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO agent RL | 不管 context cost。 | 加 omission action/reward。 | 多目标 reward tuning。 |
| ReSum / compression | 静态压缩或摘要。 | 学 turn-level omission policy。 | 需要 omission data。 |
| efficiency recipes | 只优化 inference context。 | 用 RL 联合任务成功和 token saving。 | 与 Agent Data 交叉明显。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `reward-shaping` | task reward + omission reward | task-only reward / length penalty |
| `prompt-action-interface` | omission as agent behavior | always-think / static observation compression |
| `rollout-source` | full + partial omission trajectories | full rollout only / replay |

## 方法优缺点 / 适用边界

- 优势：把 agent context efficiency 纳入 RL objective，而不是只做推理时压缩。
- 不足 / 风险：cold-start omission data 占比高，和 Agent Data 交叉；应作为 efficiency/reward-design 分支，不和 GiGPO/BEACON 直接比核心 credit。

<!-- meta:
authors: [Yansong Ning, Jun Fang, Naiqiang Tan, Hao Liu]
url: https://arxiv.org/abs/2602.04284
arxiv_id: 2602.04284
pdf: papers/2602.04284-agent-omit-adaptive-omission.pdf
brief: _meta/briefs/papers/2602.04284_agent-omit-adaptive-omission.md
survey: post-survey strict-core recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: data-centric
-->
