---
type: idea
node_id: idea:g15-sampling-distribution-gradient
title: "跨teacher采样分布梯度修正"
stage: archived
outcome: pending
added: 2026-10-15T14:00:13Z
based_on: ["paper:gao2026_openmopd_diagnosing_fixing", "paper:sun2026_d³mopd_dynamic_domain"]
target_gaps: ["gap:G15"]
tags: ["g15", "l2"]
---

# 跨teacher采样分布梯度修正

**stage:** `archived`  ·  **outcome:** `pending`

C05 · L2 · 来源 A5, S6；本轮未优先，归档保留，不是负实验或永久排除。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. B更新后，从当前student为A生成两个小轨迹批次；每批由A评分，并分别在临时参数副本上执行一次虚拟A更新。
2. 用同一组独立A探针测量虚拟更新带来的loss下降，作为该批轨迹的教学收益；丢弃临时参数。
3. 将中心化教学收益作为整批轨迹的score-function回报，执行一次采样分布校正，再继续正式多teacher训练。

【待验证假设】某些B更新损害的是随后A样本的可教学性；直接奖励能够产生A学习收益的自采样轨迹，能够修复这种跨teacher反馈。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】E-MAML、MPL及元探索直接覆盖基础机制；需证明B引起的特异采样外部性，score项不是完整无偏meta-gradient。

归档仅表示本轮不优先，允许新证据后重审。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

