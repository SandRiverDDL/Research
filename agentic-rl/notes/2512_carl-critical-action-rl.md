---
title: "CARL: Criticality-Aware Agentic Reinforcement Learning"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: none

failure_modes: [sparse-delayed-reward, long-horizon-credit, rollout-cost]
design_knobs: [credit-unit, advantage-estimation]

rl_env: mixed
rl_interaction: online
rl_reward: sparse
rl_credit: step
---

## 一句话定位

只更新 high-criticality agent actions。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `sparse-delayed-reward` | group-level policy optimization 默认每步贡献相同。 | 用 entropy 估计 state criticality，只给关键 action 分配 reward。 | entropy 是否稳定代表 causal criticality 仍需验证。 |
| `long-horizon-credit` | 长轨迹里多数 action 可能与 final outcome 弱相关。 | 只更新 high-criticality states 的 actions。[PDF abstract] | 可能漏掉低熵但长期重要的动作。 |
| `rollout-cost` | 更新所有 actions 会把梯度花在低价值步骤上。 | 作者声称更新动作数减少 72%、性能提升 3.7%。[Figure 1] | 计算收益取决于 criticality selector。 |

## 方法机制

CARL 不构造 step group、milestone 或 critic，而是先判断哪些 state/action choices 对 final outcome 更 critical。论文用 entropy 作为 state criticality 的启发式代理，只对 high-criticality actions 分配 reward 并进入 policy update。[PDF abstract] 机制增量是 **把 credit unit 从所有 steps 缩到 selected critical actions**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | 所有 action 共享 group-level signal。 | 只更新 critical actions。 | selector 错误会漏 credit。 |
| GiGPO | 依赖 repeated-state step group。 | 不要求 state recurrence。 | entropy proxy 可能偏。 |
| BEACON | 依赖 milestone boundary。 | 不需要显式 subgoal。 | criticality 不等于 progress。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `credit-unit` | high-criticality action subset | all trajectory actions / step group / segment |
| `advantage-estimation` | entropy-gated action update | trajectory advantage / segment advantage / critic Q |

## 方法优缺点 / 适用边界

- 优势：提供了和 GiGPO/BEACON 正交的 credit 路线：不是重估所有 step，而是选择哪些 step 接收梯度。
- 优势：若 criticality proxy 可靠，可以同时减少 noisy update 和训练开销。
- 不足 / 风险：当前最大不确定性是 entropy proxy；criticality 是启发式，不等于真实因果贡献。

<!-- meta:
authors: [Leyang Shen, Yang Zhang, Chun Kai Ling, Xiaoyan Zhao, Tat-Seng Chua]
url: https://arxiv.org/abs/2512.04949
arxiv_id: 2512.04949
pdf: papers/2512.04949-carl-critical-action-rl.pdf
brief: _meta/briefs/papers/2512.04949_26_carl-critical-action-rl.md
survey: Credit Assignment
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
