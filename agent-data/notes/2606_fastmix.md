---
title: "FastMix: Fast Data Mixture Optimization via Gradient Descent"
year: 2026
venue: arxiv
paper_type: data-flywheel-method
lifecycle_role: strong-baseline
boundary_risk: alignment

failure_modes: [negative-transfer, coverage-gap, difficulty-mismatch]
data_knobs: [coverage-balancing, online-data-flywheel, negative-transfer-control]

agent_domain: general
data_object: replay-buffer
data_source: synthetic
selection_signal: coverage
adaptivity: iterative
failure_use: replay
training_consumer: sft
---

## 一句话

单 proxy 的数据配比优化。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `negative-transfer` | 手工加数据容易提升一个 slice、拖累另一个 slice。 | 用 validation feedback 更新 mixture ratios。 | validation slice 设计仍由人决定。 |
| `coverage-gap` | 固定比例难覆盖目标能力。 | 把 mixture ratio 作为可优化变量。 | 不告诉你 agent bucket 应该怎么定义。 |

## 核心做法

FastMix 不是 agent data 论文，而是 data mixture optimizer。它把 mixture selection 写成 bilevel optimization，并说明在 uniform source sampling 下，优化 mixture ratios 等价于给每个 source loss 赋权。[arXiv Abstract] 算法在一个 proxy model 内交替更新 model parameters 和 mixture ratios，后者由 validation feedback 驱动。[Brief] 对本项目，它的价值是把“我感觉 M4/M5 数据该多加点”变成可被 benchmark validation slices 驱动的配比问题。

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `coverage-balancing` | validation-driven source weights。 | 手工比例 / grid search。 |
| `online-data-flywheel` | 训练中迭代更新 mixture。 | 训练前一次性定比例。 |
| `negative-transfer-control` | 通过 validation objective 间接约束。 | 只看主 benchmark 均分。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| RegMix / CLIMB | 需要训练很多 proxy models。 | 单 proxy joint optimization。 | 需要可微近似和稳定 validation。 |

## 谱系位置

- 上游：RegMix、CLIMB、DoReMi、data mixing laws。
- 同期：Dr. Post-Training。
- 下游：agent data bucket mixture search。

## 和 Agentic RL 的关系

- agentic_rl_overlap: false
- 这是 SFT / post-training mixture 方法，不是 RL。
- 不需要登记到 `agentic-rl`。

## 优缺点

- 优势：适合你把 M1-M7 failure buckets 变成数据源后做自动配比。
- 不足 / 风险：agent data 的 source 定义、slice validation 和 regression metric 仍是项目内核心工作。

<!-- meta:
authors: [Haoru Tan, et al.]
url: https://arxiv.org/abs/2606.14971
arxiv_id: 2606.14971
pdf:
brief: _meta/briefs/papers/2606.14971_fastmix.md
survey: Codex data-flywheel recall
agentic_rl_overlap: false
agentic_rl_queue: none
-->
