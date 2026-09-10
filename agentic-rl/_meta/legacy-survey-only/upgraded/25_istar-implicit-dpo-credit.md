---
title: "iStar: Implicit DPO Credit for Agent Trajectories"
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
  interaction_mode: offline-rollout
  reward_signal: sparse
  optimizer: dpo-like
  credit_assignment: step
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

从 trajectory preference pairs 中提取 implicit step credit。

## Selection Basis

Credit Assignment survey Figure 3 / Table 10 列为 Agentic RL core CA method；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Figure 3]**: iStar 位于 agentic credit assignment 的 implicit DPO 类别。

**事实 [Credit Survey Table 10]**: iStar 标注为 Step granularity、Implicit DPO methodology、Trajectory pairs。

**解释 [本项目判断]**: iStar 对应“无需显式 reward model 的 implicit credit”路线，和 ITPO / DPO-like 方法相关。

## Evidence

- source anchors: Credit Assignment survey Figure 3, Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
