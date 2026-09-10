---
title: "TARL: LLM-Judge Credit for Agentic Tasks"
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
  reward_signal: verifier
  optimizer: grpo-like
  credit_assignment: step
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

用 LLM judge 为 agent turns 提供 credit。

## Selection Basis

Credit Assignment survey Table 10 列为 Agentic RL core CA method；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Table 10]**: TARL 标注为 Turn granularity、LLM-Judge methodology、τ-bench benchmark。

**解释 [本项目判断]**: TARL 属于 LLM-as-judge / verifier credit 路线，应与 HCAPO、LaRe、CriticSearch 一起比较。

## Evidence

- source anchors: Credit Assignment survey Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
