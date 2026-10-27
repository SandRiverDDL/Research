---
type: paper
node_id: paper:liu2026_memopd_onpolicy_distillation
title: "MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents"
authors: ["Zhiyuan Liu", "Tinghong Ye", "Chenghao Liu", "Yizhuo Li", "Songfang Huang"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2608.07068"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents

## One-line thesis
【作者方法】MemOPD 记录并重构真实 invocation，保持 action mask、position 与 causal visibility，联合 full-vocabulary reverse KL 和 PPO；3B student 与独立 frozen 7B teacher。

## Problem / Gap
【作者问题】memory rewriting 后 flatten history 会改变评分时的位置和可见性，使 teacher 看到的状态偏离 rollout state。 [原文 §3.3–3.4、§4.1、§4.5／Fig.3a](https://arxiv.org/html/2608.07068v1)

## Method
【作者方法】MemOPD 记录并重构真实 invocation，保持 action mask、position 与 causal visibility，联合 full-vocabulary reverse KL 和 PPO；3B student 与独立 frozen 7B teacher。 [原文 §3.3–3.4、§4.1、§4.5／Fig.3a](https://arxiv.org/html/2608.07068v1)

## Key Results
【作者报告，未复现】§4.5／Fig.3a matched control：恢复 teacher state 比 persistent-history scoring 再提高 F1 7.0%（相对）。 [原文 §3.3–3.4、§4.1、§4.5／Fig.3a](https://arxiv.org/html/2608.07068v1)

## Assumptions
【证据边界】阅读层级：摘要＋方法、teacher 设置与 matched control；依据 §3.3–3.4、§4.1、§4.5／Fig.3a。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】主要验证文本检索/memory agent、shared tokenizer；状态表示正确不等于 teacher 行动正确。 [原文 §3.3–3.4、§4.1、§4.5／Fig.3a](https://arxiv.org/html/2608.07068v1)

## Reusable Ingredients
【解释】把真实模型 invocation 作为评分契约，检查位置、可见性与 action mask。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G3](../gap_map.md#g3)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §3.3–3.4、§4.1、§4.5／Fig.3a](https://arxiv.org/html/2608.07068v1)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2608.07068)。

> Long-horizon agents accumulate growing contexts during interaction, impairing performance and stability. Compact memory mitigates this problem by compressing and rewriting …
