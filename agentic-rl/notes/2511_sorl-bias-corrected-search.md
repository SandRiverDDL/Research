---
title: "Stabilizing Off-Policy Training for Long-Horizon LLM Agent via Turn-Level Importance Sampling and Clipping-Triggered Normalization"
year: 2025
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: none

failure_modes: [offline-online-gap, replay-bias, long-horizon-credit]
design_knobs: [replay-off-policy, advantage-estimation, credit-unit]

rl_env: tool
rl_interaction: replay
rl_reward: outcome
rl_credit: step
---

## 一句话定位

稳定 off-policy long-horizon agent RL。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `offline-online-gap` | off-policy pipelines 中 PPO/GRPO 优化不稳定，容易 collapse。 | turn-level importance sampling 修正行为策略和当前策略差异。 | IS 仍可能高方差。 |
| `replay-bias` | 旧 trajectories 被重复使用会放大 biased gradients。 | clipping-triggered normalization 稳定梯度尺度。 | replay 数据质量仍影响上限。 |
| `long-horizon-credit` | token-level optimization 和 turn-structured interaction 粒度不匹配。 | 在 turn level 做 correction / credit。[paper brief] | 不是新的 progress signal。 |

## 方法机制

SORL 面向 long-horizon LLM agent 的 off-policy training：它指出 token-level policy optimization 与 turn-structured interaction 不匹配，同时 off-policy importance sampling 会带来高方差和不可靠 gradient。方法用 turn-level IS 和 clipping-triggered normalization 稳定 GRPO-like update。[paper brief] 机制增量是 **把 replay/off-policy agent RL 的 correction 粒度提升到 turn level**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| on-policy GRPO | 数据利用率低。 | 允许 replay/off-policy reuse。 | 需要 correction。 |
| vanilla off-policy PPO/GRPO | IS 方差和 clipping 不稳定。 | turn-level IS + clipping normalization。 | 实现更复杂。 |
| StepPO | 对齐 step/action 粒度。 | SORL 对齐 off-policy correction 粒度。 | 不直接改 reward。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `replay-off-policy` | off-policy agent training with turn-level IS | pure on-policy / replay without correction |
| `credit-unit` | turn-level correction | token-level ratio / trajectory-level ratio |
| `advantage-estimation` | clipping-triggered normalization | vanilla GRPO advantage / critic baseline |

## 方法优缺点 / 适用边界

- 优势：是少数直接处理 long-horizon agent off-policy stability 的 GRPO-family 方法。
- 不足 / 风险：主要解决 optimization stability，不提供新的 reward/progress signal；效果依赖 replay 分布和 IS 估计。

<!-- meta:
authors: [Chenliang Li, Adel Elmahdy, Alex Boyd, Zhongruo Wang, et al.]
url: https://arxiv.org/abs/2511.20718
arxiv_id: 2511.20718
pdf: papers/2511.20718-sorl-bias-corrected-search.pdf
brief: _meta/briefs/papers/2511.20718_sorl-bias-corrected-search.md
survey: Credit Assignment survey
rl_optimizer: grpo-like
rl_data_reuse: off-policy
rl_warm_start: standard
-->
