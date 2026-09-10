---
title: "Co-Evolving Skill Generation and Policy Optimization"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: data

failure_modes: [warm-start-ceiling, replay-bias, long-horizon-credit]
design_knobs: [trajectory-filtering, progress-signal, prompt-action-interface]

rl_env: mixed
rl_interaction: online
rl_reward: outcome
rl_credit: trajectory
---

## 一句话定位

用 matched rollouts 验证 skill，再训练 policy 生成 skill。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `warm-start-ceiling` | 初始 skill bank 决定早期学习质量。 | 从已有 SkillRL-style skill bank 起步，并让 policy 学会生成 skill。 | 仍依赖初始 skill bank 和 skill 表达质量。 |
| `replay-bias` | 直接存储生成 skill 会把错误经验放大。 | skill 入库前做 base / skill-augmented matched rollout 验证。 | matched validation 成本和噪声仍存在。 |
| `long-horizon-credit` | 任务成功难以归因到哪个 skill。 | 用 reward gap 估计 skill-level marginal utility。 | credit 粒度主要是 skill/trajectory，不解释单步错误。 |

## 方法机制

SAPO 在同一任务和检索 context 下生成 base rollouts 与 skill-augmented rollouts，用两者 reward gap 作为 skill utility。这个 utility 同时用于 skill admission、reranking/pruning，以及训练 policy 直接生成 skill；policy optimization 仍是 GRPO-like agentic RL loop。和只检索外部 skill 不同，SAPO 试图让 policy 与 skill generator 共演化，但它的关键信号仍来自 matched rollout 对照。实验覆盖 ALFWorld、WebShop 和 search-augmented QA，并和 SkillRL、SKILL0、D2Skill、MemRL 对比。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | 没有显式 skill generation 或 skill validation。 | 在 RL loop 中加入 skill utility 和 policy-as-skill-generator。 | RL objective 和 skill data pipeline 边界不干净。 |
| SkillRL / SKILL0 | skill 多作为外部 context 或 curriculum。 | 用 matched rollout 先验证 skill，再让 policy 生成 skill。 | 强依赖 matched 对照质量。 |
| D2Skill | 也用 skill utility，但重点在双粒度 skill bank。 | 更强调 skill generation 与 policy optimization 共演化。 | 可能把 skill 工程复杂度转嫁给训练流程。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `trajectory-filtering` | skill 入库前用 matched rollout reward gap 过滤。 | 直接存储、人工规则、LLM judge 筛选。 |
| `progress-signal` | skill-augmented 相对 base rollout 的 reward gap。 | terminal success、dense process reward、milestone completion。 |
| `prompt-action-interface` | skill 既作为 context，也成为 policy 要生成的对象。 | 只检索 skill、无 skill、外部 planner 生成 skill。 |

## 方法优缺点 / 适用边界

- 优势：把 skill 生成的质量控制显式接到 RL outcome 上，避免只靠语言描述判断 skill。
- 优势：matched rollout 让 skill utility 比普通成功轨迹挖掘更可比较。
- 不足 / 风险：这是 data/skill-heavy 的 core method，不能和纯 objective 改法直接同表比较。
- 不足 / 风险：reward gap 是粗粒度 skill-level 信号，对长轨迹内部 credit 仍弱。

<!-- meta:
authors: [Zhiwei Zhang, Yudi Lin, Nikki Kuang, et al.]
url: https://arxiv.org/abs/2606.08755
arxiv_id: 2606.08755
pdf: papers/2606.08755-sapo-skill-generation-policy-optimization.pdf
brief: _meta/briefs/papers/2606.08755_sapo-skill-generation-policy-optimization.md
survey: related-work-recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: data-centric
-->
