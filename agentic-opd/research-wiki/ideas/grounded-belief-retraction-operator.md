---
type: idea
node_id: idea:grounded-belief-retraction-operator
title: "证据锚定的信念撤销蒸馏"
stage: archived
outcome: pending
added: 2026-10-18T17:03:51Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G2"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "reserve"]
---

# 证据锚定的信念撤销蒸馏

**stage:** `archived`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：SOL-02；本轮暂不投入。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。archived仅表示本轮不推荐投入，不代表实验否证。

## Thesis
具体方法（未验证）：

1. teacher批量标注轨迹中被当前观察推翻的旧判断，输出“撤销旧判断—引用新证据—更新判断”。
2. 只保留证据时间不晚于当前turn的标签，训练student生成短更新操作。
3. 让动作策略读取student自身更新结果，并联合OPD与环境奖励训练。

猜测：错误prefix压低监督价值，部分原因是模型持续沿用已经失效的内部判断。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
延续旧belief ledger；可能只是memory schema变化。完整MemOPD与等长摘要应分别作为对照，不混同两者。

原始风险：未来信息泄漏；引用存在也不能保证逻辑关系正确。

最小验证：WebShop改选属性、ALFWorld错误位置判断；对比普通摘要与同长度teacher解释。若撤销标签无额外贡献，机制被否证。

成本：每条失败轨迹一次批量标注；student只在候选冲突处输出短更新。成本随失败率与标签长度增长。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

