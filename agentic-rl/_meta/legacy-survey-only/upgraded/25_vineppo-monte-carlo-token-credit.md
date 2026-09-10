---
title: "VinePPO: Monte Carlo Token-Level Credit Assignment"
authors: [Amirhossein Kazemnejad, et al.]
year: 2025
venue: ICML 2025
url: null
arxiv_id: null

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: canonical-anchor
data_overlap: false

rl_axes:
  environment: simulated
  interaction_mode: offline-rollout
  reward_signal: verifier
  optimizer: policy-gradient
  credit_assignment: token
  data_reuse: none
  sft_warm_start: standard
---

## 一句话

Reasoning RL 的 MC token-credit anchor，给 agentic CA 提供上游基线。

## Selection Basis

Credit Assignment survey §3.1 / Table 10；Landscape references。survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey §3.1]**: VinePPO 用 Monte Carlo continuation 替代 learned value network，在 token position fork 多个 continuation 来估计 token-level value。

**事实 [Credit Survey Table 10]**: VinePPO 标注为 Reasoning RL core CA、Token granularity、MC methodology、ICML 2025。

**解释 [本项目判断]**: 虽偏 reasoning RL，但它是 fine-grained credit 的 foundational anchor；agentic 场景直接套用会受环境重执行成本限制。

## Evidence

- source anchors: Credit Assignment survey §3.1, Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
