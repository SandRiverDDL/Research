---
title: "APPO: Agentic Procedural Policy Optimization"
year: 2026
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: none

failure_modes: [long-horizon-credit, exploration-collapse, rollout-cost]
design_knobs: [rollout-source, credit-unit, advantage-estimation]

rl_env: tool
rl_interaction: online
rl_reward: outcome
rl_credit: segment
---

## 一句话定位

用 procedure-level branching 做 agent credit。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `long-horizon-credit` | tool-call boundary 或 fixed workflow 过粗，关键决策散落在 generated sequence。 | 用 procedure-level advantage scaling。 | procedure boundary 仍需可靠识别。 |
| `exploration-collapse` | token entropy alone 不可靠，可能选到 spurious high-entropy positions。 | Branching Score 结合 token uncertainty 和 continuation likelihood gain。 | score 仍是 heuristic。 |
| `rollout-cost` | 全量 tree/branch rollout 成本高。 | 选择 high-value branching locations。 | 分支覆盖不足会漏关键路径。 |

## 方法机制

APPO 继承 ARPO/Tree-GRPO 的 branching rollout 思路，但批评 tool-call / turn boundary 太粗。它用 Branching Score 选择 generated sequence 中真正影响后续的 branching locations，再用 procedure-level advantage scaling 更新 policy。[paper brief] 机制增量是 **把 branching 和 credit unit 从 tool-call/turn 推进到 procedure 粒度**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| ARPO | 用 entropy 触发 branching。 | 加 continuation likelihood gain 过滤 spurious entropy。 | score 更复杂。 |
| Tree-GRPO | tree node 多按 step 展开。 | 改成 procedure-level branching。 | boundary 定义更细。 |
| StepPO | step-level action MDP。 | APPO 更关注 procedure/branch location。 | 不是通用 step abstraction。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `rollout-source` | selected procedure branching | full trajectory / tree search / entropy-only branch |
| `credit-unit` | procedure segment | trajectory / turn / tool-call / token |
| `advantage-estimation` | procedure-level advantage scaling | trajectory GRPO / step advantage / critic Q |

## 方法优缺点 / 适用边界

- 优势：直接接在 ARPO/Tree-GRPO 之后，细化 branching location 与 credit granularity。
- 不足 / 风险：非常新，venue 和社区影响力未稳定；procedure boundary/score 可能成为实现敏感点。

<!-- meta:
authors: [Xucong Wang, Ziyu Ma, Yong Wang, et al.]
url: https://arxiv.org/abs/2606.12384
arxiv_id: 2606.12384
pdf: papers/2606.12384-appo-agentic-procedural-policy-optimization.pdf
brief: _meta/briefs/papers/2606.12384_appo-agentic-procedural-policy-optimization.md
survey: post-survey strict-core recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
