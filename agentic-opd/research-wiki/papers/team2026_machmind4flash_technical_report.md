---
type: paper
node_id: paper:team2026_machmind4flash_technical_report
title: "Mach-Mind-4-Flash Technical Report"
authors: ["Foundation Model Team"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2607.09375"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# Mach-Mind-4-Flash Technical Report

## One-line thesis
【作者方法】Mach-Mind-4-Flash 用十余冻结 RL specialists 按 domain routing 监督 student rollout，使用 sampled reverse-KL log-ratio 与 clipped policy-gradient surrogate；另有 HMPO reasoning 压缩。

## Problem / Gap
【作者问题】mixed-reward RL 存在跨领域能力的 see-saw。 [原文 §4.8、§5.1、§6、Appendices B–C](https://arxiv.org/html/2607.09375v1)

## Method
【作者方法】Mach-Mind-4-Flash 用十余冻结 RL specialists 按 domain routing 监督 student rollout，使用 sampled reverse-KL log-ratio 与 clipped policy-gradient surrogate；另有 HMPO reasoning 压缩。 [原文 §4.8、§5.1、§6、Appendices B–C](https://arxiv.org/html/2607.09375v1)

## Key Results
【作者报告，未复现】Appendix C／Table 4：加入 code teacher 后 LCB-V6 78.63→82.44，BFCL 76.30→76.39。 [原文 §4.8、§5.1、§6、Appendices B–C](https://arxiv.org/html/2607.09375v1)

## Assumptions
【证据边界】阅读层级：摘要＋方法、composition ablation 与局限；依据 §4.8、§5.1、§6、Appendices B–C。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】composition ablation 为 single run，不能概括必然正迁移；§6 将视觉 grounding/GUI 扩展列为未来工作。 [原文 §4.8、§5.1、§6、Appendices B–C](https://arxiv.org/html/2607.09375v1)

## Reusable Ingredients
【解释】逐个增加 teacher 做 composition ablation，观察目标域和非目标域。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G3](../gap_map.md#g3)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §4.8、§5.1、§6、Appendices B–C](https://arxiv.org/html/2607.09375v1)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2607.09375)。

> We present Mach-Mind-4-Flash, a 35B-parameter Mixture-of-Experts (MoE) agentic model with 3B activated parameters. Through post-training optimization alone without scaling pre-training …
