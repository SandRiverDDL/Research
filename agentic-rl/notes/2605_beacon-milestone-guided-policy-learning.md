---
title: "Milestone-Guided Policy Learning for Long-Horizon Language Agents"
year: 2026
venue: icml-2026
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: recipe

failure_modes: [sparse-delayed-reward, long-horizon-credit, rollout-cost]
design_knobs: [credit-unit, progress-signal, advantage-estimation]

rl_env: mixed
rl_interaction: online
rl_reward: sparse
rl_credit: segment
---

## 一句话定位

用 milestone segment 做 long-horizon credit。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `sparse-delayed-reward` | terminal reward 会惩罚失败轨迹里的早期正确动作。 | 用 milestone reward shaping 给 partial progress 正信号。 | milestone 错了，局部奖励也会错。 |
| `long-horizon-credit` | GRPO credit 太粗；GiGPO 的 repeated-state group 在长 horizon 下变弱。 | 用 milestone-matched segment advantage 替代 repeated-state step group。 | 任务必须有可识别 phase / subgoal。 |
| `rollout-cost` | partial success 在 trajectory-level RL 里利用率低。 | 作者报告 effective sample utilization 23.7% -> 82.0%。[PDF abstract] | 指标和 detector 设计绑定，跨环境需重验。 |

## 方法机制

BEACON 假设有 milestone detector `Φ`，能从环境转移中识别 subgoal completion，并据此把 rollout 切成 milestone-bounded segments。它在 segment 内做 temporal reward shaping，再把 segment-level advantage 和 GRPO-style trajectory advantage 组合后更新 policy。[PDF §3.1-3.4, Algorithm 1] 机制增量是 **credit unit 从 trajectory / repeated-state step 改成 milestone segment**，不是新 optimizer。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | trajectory credit 太粗。 | 加 segment-level credit。 | 仍是 on-policy rollout 成本。 |
| GiGPO | repeated-state group 在长任务里可能稀疏。 | 改用 milestone boundary。 | milestone detector 成为关键依赖。 |
| PRM / critic | 需要外部过程评分或 critic。 | 用环境 milestone 生成局部信号。 | 只适合 milestone 可检测的环境。 |
| BC | imitation 不能证明 RL credit 有效。 | 作者用 BC 对照排除纯模仿解释。 | 仍要看 detector 是否带入 oracle-like 知识。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `credit-unit` | milestone segment | trajectory / token / step / repeated-state group |
| `progress-signal` | environment milestone detector | terminal reward / PRM / hindsight critic |
| `advantage-estimation` | segment-level + trajectory-level advantage | trajectory-only GRPO / critic Q / process reward |

## 方法优缺点 / 适用边界

- 优势：segment credit 是清晰 comparison axis，可直接和 GiGPO 的 repeated-state credit、HCAPO 的 hindsight critic credit 对照。
- 优势：作者给出 GRPO/GiGPO/PPO 对比、horizon 分层和 ablation；主表显示 BEACON 在 ALFWorld/WebShop/ScienceWorld 上优于 GRPO/GiGPO。[Table 1]
- 不足 / 风险：最大风险是 milestone detector；作者明确承认需要 domain knowledge 设计 detector。[Appendix D]
- 不足 / 风险：full milestone 明显优于 dropout/random milestone，说明收益上限依赖 detector 质量；当前应视为 frontier candidate，不是 GiGPO 级 anchor。[Table 2]

<!-- meta:
authors: [Zixuan Wang, Yuchen Yan, Hongxing Li, et al.]
url: https://arxiv.org/abs/2605.06078
arxiv_id: 2605.06078
pdf: papers/2605.06078-beacon-milestone-guided-policy-learning.pdf
brief: _meta/briefs/papers/2605.06078_26_beacon-milestone-guided-policy-learning.md
survey: post-survey forward recall
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
