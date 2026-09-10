---
title: "Tool Learning with Foundation Models"
authors: [Yujia Qin, et al.]
year: 2023
venue: arxiv
url: https://arxiv.org/abs/2304.08354
arxiv_id: 2304.08354

lane: survey
lifecycle_role: survey-seed

data_axes:
  data_object: tool-call
  data_source: mixed
  selection_signal: coverage
  adaptivity: static
  failure_use: ignore
  training_stage: sft
---

## 一句话

tool learning 与 agent action grammar 的经典综述入口。

## 核心做法

综述将 tool learning 拆成 tool-augmented 和 tool-oriented learning，并提出从理解用户指令、分解任务、动态调整计划到选择工具完成子任务的一般框架。

对 Agent SFT 最重要的是：tool-use 能力不是普通文本 SFT；训练数据必须包含 action schema、tool selection、task decomposition、tool execution 和 evaluation。

## Data-Centric 判断

- data object: tool-call、subtask plan、tool execution trace。
- source: existing tool learning papers and representative tools。
- selection / filtering: 偏覆盖和评测，不是具体筛选算法。
- adaptivity: static survey。
- failure trajectory use: 非重点。
- downstream effect: 定义 tool-call SFT / action grammar 的基础问题。

## 谱系位置

- 上游：foundation model tool-use / API use。
- 下游：Agentic Tool Use in LLMs — 更新为 prompting / supervised / reward-driven 三范式。
- 下游：Agent Data — tool-call trajectory 是核心 data object。

## 优缺点

- ✅ [arXiv Abstract]: 系统讨论 tool learning 背景、framework、training for tool-use capabilities 和 evaluation。
- ⚠️ [本项目判断]: 2023 综述较早，对 2025-2026 agent RL / synthetic trajectory data 覆盖不足。

## Evidence

- arXiv: abstract lines on framework and training/evaluation.

<!-- pdf: arXiv abstract -->
<!-- survey: none -->
