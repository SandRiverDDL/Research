---
title: "ITPO: Implicit Turn-Level Preference Optimization"
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
  optimizer: dpo-like
  credit_assignment: step
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

从 preference/DPO 信号里抽取 turn-level implicit credit。

## Selection Basis

Credit Assignment survey Table 10 列为 Agentic RL core CA method；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Table 10]**: ITPO 标注为 Turn granularity、Implicit methodology、Dialogue tasks。

**事实 [Credit Survey §2.6]**: survey 将 DPO 类方法视为具备 implicit token/turn credit 的一类。

**解释 [本项目判断]**: ITPO 是 DPO-like agentic credit 路线，适合和 iStar、preference-trajectory 方法放一起。

## Evidence

- source anchors: Credit Assignment survey §2.6, Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
