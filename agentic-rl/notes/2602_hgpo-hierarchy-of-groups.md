---
title: "Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks"
year: 2026
venue: iclr-2026
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: none

failure_modes: [long-horizon-credit, state-distribution-drift]
design_knobs: [credit-unit, advantage-estimation]

rl_env: mixed
rl_interaction: online
rl_reward: sparse
rl_credit: step
---

## 一句话定位

修正 stepwise group credit 的 history bias。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `long-horizon-credit` | stepwise group-based RL 把当前 state 相似但历史不同的 steps 放在一起，advantage 会 biased。 | 按 historical context consistency 构造 hierarchy-of-groups。 | 需要能比较或切分历史上下文。 |
| `state-distribution-drift` | 长轨迹里历史上下文差异会改变同一当前 state 的真实价值。 | 对多个 hierarchical group 的 advantage 做 adaptive weighting。[PDF abstract] | summarized memory agent 上 raw-history grouping 可能不可行。 |

## 方法机制

HGPO 仍在 GRPO/GiGPO-style group rollout 上做 policy optimization，但不把每个 step 只放入一个 step group。它根据历史上下文一致性为每个 step 构建多个 hierarchical groups，分别估计 advantage，再用 adaptive weighting 聚合。[PDF abstract] 机制增量是 **在 step-level group-relative credit 里显式处理 history/context inconsistency**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | trajectory-level credit 粗。 | 保留 group-based update，但走 stepwise estimator。 | 仍需要 rollout groups。 |
| GiGPO | step group 可能混入历史不同的 contexts。 | 用 hierarchy-of-groups 修正 context inconsistency。 | grouping 规则更复杂。 |
| BEACON | 用 milestone segment anchor。 | HGPO 不需要 milestone detector。 | 依赖可划分的历史上下文。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `credit-unit` | context-aware hierarchical step groups | trajectory / repeated-state step / segment |
| `advantage-estimation` | hierarchical advantages + adaptive weighting | trajectory-only GRPO / GiGPO micro advantage / critic Q |

## 方法优缺点 / 适用边界

- 优势：对 GiGPO 的核心假设做了更细修正，不引入额外模型或 rollouts。
- 优势：作者在 ALFWorld/WebShop 上与 PPO/RLOO/GRPO/GiGPO 对比，报告同计算约束下更好结果。[PDF p.7]
- 不足 / 风险：如果 agent 用 summarized memory 而非 raw divisible history，hierarchical grouping 需要重新设计。[PDF conclusion]

<!-- meta:
authors: [Shuo He, Lang Feng, Qi Wei, et al.]
url: https://arxiv.org/abs/2602.22817
arxiv_id: 2602.22817
pdf: papers/2602.22817-hgpo-hierarchy-of-groups-policy-optimization.pdf
brief: _meta/briefs/papers/2602.22817_hgpo-hierarchy-of-groups-policy-optimization.md
survey: post-survey strict-core recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
