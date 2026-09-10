---
title: "ReSkill: Reconciling Skill Creation with Policy Optimization in Agentic RL"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: data

failure_modes: [warm-start-ceiling, exploration-collapse, replay-bias]
design_knobs: [prompt-action-interface, trajectory-filtering, exploration-strategy]

rl_env: mixed
rl_interaction: online
rl_reward: outcome
rl_credit: trajectory
---

## 一句话定位

把 skill creation 放进 GRPO group 内做受控测试。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `warm-start-ceiling` | 静态 skill 或 SFT 轨迹会限制 agent 后续探索。 | 训练时持续生成、测试和更新 skills。 | skill creator 本身仍是强外部模块。 |
| `exploration-collapse` | policy 可能只复用早期有效 skill。 | Thompson Sampling with adaptive discounting 在 skill versions 间探索。 | exploration 主要发生在 skill space，不一定解决 action space 探索。 |
| `replay-bias` | 旧 skill 可能来自过时 policy 或旧状态分布。 | 在当前 GRPO rollout group 内测试 skill version。 | 接受/拒绝仍依赖有限 group sample。 |

## 方法机制

ReSkill 把不同 skill version 分配到同一任务、同一 policy 的 GRPO rollout group 中，直接用组内 outcome reward 比较 skill 对当前 policy 的帮助。policy update 仍使用 GRPO 的 group-normalized trajectory advantage；skill update 则把失败诊断、skill version acceptance 和 bandit posterior 结合起来。关键点是 skill creation 不再是离线预处理，而是和 policy optimization 同步运行，且声称不增加额外 rollout budget。实验覆盖 ALFWorld、agentic search、InterCode-SQL、WANDS 和 ScienceWorld。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | 只更新 policy，不主动更新 skill context。 | group 内同时比较 skill version 和更新 policy。 | 方法边界混合了 RL 与 data/skill generation。 |
| SkillRL / SKILL0 | skill 生成和 policy 优化相对分离。 | 把 skill testing 嵌入每个 rollout group。 | 对 skill creator 质量敏感。 |
| 静态 skill memory | skill 是否适配当前 policy 不确定。 | 用当前 rollout reward 作为 skill acceptance 信号。 | group sample 小时判断噪声高。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `prompt-action-interface` | skill version 作为 context 条件进入 rollout。 | 不用 skill、固定 skill、把 skill 蒸馏到模型参数。 |
| `trajectory-filtering` | 当前 group reward 决定 skill version 接受和淘汰。 | 离线筛选、人工规则、teacher 过滤。 |
| `exploration-strategy` | Thompson Sampling 在 skill versions 间分配试验机会。 | 随机检索、UCB、epsilon-greedy、无探索机制。 |

## 方法优缺点 / 适用边界

- 优势：把 skill 是否有用的判断放回当前 on-policy RL loop，比离线 skill selection 更贴近 agentic RL。
- 优势：组内对照减少任务难度差异，是 skill-family 方法里比较清晰的实验设计。
- 不足 / 风险：核心创新部分是 skill 生成和选择，作为 core RL method 时需要标 `boundary_risk: data`。
- 不足 / 风险：如果 skill creator 或诊断器弱，policy update 本身没有提供新的 credit mechanism。

<!-- meta:
authors: [Zelin He, Haotian Lin, Boran Han, et al.]
url: https://arxiv.org/abs/2606.01619
arxiv_id: 2606.01619
pdf: papers/2606.01619-reskill-policy-skill-coevolution.pdf
brief: _meta/briefs/papers/2606.01619_reskill-policy-skill-coevolution.md
survey: related-work-recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: data-centric
-->
