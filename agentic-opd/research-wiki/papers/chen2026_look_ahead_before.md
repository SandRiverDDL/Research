---
type: paper
node_id: paper:chen2026_look_ahead_before
title: "Look Ahead Before You Distill: Future Trajectory Validation of Teacher Guidance for Agentic On-Policy Distillation"
authors: ["Chishui Chen", "Yaoyou Fan", "Te Sun", "Yi Yang", "Chenghao Sun", "Delin Mao", "Hongbo Qiao", "Zuowei Zhang", "Junxi Wang", "Chenxing Sun", "Yangen Hu", "Lu Pan", "Xuyang Liu", "Linfeng Zhang"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2608.01953"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# Look Ahead Before You Distill: Future Trajectory Validation of Teacher Guidance for Agentic On-Policy Distillation

## One-line thesis
【作者方法】FutureBridge-OPD 恢复候选 turn 的环境，插入 teacher bridge，并比较两条 student continuation 的 teacher-preferred token ratio，仅接受改善该代理指标的 bridge。

## Problem / Gap
【作者问题】高 teacher–student disagreement 能定位介入机会，却不能保证 teacher action 有用。 [原文 §3.2、§4.1、Table 1、Appendix G](https://arxiv.org/html/2608.01953v2)

## Method
【作者方法】FutureBridge-OPD 恢复候选 turn 的环境，插入 teacher bridge，并比较两条 student continuation 的 teacher-preferred token ratio，仅接受改善该代理指标的 bridge。 [原文 §3.2、§4.1、Table 1、Appendix G](https://arxiv.org/html/2608.01953v2)

## Key Results
【作者报告，未复现】Table 1：1.7B student ALFWorld SR 40.4±3.4，OPD 21.5±3.0。 [原文 §3.2、§4.1、Table 1、Appendix G](https://arxiv.org/html/2608.01953v2)

## Assumptions
【证据边界】阅读层级：摘要＋方法、主结果与局限；依据 §3.2、§4.1、Table 1、Appendix G。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】future preference 仍是 teacher-relative proxy；需要环境恢复和额外 continuation；跨 tokenizer/family 未验证。 [原文 §3.2、§4.1、Table 1、Appendix G](https://arxiv.org/html/2608.01953v2)

## Reusable Ingredients
【解释】用 student 后续行为核验候选 teacher 介入，而非只看当前分歧。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G2](../gap_map.md#g2)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §3.2、§4.1、Table 1、Appendix G](https://arxiv.org/html/2608.01953v2)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2608.01953)。

> On-policy distillation (OPD) provides teacher supervision on states visited by the student, reducing the distribution gap between training and inference. …
