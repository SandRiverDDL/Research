---
title: "RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning"
authors: [Zihan Wang, Kangrui Wang, Qineng Wang, et al.]
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2504.20073
arxiv_id: 2504.20073

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: frontier-candidate
data_overlap: true

rl_axes:
  environment: simulated
  interaction_mode: online
  reward_signal: sparse
  optimizer: policy-gradient
  credit_assignment: trajectory
  data_reuse: rejection-sampling
  sft_warm_start: standard
---

## 一句话

多轮 agent RL 的机制 seed：StarPO/RAGEN 暴露 rollout、reward、stability 问题。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | 四个 stylized environments，覆盖 trajectory bandit、Sokoban、Frozen Lake 等动态/随机任务。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.20073_25_ragen-multiturn-agent-rl.md` |
| Interaction loop | K-turn rollout；agent 在 state-observation-action-reward loop 中更新。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.20073_25_ragen-multiturn-agent-rl.md` |
| Reward / feedback | 以 trajectory-level reward 为主，强调缺少 fine-grained reasoning-aware reward 会导致 shallow strategies。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.20073_25_ragen-multiturn-agent-rl.md` |
| Optimizer / update | StarPO / StarPO-S，policy optimization for trajectory-level agent RL。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.20073_25_ragen-multiturn-agent-rl.md` |
| Credit assignment | 偏 trajectory-level；StarPO-S 引入 trajectory filtering、critic incorporation、gradient stabilization。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.20073_25_ragen-multiturn-agent-rl.md` |
| Exploration / replay | diverse initial states、interaction granularity、sampling frequency 是关键设计因素。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.20073_25_ragen-multiturn-agent-rl.md` |
| Warm start / data | 作为初始化存在，但不是本文核心变量。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.20073_25_ragen-multiturn-agent-rl.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: RAGEN 研究 interactive agents 的 multi-turn RL，指出挑战来自 long-horizon decision making 与 stochastic environment feedback。

**事实 [PDF abstract, p.1]**: 论文提出 StarPO，即 State-Thinking-Actions-Reward Policy Optimization，作为 trajectory-level agent RL framework，并实现 RAGEN 训练/评测系统。

**事实 [PDF abstract, p.1]**: 论文报告三个发现：Echo Trap 训练模式导致 reward variability cliffs 和 gradient spikes；多样 initial states、中等 interaction granularity、更频繁 sampling 有利于 rollout shaping；没有 fine-grained reasoning-aware reward 时，agent reasoning 难以从 multi-turn RL 中自然出现。

**解释 [本项目判断]**: 这是 `agentic-rl` 的强机制卡，因为它不是只提出环境或 benchmark，而是在分析 multi-turn RL 的 stability、rollout shaping、reward granularity。

**收录依据 [queue/audit]**: survey 正文提到 + 官方代码/环境 + 明确 multi-turn RL mechanism，走 arXiv exception。代码/环境：`https://github.com/RAGEN-AI/RAGEN`。

## 谱系位置

- 上游：single-turn RLVR / GRPO / reasoning RL。
- 同期：GiGPO、WebRL、Search-R1、Agent Lightning。
- 下游：RAGEN-2、long-horizon agent RL stability / reasoning collapse 方向。

## 优缺点

- ✅ [PDF abstract, p.1]: 明确把问题设定在 interactive agent multi-turn RL，而不是 prompt-only agent。
- ✅ [PDF abstract, p.1]: 给出可复用的 failure mode：Echo Trap、reward variability cliffs、gradient spikes。
- ⚠️ [本项目判断]: stylized environments 可能和真实 web/GUI/code agent 有差距；需要后续用 WebRL/Search-R1/GiGPO 对照。

## Evidence

- paper brief: `_meta/briefs/papers/2504.20073_25_ragen-multiturn-agent-rl.md`
- PDF / HTML: `papers/2504.20073-ragen-multiturn-agent-rl.pdf`
- survey windows: Landscape / GFCR / Credit Assignment
- PDF: `papers/2504.20073-ragen-multiturn-agent-rl.pdf`
- source anchors: abstract p.1; figure 1 p.1; introduction p.1-2。

<!-- pdf: papers/2504.20073-ragen-multiturn-agent-rl.pdf -->

<!-- brief: _meta/briefs/papers/2504.20073_25_ragen-multiturn-agent-rl.md -->

<!-- survey: Landscape / GFCR / Credit Assignment -->
