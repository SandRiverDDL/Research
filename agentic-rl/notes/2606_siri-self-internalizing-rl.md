---
title: "SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: data

failure_modes: [warm-start-ceiling, long-horizon-credit, replay-bias]
design_knobs: [progress-signal, credit-unit, warm-start]

rl_env: mixed
rl_interaction: online
rl_reward: outcome
rl_credit: step
---

## 一句话定位

用 RL credit 筛选并内化 self-mined skills。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `warm-start-ceiling` | 初始 policy 太弱时，自己挖到的 skill 质量低。 | 先用 GiGPO warm-up，再从成功 skill-free trajectories 挖 skill。 | warm-up 质量仍决定后续 internalization 上限。 |
| `long-horizon-credit` | 只知道整条轨迹成功，不知道 skill 或 action 是否该吸收。 | paired skill-augmented / skill-free rollouts 估计 skill utility，再用 action-level advantage gate。 | action-level gate 仍依赖粗粒度 rollout 对照。 |
| `replay-bias` | 直接从成功轨迹挖 skill 可能固化偶然行为。 | validation 后只内化 beneficial skill-guided action tokens。 | 成功轨迹覆盖不足时仍会偏向已有行为模式。 |

## 方法机制

SIRI 分三步：先用 GiGPO 做 warm-up，收集成功的 skill-free trajectories；再从这些轨迹中 self-mine skills，并用 paired skill-augmented vs skill-free rollouts 估计 skill utility；最后只把有正 utility 的 skill-guided action tokens 内化到普通 policy。RL 主干仍是 GRPO/GiGPO-like agentic optimization，但本文重点是把外显 skill 变成 inference-time 不需要 skill bank 的参数化能力。实验覆盖 ALFWorld 和 WebShop，并报告相对 GiGPO 的提升。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GiGPO | 能训练 agent，但不显式抽取和内化 skills。 | 用 GiGPO warm-up 后做 skill mining / validation / internalization。 | 如果 GiGPO 初始探索弱，后续 skill 也弱。 |
| Skill retrieval 方法 | inference 依赖外部 skill bank 或 prompt context。 | 训练后回到原始 prompt，不需要 skill bank。 | 内化过程可能丢失可解释 skill memory。 |
| 普通成功轨迹蒸馏 | 无法区分哪些 action 真有用。 | 用 paired utility 和 action-level advantage 筛选 token/action。 | credit 仍是近似估计。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `progress-signal` | skill-augmented 相对 skill-free rollout 的 utility gap。 | terminal reward、process reward、LLM judge。 |
| `credit-unit` | trajectory-level skill utility 加 action-level advantage gate。 | trajectory-only、token-only、step-only。 |
| `warm-start` | GiGPO warm-up 后再挖 skill。 | 从 SFT 直接挖、teacher distillation、无 warm-up。 |

## 方法优缺点 / 适用边界

- 优势：解决 skill-family 方法常见的 inference-time skill bank 依赖，把 skill 转成模型内部能力。
- 优势：paired validation 让 skill internalization 不只是成功轨迹蒸馏。
- 不足 / 风险：核心依赖 self-mined skill 数据，`boundary_risk: data` 明显。
- 不足 / 风险：如果 warm-up policy 的探索范围窄，internalized skill 会继承这个 ceiling。

<!-- meta:
authors: [Zhongyu He, Yuanfan Li, Fei Huang, et al.]
url: https://arxiv.org/abs/2606.02355
arxiv_id: 2606.02355
pdf: papers/2606.02355-siri-self-internalizing-rl.pdf
brief: _meta/briefs/papers/2606.02355_siri-self-internalizing-rl.md
survey: related-work-recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: data-centric
-->
