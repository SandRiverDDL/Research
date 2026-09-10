---
title: "DynaWeb: Model-Based Reinforcement Learning of Web Agents"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: data

failure_modes: [rollout-cost, offline-online-gap, environment-overfitting]
design_knobs: [rollout-source, environment-interface, replay-off-policy]

rl_env: web
rl_interaction: online
rl_reward: outcome
rl_credit: trajectory
---

## 一句话定位

用 web world model 生成 RL rollouts。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `rollout-cost` | live web online RL 成本高、风险大、不可控。 | 训练 web world model 生成 imagined rollouts。 | world model hallucination 会污染训练。 |
| `offline-online-gap` | 纯 expert/SFT trajectories 覆盖不足。 | synthetic trajectories 与 real expert trajectories 混合训练。 | WWM coverage 决定泛化。 |
| `environment-overfitting` | web benchmarks 状态空间变化大。 | 用 learned next-state model 扩展 experience source。[paper brief] | 模型可能过拟合训练网站分布。 |

## 方法机制

DynaWeb 训练 web world model 预测 action 后网页状态，并让 policy 在 synthetic web environment 中生成 multi-step trajectories；训练时还混入 expert trajectories 来提升稳定性和 sample efficiency。[paper brief] 机制增量是 **把 learned world model 作为 web-agent RL 的 rollout generator**，而不是只做 inference-time lookahead。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| online WebRL | 真实网页交互贵且不稳定。 | 用 WWM imagined rollout。 | model error。 |
| SFT / expert data | 只模仿已有轨迹。 | world-model-grounded policy optimization。 | data/world-model 依赖强。 |
| inference-time planning | 只在测试时 lookahead。 | 用 imagined rollout 训练 policy。 | 训练复杂度更高。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `rollout-source` | web world model imagined trajectories | live web rollout / expert trajectories / replay |
| `environment-interface` | learned next-state web simulator | browser environment / static dataset |
| `replay-off-policy` | mix synthetic rollouts with expert trajectories | pure on-policy / pure SFT |

## 方法优缺点 / 适用边界

- 优势：代表 model-based web agent RL 分支，直接针对 live web interaction 的成本和可控性。
- 不足 / 风险：boundary risk 是 data/world-model；policy 质量强依赖 WWM fidelity 和 training coverage。

<!-- meta:
authors: [Hang Ding, Peidong Liu, Junqiao Wang, et al.]
url: https://arxiv.org/abs/2601.22149
arxiv_id: 2601.22149
pdf: papers/2601.22149-dynaweb-model-based-web-agent-rl.pdf
brief: _meta/briefs/papers/2601.22149_dynaweb-model-based-web-agent-rl.md
survey: post-survey strict-core recall
rl_optimizer: grpo-like
rl_data_reuse: off-policy
rl_warm_start: standard
-->
