---
title: "SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: data

failure_modes: [warm-start-ceiling, long-horizon-credit, replay-bias]
design_knobs: [prompt-action-interface, warm-start, trajectory-filtering]

rl_env: mixed
rl_interaction: online
rl_reward: outcome
rl_credit: trajectory
---

## 一句话定位

让 skill library 在 GRPO 训练中递归演化。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `warm-start-ceiling` | 冷启动 agent 很难从 sparse reward 中找到有效行为。 | teacher distillation 建 skill library，并做 cold-start SFT。 | teacher 和 initial SkillBank 质量强影响上限。 |
| `long-horizon-credit` | agent 失败后难以把经验迁移到下一次任务。 | 失败 trajectories 在 validation epoch 触发新 skill 更新。 | policy update 仍主要是 trajectory-level GRPO。 |
| `replay-bias` | 旧 experience distillation 可能和当前 policy 分布不一致。 | 训练中递归更新 skill library，而不是一次性固定。 | skill 更新仍可能累积过时经验。 |

## 方法机制

SkillRL 先通过 teacher / experience-based distillation 构建 hierarchical SkillBank，并用 cold-start SFT 初始化 agent；随后在 GRPO 训练中检索 skills 进入 rollout context，policy 根据 group rollout reward/advantage 更新。每个 validation epoch 中的 failed trajectories 会被用来生成或更新 skills，从而形成 recursive skill-augmented RL loop。论文报告在 ALFWorld、WebShop 和多个 search QA benchmark 上相对 baselines 有提升，并声称 reduced token footprint。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | 直接从环境 reward 学，长任务探索效率低。 | 引入 hierarchical SkillBank 做经验迁移。 | 增益可能来自 teacher/skill distillation。 |
| 静态 skill prompt | skill 不随 policy 失败更新。 | validation failed trajectories 递归更新 skills。 | 维护 skill library 的工程复杂度高。 |
| 后续 D2Skill / SKILL0 | 这些方法进一步细化 utility 或 internalization。 | SkillRL 是较早的 recursive skill-augmented RL anchor。 | credit 粒度较粗。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `prompt-action-interface` | hierarchical skills 作为 rollout prompt context。 | 无 skill、外部 planner、参数内化。 |
| `warm-start` | teacher distillation + cold-start SFT。 | 纯 SFT、无 warm start、self-mined skills。 |
| `trajectory-filtering` | failed validation trajectories 触发 skill evolution。 | 只用成功轨迹、人工筛选、reward gap validation。 |

## 方法优缺点 / 适用边界

- 优势：作为 skill-augmented GRPO 分支的早期 anchor，明确把 skill library 放进 agentic RL loop。
- 优势：recursive update 比一次性 skill prompt 更适合持续任务分布。
- 不足 / 风险：teacher distillation、cold-start SFT 和 skill library 与 RL objective 强耦合，`boundary_risk: data` 高。
- 不足 / 风险：credit 仍然偏 trajectory-level，不能直接解决细粒度 long-horizon credit。

<!-- meta:
authors: [Peng Xia, Jianwen Chen, Hanyang Wang, et al.]
url: https://arxiv.org/abs/2602.08234
arxiv_id: 2602.08234
pdf: papers/2602.08234-skillrl-recursive-skill-augmented-rl.pdf
brief: _meta/briefs/papers/2602.08234_skillrl-recursive-skill-augmented-rl.md
survey: related-work-recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: data-centric
-->
