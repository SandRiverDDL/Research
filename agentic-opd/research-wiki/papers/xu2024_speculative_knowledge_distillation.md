---
type: paper
node_id: paper:xu2024_speculative_knowledge_distillation
title: "Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling"
authors: ["Wenda Xu", "Rujun Han", "Zifeng Wang", "Long T. Le", "Dhruv Madeka", "Lei Li", "William Yang Wang", "Rishabh Agarwal", "Chen-Yu Lee", "Tomas Pfister"]
year: 2024
venue: "ICLR 2025（arXiv comments 自报）"
external_ids:
  arxiv: "2410.11325"
  doi: null
  s2: null
tags: ["agentic-opd", "background"]
added: 2026-10-14T14:09:06Z
---

# Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling

## One-line thesis
【作者方法】SKD 让 student 提议 token，teacher 按自身排序替换质量较差的 token，交错生成训练序列。

## Problem / Gap
【作者问题】纯 student rollout 可能落入 teacher 不熟悉的低质量前缀。 [原文 Abstract](https://arxiv.org/html/2410.11325v3)

## Method
【作者方法】SKD 让 student 提议 token，teacher 按自身排序替换质量较差的 token，交错生成训练序列。 [原文 Abstract](https://arxiv.org/html/2410.11325v3)

## Key Results
【作者报告，未复现】摘要报告在翻译、摘要、数学与指令任务上优于对比 KD 方法；本轮未核对正文数值。 [原文 Abstract](https://arxiv.org/html/2410.11325v3)

## Assumptions
【证据边界】阅读层级：原摘要；依据 Abstract。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】token 层交错采样不等于多轮环境的 teacher 接管；不能直接外推 agent 收益。 [原文 Abstract](https://arxiv.org/html/2410.11325v3)

## Reusable Ingredients
【解释】把 teacher–student 协作采样作为多轮接管机制的基础对照。

## Open Questions
【开放问题】上述单轮机制在多轮真实环境状态上是否仍成立？本轮未验证。

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】背景。仅作为基础背景，不计作多轮机制的直接证据。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 Abstract](https://arxiv.org/html/2410.11325v3)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2410.11325)。

> Recent advances in knowledge distillation (KD) have enabled smaller student models to approach the performance of larger teacher models. However, …
