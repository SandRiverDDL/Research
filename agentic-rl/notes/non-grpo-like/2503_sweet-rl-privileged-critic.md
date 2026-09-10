---
title: "SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks"
authors: [Yifei Zhou, Song Jiang, Yuandong Tian, Jason Weston et al.]
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2503.15478
arxiv_id: 2503.15478

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
  sft_warm_start: standard
---

## 一句话

Privileged critic 给 multi-turn collaborative agents 分配 step reward。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | mixed；SWEET-RL 对应的原文任务设置。 | 判断它是否是真正的 agentic RL learning loop，而不是只做数据或普通 reasoning。 | `_meta/briefs/papers/2503.15478_sweet-rl-privileged-critic.md` |
| Interaction loop | online。 | 决定 credit/reward 是否来自真实多步交互、离线轨迹还是 replay。 | `_meta/briefs/papers/2503.15478_sweet-rl-privileged-critic.md` |
| Reward / feedback | process。 | 区分 outcome-only、process reward、critic/judge/verifier reward 的机制差异。 | `_meta/briefs/papers/2503.15478_sweet-rl-privileged-critic.md` |
| Optimizer / update | actor-critic。 | 判断贡献是否改变 policy optimization，还是只改 reward/环境。 | `_meta/briefs/papers/2503.15478_sweet-rl-privileged-critic.md` |
| Credit assignment | step。 | 这是从 survey-only 恢复为正式卡的核心判断轴。 | `_meta/briefs/papers/2503.15478_sweet-rl-privileged-critic.md` |
| Exploration / replay | data_reuse=none。 | 判断它是否解决 long-horizon exploration / off-policy reuse / curriculum。 | `_meta/briefs/papers/2503.15478_sweet-rl-privileged-critic.md` |
| Warm start / data | sft_warm_start=standard。 | 判断方法是否依赖强 SFT 起点或额外训练时信息。 | `_meta/briefs/papers/2503.15478_sweet-rl-privileged-critic.md` |

## 核心增量

**事实 [arXiv abstract / paper brief]**: Large language model (LLM) agents need to perform multi-turn interactions in real-world tasks. However, existing multi-turn RL algorithms for optimizing LLM agents fail to perform effective credit assignment over multiple turns while leveraging the generalization capabilities of LLMs and it remains unclear how to develop such algorithms.

**事实 [arXiv abstract / paper brief]**: To study this, we first introduce a new benchmark, ColBench, where an LLM agent interacts with a human collaborator over multiple turns to solve realistic tasks in backend programming and frontend design. Building on this benchmark, we propose a novel RL algorithm, SWEET-RL (RL with Step-WisE Evaluation from Training-time information), that uses a carefully designed optimization objective to train a critic model with access to additional training-time information.

**解释 [本项目判断]**: SWEET-RL 是 privileged critic 路线代表，关键在 critic 可访问训练时额外信息并输出 step-level rewards。

## 谱系位置

- 上游：PPO / GRPO / DPO-like LLM RL；对应粒度的 credit assignment 方法。
- 同期：ArCHer、GiGPO、AgentPRM、SWEET-RL、HCAPO、BEACON、CriticSearch 等 agentic credit 方法。
- 下游：后续需要在 comparison 中按 reward source、credit granularity、online/off-policy 和 environment lane 对齐。

## 优缺点

- ✅ [paper brief]: 原文提供了可核验的机制描述，已从 survey-only stub 升级为 original-paper evidence-backed card。
- ✅ [paper brief]: 该方法至少改变 reward / credit / optimizer / interaction granularity 之一，符合 Agentic RL 主线。
- ⚠️ [本项目判断]: 本卡是 L1 research index；具体实验数字、代码可用性和强 baseline 地位仍需 L2 或 comparison 深核。

## Evidence

- paper brief: `_meta/briefs/papers/2503.15478_sweet-rl-privileged-critic.md`
- PDF / HTML: `papers/2503.15478-sweet-rl-privileged-critic.pdf`
- survey windows: Credit Assignment survey Table 10 / related section
- arXiv: `https://arxiv.org/abs/2503.15478`

<!-- pdf: papers/2503.15478-sweet-rl-privileged-critic.pdf -->

<!-- brief: _meta/briefs/papers/2503.15478_sweet-rl-privileged-critic.md -->

<!-- survey: 2604.09459 Credit Assignment -->
