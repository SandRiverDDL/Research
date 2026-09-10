---
title: "Latent Reward: LLM-Empowered Credit Assignment in Episodic Reinforcement Learning"
authors: [Yun Qu, Yuhang Jiang, Boyuan Wang, Yixiu Mao et al.]
year: 2024
venue: arxiv
url: https://arxiv.org/abs/2412.11120
arxiv_id: 2412.11120

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: background
data_overlap: false

rl_axes:
  environment: simulated
  interaction_mode: offline-rollout
  reward_signal: verifier
  optimizer: other
  credit_assignment: step
  data_reuse: none
  sft_warm_start: none
---

## 一句话

LLM 生成 latent reward 做 episodic credit redistribution。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | simulated；LaRe 对应的原文任务设置。 | 判断它是否是真正的 agentic RL learning loop，而不是只做数据或普通 reasoning。 | `_meta/briefs/papers/2412.11120_lare-llm-critic-credit.md` |
| Interaction loop | offline-rollout。 | 决定 credit/reward 是否来自真实多步交互、离线轨迹还是 replay。 | `_meta/briefs/papers/2412.11120_lare-llm-critic-credit.md` |
| Reward / feedback | verifier。 | 区分 outcome-only、process reward、critic/judge/verifier reward 的机制差异。 | `_meta/briefs/papers/2412.11120_lare-llm-critic-credit.md` |
| Optimizer / update | other。 | 判断贡献是否改变 policy optimization，还是只改 reward/环境。 | `_meta/briefs/papers/2412.11120_lare-llm-critic-credit.md` |
| Credit assignment | step。 | 这是从 survey-only 恢复为正式卡的核心判断轴。 | `_meta/briefs/papers/2412.11120_lare-llm-critic-credit.md` |
| Exploration / replay | data_reuse=none。 | 判断它是否解决 long-horizon exploration / off-policy reuse / curriculum。 | `_meta/briefs/papers/2412.11120_lare-llm-critic-credit.md` |
| Warm start / data | sft_warm_start=none。 | 判断方法是否依赖强 SFT 起点或额外训练时信息。 | `_meta/briefs/papers/2412.11120_lare-llm-critic-credit.md` |

## 核心增量

**事实 [arXiv abstract / paper brief]**: Reinforcement learning (RL) often encounters delayed and sparse feedback in real-world applications, even with only episodic rewards. Previous approaches have made some progress in reward redistribution for credit assignment but still face challenges, including training difficulties due to redundancy and ambiguous attributions stemming from overlooking the multifaceted nature of mission performance evaluation.

**事实 [arXiv abstract / paper brief]**: Hopefully, Large Language Model (LLM) encompasses fruitful decision-making knowledge and provides a plausible tool for reward redistribution. Even so, deploying LLM in this case is non-trivial due to the misalignment between linguistic knowledge and the symbolic form requirement, together with inherent randomness and hallucinations in inference.

**解释 [本项目判断]**: LaRe 是 LLM-as-critic/symbolic reward redistribution 背景方法，偏传统 episodic RL，但能支撑 agentic critic credit 的谱系。

## 谱系位置

- 上游：PPO / GRPO / DPO-like LLM RL；对应粒度的 credit assignment 方法。
- 同期：ArCHer、GiGPO、AgentPRM、SWEET-RL、HCAPO、BEACON、CriticSearch 等 agentic credit 方法。
- 下游：后续需要在 comparison 中按 reward source、credit granularity、online/off-policy 和 environment lane 对齐。

## 优缺点

- ✅ [paper brief]: 原文提供了可核验的机制描述，已从 survey-only stub 升级为 original-paper evidence-backed card。
- ✅ [paper brief]: 该方法至少改变 reward / credit / optimizer / interaction granularity 之一，符合 Agentic RL 主线。
- ⚠️ [本项目判断]: 本卡是 L1 research index；具体实验数字、代码可用性和强 baseline 地位仍需 L2 或 comparison 深核。

## Evidence

- paper brief: `_meta/briefs/papers/2412.11120_lare-llm-critic-credit.md`
- PDF / HTML: `papers/2412.11120-lare-llm-critic-credit.pdf`
- survey windows: Credit Assignment survey Table 10 / related section
- arXiv: `https://arxiv.org/abs/2412.11120`

<!-- pdf: papers/2412.11120-lare-llm-critic-credit.pdf -->

<!-- brief: _meta/briefs/papers/2412.11120_lare-llm-critic-credit.md -->

<!-- survey: 2604.09459 Credit Assignment -->
