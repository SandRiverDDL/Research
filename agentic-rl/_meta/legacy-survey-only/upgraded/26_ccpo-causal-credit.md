---
title: "CCPO: Causal Counterfactual Policy Optimization"
authors: [Unknown, et al.]
year: 2026
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

用 causal/counterfactual turn analysis 做 agent credit。

## Selection Basis

Credit Assignment survey Figure 3 / Table 10 列为 Agentic/Multi-agent core CA method；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey §2.5]**: survey 将 CCPO 与 C3 并列为 counterfactual credit 方法。

**事实 [Credit Survey Table 10]**: CCPO 标注为 Turn granularity、Counterfactual methodology、Agentic tasks。

**解释 [本项目判断]**: CCPO 和 C3/HCAPO 共同构成 post-hoc retrospective credit wave。

## Evidence

- source anchors: Credit Assignment survey §2.5, Figure 3, Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
