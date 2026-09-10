---
title: "SCRIBE: Skill-Prototype Credit for Agentic Tasks"
authors: [Unknown, et al.]
year: 2025
venue: survey-derived
url: null
arxiv_id: null

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: frontier-candidate
data_overlap: true

rl_axes:
  environment: mixed
  interaction_mode: online
  reward_signal: sparse
  optimizer: other
  credit_assignment: step
  data_reuse: replay
  sft_warm_start: unclear
---

## 一句话

用 skill prototype 辅助 agentic credit / experience reuse。

## Selection Basis

Credit Assignment survey Table 10 列为 CA-adjacent enabler；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey Table 10]**: SCRIBE 标注为 Step granularity、Skill-prototype methodology、Agentic tasks。

**解释 [本项目判断]**: SCRIBE 可能有 data/replay overlap；当前先作为 core-method-adjacent 卡保留，后续核查是否应转 Agent Data。

## Evidence

- source anchors: Credit Assignment survey Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
