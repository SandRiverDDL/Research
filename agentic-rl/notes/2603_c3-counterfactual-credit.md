---
title: "Exact Is Easier: Credit Assignment for Cooperative LLM Agents"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: background
boundary_risk: reasoning

failure_modes: [long-horizon-credit, sparse-delayed-reward]
design_knobs: [credit-unit, advantage-estimation, rollout-source]

rl_env: mixed
rl_interaction: online
rl_reward: sparse
rl_credit: step
---

## 一句话定位

Cooperative LLM agents 的 exact counterfactual credit。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `long-horizon-credit` | shared terminal reward 难以分辨每个 agent/decision 的贡献。 | fixed-history intervention + alternative action rollout。 | 需要可恢复同一文本历史。 |
| `sparse-delayed-reward` | terminal reward 只在最终 cooperative outcome 给出。 | 用 leave-one-out baseline 得到 per-decision advantage。[paper brief] | Monte Carlo alternatives 增加 rollout cost。 |

## 方法机制

C3 记录 cooperative trajectory 中每个 decision point 的 role 和完整文本历史；训练时恢复该历史，用 frozen behavior policy 采样 alternative actions，并从相同历史继续 rollout 得到 returns。每个 action 的 advantage 用该 action return 减去其他 alternatives 的 leave-one-out baseline。[paper brief] 机制增量是 **用 exact fixed-history counterfactual 替代 learned critic 或 agent-removal counterfactual**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| agent-removal counterfactual | 改变 downstream history，造成 distribution shift。 | 固定历史只干预单个 decision。 | 需要可 checkpoint/恢复历史。 |
| MAPPO / GRPO | shared reward 粗。 | per-decision counterfactual advantage。 | alternative rollout 成本。 |
| HCAPO / critic route | 用 critic 估 credit。 | C3 直接采样 counterfactual returns。 | 适用环境更窄。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `credit-unit` | cooperative decision point | trajectory / agent-level / step |
| `advantage-estimation` | fixed-history counterfactual LOO advantage | learned critic / shared reward baseline |
| `rollout-source` | alternative actions from identical history | agent removal / no counterfactual |

## 方法优缺点 / 适用边界

- 优势：清楚解决 agent-removal counterfactual 的 history distribution shift，credit 信号较干净。
- 不足 / 风险：主要实验是 reasoning/code cooperative protocol，不是典型 web/tool/GUI environment；应作为 multi-agent credit background 而非主 anchor。

<!-- meta:
authors: [Yanjun Chen, Yirong Sun, Hanlin Wang, Jinghan Wang, et al.]
url: https://arxiv.org/abs/2603.06859
arxiv_id: 2603.06859
pdf: papers/2603.06859-c3-counterfactual-credit.pdf
brief: _meta/briefs/papers/2603.06859_c3-counterfactual-credit.md
survey: Credit Assignment survey
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
