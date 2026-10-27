---
type: paper
node_id: paper:song2026_survey_onpolicy_distillation
title: "A Survey of On-Policy Distillation for Large Language Models"
authors: ["Mingyang Song", "Mao Zheng"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2604.00626"
  doi: null
  s2: null
tags: ["agentic-opd", "background"]
added: 2026-10-14T14:09:06Z
---

# A Survey of On-Policy Distillation for Large Language Models

## One-line thesis
【作者方法】Survey 按 objective functions、signal sources、training dynamics 梳理 OPD、失败模式及与 KL-constrained RL 的联系。

## Problem / Gap
【作者问题】OPD 的目标、信号来源与训练动态分散在多类文献中。 [原文 Abstract](https://arxiv.org/html/2604.00626v4)

## Method
【作者方法】Survey 按 objective functions、signal sources、training dynamics 梳理 OPD、失败模式及与 KL-constrained RL 的联系。 [原文 Abstract](https://arxiv.org/html/2604.00626v4)

## Key Results
【作者报告，未复现】提供分类与开放问题，不是提出新算法的实验效果证据；本轮仅读原摘要。 [原文 Abstract](https://arxiv.org/html/2604.00626v4)

## Assumptions
【证据边界】阅读层级：原摘要；依据 Abstract。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】综述只作导航；其中 OPSD 与其他排除分支不计入本轮方法清单。 [原文 Abstract](https://arxiv.org/html/2604.00626v4)

## Reusable Ingredients
【解释】用目标、信号来源、训练动态三个轴组织比较。

## Open Questions
【开放问题】上述单轮机制在多轮真实环境状态上是否仍成立？本轮未验证。

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】背景。仅作为基础背景，不计作多轮机制的直接证据。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 Abstract](https://arxiv.org/html/2604.00626v4)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2604.00626)。

> As Large Language Models continue to grow in both capability and cost, transferring frontier capabilities into smaller, deployable students has …
