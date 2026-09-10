---
title: "PRS: Progressive Reward Shaping for Agentic Tasks"
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
  reward_signal: dense
  optimizer: grpo-like
  credit_assignment: step
  data_reuse: curriculum
  sft_warm_start: unclear
---

## 一句话

Progressive tasks 中用逐步 reward shaping 缓解稀疏反馈。

## Selection Basis

Credit Assignment survey Table 10 列为 CA-adjacent enabler；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Table 10]**: PRS 标注为 Step granularity、Progressive methodology、Progressive tasks。

**解释 [本项目判断]**: PRS 可能更像 reward/curriculum 机制，应与 SPA-RL、BEACON、Atom-Searcher 的过程 reward 轴对照。

## Evidence

- source anchors: Credit Assignment survey Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
