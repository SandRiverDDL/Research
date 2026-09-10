---
title: "Reinforcing Language Agents via Policy Optimization with Action Decomposition"
authors: [Muning Wen, Ziyu Wan, Weinan Zhang, Jun Wang et al.]
year: 2024
venue: arxiv
url: https://arxiv.org/abs/2405.15821
arxiv_id: 2405.15821

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: canonical-anchor
data_overlap: false

rl_axes:
  environment: mixed
  interaction_mode: online
  reward_signal: sparse
  optimizer: policy-gradient
  credit_assignment: tool-call
  data_reuse: none
  sft_warm_start: standard
---

## 一句话

把语言 agent action decomposition 后再做 policy optimization。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | mixed；POAD 对应的原文任务设置。 | 判断它是否是真正的 agentic RL learning loop，而不是只做数据或普通 reasoning。 | `_meta/briefs/papers/2405.15821_poad-action-decomposition.md` |
| Interaction loop | online。 | 决定 credit/reward 是否来自真实多步交互、离线轨迹还是 replay。 | `_meta/briefs/papers/2405.15821_poad-action-decomposition.md` |
| Reward / feedback | sparse。 | 区分 outcome-only、process reward、critic/judge/verifier reward 的机制差异。 | `_meta/briefs/papers/2405.15821_poad-action-decomposition.md` |
| Optimizer / update | policy-gradient。 | 判断贡献是否改变 policy optimization，还是只改 reward/环境。 | `_meta/briefs/papers/2405.15821_poad-action-decomposition.md` |
| Credit assignment | tool-call。 | 这是从 survey-only 恢复为正式卡的核心判断轴。 | `_meta/briefs/papers/2405.15821_poad-action-decomposition.md` |
| Exploration / replay | data_reuse=none。 | 判断它是否解决 long-horizon exploration / off-policy reuse / curriculum。 | `_meta/briefs/papers/2405.15821_poad-action-decomposition.md` |
| Warm start / data | sft_warm_start=standard。 | 判断方法是否依赖强 SFT 起点或额外训练时信息。 | `_meta/briefs/papers/2405.15821_poad-action-decomposition.md` |

## 核心增量

**事实 [arXiv abstract / paper brief]**: Language models as intelligent agents push the boundaries of sequential decision-making agents but struggle with limited knowledge of environmental dynamics and exponentially huge action space. Recent efforts like GLAM and TWOSOME manually constrain the action space to a restricted subset and employ reinforcement learning to align agents' knowledge with specific environments.

**事实 [arXiv abstract / paper brief]**: However, they overlook fine-grained credit assignments for intra-action tokens, which is essential for efficient language agent optimization, and rely on human's prior knowledge to restrict action space. This paper proposes decomposing language agent optimization from the action level to the token level, offering finer supervision for each intra-action token and manageable optimization complexity in environments with unrestricted action spaces.

**解释 [本项目判断]**: POAD 是 action-grammar / tool-call 级 credit 的早期 anchor，直接改变动作空间与优化粒度。

## 谱系位置

- 上游：PPO / GRPO / DPO-like LLM RL；对应粒度的 credit assignment 方法。
- 同期：ArCHer、GiGPO、AgentPRM、SWEET-RL、HCAPO、BEACON、CriticSearch 等 agentic credit 方法。
- 下游：后续需要在 comparison 中按 reward source、credit granularity、online/off-policy 和 environment lane 对齐。

## 优缺点

- ✅ [paper brief]: 原文提供了可核验的机制描述，已从 survey-only stub 升级为 original-paper evidence-backed card。
- ✅ [paper brief]: 该方法至少改变 reward / credit / optimizer / interaction granularity 之一，符合 Agentic RL 主线。
- ⚠️ [本项目判断]: 本卡是 L1 research index；具体实验数字、代码可用性和强 baseline 地位仍需 L2 或 comparison 深核。

## Evidence

- paper brief: `_meta/briefs/papers/2405.15821_poad-action-decomposition.md`
- PDF / HTML: `papers/2405.15821-poad-action-decomposition.pdf`
- survey windows: Credit Assignment survey Table 10 / related section
- arXiv: `https://arxiv.org/abs/2405.15821`

<!-- pdf: papers/2405.15821-poad-action-decomposition.pdf -->

<!-- brief: _meta/briefs/papers/2405.15821_poad-action-decomposition.md -->

<!-- survey: 2604.09459 Credit Assignment -->
