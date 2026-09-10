---
title: "Learning to Explore: Scaling Agentic Reasoning via Exploration-Aware Policy Optimization"
year: 2026
venue: icml-2026
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: data

failure_modes: [exploration-collapse, long-horizon-credit, warm-start-ceiling]
design_knobs: [exploration-strategy, progress-signal, advantage-estimation]

rl_env: mixed
rl_interaction: online
rl_reward: dense
rl_credit: state
---

## 一句话定位

把 exploration actions 和 execution actions 分组训练。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `exploration-collapse` | GRPO 会低估 exploration actions，因为它们不直接完成任务。 | 显式训练 exploration-and-memory reasoning mode。 | exploration/memory 表示仍手工指定。 |
| `long-horizon-credit` | 探索动作和执行动作混在同一 advantage group，不公平。 | 按 state 和 visitation depth 构造 localized transition groups。 | state grouping 质量决定 credit。 |
| `warm-start-ceiling` | agent 需要 rollback/exploration capability 才能训练。 | 先 SFT rollback，再做 exploration-aware GRPO。[paper brief] | 数据阶段依赖强。 |

## 方法机制

EAPO 先用 SFT 教 agent rollback/exploration capability，再用 exploration-aware GRPO 训练 policy：方法用细粒度 reward function 估计 exploration action 对未来决策的价值，并按 environment state / visitation depth 构造 localized transition groups 来计算 advantage。[paper brief] 机制增量是 **把 information-gathering exploration 从普通 execution action 中分离出来建模**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | exploration action 被 outcome reward 低估。 | localized transition groups。 | 需要状态/深度分组。 |
| IGPO / ARPO | search/tool 里的信息增益或 entropy。 | EAPO 覆盖 text + GUI agent exploration。 | 表示设计更重。 |
| EMPO2 | memory-augmented exploration。 | EAPO 显式区分 exploration/execution。 | 需要 rollback SFT。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `exploration-strategy` | uncertainty-triggered exploration + memory reasoning | no exploration / entropy branch / world-model rollout |
| `progress-signal` | fine-grained reward for exploration value | terminal reward / information gain / critic |
| `advantage-estimation` | state/depth localized transition advantage | trajectory GRPO / step group / critic Q |

## 方法优缺点 / 适用边界

- 优势：少数把 exploration 与 execution 明确拆开的 GRPO-family 方法，且覆盖 ALFWorld/WebShop/AndroidWorld/OSWorld。
- 不足 / 风险：boundary risk 是数据/表示；作者承认 exploration / memory representations 仍手工指定。[paper brief]

<!-- meta:
authors: [Xingyuan Hua, Sheng Yue, Ju Ren]
url: https://arxiv.org/abs/2605.08978
arxiv_id: 2605.08978
pdf: papers/2605.08978-eapo-exploration-aware-policy-optimization.pdf
brief: _meta/briefs/papers/2605.08978_eapo-exploration-aware-policy-optimization.md
survey: post-survey strict-core recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: required
-->
