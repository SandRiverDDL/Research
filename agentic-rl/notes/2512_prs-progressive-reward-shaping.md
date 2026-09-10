---
title: "Enhancing Agentic RL with Progressive Reward Shaping and Value-based Sampling Policy Optimization"
year: 2025
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: recipe

failure_modes: [sparse-delayed-reward, process-reward-misalignment, rollout-cost]
design_knobs: [reward-shaping, trajectory-filtering, advantage-estimation]

rl_env: tool
rl_interaction: online
rl_reward: dense
rl_credit: step
---

## 一句话定位

PRS reward shaping + VSPO sampling。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `sparse-delayed-reward` | binary verifiable reward 对 intermediate tool steps 指导弱。 | PRS 给 parseable tool call、factual correctness、answer quality 阶段性 dense reward。[PDF abstract] | 阶段 reward 可能偏离最终任务。 |
| `process-reward-misalignment` | dense reward 若设计不好会 reward hacking。 | short-form 用 length-aware BLEU，long-form 用 LLM-as-judge。 | judge/metric 本身仍可能被 game。 |
| `rollout-cost` | GRPO group 内 identical rewards 造成 zero advantage，样本效率低。 | VSPO 用 task-value 选择 prompts，并用 value-smoothing clipping 稳定梯度。 | value metric 是额外 heuristic。 |

## 方法机制

PRS/VSPO 是 TIR agent 的 reward+sampling 组合：PRS 用 curriculum-style dense feedback 先训练可解析/格式正确的 tool calls，再优化事实正确性和答案质量；VSPO 是 GRPO variant，用 value-based sampling 替换 zero-advantage samples，并做 value-smoothing clipping。[PDF abstract] 机制增量是 **把 outcome-only GRPO 改成 stage-wise reward shaping + value-aware sampling**。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| GRPO | identical rewards 导致 zero advantage。 | value-based sampling + smoothing clipping。 | sampling metric 需设计。 |
| binary RLVR | intermediate steps 无指导。 | progressive dense reward。 | process reward 可能 misalign。 |
| CriticSearch / HCAPO | 用 critic 回推 credit。 | PRS 用手工/metric shaping。 | 更轻但更 recipe-like。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `reward-shaping` | stage-wise dense reward | binary outcome / PRM / hindsight critic |
| `trajectory-filtering` | value-based prompt/sample selection | random rollout group / rejection sampling |
| `advantage-estimation` | VSPO stabilizes GRPO zero-advantage cases | vanilla GRPO / critic baseline |

## 方法优缺点 / 适用边界

- 优势：直接处理 TIR agents 的 sparse reward 和 GRPO zero-advantage 问题，适合作为 reward-design 对照。
- 不足 / 风险：边界风险是 recipe；reward shaping 和 value metric 很依赖任务/答案形式。

<!-- meta:
authors: [Jianghao Su, Xia Zeng, Luhui Liu, Chao Luo, et al.]
url: https://arxiv.org/abs/2512.07478
arxiv_id: 2512.07478
pdf: papers/2512.07478-prs-progressive-reward-shaping.pdf
brief: _meta/briefs/papers/2512.07478_prs-progressive-reward-shaping.md
survey: Credit Assignment survey
rl_optimizer: grpo-like
rl_data_reuse: curriculum
rl_warm_start: standard
-->
