---
type: idea
node_id: idea:g15-temporary-capability-buffer
title: "临时能力残差与零残差回收"
stage: archived
outcome: pending
added: 2026-10-15T14:00:14Z
based_on: ["paper:zhu2026_upmopd_update_projection", "paper:liu2026_pmopd_task_ordering"]
target_gaps: ["gap:G15"]
tags: ["g15", "l5"]
---

# 临时能力残差与零残差回收

**stage:** `archived`  ·  **outcome:** `pending`

C13 · L5 · 来源 S8；本轮未优先，归档保留，不是负实验或永久排除。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. 给已学A的student添加训练期低秩残差，并用已知训练域标签启用；A轨迹由带残差的当前student自采样。
2. 让共享主干学习B，同时在A轨迹上拟合残差以承接主干更新造成的A损伤；不投影主干B更新。
3. 逐步把残差门控降到零，通过联合teacher OPD将能力回收到主干；最终删除残差，仅评估原架构student。

【待验证假设】最终原架构具有联合容量，但直接共享参数学习受到路径限制；临时缓冲能把获得B与回收A分开完成。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】Progress & Compress/FOSTER已有扩容压缩；必须撤残差后保收益且超过普通expand/compress。

归档仅表示本轮不优先，允许新证据后重审。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

