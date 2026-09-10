---
title: "Towards Alignment-Centric Paradigm: A Survey of Instruction Tuning in Large Language Models"
authors: [Xudong Han, et al.]
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2508.17184
arxiv_id: 2508.17184

lane: survey
lifecycle_role: survey-seed

data_axes:
  data_object: instruction
  data_source: mixed
  selection_signal: quality
  adaptivity: static
  failure_use: discard
  training_stage: sft
---

## 一句话

SFT / instruction tuning 背景综述。

## 核心做法

综述覆盖 instruction tuning pipeline：data collection、full-parameter / parameter-efficient fine-tuning、evaluation protocols。它将数据构造分成 expert annotation、distillation from larger models、self-improvement mechanisms。

对本项目的用途是提供 supervised data / instruction tuning 的非 agent 背景，避免把普通 instruction tuning 问题误认为 agent-specific。

## Data-Centric 判断

- data object: instruction / response pair。
- source: expert annotation、larger-model distillation、self-improvement。
- selection / filtering: quality、scalability、resource cost tradeoff。
- adaptivity: mostly static / some self-improvement。
- failure trajectory use: 普通 instruction tuning 不强调 trajectory failure。
- downstream effect: alignment and domain adaptation。

## 谱系位置

- 上游：instruction tuning / alignment tuning。
- 下游：Agent SFT — 提供 baseline data collection / fine-tuning / evaluation 概念。

## 优缺点

- ✅ [arXiv Abstract]: 覆盖 data collection、fine-tuning strategies、evaluation protocols，并总结三类 data construction。
- ⚠️ [本项目判断]: 不是 agent training survey；缺少 tool-call / environment state / trajectory structure。

## Evidence

- arXiv: abstract。

<!-- pdf: arXiv abstract -->
<!-- survey: none -->
