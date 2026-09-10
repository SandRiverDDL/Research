---
title: "Turn-PPO: Turn-Level MDP for Agentic RL"
authors: [Unknown, et al.]
year: 2025
venue: survey-derived
url: null
arxiv_id: null

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: frontier-candidate
data_overlap: false

rl_axes:
  environment: web
  interaction_mode: online
  reward_signal: sparse
  optimizer: policy-gradient
  credit_assignment: step
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

把 agent 交互重写成 turn-level MDP 来做 PPO。

## Selection Basis

Credit Assignment survey Table 10 列为 Agentic RL core CA method；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Table 10]**: Turn-PPO 标注为 Turn granularity、Turn-level MDP methodology、WebShop benchmark。

**解释 [本项目判断]**: 这是把长 token trajectory 提升到 turn/state/action 层面的建模路线，可和 ArCHer、Agent Lightning 对比。

## Evidence

- source anchors: Credit Assignment survey Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
