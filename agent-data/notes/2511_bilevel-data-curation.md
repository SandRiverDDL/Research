---
title: "Bilevel Data Curation for LLM Fine-tuning: Offline Selection and Online Self-Refining Generation"
year: 2025
venue: arxiv
paper_type: data-flywheel-method
lifecycle_role: strong-baseline
boundary_risk: alignment

failure_modes: [low-quality-demonstration, failure-signal-waste, static-data-ceiling]
data_knobs: [failure-repair, student-feedback-loop, online-data-flywheel, coverage-balancing]

agent_domain: general
data_object: demo
data_source: self-generated
selection_signal: verifier
adaptivity: student-feedback
failure_use: repair
training_consumer: sft
---

## 一句话

离线筛选和在线修复的统一框架。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `low-quality-demonstration` | SFT 数据含低质或有害 question-response pairs。 | bilevel data selection 最大化 validation performance。 | 需要高质量 validation set。 |
| `failure-signal-waste` | 离线 selection 可能连同坏 response 一起丢掉有价值 question。 | selected questions 上做 online self-refining generation。 | agent trajectory 的多步修复比单 response 更难。 |

## 核心做法

这篇当前 arXiv 标题已改为 Bilevel Data Curation。它把 offline data selection 和 online self-refining generation 放进同一个 bilevel 框架：离线阶段选择能最大化 validation performance 的 question-response pairs；在线阶段针对保留下来的 question 重新生成 / 修复 response，并用 response-level weighting 适配 regenerated responses。[arXiv Abstract] 对本项目，它提供的是“坏 response 不等于坏 task”的飞轮思想：benchmark bad case 里的任务可能应该保留，只修复或重采 agent 轨迹。

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `failure-repair` | 保留问题、修复 response。 | 整条样本丢弃。 |
| `student-feedback-loop` | online self-refining generation。 | 静态离线筛选。 |
| `coverage-balancing` | validation-aligned data weights。 | heuristic quality filter。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| Offline-only selection | 会牺牲 question diversity。 | selected questions 上在线重生成 response。 | 生成质量和 validation objective 强相关。 |

## 谱系位置

- 上游：bilevel data selection、self-refinement。
- 同期：FastMix、Dr. Post-Training。
- 下游：agent failure trajectory repair / task-preserving regeneration。

## 和 Agentic RL 的关系

- agentic_rl_overlap: false
- 这是 SFT data curation / generation 框架。
- 不登记到 `agentic-rl`。

## 优缺点

- 优势：很适合你从 bad case 反推数据动作时区分“任务有价值但答案/轨迹坏”。
- 不足 / 风险：原文是 general SFT response，不是 multi-step tool trajectory；迁移时要改成 step/trajectory-level weighting。

<!-- meta:
authors: [Quan Xiao, et al.]
url: https://arxiv.org/abs/2511.21056
arxiv_id: 2511.21056
pdf:
brief: _meta/briefs/papers/2511.21056_bilevel-data-curation.md
survey: Codex data-flywheel recall
agentic_rl_overlap: false
agentic_rl_queue: none
-->
