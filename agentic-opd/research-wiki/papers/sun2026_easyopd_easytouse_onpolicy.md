---
type: paper
node_id: paper:sun2026_easyopd_easytouse_onpolicy
title: "EasyOPD: An Easy-to-use On-Policy Distillation Framework for Large Language Models"
authors: ["Jie Sun", "Mao Zheng", "Mingyang Song", "Qiyong Zhong", "Gengsheng Li", "Zhepei Hong", "Chang Wu", "Pengfei Liu", "Junfeng Fang", "Xiang Wang"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2607.11012"
  doi: null
  s2: null
tags: ["agentic-opd", "infrastructure"]
added: 2026-10-14T14:09:06Z
---

# EasyOPD: An Easy-to-use On-Policy Distillation Framework for Large Language Models

## One-line thesis
【作者方法】EasyOPD 在 verl 上分开用户配置、方法监督逻辑与分布式执行，为 loss、rollout metadata、reward、tokenizer alignment 和 teacher computation 提供扩展边界。

## Problem / Gap
【作者问题】OPD 的 teacher access、tokenizer 和监督粒度不同，导致实现碎片化。 [原文 §3、§4.1、Table 4](https://arxiv.org/html/2607.11012v1)

## Method
【作者方法】EasyOPD 在 verl 上分开用户配置、方法监督逻辑与分布式执行，为 loss、rollout metadata、reward、tokenizer alignment 和 teacher computation 提供扩展边界。 [原文 §3、§4.1、Table 4](https://arxiv.org/html/2607.11012v1)

## Key Results
【作者报告，未复现】Table 4：1.7B student／独立4B teacher 的 step-wise 示例，OPD平均34.81、SOD39.95；这是框架内的具体配置结果。 [原文 §3、§4.1、Table 4](https://arxiv.org/html/2607.11012v1)

## Assumptions
【证据边界】阅读层级：摘要＋框架接口、step-wise 实验；依据 §3、§4.1、Table 4。范围：仅提取普通／step-wise OPD 接口，不纳入 OPSD 分支。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】同时包含 OPSD 实现，但该分支不纳入本轮；统一 backend 不等于跨 regime 公平排行。 [原文 §3、§4.1、Table 4](https://arxiv.org/html/2607.11012v1)

## Reusable Ingredients
【解释】使用共享执行 backend，保留方法专属目标和诊断，减少比较中的工程差异。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】框架。边界：仅提取普通／step-wise OPD 接口，不纳入 OPSD 分支。对应 [G4](../gap_map.md#g4)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §3、§4.1、Table 4](https://arxiv.org/html/2607.11012v1)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2607.11012)。

> Conventional language-model distillation often relies on fixed teacher-generated data, which may not cover the states encountered by an evolving student …
