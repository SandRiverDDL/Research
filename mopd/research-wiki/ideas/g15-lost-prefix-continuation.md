---
type: idea
node_id: idea:g15-lost-prefix-continuation
title: "丢失前缀的当前student续写补偿"
stage: archived
outcome: pending
added: 2026-10-15T14:00:13Z
based_on: ["paper:gao2026_openmopd_diagnosing_fixing", "paper:tian2026_beyond_domainrouted_supervision"]
target_gaps: ["gap:G15"]
tags: ["g15", "l2"]
---

# 丢失前缀的当前student续写补偿

**stage:** `archived`  ·  **outcome:** `pending`

C06 · L2 · 来源 A6, S5；本轮未优先，归档保留，不是负实验或永久排除。 [完整报告](../../synthesis/g15-idea-report.md) · [查新证据](../../synthesis/g15-novelty-evidence.md)。

## Thesis
【方法候选】
1. 缓存A训练中可被A成功纠正的student前缀；B更新后重新计算其概率，只选择显著下降且仍可被A纠正的前缀。
2. 从这些前缀开始，让当前student重新生成后缀并接受A监督；不复用旧后缀，不对强制输入的前缀计算蒸馏loss。
3. 后缀学会后逐段缩短强制前缀，使被释放的段落重新进入student采样与A监督；最终撤掉桥接，并仅从根节点评测。

【待验证假设】B可能切断student进入A有效教学区域的路径；从尚可学习的后缀向根节点逐步恢复路径，比增加同量根节点rollout更有效。

原始变体均保留在[候选记录](../../.aris/traces/idea-creator/2026-10-15_run02/g15-candidates.json)。

## Key risks
【本轮审阅】STRIDE已有多teacher前缀fresh续写；Backplay已有渐退。conditional roll-in须在root部署分布产生收益。

归档仅表示本轮不优先，允许新证据后重审。所有pilot未运行；outcome=pending。审阅为same-family provisional。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

