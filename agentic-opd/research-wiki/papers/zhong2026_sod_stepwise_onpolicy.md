---
type: paper
node_id: paper:zhong2026_sod_stepwise_onpolicy
title: "SOD: Step-wise On-policy Distillation for Small Language Model Agents"
authors: ["Qiyong Zhong", "Mao Zheng", "Mingyang Song", "Xin Lin", "Jie Sun", "Houcheng Jiang", "Xiang Wang", "Junfeng Fang"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2605.07725"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# SOD: Step-wise On-policy Distillation for Small Language Model Agents

## One-line thesis
【作者方法】SOD 按 tool observations 之间的 response 划 step，依据 sampled-token log-prob gap 衰减高 divergence step 的蒸馏权重，并联合 GRPO；teacher 为独立训练的较大模型。

## Problem / Gap
【作者问题】错误工具调用导致状态离散漂移，后续 dense OPD 可能不稳定。 [原文 §4、§5.1、§5.4及主结果表](https://arxiv.org/html/2605.07725v3)

## Method
【作者方法】SOD 按 tool observations 之间的 response 划 step，依据 sampled-token log-prob gap 衰减高 divergence step 的蒸馏权重，并联合 GRPO；teacher 为独立训练的较大模型。 [原文 §4、§5.1、§5.4及主结果表](https://arxiv.org/html/2605.07725v3)

## Key Results
【作者报告，未复现】§5主表：0.6B student AIME2025 average@32 为 26.13±1.07，OPD 22.95±0.97。 [原文 §4、§5.1、§5.4及主结果表](https://arxiv.org/html/2605.07725v3)

## Assumptions
【证据边界】阅读层级：摘要＋方法、主结果和 teacher 设置；依据 §4、§5.1、§5.4及主结果表。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】高 divergence 只是 teacher 不可靠的代理，也可能压低关键纠错状态上的监督。 [原文 §4、§5.1、§5.4及主结果表](https://arxiv.org/html/2605.07725v3)

## Reusable Ingredients
【解释】按环境交互边界定义 step，再调整监督权重。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G2](../gap_map.md#g2)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §4、§5.1、§5.4及主结果表](https://arxiv.org/html/2605.07725v3)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2605.07725)。

> Tool-integrated reasoning (TIR) is difficult to scale to small language models due to instability in long-horizon tool interactions and limited …
