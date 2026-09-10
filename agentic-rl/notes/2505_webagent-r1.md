---
title: "WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning"
authors: [Zhepei Wei, Wenlin Yao, Yao Liu, et al.]
year: 2025
venue: EMNLP 2025
url: https://arxiv.org/abs/2505.16421
arxiv_id: 2505.16421

lane: web-rl
paper_type: environment-recipe
lifecycle_role: frontier-candidate
data_overlap: true

rl_axes:
  environment: web
  interaction_mode: online
  reward_signal: sparse
  optimizer: grpo-like
  credit_assignment: trajectory
  data_reuse: rejection-sampling
  sft_warm_start: standard
---

## 一句话

Web agent end-to-end multi-turn RL：在线 web trajectories + binary success reward。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | WebArena-Lite web environment。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.16421_25_webagent-r1.md` |
| Interaction loop | online multi-turn web interaction。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.16421_25_webagent-r1.md` |
| Reward / feedback | binary success reward。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.16421_25_webagent-r1.md` |
| Optimizer / update | R1/GRPO-like end-to-end RL。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.16421_25_webagent-r1.md` |
| Credit assignment | trajectory-level sparse reward。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.16421_25_webagent-r1.md` |
| Exploration / replay | parallel diverse trajectories；test-time scaling analysis。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.16421_25_webagent-r1.md` |
| Warm start / data | warm-up behavior cloning is important。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.16421_25_webagent-r1.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: WebAgent-R1 提出 end-to-end multi-turn RL framework for training web agents，直接从 web environments 的 online interactions 学习。

**事实 [PDF abstract, p.1]**: 方法 parallel 生成 diverse trajectories，完全由 binary task success reward 指导。

**事实 [PDF abstract, p.1]**: 在 WebArena-Lite 上，Qwen-2.5-3B 从 6.1% 到 33.9%，Llama-3.1-8B 从 8.5% 到 44.8%；还分析 thinking prompting、test-time scaling、warm-up training 和 long CoT。

**解释 [本项目判断]**: 这是 WebRL 之后更直接的 end-to-end web RL 卡；关键比较点是 WebRL 的 curriculum/ORM vs WebAgent-R1 的 binary reward + parallel rollout。

**收录依据 [queue/audit]**: survey/queue 正文提到 + EMNLP 2025 + 官方代码/artifacts，直接抽卡。代码：`https://github.com/weizhepei/WebAgent-R1`。

## 谱系位置

- 上游：WebArena、WebRL、behavior cloning web agents。
- 同期：RAGEN、GiGPO。
- 下游：web/GUI end-to-end RL。

## 优缺点

- ✅ [PDF abstract, p.1]: 简单 end-to-end multi-turn RL formulation。
- ✅ [PDF p.1 footnote]: 代码和 artifacts 开源。
- ⚠️ [本项目判断]: binary reward 下的 credit assignment 仍粗，需和 WebRL/GiGPO 对照。

## Evidence

- paper brief: `_meta/briefs/papers/2505.16421_25_webagent-r1.md`
- PDF / HTML: `papers/2505.16421-webagent-r1.pdf`
- survey windows: queue / web lane
- PDF: `papers/2505.16421-webagent-r1.pdf`
- source anchors: abstract p.1; introduction p.1-2。

<!-- pdf: papers/2505.16421-webagent-r1.pdf -->

<!-- brief: _meta/briefs/papers/2505.16421_25_webagent-r1.md -->

<!-- survey: queue / web lane -->
