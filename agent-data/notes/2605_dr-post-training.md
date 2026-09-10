---
title: "Dr. Post-Training: A Data Regularization Perspective on LLM Post-Training"
year: 2026
venue: arxiv
paper_type: data-flywheel-method
lifecycle_role: strong-baseline
boundary_risk: alignment

failure_modes: [negative-transfer, difficulty-mismatch, static-data-ceiling]
data_knobs: [negative-transfer-control, coverage-balancing, online-data-flywheel]

agent_domain: general
data_object: replay-buffer
data_source: replay
selection_signal: coverage
adaptivity: iterative
failure_use: replay
training_consumer: sft
---

## 一句话

目标数据与通用数据的正则化视角。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `negative-transfer` | 只追目标 slice 可能过拟合并伤害通用能力。 | general data 作为 update-direction regularizer。 | 哪些 agent data 算 general 仍需项目定义。 |
| `static-data-ceiling` | 固定 target data 稀缺时容易过拟合。 | 每步用 general data 约束 target update。 | 不直接生成新 agent 数据。 |

## 核心做法

Dr. Post-Training 把 post-training data selection 改写成 data regularization：scarce target data 决定想走的更新方向，abundant general data 构造可行更新方向集合，训练时把 target update 投影到 general-data feasible set。[arXiv Abstract] 作者把 standard training 和已有 data selection 视为这个框架下不同 regularization strength 的特例，并放到 bias-variance spectrum 上理解。[Brief] 对本项目，它不是告诉你造什么 agent 轨迹，而是告诉你 narrow bad-case 数据加入后如何防 regression。

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `negative-transfer-control` | general data 约束 target update。 | target-only SFT / 简单混合。 |
| `coverage-balancing` | bias-variance regularization lens。 | 固定数据比例。 |
| `online-data-flywheel` | training-step level update projection。 | 训练前 selection。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| 普通 data selection | 把 general data 当候选池，而非正则信号。 | general data 诱导可行 update set。 | 实现复杂，需读全文确认系统成本。 |

## 谱系位置

- 上游：data selection、RLHF/RLVR post-training。
- 同期：FastMix、bilevel data curation。
- 下游：agent SFT target/general data regularization。

## 和 Agentic RL 的关系

- agentic_rl_overlap: false
- 覆盖 RLHF / RLVR，但本项目只使用 post-training data regularization lens。
- 不登记到 `agentic-rl`。

## 优缺点

- 优势：正好对应你“按 bad case 定向增强，但不能把原能力训坏”的问题。
- 不足 / 风险：需要把 agent benchmark slices 转成 target objective，否则只是抽象优化框架。

<!-- meta:
authors: [Pingbang Hu, et al.]
url: https://arxiv.org/abs/2605.07063
arxiv_id: 2605.07063
pdf:
brief: _meta/briefs/papers/2605.07063_dr-post-training.md
survey: Codex data-flywheel recall
agentic_rl_overlap: false
agentic_rl_queue: none
-->
