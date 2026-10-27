---
type: paper
node_id: paper:li2026_onpolicy_distillation_curriculum
title: "On-Policy Distillation with Curriculum Turn-level Guidance for Multi-turn Agents"
authors: ["Gengsheng Li", "Mao Zheng", "Mingyang Song", "Ruiqi Liu", "Tianyu Yang", "Jie Sun", "Qiyong Zhong", "Haiyun Guo", "Junfeng Fang", "Dan Zhang", "Jinqiao Wang"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2606.15912"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# On-Policy Distillation with Curriculum Turn-level Guidance for Multi-turn Agents

## One-line thesis
【作者方法】Guided-OPD 按 turn 概率混合 teacher/student 执行，并逐渐将 teacher 介入概率降到零；student turns 用 reverse KL、teacher turns 用 forward KL。

## Problem / Gap
【作者问题】错误累积后 teacher 在 student 访问状态上的监督可能失效。 [原文 Abstract、§3、§4.1](https://arxiv.org/html/2606.15912v2)

## Method
【作者方法】Guided-OPD 按 turn 概率混合 teacher/student 执行，并逐渐将 teacher 介入概率降到零；student turns 用 reverse KL、teacher turns 用 forward KL。 [原文 Abstract、§3、§4.1](https://arxiv.org/html/2606.15912v2)

## Key Results
【作者报告，未复现】摘要报告相对 vanilla OPD，平均 Score +21.1%、SR +25.5%；保留作者原指标口径。 [原文 Abstract、§3、§4.1](https://arxiv.org/html/2606.15912v2)

## Assumptions
【证据边界】阅读层级：摘要＋方法、实验设置与局限；依据 Abstract、§3、§4.1。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】主要验证三类文本离散动作环境和同 family transfer；开放工具/API 的外推未验证。 [原文 Abstract、§3、§4.1](https://arxiv.org/html/2606.15912v2)

## Reusable Ingredients
【解释】分别定义谁执行 action、哪种 KL 监督以及退火时机。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G1](../gap_map.md#g1)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 Abstract、§3、§4.1](https://arxiv.org/html/2606.15912v2)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2606.15912)。

> Multi-turn agents that plan, invoke tools, and interact with environments offer a promising paradigm for solving complex tasks, yet their …
