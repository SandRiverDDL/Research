---
title: "C3: Counterfactual Credit for Agentic and Multi-Agent Tasks"
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

通过 leave-one-out / counterfactual 分析判断哪一步真的贡献成功。

## Selection Basis

Credit Assignment survey Figure 3 / Table 10 列为 Agentic/Multi-agent core CA method；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey §2.5]**: survey 将 C3 与 CCPO 描述为在 LLM setting 中实现 counterfactual credit via leave-one-out analysis of agent turns。

**事实 [Credit Survey Table 10]**: C3 标注为 Turn granularity、Counterfactual methodology、Multi-agent + agentic。

**解释 [本项目判断]**: C3 是 hindsight/counterfactual credit wave 的核心节点，和 HCAPO/CCPO 应并列。

## Evidence

- source anchors: Credit Assignment survey §2.5, Figure 3, Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
