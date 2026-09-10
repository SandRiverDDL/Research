---
title: "Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models"
year: 2025
venue: arxiv
paper_type: data-flywheel-method
lifecycle_role: strong-baseline
boundary_risk: alignment

failure_modes: [negative-transfer, coverage-gap, difficulty-mismatch]
data_knobs: [coverage-balancing, negative-transfer-control]

agent_domain: general
data_object: replay-buffer
data_source: replay
selection_signal: coverage
adaptivity: static
failure_use: replay
training_consumer: sft
---

## 一句话

SFT 数据配比的 validation-loss 优化。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `coverage-gap` | SFT 多域数据比例影响整体和单域能力。 | 用 validation loss 参数化并求 domain weights。 | agent-specific domain 划分仍需项目定义。 |
| `negative-transfer` | 某域权重过高会让其他域 underperform。 | 优化目标强调 balanced performance。 | 需要可靠 per-domain validation set。 |

## 核心做法

这篇不是 2025Q4 之后，但它是 SFT data mixture 的直接方法锚点。论文指出 pretraining mixture 方法不一定适合 SFT：proxy weights 未必能迁移，且 loss 参数化可能忽略 domain interaction。[arXiv HTML §1] 它把 SFT data mixing 写成固定 token budget 下最小化 validation loss 的优化问题，用 effective data transferred 和 fine-tuning scaling laws 参数化 loss，再求 domain weights。[Brief] 报告中优化权重接近 grid-search optimum，平均 per-domain loss 只比 grid search 的最佳 domain loss 高 0.66%。[Brief]

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `coverage-balancing` | 按 validation loss 求 domain weights。 | 人工比例 / equal mix。 |
| `negative-transfer-control` | balanced per-domain performance。 | 单一主指标。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| pretraining data mixing laws | 不直接适配 SFT 阶段。 | SFT-specific loss parameterization。 | 需小规模混合实验拟合参数。 |

## 谱系位置

- 上游：DoReMi、RegMix、Data Mixing Laws、SMART。
- 同期：bilevel data curation。
- 下游：agent SFT data bucket mixture optimization。

## 和 Agentic RL 的关系

- agentic_rl_overlap: false
- 纯 SFT data mixture 方法。
- 不登记到 `agentic-rl`。

## 优缺点

- 优势：可作为你后续“benchmark 表现 -> 数据配比”的最直接数学 seed。
- 不足 / 风险：不是 agent-specific；如果 validation set 和真实 benchmark 不一致，会优化错方向。

<!-- meta:
authors: [Yuan Li, et al.]
url: https://arxiv.org/abs/2508.11953
arxiv_id: 2508.11953
pdf:
brief: _meta/briefs/papers/2508.11953_data-mixing-optimization-sft.md
survey: Codex data-flywheel recall
agentic_rl_overlap: false
agentic_rl_queue: none
-->
