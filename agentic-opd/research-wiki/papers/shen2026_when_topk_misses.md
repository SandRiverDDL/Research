---
type: paper
node_id: paper:shen2026_when_topk_misses
title: "When Top-K Misses the Decision: Tool-Call Drift in Multi-Teacher On-Policy Distillation"
authors: ["Jiabin Shen", "Guang Chen", "Chengjun Mao"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2607.07050"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# When Top-K Misses the Decision: Tool-Call Drift in Multi-Teacher On-Policy Distillation

## One-line thesis
【作者方法】Top-K Drift 用 frozen full-vocabulary audit、entry-coordinate restoration 和对照诊断 tool-call drift，比较 support union、loss shaping 与 decoding bias。teacher 为分别 SFT 的独立专家。

## Problem / Gap
【作者问题】top-k 保留概率质量很高，也可能漏掉工具调用的决策关键 token。 [原文 §2、§5、§6、Appendix A.3](https://arxiv.org/html/2607.07050v6)

## Method
【作者方法】Top-K Drift 用 frozen full-vocabulary audit、entry-coordinate restoration 和对照诊断 tool-call drift，比较 support union、loss shaping 与 decoding bias。teacher 为分别 SFT 的独立专家。 [原文 §2、§5、§6、Appendix A.3](https://arxiv.org/html/2607.07050v6)

## Key Results
【作者报告，未复现】摘要及正文：三 seed 全位置 restoration，over-calling 14.2±2.1%→3.7±0.5%，同时 call recall 损失12.4点。 [原文 §2、§5、§6、Appendix A.3](https://arxiv.org/html/2607.07050v6)

## Assumptions
【证据边界】阅读层级：摘要＋诊断方法、结果与局限；依据 §2、§5、§6、Appendix A.3。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】因果链主要限 Qwen/top-32；Llama 未提供第二套完整 restoration 复现；降低 over-calling 不等于全面改善。 [原文 §2、§5、§6、Appendix A.3](https://arxiv.org/html/2607.07050v6)

## Reusable Ingredients
【解释】直接核验 action decision token 的 support，而不只看累计保留质量。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G3](../gap_map.md#g3)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §2、§5、§6、Appendix A.3](https://arxiv.org/html/2607.07050v6)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2607.07050)。

> Top-$K$ teacher logits make on-policy distillation tractable, but retained teacher mass does not certify student-relative gradient fidelity. We study routed, …
