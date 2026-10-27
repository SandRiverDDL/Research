---
type: paper
node_id: paper:gu2023_minillm_onpolicy_distillation
title: "MiniLLM: On-Policy Distillation of Large Language Models"
authors: ["Yuxian Gu", "Li Dong", "Furu Wei", "Minlie Huang"]
year: 2023
venue: "ICLR 2024（arXiv comments 自报）"
external_ids:
  arxiv: "2306.08543"
  doi: null
  s2: null
tags: ["agentic-opd", "background"]
added: 2026-10-14T14:09:06Z
---

# MiniLLM: On-Policy Distillation of Large Language Models

## One-line thesis
【作者方法】MiniLLM 使用 reverse KL 与 on-policy 优化，将较大白盒 teacher 的分布迁移给小 student。

## Problem / Gap
【作者问题】生成模型的 forward-KL 蒸馏可能高估 teacher 的低概率输出。 [原文 Abstract](https://arxiv.org/html/2306.08543v6)

## Method
【作者方法】MiniLLM 使用 reverse KL 与 on-policy 优化，将较大白盒 teacher 的分布迁移给小 student。 [原文 Abstract](https://arxiv.org/html/2306.08543v6)

## Key Results
【作者报告，未复现】摘要报告覆盖 120M–13B 模型，改善 instruction following、calibration 和长文本生成；未核对正文效果量。 [原文 Abstract](https://arxiv.org/html/2306.08543v6)

## Assumptions
【证据边界】阅读层级：原摘要；依据 Abstract。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】单轮语言生成基础，不提供多轮工具状态上的 teacher 可靠性证据。 [原文 Abstract](https://arxiv.org/html/2306.08543v6)

## Reusable Ingredients
【解释】明确 KL 的方向与采样分布，避免仅以 OPD 名称比较方法。

## Open Questions
【开放问题】上述单轮机制在多轮真实环境状态上是否仍成立？本轮未验证。

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】背景。仅作为基础背景，不计作多轮机制的直接证据。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 Abstract](https://arxiv.org/html/2306.08543v6)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2306.08543)。

> Knowledge Distillation (KD) is a promising technique for reducing the high computational demand of large language models (LLMs). However, previous …
