---
type: idea
node_id: idea:amortized-external-teacher-correction-model
title: "外部Teacher纠正信号的在线摊销"
stage: archived
outcome: pending
added: 2026-10-18T17:03:51Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G2"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "reserve"]
---

# 外部Teacher纠正信号的在线摊销

**stage:** `archived`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：SOL-06；本轮暂不投入。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。archived仅表示本轮不推荐投入，不代表实验否证。

## Thesis
具体方法（未验证）：

1. 在固定比例的完整student轨迹上查询teacher，获取真实token log-prob纠正信号。
2. 用冻结student特征训练小型纠正预测器，并以保留的teacher标签校准误差。
3. 其余轨迹使用预测信号；优先刷新高预测误差轨迹，同时保留随机teacher查询下限。

猜测：teacher纠正信号具有可压缩结构，足以用低成本模型覆盖常见状态。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
proxy teacher、active distillation近邻；需胜过随机查询/缓存/普通小teacher，在漂移下证明同总算力收益。

原始风险：student持续变化造成分布漂移；预测器置信度可能无法识别系统误差。

最小验证：固定总teacher FLOPs比较ATOD抽样查询、随机缓存和在线摊销；若预测误差累积使收益消失，压缩假设失败。

成本：teacher计算约为原来的查询比例f，加全轨迹小预测头；扫描长prefix的成本仍须实测。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

