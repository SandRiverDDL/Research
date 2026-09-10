---
title: "Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning"
year: 2025
venue: arxiv
paper_type: core-rl-method
lifecycle_role: background
boundary_risk: reasoning

failure_modes: [long-horizon-credit]
design_knobs: [credit-unit, advantage-estimation]

rl_env: simulated
rl_interaction: offline-rollout
rl_reward: verifier
rl_credit: step
---

## 一句话定位

Reasoning RL 的 hierarchical credit 背景。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `long-horizon-credit` | RL 后模型表现出从低级 procedural correctness 到高级 strategic planning 的学习阶段转移。 | 用 hierarchical reasoning 视角解释 aha、length scaling、entropy dynamics。[paper brief] | 更偏机制解释，不是直接 agent-environment 方法。 |

## 方法机制

HICRA 不是典型 tool/web/GUI agent training method，而是分析 RL 如何诱发 LLM reasoning hierarchy。它把 RL 中出现的 aha moments、length scaling、entropy dynamics 解释为高层规划和低层执行逐步分离的结果。[paper brief] 在本项目里它主要作为 **hierarchical credit / reasoning emergence 背景卡**，用于对照 HGPO、ArCHer、skill/internalization 类方法。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO reasoning RL | 只看最终 reward 改善。 | 分析层级能力如何涌现。 | 不提供通用 agent loop 算法。 |
| HGPO / ArCHer | 明确设计 hierarchy/group。 | HICRA 更偏解释性。 | 证据链不直接迁移到 tool/web agent。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `credit-unit` | hierarchical reasoning level | trajectory / step / segment |
| `advantage-estimation` | 分析 RL 信号如何推动层级能力 | explicit step/group advantage |

## 方法优缺点 / 适用边界

- 优势：提供“RL 学到层级规划/执行分离”的解释框架，可辅助理解 agentic hierarchy 方法。
- 不足 / 风险：不是 strict tool/web agent RL anchor；重写后仍应标为 background，而非 GRPO-family 主比较对象。

<!-- meta:
authors: [Haozhe Wang, Qixin Xu, Che Liu, Junhong Wu, et al.]
url: https://arxiv.org/abs/2509.03646
arxiv_id: 2509.03646
pdf: papers/2509.03646-hicra-hierarchical-credit.pdf
brief: _meta/briefs/papers/2509.03646_hicra-hierarchical-credit.md
survey: Credit Assignment survey
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
