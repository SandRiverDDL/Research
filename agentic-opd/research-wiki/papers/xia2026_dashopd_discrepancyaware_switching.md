---
type: paper
node_id: paper:xia2026_dashopd_discrepancyaware_switching
title: "DASH-OPD: Discrepancy-Aware Switching with Hysteresis for On-Policy Distillation"
authors: ["Yuchen Xia", "Qianguo Sun", "Chao Song", "Junlong Wu", "Yiyan Qi", "Yunjian Xu"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2607.29078"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# DASH-OPD: Discrepancy-Aware Switching with Hysteresis for On-Policy Distillation

## One-line thesis
【作者方法】DASH-OPD 在 action tokens 上累计方向性 teacher/student likelihood-ratio evidence，以不同阈值及 hysteresis 双向切换；student/teacher turns 分别用 reverse/forward KL。

## Problem / Gap
【作者问题】介入调度不仅要决定多少，还要决定何时接管、何时归还。 [原文 §5.1–5.2、Table 1](https://arxiv.org/html/2607.29078v4)

## Method
【作者方法】DASH-OPD 在 action tokens 上累计方向性 teacher/student likelihood-ratio evidence，以不同阈值及 hysteresis 双向切换；student/teacher turns 分别用 reverse/forward KL。 [原文 §5.1–5.2、Table 1](https://arxiv.org/html/2607.29078v4)

## Key Results
【作者报告，未复现】Table 1／§5.2：4B ScienceWorld SR 22.40%，最佳对比方法 20.34%。 [原文 §5.1–5.2、Table 1](https://arxiv.org/html/2607.29078v4)

## Assumptions
【证据边界】阅读层级：摘要＋方法概述、实验设置与主结果；依据 §5.1–5.2、Table 1。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】主比较只用 seed42，无跨 seed 误差；阈值鲁棒性仅在局部扰动验证。 [原文 §5.1–5.2、Table 1](https://arxiv.org/html/2607.29078v4)

## Reusable Ingredients
【解释】把接管阈值和归还阈值拆开，减少反复切换。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G1](../gap_map.md#g1)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §5.1–5.2、Table 1](https://arxiv.org/html/2607.29078v4)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2607.29078)。

> While on-policy distillation (OPD) reduces exposure bias by training student language models on their own rollouts, early student errors in …
