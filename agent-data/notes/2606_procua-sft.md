---
title: "ProCUA-SFT Technical Report"
year: 2026
venue: arxiv
paper_type: synthetic-verifiable-data
lifecycle_role: frontier-candidate
boundary_risk: none

failure_modes: [negative-transfer, coverage-gap, invalid-environment-state]
data_knobs: [environment-synthesis, verifier-design, negative-transfer-control, process-supervision]

agent_domain: gui
data_object: trajectory
data_source: synthetic
selection_signal: verifier
adaptivity: static
failure_use: discard
training_consumer: sft
---

## 一句话

大规模 GUI step-level SFT 数据。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `negative-transfer` | AgentNet human trajectories 继续训 UI-TARS 7B 反而让 OSWorld 从 26.3% 降到 8-10%。 | 构造 synthetic live-desktop trajectories，并做自动生成与验证。 | 仍需读全文确认哪些数据导致 negative transfer。 |
| `invalid-environment-state` | GUI 任务必须在真实桌面状态中成立。 | 用 live desktops、real-world content 和 precondition checking。 | verifier 覆盖不到的视觉/语义错误仍可能存在。 |

## 核心做法

ProCUA-SFT 是 computer-use agent SFT 的强 seed。它从 negative transfer 出发，指出简单加入已有 human trajectory 可能显著伤害 OSWorld。[Brief] 数据上，作者构造 93K synthetic trajectories，蒸馏成 3.1M step-level SFT samples，覆盖 2,484 application combinations。[Brief] pipeline 还用 SpreadsheetBench、Zenodo10K、OSWorld configs 等真实内容 seeded live desktops，并结合 task generation / verification / precondition checking。[Brief]

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `environment-synthesis` | live desktop + real-world content 生成 GUI 任务。 | 静态截图或人工轨迹。 |
| `process-supervision` | step-level SFT samples。 | trajectory-level final success imitation。 |
| `negative-transfer-control` | 显式诊断 AgentNet 继续训练负迁移。 | 默认“更多数据更好”。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| AgentNet human trajectories | 继续 SFT 产生 negative transfer。 | synthetic verified desktop trajectories。 | 合成 GUI 分布可能偏 OSWorld / UI-TARS。 |

## 谱系位置

- 上游：UI-TARS、OSWorld、AgentNet。
- 同期：PC Agent-E、ToolGym、S1-DeepResearch。
- 下游：artifact verification、GUI step trace、negative-transfer-aware data mixture。

## 和 Agentic RL 的关系

- agentic_rl_overlap: false
- 这是 SFT data / verification pipeline。
- 不需要登记到 `agentic-rl`。

## 优缺点

- 优势：最直接提醒你做数据 mixture 时必须监控 negative transfer，而不是只加 GUI 数据。
- 不足 / 风险：需要完整 PDF 才能提取可复用的 filtering rules 和 ablation。

<!-- meta:
authors: [Jaehun Jung, et al.]
url: https://arxiv.org/abs/2606.17321
arxiv_id: 2606.17321
pdf:
brief: _meta/briefs/papers/2606.17321_procua-sft.md
survey: user known-item / Codex HF recall
agentic_rl_overlap: false
agentic_rl_queue: none
-->
