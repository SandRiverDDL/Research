---
title: "Implicit Turn-Wise Policy Optimization for Proactive User-LLM Interaction"
authors: [Haoyu Wang, Yuxin Chen, Liang Luo, Buyun Zhang et al.]
year: 2026
venue: arxiv
url: https://arxiv.org/abs/2603.23550
arxiv_id: 2603.23550

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
  sft_warm_start: standard
---

## 一句话

面向主动交互的 implicit turn-wise preference optimization。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | mixed；ITPO 对应的原文任务设置。 | 判断它是否是真正的 agentic RL learning loop，而不是只做数据或普通 reasoning。 | `_meta/briefs/papers/2603.23550_itpo-implicit-turn-credit.md` |
| Interaction loop | online。 | 决定 credit/reward 是否来自真实多步交互、离线轨迹还是 replay。 | `_meta/briefs/papers/2603.23550_itpo-implicit-turn-credit.md` |
| Reward / feedback | sparse。 | 区分 outcome-only、process reward、critic/judge/verifier reward 的机制差异。 | `_meta/briefs/papers/2603.23550_itpo-implicit-turn-credit.md` |
| Optimizer / update | dpo-like。 | 判断贡献是否改变 policy optimization，还是只改 reward/环境。 | `_meta/briefs/papers/2603.23550_itpo-implicit-turn-credit.md` |
| Credit assignment | step。 | 这是从 survey-only 恢复为正式卡的核心判断轴。 | `_meta/briefs/papers/2603.23550_itpo-implicit-turn-credit.md` |
| Exploration / replay | data_reuse=none。 | 判断它是否解决 long-horizon exploration / off-policy reuse / curriculum。 | `_meta/briefs/papers/2603.23550_itpo-implicit-turn-credit.md` |
| Warm start / data | sft_warm_start=standard。 | 判断方法是否依赖强 SFT 起点或额外训练时信息。 | `_meta/briefs/papers/2603.23550_itpo-implicit-turn-credit.md` |

## 核心增量

**事实 [arXiv abstract / paper brief]**: Multi-turn human-AI collaboration is fundamental to deploying interactive services such as adaptive tutoring, conversational recommendation, and professional consultation. However, optimizing these interactions via reinforcement learning is hindered by the sparsity of verifiable intermediate rewards and the high stochasticity of user responses.

**事实 [arXiv abstract / paper brief]**: To address these challenges, we introduce Implicit Turn-wise Policy Optimization (ITPO). ITPO leverages an implicit process reward model to derive fine-grained, turn-wise process rewards from sparse outcome signals.

**解释 [本项目判断]**: ITPO 将 preference optimization 提升到 turn-wise 交互层，适合和 iStar/Turn-PPO 对照。

## 谱系位置

- 上游：PPO / GRPO / DPO-like LLM RL；对应粒度的 credit assignment 方法。
- 同期：ArCHer、GiGPO、AgentPRM、SWEET-RL、HCAPO、BEACON、CriticSearch 等 agentic credit 方法。
- 下游：后续需要在 comparison 中按 reward source、credit granularity、online/off-policy 和 environment lane 对齐。

## 优缺点

- ✅ [paper brief]: 原文提供了可核验的机制描述，已从 survey-only stub 升级为 original-paper evidence-backed card。
- ✅ [paper brief]: 该方法至少改变 reward / credit / optimizer / interaction granularity 之一，符合 Agentic RL 主线。
- ⚠️ [本项目判断]: 本卡是 L1 research index；具体实验数字、代码可用性和强 baseline 地位仍需 L2 或 comparison 深核。

## Evidence

- paper brief: `_meta/briefs/papers/2603.23550_itpo-implicit-turn-credit.md`
- PDF / HTML: `papers/2603.23550-itpo-implicit-turn-credit.pdf`
- survey windows: Credit Assignment survey Table 10 / related section
- arXiv: `https://arxiv.org/abs/2603.23550`

<!-- pdf: papers/2603.23550-itpo-implicit-turn-credit.pdf -->

<!-- brief: _meta/briefs/papers/2603.23550_itpo-implicit-turn-credit.md -->

<!-- survey: 2604.09459 Credit Assignment -->
