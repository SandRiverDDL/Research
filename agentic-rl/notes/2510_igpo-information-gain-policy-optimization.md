---
title: "Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn Search Agents"
year: 2025
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: none

failure_modes: [sparse-delayed-reward, long-horizon-credit, rollout-cost]
design_knobs: [progress-signal, reward-shaping, advantage-estimation]

rl_env: tool
rl_interaction: online
rl_reward: outcome
rl_credit: step
---

## 一句话定位

用 information gain 给 search turns 做 credit。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `sparse-delayed-reward` | multi-turn search 只在最终答案给 reward。 | 用每个 turn 对成功概率的增量作为 dense intrinsic signal。 | information gain proxy 未必等于真实 causality。 |
| `long-horizon-credit` | intermediate retrieval/reasoning turns 的贡献被最终 outcome 淹没。 | 把 turn-level information gain 接入 policy optimization。[paper brief] | 长轨迹中 noisy retrieval 可能被误奖。 |
| `rollout-cost` | 每条 rollout 只有一个 outcome signal，样本利用率低。 | 从同一 trajectory 里抽取多个 turn-level learning signals。 | 额外评估/估计成功概率可能有成本。 |

## 方法机制

IGPO 面向 multi-turn search agents，把“每个 turn 带来的信息增益”作为过程信号：如果某个 search/reasoning turn 提高后续成功概率，就给它更高 credit。[paper brief] 机制增量是 **把 final answer reward 扩展成 turn-level progress signal**，从而缓解 outcome-only GRPO 在 search setting 的 advantage collapse 和 credit 粗糙。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO / Search-R1 | final answer reward 太稀疏。 | 加 information-gain turn credit。 | proxy 质量决定收益。 |
| CriticSearch | 用 retrospective critic。 | IGPO 用信息增益 proxy。 | 少 critic 但可能更粗。 |
| ARPO | 用 entropy 决定探索位置。 | IGPO 用 progress/information signal 做 credit。 | 不直接解决 rollout branching。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `progress-signal` | turn-level information gain | terminal reward / critic / milestone |
| `reward-shaping` | dense intrinsic supervision for search turns | process reward / hindsight Q / verifier-only |
| `advantage-estimation` | information-gain shaped advantage | trajectory-only GRPO / critic advantage |

## 方法优缺点 / 适用边界

- 优势：对 search agent 的多轮知识获取过程给出轻量 progress signal，和 CriticSearch/HCAPO 构成天然对照。
- 不足 / 风险：information gain 是 proxy；如果检索带来信息但不服务最终答案，reward shaping 可能偏离目标。

<!-- meta:
authors: [Guoqing Wang, Sunhao Dai, Guangze Ye, Zeyu Gan, et al.]
url: https://arxiv.org/abs/2510.14967
arxiv_id: 2510.14967
pdf: papers/2510.14967-igpo-information-gain-policy-optimization.pdf
brief: _meta/briefs/papers/2510.14967_igpo-information-gain-policy-optimization.md
survey: Credit Assignment survey
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
