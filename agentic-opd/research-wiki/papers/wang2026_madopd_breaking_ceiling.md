---
type: paper
node_id: paper:wang2026_madopd_breaking_ceiling
title: "MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate"
authors: ["Jianze Wang", "Ying Liu", "Jinlong Chen", "Xuchun Hu", "Qilong Zhang", "Yu Cao", "Jun Wang", "Hua Yang", "Yong Xie", "Qianglong Chen"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2605.01347"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate

## One-line thesis
【作者方法】MAD-OPD 在 student-visited state 上让多个独立 teacher debate，并按自报 confidence 加权监督；agent 场景用 JSD，code 用 reverse KL。

## Problem / Gap
【作者问题】单 teacher 错误限制 student，多步环境交互进一步放大错误。 [原文 §4、§5.1–5.2、Table 1、§6](https://arxiv.org/html/2605.01347v1)

## Method
【作者方法】MAD-OPD 在 student-visited state 上让多个独立 teacher debate，并按自报 confidence 加权监督；agent 场景用 JSD，code 用 reverse KL。 [原文 §4、§5.1–5.2、Table 1、§6](https://arxiv.org/html/2605.01347v1)

## Key Results
【作者报告，未复现】Table 1：14B＋8B→4B，agent average 从单 teacher OPD 23.26→25.69。 [原文 §4、§5.1–5.2、Table 1、§6](https://arxiv.org/html/2605.01347v1)

## Assumptions
【证据边界】阅读层级：摘要＋方法、主结果与局限；依据 §4、§5.1–5.2、Table 1、§6。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】要求 shared vocabulary 与 teacher distributions；teacher 数与 debate rounds 增加成本，自报 confidence 不等于校准可靠性。 [原文 §4、§5.1–5.2、Table 1、§6](https://arxiv.org/html/2605.01347v1)

## Reusable Ingredients
【解释】把多教师组合策略与额外 teacher inference 成本一起比较。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G3](../gap_map.md#g3)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §4、§5.1–5.2、Table 1、§6](https://arxiv.org/html/2605.01347v1)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2605.01347)。

> On-policy distillation (OPD) trains a student on its own trajectories under token-level teacher supervision, but existing methods are capped by …
