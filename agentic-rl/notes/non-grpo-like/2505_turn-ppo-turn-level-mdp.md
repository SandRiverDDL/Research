---
title: "Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design"
authors: [Quan Wei, Siliang Zeng, Chenliang Li, William Brown et al.]
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2505.11821
arxiv_id: 2505.11821

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: canonical-anchor
data_overlap: false

rl_axes:
  environment: mixed
  interaction_mode: online
  reward_signal: sparse
  optimizer: policy-gradient
  credit_assignment: step
  data_reuse: none
  sft_warm_start: standard
---

## 一句话

把 multi-turn agent interaction 建模成 turn-level MDP。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | mixed；Turn-PPO 对应的原文任务设置。 | 判断它是否是真正的 agentic RL learning loop，而不是只做数据或普通 reasoning。 | `_meta/briefs/papers/2505.11821_turn-ppo-turn-level-mdp.md` |
| Interaction loop | online。 | 决定 credit/reward 是否来自真实多步交互、离线轨迹还是 replay。 | `_meta/briefs/papers/2505.11821_turn-ppo-turn-level-mdp.md` |
| Reward / feedback | sparse。 | 区分 outcome-only、process reward、critic/judge/verifier reward 的机制差异。 | `_meta/briefs/papers/2505.11821_turn-ppo-turn-level-mdp.md` |
| Optimizer / update | policy-gradient。 | 判断贡献是否改变 policy optimization，还是只改 reward/环境。 | `_meta/briefs/papers/2505.11821_turn-ppo-turn-level-mdp.md` |
| Credit assignment | step。 | 这是从 survey-only 恢复为正式卡的核心判断轴。 | `_meta/briefs/papers/2505.11821_turn-ppo-turn-level-mdp.md` |
| Exploration / replay | data_reuse=none。 | 判断它是否解决 long-horizon exploration / off-policy reuse / curriculum。 | `_meta/briefs/papers/2505.11821_turn-ppo-turn-level-mdp.md` |
| Warm start / data | sft_warm_start=standard。 | 判断方法是否依赖强 SFT 起点或额外训练时信息。 | `_meta/briefs/papers/2505.11821_turn-ppo-turn-level-mdp.md` |

## 核心增量

**事实 [arXiv abstract / paper brief]**: This paper investigates Reinforcement Learning (RL) approaches to enhance the reasoning capabilities of Large Language Model (LLM) agents in long-horizon, multi-turn scenarios. Although RL algorithms such as Group Relative Policy Optimization (GRPO) and Proximal Policy Optimization (PPO) have been widely applied to train multi-turn LLM agents, they typically rely only on sparse outcome rewards and lack dense intermediate signals across multiple decision steps, limiting their performance on complex reasoning tasks.

**事实 [arXiv abstract / paper brief]**: To bridge this gap, we present the first systematic study of turn-level reward design for multi-turn RL algorithms and agent applications. By integrating turn-level rewards, we extend GRPO and PPO to their respective multi-turn variants, enabling fine-grained credit assignment.

**解释 [本项目判断]**: Turn-level reward design 是把 token trajectory 提升到 turn/state/action 层面的建模路线，和 ArCHer/Agent Lightning 同属 granularity redesign。

## 谱系位置

- 上游：PPO / GRPO / DPO-like LLM RL；对应粒度的 credit assignment 方法。
- 同期：ArCHer、GiGPO、AgentPRM、SWEET-RL、HCAPO、BEACON、CriticSearch 等 agentic credit 方法。
- 下游：后续需要在 comparison 中按 reward source、credit granularity、online/off-policy 和 environment lane 对齐。

## 优缺点

- ✅ [paper brief]: 原文提供了可核验的机制描述，已从 survey-only stub 升级为 original-paper evidence-backed card。
- ✅ [paper brief]: 该方法至少改变 reward / credit / optimizer / interaction granularity 之一，符合 Agentic RL 主线。
- ⚠️ [本项目判断]: 本卡是 L1 research index；具体实验数字、代码可用性和强 baseline 地位仍需 L2 或 comparison 深核。

## Evidence

- paper brief: `_meta/briefs/papers/2505.11821_turn-ppo-turn-level-mdp.md`
- PDF / HTML: `papers/2505.11821-turn-ppo-turn-level-mdp-alt.pdf`
- survey windows: Credit Assignment survey Table 10 / related section
- arXiv: `https://arxiv.org/abs/2505.11821`

<!-- pdf: papers/2505.11821-turn-ppo-turn-level-mdp-alt.pdf -->

<!-- brief: _meta/briefs/papers/2505.11821_turn-ppo-turn-level-mdp.md -->

<!-- survey: 2604.09459 Credit Assignment -->
