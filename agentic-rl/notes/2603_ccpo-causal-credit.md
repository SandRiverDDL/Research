---
title: "Counterfactual Credit Policy Optimization for Multi-Agent Collaboration"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: reasoning

failure_modes: [long-horizon-credit, sparse-delayed-reward, reward-hacking]
design_knobs: [credit-unit, progress-signal, advantage-estimation]

rl_env: mixed
rl_interaction: online
rl_reward: sparse
rl_credit: step
---

## 一句话定位

把 shared outcome 转成 agent-specific credit。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `long-horizon-credit` | multi-agent collaboration 的 shared terminal reward 掩盖个体贡献。 | CCPO 用 agent-removal counterfactual 估 marginal contribution。 | removal 会改变下游互动分布。 |
| `sparse-delayed-reward` | joint outcome 只给最终成败。 | SEPO 用 constrained self/peer evaluation 生成 role-specific credit。 | self/peer credit 可能被操纵。 |
| `reward-hacking` | agents 可能 free-ride 或夸大自身贡献。 | 外部 task outcome 仍保持主导，self-eval 受约束。 | verifier 约束质量关键。 |

## 方法机制

CCPO/SEPO 是 optimizer-agnostic credit construction：CCPO 比较 realized joint outcome 与移除某个 agent 后的 counterfactual outcome，估计该 agent 的 marginal contribution；SEPO 用 constrained self- and peer-evaluations 作为 verifier-anchored credit，同时保持 external task outcome dominant。[paper brief] 机制增量是 **把 shared multi-agent reward 转成 role-specific learning signal**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO / shared reward | free-riding 和 credit 混淆。 | agent-specific counterfactual/self-eval credit。 | counterfactual/eval 可靠性。 |
| C3 | 固定历史 exact counterfactual。 | CCPO 更 general，但 removal 更粗。 | distribution shift 更大。 |
| HCAPO / critic | critic 回推 step Q。 | CCPO 关注 role/agent contribution。 | 偏 multi-agent protocol。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `credit-unit` | agent/role-specific contribution | shared trajectory / decision point / step |
| `progress-signal` | counterfactual marginal contribution + self/peer credit | terminal reward / critic / PRM |
| `advantage-estimation` | optimizer-agnostic credit plugged into GRPO/GSPO/REINFORCE++ | vanilla group advantage |

## 方法优缺点 / 适用边界

- 优势：明确处理 multi-agent free-riding 和 shared reward credit 混淆。
- 不足 / 风险：boundary risk 是 reasoning/multi-agent protocol；agent removal counterfactual 会引入 distribution shift，需和 C3 分开比较。

<!-- meta:
authors: [Zhongyi Li, Wan Tian, Jinju Chen, Huiming Zhang, et al.]
url: https://arxiv.org/abs/2603.21563
arxiv_id: 2603.21563
pdf: papers/2603.21563-ccpo-causal-credit.pdf
brief: _meta/briefs/papers/2603.21563_ccpo-causal-credit.md
survey: Credit Assignment survey
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
