---
title: "Alignment Tuning for Large Language Models: A Data-Centric Lens on Alignment Data Pipelines"
year: 2026
venue: findings-acl-2026
paper_type: alignment-data
lifecycle_role: survey-seed
boundary_risk: alignment

failure_modes: [verifier-noise, reward-proxy-bias]
data_knobs: [verifier-design, failure-contrast, process-supervision]

agent_domain: general
data_object: prompt
data_source: mixed
selection_signal: reward
adaptivity: iterative
failure_use: contrast
training_consumer: pre-rl
---

## 一句话

alignment data pipeline 的 data-centric 综述入口。

## 核心做法

综述把 alignment tuning 从 optimization objective 视角改写为 data pipeline design problem，并拆成 response synthesis、preference evaluation、preference instantiation 三个互动阶段。

它不是 agent 专属，但提供了本项目 Agent Data lens 的上位框架：不要只问 loss，而要问数据如何合成、评价、实例化成优化信号。

## Data-Centric 判断

- data object: prompt / response / preference instance。
- source: synthetic、teacher、human、model-generated。
- selection / filtering: preference evaluation / instantiation。
- adaptivity: iterative pipeline。
- failure trajectory use: contrast / preference。
- training consumer: pre-RL / alignment tuning；迁移到 Agent Data 时主要用作 data pipeline lens。
- downstream effect: optimization signal quality。

## 谱系位置

- 上游：alignment tuning / preference learning surveys。
- 下游：Agent Data pipeline — 可迁移 response synthesis / evaluation / instantiation 视角。
- 下游：agentic settings — paper abstract 明确列为 open challenge 之一。

## 优缺点

- ✅ [arXiv Abstract]: 提供 response synthesis、preference evaluation、preference instantiation 三阶段框架，并讨论 agentic settings。
- ⚠️ [本项目判断]: 不是 agent-specific，必须结合 tool/action/environment data 重解释。

## Evidence

- arXiv: abstract / Findings ACL 2026 note。

<!-- meta:
authors: [Hwanjun Song]
url: https://arxiv.org/abs/2605.26442
arxiv_id: 2605.26442
pdf: arXiv abstract
brief:
survey: none
agentic_rl_overlap: false
agentic_rl_queue: none
-->
