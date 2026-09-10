---
title: "Hindsight Credit Assignment for Long-Horizon LLM Agents"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: reasoning

failure_modes: [sparse-delayed-reward, long-horizon-credit]
design_knobs: [credit-unit, progress-signal, advantage-estimation]

rl_env: mixed
rl_interaction: online
rl_reward: sparse
rl_credit: step
---

## 一句话定位

用 hindsight critic 回推 step Q。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `sparse-delayed-reward` | value-free GRPO-style update 难以给关键中间步骤准确信号。 | 用 LLM post-hoc critic 从完整轨迹和结果回推 step-level Q。 | critic 可能把相关性误判为因果。 |
| `long-horizon-credit` | step Q 估计不准，intermediate-state baseline 和关键决策状态错位。 | 用 hindsight Q + multi-scale advantage 修正局部/全局 credit。[PDF abstract] | 额外 critic pass 带来成本和复现风险。 |

## 方法机制

HCAPO 在 rollout 完成后，让 LLM critic 回看整条 trajectory 和 outcome，估计关键 step 的 hindsight Q-values。然后用 multi-scale advantage 把局部 step credit 和全局 trajectory outcome 结合到 policy update 中。[PDF abstract] 机制增量是 **用 retrospective critic signal 替代 repeated-state/milestone credit anchor**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | trajectory-level signal 无法估 step Q。 | 加 hindsight step Q。 | 依赖 critic 质量。 |
| GiGPO | 依赖 repeated state 构造 step group。 | 不要求 state recurrence。 | 多一次 LLM critic 推理。 |
| BEACON | 依赖 milestone detector。 | 不要求显式 milestone。 | critic bias 可能污染 dense signal。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `progress-signal` | hindsight critic / retrospective Q | terminal reward / milestone / PRM |
| `credit-unit` | critic-labeled step | trajectory / segment / repeated-state group |
| `advantage-estimation` | multi-scale advantage | trajectory-only GRPO / segment advantage / process reward |

## 方法优缺点 / 适用边界

- 优势：不需要 repeated state 或 milestone detector，适合 arbitrary completed trajectory 的 retrospective credit。
- 优势：作者报告 WebShop、ALFWorld 上相对 GRPO 在 Qwen2.5-7B-Instruct 分别提升 7.7% 和 13.8% success rate。[PDF abstract]
- 不足 / 风险：边界风险是 reasoning/critic 依赖；如果 critic 不稳定，policy 会被错误 step credit 牵引。

<!-- meta:
authors: [Hui-Ze Tan, Xiao-Wen Yang, Hao Chen, et al.]
url: https://arxiv.org/abs/2603.08754
arxiv_id: 2603.08754
pdf: papers/2603.08754-hcapo-hindsight-credit.pdf
brief: _meta/briefs/papers/2603.08754_26_hcapo-hindsight-credit.md
survey: Credit Assignment
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
