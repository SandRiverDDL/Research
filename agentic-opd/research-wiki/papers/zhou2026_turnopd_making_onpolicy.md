---
type: paper
node_id: paper:zhou2026_turnopd_making_onpolicy
title: "TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training"
authors: ["Yuhang Zhou", "Kai Zheng", "Haoling Li", "Dengyun Peng", "Can Xu", "Jingjing Chen"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2607.05804"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training

## One-line thesis
【作者方法】TurnOPD 结合 probe-based adaptive rollout depth 与渐进 turn-normalized KL weighting，分配环境交互和蒸馏预算。

## Problem / Gap
【作者问题】长 rollout 尾部可能消耗预算，token objective 也可能过度偏向浅层 turn。 [原文 §6、Table 2](https://arxiv.org/html/2607.05804v2)

## Method
【作者方法】TurnOPD 结合 probe-based adaptive rollout depth 与渐进 turn-normalized KL weighting，分配环境交互和蒸馏预算。 [原文 §6、Table 2](https://arxiv.org/html/2607.05804v2)

## Key Results
【作者报告，未复现】Table 2：ALFWorld-1.7B 的 100步时间 4.42h→1.93h，同步数 accuracy 83.00→86.29。 [原文 §6、Table 2](https://arxiv.org/html/2607.05804v2)

## Assumptions
【证据边界】阅读层级：摘要＋诊断、方法概述、主实验；依据 §6、Table 2。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】表中±为末四 evaluation checkpoints 波动，不是独立 seed 方差；部分搜索任务同 step accuracy 略低。 [原文 §6、Table 2](https://arxiv.org/html/2607.05804v2)

## Reusable Ingredients
【解释】同时报告固定 update 与固定 wall-clock 的比较。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G4](../gap_map.md#g4)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §6、Table 2](https://arxiv.org/html/2607.05804v2)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2607.05804)。

> On-policy distillation (OPD) trains a student policy by matching a stronger teacher on the student's own trajectories, offering a promising …
