---
title: "PaperScout: Training LLM Agents for Academic Paper Search via Proximal Sequence Policy Optimization"
authors: [Tingyue Pan, Jie Ouyang, Mingyue Cheng, et al.]
year: 2026
venue: arxiv
url: https://arxiv.org/abs/2601.10029
arxiv_id: 2601.10029

lane: tool-rl
paper_type: core-rl-method
lifecycle_role: frontier-candidate
data_overlap: false

rl_axes:
  environment: tool
  interaction_mode: online
  reward_signal: process
  optimizer: policy-gradient
  credit_assignment: segment
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

把 paper search agent 的 RL 粒度对齐到 sequence-level interaction。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | Academic paper search，被形式化为包含 Search / Expand 决策的 POMDP。 | 这是 tool-use/search agent，不是单轮检索排序。 | `_meta/briefs/papers/2601.10029_paperscout-pspo.md` p.1, p.3 |
| Interaction loop | agent 根据累积 paper pool 和历史决定是否、何时、如何调用 search / expand。 | 让训练目标覆盖多轮 retrieval frontier 管理。 | brief p.1, p.3 |
| Reward / feedback | sequence-level feedback 加中间 process reward。 | 避免只用 terminal outcome 时无法利用多轮检索过程信号。 | brief p.1-p.2, p.8 |
| Optimizer / update | Proximal Sequence Policy Optimization, process-aware sequence-level policy optimization。 | 把 policy update 的粒度从 token 或整条 trajectory 改到 interaction sequence。 | brief p.1, p.3 |
| Credit assignment | critic 利用 process rewards 支持 sequence-level credit。 | 针对 multi-turn agent 的 granularity mismatch。 | brief p.1-p.2, p.8 |
| Exploration / replay | 通过 Search / Expand 工具探索 paper graph / corpus；不是 replay 主轴。 | 重点是 agent 决策粒度和检索过程反馈。 | brief p.3 |
| Warm start / data | 论文报告 synthetic + real-world search benchmarks；官方代码公开。 | 可复现性和后续比较价值高于普通应用 demo。 | brief p.1, p.2 |

## 核心增量

**事实 [brief p.1]**: PaperScout 把 academic paper search 改写为 sequential decision-making，agent 动态决定是否、何时、如何调用 search 和 expand tools。

**事实 [brief p.1-p.2]**: 论文指出标准 RL 方法在 multi-turn agent task 上存在 granularity mismatch；PSPO 是 process-aware sequence-level policy optimization，用于对齐优化粒度和 agent-environment interaction。

**事实 [brief p.8]**: 结论窗口称 PSPO 相比 PPO、GSPO 和只聚合 process reward 的变体收敛更快、稳定性更好。

**解释 [本项目判断]**: 这是 strict core method，但应用域较窄；comparison 中应放在 sequence-level / process-aware optimizer 分支，而不是作为通用 web/tool recipe。

## 谱系位置

- 上游：PPO、GRPO、GSPO。
- 同期：StepPO、AT^2PO、Tree-GRPO。
- 下游：agentic search / deep research 系统里的 process-aware RL。

## 优缺点

- ✅ [brief p.1-p.3]: 明确把 tool-search agent 的状态、动作和 observation 形式化为 POMDP。
- ✅ [brief p.1]: 官方代码链接公开。
- ⚠️ [本项目判断]: 方法证据主要来自 paper-search 环境；能否迁移到 web/GUI/tool-mix agent 需要单独验证。

## Evidence

- paper brief: `_meta/briefs/papers/2601.10029_paperscout-pspo.md`
- PDF / HTML: `papers/2601.10029-paperscout-pspo.pdf`
- survey windows: post-survey strict-core recall

<!-- pdf: papers/2601.10029-paperscout-pspo.pdf -->
<!-- brief: _meta/briefs/papers/2601.10029_paperscout-pspo.md -->
<!-- survey: post-survey strict-core recall -->
