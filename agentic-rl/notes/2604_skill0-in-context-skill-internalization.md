---
title: "SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: data

failure_modes: [warm-start-ceiling, long-horizon-credit, rollout-cost]
design_knobs: [warm-start, prompt-action-interface, trajectory-filtering]

rl_env: mixed
rl_interaction: online
rl_reward: outcome
rl_credit: trajectory
---

## 一句话定位

训练时给 skill context，再逐步撤掉让 policy internalize。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `warm-start-ceiling` | skill context 能帮助早期探索，但会变成推理依赖。 | training-time in-context skill 加 dynamic curriculum，skill budget 线性降到 0。 | 初始 SkillBank 和离线 grouping 决定可迁移能力。 |
| `long-horizon-credit` | 整条轨迹 reward 很难判断某个 skill 是否帮忙。 | 在 validation sub-task 上比较 with-skill / without-skill helpfulness。 | helpfulness 仍是局部近似，不是细粒度 action credit。 |
| `rollout-cost` | skill 验证和 curriculum 需要额外比较。 | 只保留 compact skill context，并控制在较短 token budget。 | 大任务或长 skill 文件下成本仍可能上升。 |

## 方法机制

SKILL0 在训练 rollout 中给 policy 提供 compact skill context，policy update 采用 GRPO-like in-context agentic RL；推理时则不再检索 skill。Dynamic Curriculum 会在 validation sub-task 上比较 with-skill 和 without-skill 的表现，得到 skill helpfulness `Delta_k`，再据此过滤、排序和选择 skill 文件，并逐步降低 skill budget 到 0。它的目标不是长期依赖 skill memory，而是借 skill 改善探索和早期学习，再把能力内化进 policy。任务包括 ALFWorld、Search-QA 和 WebShop。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | 从 sparse reward 直接探索，早期有效轨迹少。 | 训练时加入 skill context 作为探索 scaffolding。 | 不是纯 objective 改法。 |
| Skill retrieval at inference | 推理依赖外部 skill bank 和额外 tokens。 | 训练中逐步撤掉 skill，推理用原始 prompt。 | 内化是否充分取决于 curriculum。 |
| 固定 skill curriculum | skill 可能过时或无效。 | 用 helpfulness validation 动态筛选。 | validation 本身增加流程复杂度。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `warm-start` | skill context 作为训练期 scaffolding。 | SFT warm start、teacher trajectories、无 skill。 |
| `prompt-action-interface` | skill 以 compact context 进入 prompt。 | 外部 tool wrapper、hidden memory、参数内化后无 context。 |
| `trajectory-filtering` | 用 with/without skill helpfulness 选择训练 skill。 | 静态 skill bank、人工筛选、随机检索。 |

## 方法优缺点 / 适用边界

- 优势：把 skill prompt 的收益和推理成本拆开，适合关心 inference prompt 简洁性的 agent。
- 优势：helpfulness validation 比静态 skill bank 更接近 online training loop。
- 不足 / 风险：核心贡献很大一部分是 skill curriculum，data boundary 高。
- 不足 / 风险：trajectory-level helpfulness 不能解释具体失败步骤。

<!-- meta:
authors: [Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, et al.]
url: https://arxiv.org/abs/2604.02268
arxiv_id: 2604.02268
pdf: papers/2604.02268-skill0-in-context-skill-internalization.pdf
brief: _meta/briefs/papers/2604.02268_skill0-in-context-skill-internalization.md
survey: related-work-recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: data-centric
-->
