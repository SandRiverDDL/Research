---
title: "Self-Distilled Agentic Reinforcement Learning"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: data

failure_modes: [sparse-delayed-reward, process-reward-misalignment, warm-start-ceiling]
design_knobs: [advantage-estimation, credit-unit, warm-start]

rl_env: mixed
rl_interaction: online
rl_reward: outcome
rl_credit: token
---

## 一句话定位

在 GRPO 主干上加 gated on-policy self-distillation。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `sparse-delayed-reward` | 只用 task-level outcome 难以教会中间 token/action。 | 用 privileged-context teacher 分支给 token-level auxiliary signal。 | teacher 信号仍受 context 和 skill 质量限制。 |
| `process-reward-misalignment` | 直接蒸馏 teacher token 可能和最终 reward 不一致。 | 用 positive-gap / negative-gap gate 控制哪些 token 接收 distillation。 | gate 是启发式，不保证 process signal 完全对齐最终成功。 |
| `warm-start-ceiling` | SkillBank 或 privileged context 影响能学到的行为范围。 | on-policy self-distillation 只作为 GRPO 的辅助项。 | 仍不是从无 skill 的纯 RL 探索。 |

## 方法机制

SDAR 保留 GRPO 作为主 objective，并增加 `L = L_GRPO + lambda * L_SDAR` 的 on-policy self-distillation 分支。teacher/privileged-context 产生 token-level guidance，但 token 是否参与辅助损失由 sigmoid gate 决定：正向 gap token 被强化，负向信号被软化，避免把错误过程强行蒸馏进 policy。它不是 replay 方法，rollouts 仍是 on-policy；额外模块主要在同一批 trajectory 上提供 token-level shaping。实验比较 GRPO、GRPO+OPSD、Skill-SD 和 RLSD，任务包括 ALFWorld、WebShop 和 search-QA。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | 只有 outcome/group advantage，token credit 粗。 | 加 gated self-distillation 辅助损失。 | 主信号仍是 sparse outcome。 |
| 直接 self-distillation | teacher token 可能错误或和最终 reward 不一致。 | 用 reward gap gate 控制蒸馏强度。 | gate 设计可能过拟合任务。 |
| Skill-SD / RLSD | distillation 与 RL 信号耦合较弱。 | on-policy rollout 内同时做 GRPO 和 token guidance。 | 需要 privileged context 或 skill source。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `advantage-estimation` | GRPO advantage 仍主导，SDAR 作为 gated auxiliary。 | PPO value baseline、critic、纯 process reward。 |
| `credit-unit` | 辅助信号落在 token level。 | trajectory、step、segment、state credit。 |
| `warm-start` | privileged skill/context 参与 teacher signal。 | 无 teacher、SFT-only、外部 replay。 |

## 方法优缺点 / 适用边界

- 优势：相比纯 GRPO，它明确尝试把 outcome-level reward 转成 token-level learning signal。
- 优势：gating 让 self-distillation 不完全脱离 RL reward。
- 不足 / 风险：依赖 privileged context/SkillBank，仍有 data boundary risk。
- 不足 / 风险：token-level gate 的因果解释弱，可能只是更稳定的辅助监督。

<!-- meta:
authors: [Zhengxi Lu, Zhiyuan Yao, Zhuowen Han, et al.]
url: https://arxiv.org/abs/2605.15155
arxiv_id: 2605.15155
pdf: papers/2605.15155-self-distilled-agentic-rl.pdf
brief: _meta/briefs/papers/2605.15155_sdar-self-distilled-agentic-rl.md
survey: related-work-recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: data-centric
-->
