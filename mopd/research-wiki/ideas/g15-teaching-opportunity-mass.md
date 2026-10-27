---
type: idea
node_id: idea:g15-teaching-opportunity-mass
title: "教学前缀概率质量保护（S4条件推荐）"
stage: proposed
outcome: pending
added: 2026-10-15T14:00:13Z
based_on: ["paper:gao2026_openmopd_diagnosing_fixing", "paper:zhu2026_upmopd_update_projection"]
target_gaps: ["gap:G15"]
tags: ["g15", "l2"]
---

# 教学前缀概率质量保护（S4条件推荐）

**stage:** `proposed`  ·  **outcome:** `pending`

C04 · L2 · 来源 A4, S4；本轮推荐，待验证。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. 固定A/B监督预算；收集A自采样的定长前缀，经少量探测筛出能产生A学习收益的区域，保存采样概率。
2. B更新提交前，用前缀likelihood ratio估计这些区域的概率质量变化；若下降超过阈值，对实际optimizer displacement施加一个机会质量下界约束。
3. 提交修正更新，滚动替换已学会的前缀；A监督量和loss尺度保持固定。

【待验证假设】B可能降低student进入A可学习轨迹区域的概率；保护这些区域能改善后续A监督的有效性。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】仅S4条件推荐：有效区域定义、采样测度与likelihood-ratio估计尚未闭合，须先对应fresh root频率及后续收益。A4为CAUTION，常见hinge近似触发式CE replay，不继承S4结论。

主推荐/条件推荐不是通过实验。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

