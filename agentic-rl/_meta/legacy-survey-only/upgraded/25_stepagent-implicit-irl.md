---
title: "StepAgent: Implicit + IRL Credit for Tool-Use Tasks"
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
  reward_signal: sparse
  optimizer: other
  credit_assignment: step
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

Tool-use tasks 中的 implicit + IRL step credit 方法。

## Selection Basis

Credit Assignment survey Table 10 列为 Agentic RL core CA method；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Table 10]**: StepAgent 标注为 Step granularity、Implicit+IRL methodology、Tool-use tasks。

**解释 [本项目判断]**: StepAgent 可能连接 inverse RL 与 agent tool-use credit，后续需要核查它是否依赖 demonstrations。

## Evidence

- source anchors: Credit Assignment survey Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
