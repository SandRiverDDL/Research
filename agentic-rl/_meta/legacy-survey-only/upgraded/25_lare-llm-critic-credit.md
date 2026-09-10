---
title: "LaRe: LLM-Critic Credit for Symbolic and Agentic Tasks"
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

用 LLM critic 给 symbolic + agentic trajectory 分配 credit。

## Selection Basis

Credit Assignment survey Figure 3 / Table 10 提到 LaRe；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Figure 3]**: LaRe 属于 LLM-as-Critic / retrospective credit 方法族。

**事实 [Credit Survey Table 10]**: LaRe 标注为 Step granularity、LLM-Critic methodology、Symbolic + agentic tasks。

**解释 [本项目判断]**: LaRe 是 verifier/critic-based credit 方向的候选，应和 HCAPO、TARL、CriticSearch 对照。

## Evidence

- source anchors: Credit Assignment survey Figure 3, Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
