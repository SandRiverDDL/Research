---
title: "HICRA: Hierarchical Credit Assignment for LLM RL"
authors: [Unknown, et al.]
year: 2025
venue: survey-derived
url: null
arxiv_id: null

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: background
data_overlap: false

rl_axes:
  environment: simulated
  interaction_mode: offline-rollout
  reward_signal: verifier
  optimizer: grpo-like
  credit_assignment: step
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

Reasoning-side hierarchy credit 方法，可作为 agentic hierarchy 的背景。

## Selection Basis

Credit Assignment survey Table 10 / Table 8 提到；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Table 10]**: HICRA 标注为 Reasoning RL core CA、Step granularity、Hierarchy methodology、AIME’24/AIME’25。

**解释 [本项目判断]**: HICRA 不是一线 agentic card，但对理解 hierarchy credit 与 ArCHer/Agent Lightning 有背景价值。

## Evidence

- source anchors: Credit Assignment survey Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
