---
title: "SORL: Bias-Corrected Credit for Multi-Turn Search"
authors: [Unknown, et al.]
year: 2025
venue: survey-derived
url: null
arxiv_id: null

lane: tool-rl
paper_type: core-rl-method
lifecycle_role: frontier-candidate
data_overlap: false

rl_axes:
  environment: tool
  interaction_mode: online
  reward_signal: outcome
  optimizer: grpo-like
  credit_assignment: step
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

面向 multi-turn search 的 bias-corrected turn credit。

## Selection Basis

Credit Assignment survey Table 10 列为 Agentic RL core CA method；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Table 10]**: SORL 标注为 Turn granularity、Bias-corrected methodology、Multi-turn search benchmark。

**解释 [本项目判断]**: SORL 应作为 search lane 内的 core credit method，而不是普通 search recipe；后续需要核验 bias correction 具体形式。

## Evidence

- source anchors: Credit Assignment survey Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
