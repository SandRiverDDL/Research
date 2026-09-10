---
title: "SWEET-RL: Privileged Critic for Multi-Turn Agents"
authors: [Xudong Zhou, et al.]
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
  optimizer: actor-critic
  credit_assignment: step
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

用 privileged critic 给 multi-turn agent 更细的中间 credit。

## Selection Basis

Credit Assignment survey Table 10 / §5.1 和 Landscape references 提到；survey-derived card，尚未核原论文 PDF。

## Bounded Brief

**事实 [Credit Survey §5.1]**: SWEET-RL 引入 privileged information critic，critic 可访问任务或环境中的额外状态变量来估计 credit。

**事实 [Credit Survey Table 7]**: survey 报告 SWEET-RL 在 ColBench Backend 上相对 MT-DPO 有 +6.0%。

**解释 [本项目判断]**: 这是 agentic RL 里“privileged critic”路线的代表，和 HCAPO 的 LLM hindsight critic、AgentPRM 的 learned value/PRM 路线互补。

## Evidence

- source anchors: Credit Assignment survey §5.1, Table 7, Table 10。

<!-- pdf: none -->
<!-- survey: 2604.09459 Credit Assignment -->
