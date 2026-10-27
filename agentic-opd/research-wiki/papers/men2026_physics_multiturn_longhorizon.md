---
type: paper
node_id: paper:men2026_physics_multiturn_longhorizon
title: "The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation"
authors: ["Tianyi Men", "Zhuoran Jin", "Kang Liu", "Jun Zhao"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2607.24720"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation

## One-line thesis
【作者方法】在受控文本 crafting 环境改变预训练轨迹质量和 planning templates，对比 OPD/GRPO；顺序蒸馏三个独立域专家，检验 shared/conflicting patterns。

## Problem / Gap
【作者问题】planning pattern、procedural knowledge 与多教师兼容性对长程学习的作用未分清。 [原文 §5.2、§6.2–6.3、Table 6](https://arxiv.org/html/2607.24720v1)

## Method
【作者方法】在受控文本 crafting 环境改变预训练轨迹质量和 planning templates，对比 OPD/GRPO；顺序蒸馏三个独立域专家，检验 shared/conflicting patterns。 [原文 §5.2、§6.2–6.3、Table 6](https://arxiv.org/html/2607.24720v1)

## Key Results
【作者报告，未复现】Table 6／§6.2：4 Opt.:4 Sub.(a) 中，只蒸馏 FA teacher，未见 LF 中等难度 avg@8 34.92→52.58。 [原文 §5.2、§6.2–6.3、Table 6](https://arxiv.org/html/2607.24720v1)

## Assumptions
【证据边界】阅读层级：摘要＋受控实验及多教师结果；依据 §5.2、§6.2–6.3、Table 6。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】合成环境和人为模板提供机制证据，真实工具 agent 外推未验证；不是 benchmark-only 论文。 [原文 §5.2、§6.2–6.3、Table 6](https://arxiv.org/html/2607.24720v1)

## Reusable Ingredients
【解释】在受控环境中分开改变知识、规划模式与 teacher 组合。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G3](../gap_map.md#g3)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §5.2、§6.2–6.3、Table 6](https://arxiv.org/html/2607.24720v1)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2607.24720)。

> Multi-turn long-horizon planning is critical for foundation model agents, yet how to fundamentally improve it remains unclear. Existing models are …
