---
title: "PilotRL: Training Language Model Agents via Global Planning-Guided Progressive Reinforcement Learning"
year: 2025
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: recipe

failure_modes: [warm-start-ceiling, long-horizon-credit, exploration-collapse]
design_knobs: [warm-start, progress-signal, policy-objective]

rl_env: mixed
rl_interaction: online
rl_reward: sparse
rl_credit: step
---

## 一句话定位

用 global plan curriculum 训练 agent。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `warm-start-ceiling` | SFT 容易记住任务轨迹，泛化到新场景差。 | 用 progressive RL 替代单纯模仿，逐步训练 planning/execution。 | 仍依赖 planner/executor 任务设计。 |
| `long-horizon-credit` | ReAct 的单步 thought-action 难以覆盖长期战略规划。 | AdaPlan 生成并持续更新 global plan，引导执行。 | planning 错误会传递到 execution。 |
| `exploration-collapse` | planner 和 executor 分离会导致计划无法被执行策略吸收。 | 三阶段训练：executor following、planner cultivation、joint optimization。[PDF p.2] | 更像 planning recipe，不是纯 optimizer 改动。 |

## 方法机制

PilotRL 先提出 AdaPlan：同一模型在执行过程中动态生成/更新 global plan，并用该 plan 指导后续 actions。训练上分三阶段推进：先让 executor 学会遵循 global plan，再优化 planner 生成更好计划，最后联合优化 planning-execution coordination。[PDF p.2] 机制增量是 **把 global plan 作为 agent policy 的中间结构，并用 progressive RL curriculum 训练它**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| ReAct | 只做单步 reasoning/action。 | 加 adaptive global plan。 | plan 质量成为瓶颈。 |
| GRPO-style RL | 直接优化完整轨迹。 | 分阶段优化 executor/planner/joint coordination。 | pipeline 更复杂。 |
| INSPO / skill methods | 改 instruction/skill。 | PilotRL 改显式 global plan。 | planning template 泛化需验证。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `warm-start` | progressive RL stages for plan following/planning/joint optimization | SFT-only / single-stage RL |
| `progress-signal` | global plan adherence and task success | terminal reward / milestone / critic |
| `policy-objective` | planning-guided RL objective | trajectory-only GRPO / step credit |

## 方法优缺点 / 适用边界

- 优势：把 long-horizon planning 显式放进 agent RL loop，适合 ALFWorld/Web 等需要全局计划的任务。
- 不足 / 风险：边界风险是 recipe；initial plans 和训练评估依赖 advanced LLMs，作者在 limitations 中也承认可能传播 bias。[PDF p.9]

<!-- meta:
authors: [Keer Lu, Chong Chen, Xili Wang, Bin Cui, et al.]
url: https://arxiv.org/abs/2508.00344
arxiv_id: 2508.00344
pdf: papers/2508.00344-pilotrl-progressive-credit.pdf
brief: _meta/briefs/papers/2508.00344_pilotrl-progressive-credit.md
survey: Credit Assignment survey
rl_optimizer: grpo-like
rl_data_reuse: curriculum
rl_warm_start: standard
-->
