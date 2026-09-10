---
title: "Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization"
authors: [Zeyuan Liu, Jeonghye Kim, Xufang Luo, et al.]
year: 2026
venue: ICLR 2026
url: https://arxiv.org/abs/2602.23008
arxiv_id: 2602.23008

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: frontier-candidate
data_overlap: false

rl_axes:
  environment: mixed
  interaction_mode: online
  reward_signal: outcome
  optimizer: policy-gradient
  credit_assignment: trajectory
  data_reuse: off-policy
  sft_warm_start: standard
---

## 一句话

用 memory 同时驱动探索和 hybrid on/off-policy update。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | ScienceWorld 和 WebShop multi-step agent tasks。 | 关注需要探索 novel states 的 agent 环境。 | `_meta/briefs/papers/2602.23008_empo2-memory-augmented-agent.md` p.1-p.2 |
| Interaction loop | agent 与环境交互，同时更新 parametric policy 和 non-parametric memory。 | 把 memory 从 inference aid 变成训练期探索机制。 | brief p.2 |
| Reward / feedback | 环境 outcome reward；OOD 时可用少量 trials + memory 适应。 | 强调探索瓶颈而非只拟合已有轨迹。 | brief p.1-p.2 |
| Optimizer / update | EMPO2 结合 with-memory / without-memory rollouts 和 on-policy / off-policy updates。 | 同时让模型会用 memory，也能在无 memory 时保持鲁棒。 | brief p.1-p.2, p.10 |
| Credit assignment | 主要是 trajectory-level RL signal；另有 intrinsic reward 鼓励 novel states。 | 方法重点是 exploration 和 update source，不是 step credit。 | brief p.6, p.10 |
| Exploration / replay | non-parametric memory 鼓励探索，并用 off-policy update 把 memory-guided behavior 写入 policy。 | 针对 GRPO 早停在 suboptimal solution 的问题。 | brief p.1-p.2 |
| Warm start / data | 使用 Qwen2.5-7B-Instruct；project page 为 agent-lightning/empo2。 | 属于可比较的 agent RL training method。 | brief p.1, p.10 |

## 核心增量

**事实 [brief p.1]**: EMPO2 是 hybrid RL framework，使用 memory 做 exploration，并结合 on-policy 与 off-policy updates。

**事实 [brief p.2]**: 框架同时更新 parametric policy parameters 和 non-parametric memory module；包含是否使用 memory 的两种 rollout mode，以及 on/off-policy 两种 update mode。

**事实 [brief p.1-p.2]**: 在 ScienceWorld 和 WebShop 上相对 GRPO 报告 128.6% 和 11.3% improvement，并在 OOD 设置下展示 few trials with memory / no weight update 的适应能力。

**解释 [本项目判断]**: 这是 strict core 的 exploration / memory-augmented RL 分支；与 Reflexion/REMEMBERER 的差异在于参数策略也通过 RL 更新。

## 谱系位置

- 上游：GRPO、Reflexion、REMEMBERER、Retrospex。
- 同期：DynaWeb、RAPO、EDGE。
- 下游：memory-assisted exploration、hybrid on/off-policy agent training。

## 优缺点

- ✅ [brief p.1-p.2]: 直接攻击 LLM agent RL 的 exploration bottleneck。
- ✅ [brief p.10]: 消融强调 on-policy 与 off-policy updates 的互补作用。
- ⚠️ [brief p.10]: memory retrieval 仍是简单 similarity search；更复杂 retrieval 机制可能改变结果。

## Evidence

- paper brief: `_meta/briefs/papers/2602.23008_empo2-memory-augmented-agent.md`
- PDF / HTML: `papers/2602.23008-empo2-memory-augmented-agent.pdf`
- survey windows: post-survey strict-core recall

<!-- pdf: papers/2602.23008-empo2-memory-augmented-agent.pdf -->
<!-- brief: _meta/briefs/papers/2602.23008_empo2-memory-augmented-agent.md -->
<!-- survey: post-survey strict-core recall -->
