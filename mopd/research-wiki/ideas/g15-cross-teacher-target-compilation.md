---
type: idea
node_id: idea:g15-cross-teacher-target-compilation
title: "交叉学习反应驱动的监督目标编译"
stage: archived
outcome: pending
added: 2026-10-15T14:00:14Z
based_on: ["paper:tian2026_beyond_domainrouted_supervision", "paper:li2026_beyond_teacher_assignment"]
target_gaps: ["gap:G15"]
tags: ["g15", "l1"]
---

# 交叉学习反应驱动的监督目标编译

**stage:** `archived`  ·  **outcome:** `pending`

C12 · L1 · 来源 S3；本轮未优先，归档保留，不是负实验或永久排除。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. 在固定student prefixes上，为A的teacher logits添加训练专用低秩修正器；限制修正后的分布接近原teacher，并保持监督logratio尺度。
2. 通过短虚拟A更新和固定步数B更新训练修正器，使B的held-out学习收益提高；收益按B起点loss校正，同时约束A自身监督收益，交换A/B执行。
3. 常规OPD使用编译后的目标训练同一个student；修正器仅处理训练监督，部署时删除。

【待验证假设】同一teacher分布中存在教学效果近似等价的监督方向，其中部分方向会使另一个teacher后续更容易学习；单纯调权无法选择这些方向。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】MetaDistil已有student反馈改teacher；需区别于换quiz域并排除牺牲A、增大B起点误差。

归档仅表示本轮不优先，允许新证据后重审。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

