---
title: "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress"
authors: [Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang et al.]
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2511.08325
arxiv_id: 2511.08325

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: frontier-candidate
data_overlap: false

rl_axes:
  environment: mixed
  interaction_mode: online
  reward_signal: process
  optimizer: actor-critic
  credit_assignment: step
  data_reuse: none
  sft_warm_start: unclear
---

## 一句话

Agent PRM 路线：用 promise/progress 建 turn-level process reward。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | mixed；AgentPRM 对应的原文任务设置。 | 判断它是否是真正的 agentic RL learning loop，而不是只做数据或普通 reasoning。 | `_meta/briefs/papers/2511.08325_agentprm-process-reward-model-agents.md` |
| Interaction loop | online。 | 决定 credit/reward 是否来自真实多步交互、离线轨迹还是 replay。 | `_meta/briefs/papers/2511.08325_agentprm-process-reward-model-agents.md` |
| Reward / feedback | process。 | 区分 outcome-only、process reward、critic/judge/verifier reward 的机制差异。 | `_meta/briefs/papers/2511.08325_agentprm-process-reward-model-agents.md` |
| Optimizer / update | actor-critic。 | 判断贡献是否改变 policy optimization，还是只改 reward/环境。 | `_meta/briefs/papers/2511.08325_agentprm-process-reward-model-agents.md` |
| Credit assignment | step。 | 这是从 survey-only 恢复为正式卡的核心判断轴。 | `_meta/briefs/papers/2511.08325_agentprm-process-reward-model-agents.md` |
| Exploration / replay | data_reuse=none。 | 判断它是否解决 long-horizon exploration / off-policy reuse / curriculum。 | `_meta/briefs/papers/2511.08325_agentprm-process-reward-model-agents.md` |
| Warm start / data | sft_warm_start=unclear。 | 判断方法是否依赖强 SFT 起点或额外训练时信息。 | `_meta/briefs/papers/2511.08325_agentprm-process-reward-model-agents.md` |

## 核心增量

**事实 [arXiv abstract / paper brief]**: Despite rapid development, large language models (LLMs) still encounter challenges in multi-turn decision-making tasks (i.e., agent tasks) like web shopping and browser navigation, which require making a sequence of intelligent decisions based on environmental feedback. Previous work for LLM agents typically relies on elaborate prompt engineering or fine-tuning with expert trajectories to improve performance.

**事实 [arXiv abstract / paper brief]**: In this work, we take a different perspective: we explore constructing process reward models (PRMs) to evaluate each decision and guide the agent's decision-making process. Unlike LLM reasoning, where each step is scored based on correctness, actions in agent tasks do not have a clear-cut correctness.

**解释 [本项目判断]**: 这是 process reward / learned value 路线的 agentic 版本，和 SWEET-RL、HCAPO、CriticSearch 的 critic route 直接可比。

## 谱系位置

- 上游：PPO / GRPO / DPO-like LLM RL；对应粒度的 credit assignment 方法。
- 同期：ArCHer、GiGPO、AgentPRM、SWEET-RL、HCAPO、BEACON、CriticSearch 等 agentic credit 方法。
- 下游：后续需要在 comparison 中按 reward source、credit granularity、online/off-policy 和 environment lane 对齐。

## 优缺点

- ✅ [paper brief]: 原文提供了可核验的机制描述，已从 survey-only stub 升级为 original-paper evidence-backed card。
- ✅ [paper brief]: 该方法至少改变 reward / credit / optimizer / interaction granularity 之一，符合 Agentic RL 主线。
- ⚠️ [本项目判断]: 本卡是 L1 research index；具体实验数字、代码可用性和强 baseline 地位仍需 L2 或 comparison 深核。

## Evidence

- paper brief: `_meta/briefs/papers/2511.08325_agentprm-process-reward-model-agents.md`
- PDF / HTML: `papers/2511.08325-agentprm-process-reward-model-agents.pdf`
- survey windows: Credit Assignment survey Table 10 / related section
- arXiv: `https://arxiv.org/abs/2511.08325`

<!-- pdf: papers/2511.08325-agentprm-process-reward-model-agents.pdf -->

<!-- brief: _meta/briefs/papers/2511.08325_agentprm-process-reward-model-agents.md -->

<!-- survey: 2604.09459 Credit Assignment -->
