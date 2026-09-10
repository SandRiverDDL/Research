---
title: "Agentic Reinforced Policy Optimization"
year: 2025
venue: iclr-2026
paper_type: core-rl-method
lifecycle_role: canonical-anchor
boundary_risk: none

failure_modes: [sparse-delayed-reward, rollout-cost, exploration-collapse]
design_knobs: [rollout-source, exploration-strategy, advantage-estimation]

rl_env: tool
rl_interaction: online
rl_reward: outcome
rl_credit: step
---

## 一句话定位

用 entropy 触发 tool-step branching。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `exploration-collapse` | tool feedback 后 token entropy 升高，但 trajectory-level RL 不专门探索这些不确定步骤。 | 在 high-entropy tool-call rounds 做 partial sampling。 | 高熵可能是噪声，不一定是有价值探索。 |
| `rollout-cost` | 完整 trajectory sampling 工具调用成本高。 | 混合 global sampling 和 step-level partial sampling，作者称只需约一半 tool-use budget。[PDF abstract] | budget 节省依赖 entropy trigger。 |
| `sparse-delayed-reward` | final outcome reward 难以归因到具体 tool-use step。 | Advantage Attribution Estimation 学习 stepwise tool-use advantage differences。 | step credit 仍来自 outcome 传播。 |

## 方法机制

ARPO 面向 multi-turn tool-use agents：先做 global trajectory sampling，同时监控 tool feedback 后 token entropy；当 entropy change 超过阈值时，在该 step 追加 partial sampling 以扩展局部行为。[PDF p.2-p.3] 它再用 Advantage Attribution Estimation 把这些分支行为的优劣转成 stepwise tool-use credit。机制增量是 **把 rollout budget 从均匀完整轨迹改成 high-entropy tool step 的自适应分支**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO / trajectory RL | 只比较完整 trajectories。 | 在高熵 tool step 局部分支采样。 | entropy 阈值成为关键超参。 |
| GiGPO | 关注 state/action credit。 | ARPO 更关注 rollout allocation。 | credit 机制相对粗。 |
| Tree-GRPO / AT^2PO | 用树搜索扩展决策。 | ARPO 用 entropy 选择扩展点。 | 搜索深度/广度较受 heuristic 限制。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `rollout-source` | global trajectory + high-entropy partial rollout | full trajectory group / tree search / replay |
| `exploration-strategy` | entropy-triggered branching after tool feedback | random sampling / beam/tree expansion / uncertainty critic |
| `advantage-estimation` | stepwise tool-use advantage attribution | trajectory-only GRPO / critic Q / process reward |

## 方法优缺点 / 适用边界

- 优势：直接针对 tool-use agent 的交互结构，适合 deep search / tool QA 这类工具反馈改变后续策略的任务。
- 优势：作者在 13 个 computational/knowledge/deep search benchmarks 上报告优于 trajectory-level RL。[PDF abstract]
- 不足 / 风险：entropy trigger 是否稳定区分“有价值探索”和“模型困惑”是核心不确定性。

<!-- meta:
authors: [Guanting Dong, Hangyu Mao, Kai Ma, et al.]
url: https://arxiv.org/abs/2507.19849
arxiv_id: 2507.19849
pdf: papers/2507.19849-arpo-agentic-reinforced-policy-optimization.pdf
brief: _meta/briefs/papers/2507.19849_arpo-agentic-reinforced-policy-optimization.md
survey: post-survey strict-core recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
