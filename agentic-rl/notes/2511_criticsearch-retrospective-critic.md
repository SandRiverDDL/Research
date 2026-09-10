---
title: "CriticSearch: Fine-Grained Credit Assignment for Search Agents via a Retrospective Critic"
year: 2025
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: reasoning

failure_modes: [sparse-delayed-reward, long-horizon-credit, verifier-noise]
design_knobs: [progress-signal, verifier-design, advantage-estimation]

rl_env: tool
rl_interaction: online
rl_reward: verifier
rl_credit: step
---

## 一句话定位

Search agent 的 retrospective critic credit。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `sparse-delayed-reward` | search agent 只靠最终答案 reward，探索效率低且训练不稳定。 | 用 retrospective critic 给 turn-level dense reward。 | critic 质量决定信号可靠性。 |
| `long-horizon-credit` | 多轮检索中间 turn 的贡献被最终 outcome 淹没。 | frozen asymmetric critique LLM 用完整轨迹和 gold answer 回看每个 turn。 | privileged information 训练时可用，部署时不可用。 |
| `verifier-noise` | verifier/critic 可能把错误检索路径评成有效。 | 用 frozen critic 稳定反馈来源。 | 仍可能有 critic bias。 |

## 方法机制

CriticSearch 在 search-agent RL 中加入 retrospective critic：训练时，一个 frozen critique LLM 使用完整 trajectory 和 gold answer 等 privileged information 评价每个 turn，并把评价转成 dense rewards 指导 policy improvement。[paper brief] 机制增量是 **把 outcome-only search RL 改成 critic-labeled turn-level credit**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO / outcome RL | final reward 太稀疏。 | 加 turn-level critic reward。 | 需要额外 critic。 |
| HCAPO | hindsight critic 做 general agent credit。 | CriticSearch 聚焦 search/TIR。 | gold-answer privileged critic 更专用。 |
| IGPO | 用 information gain 做 intrinsic credit。 | 用 retrospective critic 评估 turn。 | critic bias vs metric proxy。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `progress-signal` | retrospective critic turn score | terminal reward / information gain / milestone |
| `verifier-design` | frozen asymmetric critique LLM | rule verifier / PRM / self-critic |
| `advantage-estimation` | dense turn rewards for policy update | trajectory-only GRPO / hindsight Q / segment advantage |

## 方法优缺点 / 适用边界

- 优势：对 search/TIR 的 sparse outcome reward 给出直接 dense turn feedback，适合作为 IGPO/HCAPO 的关键对照。
- 不足 / 风险：边界风险是 reasoning/critic 依赖；使用 gold answer 和完整轨迹的 privileged critic 可能降低通用性。

<!-- meta:
authors: [Yaocheng Zhang, Haohuan Huang, Zijun Song, Yuanheng Zhu, et al.]
url: https://arxiv.org/abs/2511.12159
arxiv_id: 2511.12159
pdf: papers/2511.12159-criticsearch-retrospective-critic.pdf
brief: _meta/briefs/papers/2511.12159_criticsearch-retrospective-critic.md
survey: Credit Assignment survey
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
