---
title: "PilotRL: Progressive Credit for Agentic Planning"
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
  environment: mixed
  interaction_mode: online
  reward_signal: sparse
  optimizer: grpo-like
  credit_assignment: step
  data_reuse: curriculum
  sft_warm_start: unclear
---

## 一句话

Progressive credit / planning 型 agentic CA 方法。

## Selection Basis

Credit Assignment survey Table 10 列为 Agentic RL core CA method；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Table 10]**: PilotRL 标注为 Step granularity、Progressive methodology、Agentic planning benchmark。

**解释 [本项目判断]**: PilotRL 可能和 curriculum / planning decomposition 相关，后续应核查它是否属于 core RL method 还是 environment recipe。

## Evidence

- source anchors: Credit Assignment survey Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
