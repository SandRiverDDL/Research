---
type: paper
node_id: paper:zhou2026_sageopd_selective_agentguided
title: "SAGE-OPD: Selective Agent-Guided Intervention for Multi-Turn On-Policy Distillation"
authors: ["Yuhang Zhou", "Lizhu Zhang", "Yifan Wu", "Mingyi Wang", "Bo Peng", "Jiayi Liu", "Xiangjun Fan", "Zhuokai Zhao"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2606.19659"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# SAGE-OPD: Selective Agent-Guided Intervention for Multi-Turn On-Policy Distillation

## One-line thesis
【作者方法】SAGE-OPD 基于 environment feedback、teacher 判断和 confidence，选择 Skip/Weak/Strong 监督强度并归一化 loss；这里 intervention 是监督选择，不是 teacher 接管。

## Problem / Gap
【作者问题】无差别 KL 可能惩罚有效替代动作，或强化重复行为及坏历史。 [原文 §3.1–3.3、§4主结果](https://arxiv.org/html/2606.19659v1)

## Method
【作者方法】SAGE-OPD 基于 environment feedback、teacher 判断和 confidence，选择 Skip/Weak/Strong 监督强度并归一化 loss；这里 intervention 是监督选择，不是 teacher 接管。 [原文 §3.1–3.3、§4主结果](https://arxiv.org/html/2606.19659v1)

## Key Results
【作者报告，未复现】§4：8B→1.7B，ALFWorld unseen SR 从 OPD 61.94→70.15。 [原文 §3.1–3.3、§4主结果](https://arxiv.org/html/2606.19659v1)

## Assumptions
【证据边界】阅读层级：摘要＋方法、实验设置与主结果；依据 §3.1–3.3、§4主结果。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】判断及置信度仍来自 teacher，缺乏独立监督正确性保证；收益依任务与配置。 [原文 §3.1–3.3、§4主结果](https://arxiv.org/html/2606.19659v1)

## Reusable Ingredients
【解释】把监督强度选择与 rollout 执行主体分开。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G2](../gap_map.md#g2)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §3.1–3.3、§4主结果](https://arxiv.org/html/2606.19659v1)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2606.19659)。

> On-policy distillation (OPD) improves student models by training them on trajectories induced by their own policy, making it a promising …
