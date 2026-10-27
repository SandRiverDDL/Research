---
type: idea
node_id: idea:g15-channel-split-rejoin
title: "通道分裂与重合"
stage: archived
outcome: pending
added: 2026-10-15T14:00:14Z
based_on: ["paper:zhu2026_upmopd_update_projection", "paper:liu2026_pmopd_task_ordering"]
target_gaps: ["gap:G15"]
tags: ["g15", "l5"]
---

# 通道分裂与重合

**stage:** `archived`  ·  **outcome:** `pending`

C09 · L5 · 来源 A9；本轮未优先，归档保留，不是负实验或永久排除。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. 在少数MLP层复制部分通道，将输出权重平分；用成对参数μ±λδ表示复制通道，λ=0时严格保持原函数。
2. 逐渐增大λ，以原有A/B教师进行联合OPD，让临时增加的自由度承担能力整合过程中的冲突。
3. 逐渐将λ收回零，同时继续优化共享中心μ；成对通道重合后合并输出权重，恢复原student宽度并评测。

【待验证假设】原容量存在较好的联合解，但固定参数化下的受保护路径难以抵达；临时增宽能提供可收缩的绕行通道。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】Net2Net和ExpandNets已有增宽/收缩；非线性通道不能一般精确压回，收益可能依赖临时容量。

归档仅表示本轮不优先，允许新证据后重审。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

