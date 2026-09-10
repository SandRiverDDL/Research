---
title: "POAD: Action Decomposition for Agentic Credit Assignment"
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
  optimizer: policy-gradient
  credit_assignment: tool-call
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

把 agent action 分解后做更细粒度 credit。

## Selection Basis

Credit Assignment survey Figure 3 / Table 10 将 POAD 标为 Agentic RL core CA method；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Figure 3]**: POAD 位于 agentic credit assignment 的 action decomposition 类别。

**事实 [Credit Survey Table 10]**: POAD 标注为 Token/Turn granularity、Action Decomposition methodology、interactive tasks。

**解释 [本项目判断]**: POAD 适合放在 tool-call / action-grammar credit 轴，后续需核查它如何定义可分解 action。

## Evidence

- source anchors: Credit Assignment survey Figure 3, Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
