---
type: paper
node_id: paper:agarwal2023_onpolicy_distillation_language
title: "On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes"
authors: ["Rishabh Agarwal", "Nino Vieillard", "Yongchao Zhou", "Piotr Stanczyk", "Sabela Ramos", "Matthieu Geist", "Olivier Bachem"]
year: 2023
venue: "ICLR 2024（arXiv comments 自报）"
external_ids:
  arxiv: "2306.13649"
  doi: null
  s2: null
tags: ["agentic-opd", "background"]
added: 2026-10-14T14:09:06Z
---

# On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes

## One-line thesis
【作者方法】GKD 在 student 自生成序列上查询 teacher，并允许选择不同 divergence 或与 RL 结合。

## Problem / Gap
【作者问题】离线 teacher 数据与 student 推理时的前缀分布不匹配。 [原文 Abstract](https://arxiv.org/html/2306.13649v3)

## Method
【作者方法】GKD 在 student 自生成序列上查询 teacher，并允许选择不同 divergence 或与 RL 结合。 [原文 Abstract](https://arxiv.org/html/2306.13649v3)

## Key Results
【作者报告，未复现】摘要报告在摘要、翻译、推理和 instruction tuning 上有效；本轮未核对正文数值。 [原文 Abstract](https://arxiv.org/html/2306.13649v3)

## Assumptions
【证据边界】阅读层级：原摘要；依据 Abstract。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】单轮自回归生成基础工作，不能直接证明多轮环境状态覆盖或纠错能力。 [原文 Abstract](https://arxiv.org/html/2306.13649v3)

## Reusable Ingredients
【解释】将 student 自采样分布与 teacher 评分接口分开定义。

## Open Questions
【开放问题】上述单轮机制在多轮真实环境状态上是否仍成立？本轮未验证。

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】背景。仅作为基础背景，不计作多轮机制的直接证据。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 Abstract](https://arxiv.org/html/2306.13649v3)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2306.13649)。

> Knowledge distillation (KD) is widely used for compressing a teacher model to reduce its inference cost and memory footprint, by …
