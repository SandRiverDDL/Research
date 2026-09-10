---
title: "A Survey on Large Language Model based Autonomous Agents"
authors: [Lei Wang, et al.]
year: 2023
venue: arxiv
url: https://arxiv.org/abs/2308.11432
arxiv_id: 2308.11432

lane: survey
lifecycle_role: survey-seed

data_axes:
  data_object: trajectory
  data_source: mixed
  selection_signal: coverage
  adaptivity: static
  failure_use: ignore
  training_stage: eval-only
---

## 一句话

LLM-based autonomous agents 的全局入口综述。

## 核心做法

综述从 holistic perspective 系统整理 LLM-based autonomous agents，先给出统一 construction framework，再覆盖 applications、evaluation strategies、challenges 和 future directions。

对本项目最有价值的是它定义 agent construction / application / evaluation 的大边界，而不是直接给 Agent SFT training taxonomy。

## Data-Centric 判断

- data object: 主要是 agent construction、application、evaluation 层面的任务/轨迹/环境描述。
- source: 文献综述和维护中的 references repository。
- selection / filtering: 不提供训练数据筛选口径，但能给 seed references。
- adaptivity: 综述本身静态；repository 可作为持续更新入口。
- failure trajectory use: 非重点。
- downstream effect: 给 `agent-data` 项目定义全局 scope 和 benchmark/evaluation 背景。

## 谱系位置

- 上游：classical autonomous agents — 提供 agent 概念背景。
- 同期：The Rise and Potential of LLM-based Agents — 都是宏观 agent survey。
- 下游：Agent SFT / Agent RL 调研 — 作为 taxonomy 和 references seed。

## 优缺点

- ✅ [arXiv Abstract]: 覆盖 construction、applications、evaluation，并维护相关 references repository。
- ⚠️ [本项目判断]: 不是 training-stage taxonomy，不能直接回答 Agent SFT / data-centric 问题。

## Evidence

- arXiv: title / abstract / update history。

<!-- pdf: arXiv abstract -->
<!-- survey: none -->
