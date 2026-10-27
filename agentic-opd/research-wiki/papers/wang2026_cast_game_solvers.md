---
type: paper
node_id: paper:wang2026_cast_game_solvers
title: "CAST: Game Solvers as Turn-Level Teachers for LLM Agents"
authors: ["Yu Wang", "Yi-Kai Zhang", "Wentao Shi", "Ziang Ye", "Yuchun Miao", "Yueqing Sun", "Qi Gu", "Xunliang Cai", "Lan-Zhe Guo", "Han-Jia Ye", "Fuli Feng"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2607.25308"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# CAST: Game Solvers as Turn-Level Teachers for LLM Agents

## One-line thesis
【作者方法】CAST 用独立游戏 solver 的 state/action value 构造 turn advantage，经 asinh/RMS 变换后用于 DAPO/RLVR；在特定假设下联系 OPD，并非直接匹配 LM logits。

## Problem / Gap
【作者问题】文本游戏中的稀疏 outcome reward 缺少 turn-level 行动价值指导。 [原文 §3.1–3.2、Table 1、Appendix C.5](https://arxiv.org/html/2607.25308v1)

## Method
【作者方法】CAST 用独立游戏 solver 的 state/action value 构造 turn advantage，经 asinh/RMS 变换后用于 DAPO/RLVR；在特定假设下联系 OPD，并非直接匹配 LM logits。 [原文 §3.1–3.2、Table 1、Appendix C.5](https://arxiv.org/html/2607.25308v1)

## Key Results
【作者报告，未复现】Table 1：三游戏平均 ID/Unseen SR 62.1/28.4，DAPO 44.7/18.7。 [原文 §3.1–3.2、Table 1、Appendix C.5](https://arxiv.org/html/2607.25308v1)

## Assumptions
【证据边界】阅读层级：摘要＋方法、主表与理论片段；依据 §3.1–3.2、Table 1、Appendix C.5。范围：solver teacher 边界类。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】需要可查询 solver/value；OPD 等价依赖 soft-optimal 与 small-signal 等假设。输入是文本 board，不是视觉任务。 [原文 §3.1–3.2、Table 1、Appendix C.5](https://arxiv.org/html/2607.25308v1)

## Reusable Ingredients
【解释】用可验证行动价值考察 teacher 信号质量，同时保留与标准 KL-OPD 的区别。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。边界：solver teacher 边界类。对应 [G2](../gap_map.md#g2)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §3.1–3.2、Table 1、Appendix C.5](https://arxiv.org/html/2607.25308v1)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2607.25308)。

> Training large language models (LLMs) to act in long-horizon games is a promising step toward generalist decision-making, yet reinforcement learning …
