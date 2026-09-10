---
title: "IGPO: Information Gain Policy Optimization"
authors: [Hanlin Wang, et al.]
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
  reward_signal: sparse
  optimizer: grpo-like
  credit_assignment: step
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

用 information gain 做 turn-level credit，适合需要探索的 agent 状态。

## Selection Basis

Credit Assignment survey Table 10 / Section 5.5 列为 Agentic RL core CA method；当前为 survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey §5.5]**: IGPO 将每个 turn 的 credit 定义为该 turn 对成功概率带来的 information gain。

**事实 [Credit Survey §5.5]**: survey 指出 IGPO 的限制是需要可靠的 per-turn success probability estimator。

**解释 [本项目判断]**: IGPO 是 credit assignment 与 exploration 交界的方法：高不确定/高信息增益状态更值得探索和更新。

## Evidence

- source anchors: Credit Assignment survey §5.5, Table 5, Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
