---
title: "Dynamic Dual-Granularity Skill Bank for Agentic RL"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: data

failure_modes: [warm-start-ceiling, long-horizon-credit, exploration-collapse]
design_knobs: [progress-signal, credit-unit, prompt-action-interface]

rl_env: mixed
rl_interaction: online
rl_reward: outcome
rl_credit: step
---

## 一句话定位

用 task/step 双粒度 skill utility 改进 GRPO agent 训练。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `warm-start-ceiling` | skill bank 能显著改变早期探索和上限。 | 训练中动态维护 task-level 和 step-level skills。 | 最强设定依赖外部 reflector，和 data mechanism 边界强。 |
| `long-horizon-credit` | 只看整条轨迹成功很难知道哪个 skill 有用。 | 用 paired baseline / skill-injected rollouts 的差值估计 hindsight utility。 | utility 仍是 rollout-level 对比，非严格因果 credit。 |
| `exploration-collapse` | 已有 skills 可能被过早固定或反复使用。 | retrieval 加 UCB-style bonus，低使用 skill 有额外探索机会。 | 探索收益和 skill bank 膨胀需要 pruning 平衡。 |

## 方法机制

D2Skill 在同一任务上跑 baseline rollout 和 skill-injected rollout，用两者 performance gap 估计 skill 的 hindsight utility，再把 task skill 和 step skill 写回 skill bank。训练主干仍是 GRPO，区别是 rollout prompt 会检索双粒度 skill，policy 在 skill-augmented context 下更新；skill bank 则通过 reflection、utility-aware pruning 和 UCB-style retrieval bonus 持续变化。实验覆盖 ALFWorld、WebShop 和 search-augmented QA，作者报告训练成本接近 GRPO、快于 SkillRL，并开源代码。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | 没有跨任务经验迁移，稀疏 reward 下探索慢。 | 把可检索 skill 放进 rollout context。 | 容易把 data/skill 工程误读成纯 RL objective 改动。 |
| SkillRL | skill library 演化较粗，且训练成本更高。 | 细分 task-level / step-level skill，并用 paired utility 做更新。 | paired rollout 增加评估和维护复杂度。 |
| 普通 skill retrieval | 只检索经验，不判断 skill 是否真实有用。 | 用 hindsight utility 和 pruning 控制 skill 生命周期。 | utility 信号受 rollout 随机性影响。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `progress-signal` | 用 skill-injected 相对 baseline 的 reward gap 表示 skill progress。 | terminal success、process reward、milestone reward。 |
| `credit-unit` | 同时维护 task-level 和 step-level skill credit。 | trajectory-only、token-level、state-level credit。 |
| `prompt-action-interface` | skill 作为 prompt/context 进入 policy rollout。 | 不提供 skill、把 skill 蒸馏进参数、tool API 层封装。 |

## 方法优缺点 / 适用边界

- 优势：把 skill retrieval、utility 估计和 GRPO 更新放进同一个 online loop，适合多任务 agent benchmark。
- 优势：step-level skill 让它比纯 trajectory-level skill memory 更接近 credit assignment 问题。
- 不足 / 风险：核心增益可能来自 skill bank 和 reflector，`boundary_risk: data` 高；作为 GRPO-family comparison 时应单独标注。
- 不足 / 风险：paired utility 不是无偏因果估计，且需要额外 rollout 对照。

<!-- meta:
authors: [Songjun Tu, Chengdong Xu, Qichao Zhang, et al.]
url: https://arxiv.org/abs/2603.28716
arxiv_id: 2603.28716
pdf: papers/2603.28716-d2skill-dual-granularity-skill-bank.pdf
brief: _meta/briefs/papers/2603.28716_d2skill-dual-granularity-skill-bank.md
survey: related-work-recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: data-centric
-->
