---
type: idea
node_id: idea:g15-teacher-commutator-steering
title: "教师更新对易子转向"
stage: archived
outcome: pending
added: 2026-10-15T14:00:13Z
based_on: ["paper:liu2026_pmopd_task_ordering", "paper:zhu2026_upmopd_update_projection"]
target_gaps: ["gap:G15"]
tags: ["g15", "l5"]
---

# 教师更新对易子转向

**stage:** `archived`  ·  **outcome:** `pending`

C08 · L5 · 来源 A8, S9；本轮未优先，归档保留，不是负实验或永久排除。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. 每隔K步固定A/B轨迹与预条件器，从同一θ分别虚拟执行AB、BA两种更新，计算顺序差c=θ_AB−θ_BA。
2. 提取c中普通加权更新无法表达的分量，用少量系数构造θ+d+κc候选终点；d取原有联合更新。
3. 用独立轨迹选择满足A终点保护且改善B的候选，分两段执行d和κc；宏步后重新检验，允许中间A暂时下降。

【待验证假设】教师更新不交换产生的曲率方向包含有效绕行通道；逐步一阶保护可能删除进入这些通道所需的位移。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】Commute Your Domains已有交换子与顺序效应；显式方向必须胜过等成本AB/BA选择，且考虑optimizer状态及噪声。

归档仅表示本轮不优先，允许新证据后重审。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

