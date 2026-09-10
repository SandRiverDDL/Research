---
title: "Generate, Filter, Control, Replay: A Comprehensive Survey of Rollout Strategies for LLM Reinforcement Learning"
authors: [Rohan Surana, Gagan Mundada, Xunyi Jiang, et al.]
year: 2026
venue: arxiv
url: https://arxiv.org/abs/2605.02913
arxiv_id: 2605.02913

lane: survey
paper_type: survey
lifecycle_role: survey-seed
data_overlap: true

rl_axes:
  environment: mixed
  interaction_mode: offline-rollout
  reward_signal: verifier
  optimizer: other
  credit_assignment: trajectory
  data_reuse: replay
  sft_warm_start: unclear
---

## 一句话

Rollout / replay 机制 seed：把 RL 数据生命周期拆成 GFCR。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | mixed；case studies 包含 math、code/SQL、multimodal reasoning、tool-using agents、agentic skill benchmarks。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2605.02913_26_gfcr-rollout-strategies-llm-rl-survey.md` |
| Interaction loop | sampled rollout trajectory，可包含 tool/environment interaction。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2605.02913_26_gfcr-rollout-strategies-llm-rl-survey.md` |
| Reward / feedback | Filter 阶段覆盖 verifier、judge、critic、process supervision。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2605.02913_26_gfcr-rollout-strategies-llm-rl-survey.md` |
| Optimizer / update | optimizer-agnostic；不主张具体 PPO/GRPO 变体。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2605.02913_26_gfcr-rollout-strategies-llm-rl-survey.md` |
| Credit assignment | 主要通过 rollout structure、filtering signal、partial/segment rollouts 影响 credit。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2605.02913_26_gfcr-rollout-strategies-llm-rl-survey.md` |
| Exploration / replay | Replay 阶段包含 self-evolving curricula 和数据复用。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2605.02913_26_gfcr-rollout-strategies-llm-rl-survey.md` |
| Warm start / data | 非核心。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2605.02913_26_gfcr-rollout-strategies-llm-rl-survey.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: 论文认为 rollout 是 prompt 到 termination 的 sampled trajectory，可包含 intermediate reasoning steps 与 optional tool/environment interactions；rollout 决定 optimizer 最终学习的数据，但常被当成 implementation detail。

**事实 [PDF abstract, p.1]**: 论文提出 Generate-Filter-Control-Replay taxonomy：Generate 产生候选 trajectories/topologies，Filter 用 verifiers/judges/critics 构造中间信号，Control 分配 compute 并决定 continuation/branching/stopping，Replay 保留和复用 rollout artifacts。

**解释 [本项目判断]**: 这篇适合留在 `agentic-rl`，但需要标注 data overlap。它不是纯 Agentic RL survey，而是 rollout pipeline survey；对本项目的价值是把 rollout/replay 从“数据来源”提升成 RL learning loop 的机制变量。

## 谱系位置

- 上游：RLVR / reasoning LLM post-training / process supervision。
- 同期：credit assignment survey、Landscape survey。
- 下游：RAGEN、Search-R1、WebRL、SWE-Gym、GiGPO、VerlTool、self-evolving curricula。

## 优缺点

- ✅ [PDF abstract, p.1]: GFCR taxonomy 直接对应本项目的 rollout / verifier / compute control / replay axes。
- ✅ [PDF p.29]: 明确连接 agentic settings、SWE-Gym、WebRL、RAGEN、Search-R1、VerlTool 等多轮环境 RL 文献。
- ⚠️ [本项目判断]: 更偏 LLM RL post-training 与 reasoning rollout，不应替代 Agentic RL 总览；只作为 rollout-replay track seed。

## Evidence

- paper brief: `_meta/briefs/surveys/2605.02913_26_gfcr-rollout-strategies-llm-rl-survey.md`
- PDF / HTML: `papers/2605.02913-gfcr-rollout-strategies-llm-rl.pdf`
- survey windows: seed
- PDF: `papers/2605.02913-gfcr-rollout-strategies-llm-rl.pdf`
- source anchors: abstract p.1; introduction p.1; agentic settings discussion p.29。

<!-- pdf: papers/2605.02913-gfcr-rollout-strategies-llm-rl.pdf -->

<!-- brief: _meta/briefs/surveys/2605.02913_26_gfcr-rollout-strategies-llm-rl-survey.md -->

<!-- survey: seed -->
