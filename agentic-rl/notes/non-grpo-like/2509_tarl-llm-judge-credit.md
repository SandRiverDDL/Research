---
title: "Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents"
authors: [Weiting Tan, Xinghua Qu, Ming Tu, Meng Ge et al.]
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2509.14480
arxiv_id: 2509.14480

lane: tool-rl
paper_type: core-rl-method
lifecycle_role: frontier-candidate
data_overlap: false

rl_axes:
  environment: tool
  interaction_mode: online
  reward_signal: verifier
  optimizer: policy-gradient
  credit_assignment: step
  data_reuse: curriculum
  sft_warm_start: standard
---

## 一句话

LLM judge turn-level adjudication for interactive multimodal tool-use。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | tool；TARL 对应的原文任务设置。 | 判断它是否是真正的 agentic RL learning loop，而不是只做数据或普通 reasoning。 | `_meta/briefs/papers/2509.14480_tarl-llm-judge-credit.md` |
| Interaction loop | online。 | 决定 credit/reward 是否来自真实多步交互、离线轨迹还是 replay。 | `_meta/briefs/papers/2509.14480_tarl-llm-judge-credit.md` |
| Reward / feedback | verifier。 | 区分 outcome-only、process reward、critic/judge/verifier reward 的机制差异。 | `_meta/briefs/papers/2509.14480_tarl-llm-judge-credit.md` |
| Optimizer / update | policy-gradient。 | 判断贡献是否改变 policy optimization，还是只改 reward/环境。 | `_meta/briefs/papers/2509.14480_tarl-llm-judge-credit.md` |
| Credit assignment | step。 | 这是从 survey-only 恢复为正式卡的核心判断轴。 | `_meta/briefs/papers/2509.14480_tarl-llm-judge-credit.md` |
| Exploration / replay | data_reuse=curriculum。 | 判断它是否解决 long-horizon exploration / off-policy reuse / curriculum。 | `_meta/briefs/papers/2509.14480_tarl-llm-judge-credit.md` |
| Warm start / data | sft_warm_start=standard。 | 判断方法是否依赖强 SFT 起点或额外训练时信息。 | `_meta/briefs/papers/2509.14480_tarl-llm-judge-credit.md` |

## 核心增量

**事实 [arXiv abstract / paper brief]**: Effective interactive tool use requires agents to master Tool Integrated Reasoning (TIR): a complex process involving multi-turn planning and long-context dialogue management. To train agents for this dynamic process, particularly in multi-modal contexts, we introduce a sandbox environment for reinforcement learning (RL) that supports interleaved speech-text rollouts.

**事实 [arXiv abstract / paper brief]**: Our core strategy, Turn-level Adjudicated Reinforcement Learning (TARL), addresses the challenge of credit assignment in long-horizon tasks by employing a Large Language Model (LLM) as a judge to provide turn-level evaluation. To enhance exploration, we integrate a mixed-task training curriculum with mathematical reasoning problems.

**解释 [本项目判断]**: TARL 属于 LLM-as-judge process supervision，把 τ-bench/多模态 tool-use 的长程 credit 转成 turn-level feedback。

## 谱系位置

- 上游：PPO / GRPO / DPO-like LLM RL；对应粒度的 credit assignment 方法。
- 同期：ArCHer、GiGPO、AgentPRM、SWEET-RL、HCAPO、BEACON、CriticSearch 等 agentic credit 方法。
- 下游：后续需要在 comparison 中按 reward source、credit granularity、online/off-policy 和 environment lane 对齐。

## 优缺点

- ✅ [paper brief]: 原文提供了可核验的机制描述，已从 survey-only stub 升级为 original-paper evidence-backed card。
- ✅ [paper brief]: 该方法至少改变 reward / credit / optimizer / interaction granularity 之一，符合 Agentic RL 主线。
- ⚠️ [本项目判断]: 本卡是 L1 research index；具体实验数字、代码可用性和强 baseline 地位仍需 L2 或 comparison 深核。

## Evidence

- paper brief: `_meta/briefs/papers/2509.14480_tarl-llm-judge-credit.md`
- PDF / HTML: `papers/2509.14480-tarl-llm-judge-credit.pdf`
- survey windows: Credit Assignment survey Table 10 / related section
- arXiv: `https://arxiv.org/abs/2509.14480`

<!-- pdf: papers/2509.14480-tarl-llm-judge-credit.pdf -->

<!-- brief: _meta/briefs/papers/2509.14480_tarl-llm-judge-credit.md -->

<!-- survey: 2604.09459 Credit Assignment -->
