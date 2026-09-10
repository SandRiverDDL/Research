---
title: "Efficient Agent Training for Computer Use"
year: 2025
venue: arxiv
paper_type: synthetic-verifiable-data
lifecycle_role: canonical-anchor
boundary_risk: none

failure_modes: [low-quality-demonstration, coverage-gap, synthetic-data-bias]
data_knobs: [teacher-rollout, trajectory-source, coverage-balancing]

agent_domain: gui
data_object: trajectory
data_source: human
selection_signal: coverage
adaptivity: static
failure_use: ignore
training_consumer: sft
---

## 一句话

少量人工轨迹加 teacher action 增广。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `coverage-gap` | computer-use agent 缺高质量 trajectory。 | 312 条人工轨迹作为 seed，再用 Claude 合成 alternative action decisions。 | 合成动作的质量过滤细节需读全文。 |
| `synthetic-data-bias` | 直接 teacher distillation 可能不如 human skill seed。 | 人类轨迹承载 robust computer-use skills，teacher 只做 action augmentation。 | 依赖 teacher 风格与 benchmark 是否匹配。 |

## 核心做法

PC Agent-E 的价值是说明 GUI/computer-use SFT 不一定需要海量人工轨迹：它从 312 条 human-annotated trajectories 出发，用 Claude 3.7 Sonnet 合成 diverse alternative action decisions，再训练 computer-use agent。[Brief] 摘要称模型在 WindowsAgentArena-V2 上相对提升 141%，并相对 Claude 3.7 Sonnet 高 10%；代码、数据、模型公开。[Brief]

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `trajectory-source` | 少量人类 GUI 轨迹作为高质量 seed。 | 大规模低质量 human / synthetic traces。 |
| `teacher-rollout` | teacher 合成 alternative action decisions。 | 直接蒸馏完整 teacher 轨迹。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| 直接 teacher distillation | 可能缺 human computer-use skill grounding。 | human seed + teacher action augmentation。 | 需要验证 teacher action 是否真实可执行。 |

## 谱系位置

- 上游：computer-use demonstrations、WindowsAgentArena。
- 同期：ProCUA-SFT、UI-TARS / OSWorld 系列。
- 下游：内部 GUI/桌面任务的少量人工 seed + teacher augmentation 数据方案。

## 和 Agentic RL 的关系

- agentic_rl_overlap: false
- 这是 SFT 数据增强框架，不是 RL algorithm。
- 不需要登记到 `agentic-rl`。

## 优缺点

- 优势：给出低成本 GUI 数据放大策略，适合资源受限场景。
- 不足 / 风险：偏 computer-use，不一定覆盖文档/数据分析的 artifact verification。

<!-- meta:
authors: [Yanheng He, et al.]
url: https://arxiv.org/abs/2505.13909
arxiv_id: 2505.13909
pdf:
brief: _meta/briefs/papers/2505.13909_pc-agent-e.md
survey: Codex HF/arXiv recall
agentic_rl_overlap: false
agentic_rl_queue: none
-->
