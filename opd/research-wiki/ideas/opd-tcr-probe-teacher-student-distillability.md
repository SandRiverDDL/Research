---
type: idea
node_id: idea:opd-tcr-probe-teacher-student-distillability
title: "Teacher-Causal Response Probe (TCR-Probe)"
stage: archived
outcome: unknown
added: 2026-08-21T07:04:46Z
based_on: []
target_gaps: []
tags: ["opd", "teacher-student-gap", "distillability", "archived", "user-rejected"]
---

# Teacher-Causal Response Probe (TCR-Probe)

**stage:** `archived`  ·  **outcome:** `unknown`

在完整 OPD 前，用匹配的 TEACH 与 frozen-SELF 微训练分支测量 teacher-specific response，并按 verifier headroom 归一化。

## Thesis
归一化的 teacher-specific 微训练响应或许能在未见 teacher–student–data 三元组上排序完整 OPD 增益。

## Key risks
用户已明确否定该方向：训练前预测可蒸馏性的基本问题被 Rethinking OPD/capacity-gap 文献明显覆盖，且跨 family/data 的 transport 假设过强。该 idea 未经实验，因此 outcome 保持 unknown。来源：ideaspark_run/teacher-student-distillability/phase4/idea.std.zh.md。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

