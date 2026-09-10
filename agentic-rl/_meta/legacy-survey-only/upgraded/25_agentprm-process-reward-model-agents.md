---
title: "AgentPRM: Process Reward Model for LLM Agents"
authors: [Zhen Xi, et al.]
year: 2025
venue: survey-derived
url: null
arxiv_id: null

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: frontier-candidate
data_overlap: false

rl_axes:
  environment: mixed
  interaction_mode: online
  reward_signal: process
  optimizer: actor-critic
  credit_assignment: step
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

把 PRM 思路迁移到 agent，学习 step/turn-level value。

## Selection Basis

Credit Assignment survey Table 10 / §5.1 列为 Agentic RL core CA method；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey §5.1]**: AgentPRM 直接将 TD+GAE 风格的 turn-level value learning 用于 agents。

**事实 [Credit Survey Table 7]**: survey 报告 AgentPRM 在 WebShop / TextCraft 上相对 ORM baseline 有明显提升。

**解释 [本项目判断]**: AgentPRM 是 process reward / value learning 路线的核心卡，适合和 ArCHer、SWEET-RL 对比。

## Evidence

- source anchors: Credit Assignment survey §5.1, Table 7, Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
