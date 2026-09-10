---
title: "CriticSearch: Retrospective Critic for Multi-Hop QA"
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
  reward_signal: verifier
  optimizer: grpo-like
  credit_assignment: step
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

Search/multi-hop QA 中的 retrospective critic credit 方法。

## Selection Basis

Credit Assignment survey Figure 3 / Table 10 提到；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Figure 3]**: CriticSearch 位于 LLM-as-Critic / retrospective credit 方法族。

**事实 [Credit Survey Table 10]**: CriticSearch 标注为 Turn granularity、Retrospective Critic methodology、Multi-hop QA。

**解释 [本项目判断]**: CriticSearch 是 search lane 与 LLM-as-critic credit 的交叉点，值得后续核原文。

## Evidence

- source anchors: Credit Assignment survey Figure 3, Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
