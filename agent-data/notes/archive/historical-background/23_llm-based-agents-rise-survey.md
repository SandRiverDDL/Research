---
title: "The Rise and Potential of Large Language Model Based Agents: A Survey"
authors: [Zhiheng Xi, et al.]
year: 2023
venue: arxiv
url: https://arxiv.org/abs/2309.07864
arxiv_id: 2309.07864

lane: survey
lifecycle_role: survey-seed

data_axes:
  data_object: benchmark-task
  data_source: mixed
  selection_signal: coverage
  adaptivity: static
  failure_use: ignore
  training_stage: eval-only
---

## 一句话

brain / perception / action 视角的 LLM agent 宏观综述。

## 核心做法

综述从 agent 概念、LLM 作为 agent foundation 的理由、brain/perception/action 三组件框架、single-agent / multi-agent / human-agent cooperation、agent societies 和 open problems 组织文献。

对本项目的用途是补 agent 架构和 action/perception 边界，帮助判断某篇 paper 是否真是 agent training，而不是普通 instruction tuning。

## Data-Centric 判断

- data object: agent tasks、applications、evaluation settings。
- source: 既有 LLM agent 文献和维护的 paper repository。
- selection / filtering: 偏 taxonomy，不提供 data pipeline。
- adaptivity: static survey。
- failure trajectory use: 非重点。
- downstream effect: 用于 `agent-sft` / `agent-rl` 的 scope guard。

## 谱系位置

- 同期：A Survey on LLM-based Autonomous Agents — 都是宏观 agent survey。
- 下游：tool-use / agent training survey — 可把 brain/perception/action 作为高层框架。

## 优缺点

- ✅ [arXiv Abstract]: 提供 brain / perception / action 通用框架，并覆盖 single-agent、multi-agent、human-agent cooperation。
- ⚠️ [本项目判断]: 训练数据、trajectory filtering、SFT/RL 细节不是主线。

## Evidence

- arXiv: title / abstract。

<!-- pdf: arXiv abstract -->
<!-- survey: none -->
