---
type: idea
node_id: idea:blackbox-conditional-action-density-ratio
title: "黑盒Teacher的条件密度比蒸馏"
stage: archived
outcome: pending
added: 2026-10-18T17:03:51Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G2"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "reserve"]
---

# 黑盒Teacher的条件密度比蒸馏

**stage:** `archived`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：SOL-08；本轮暂不投入。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。archived仅表示本轮不推荐投入，不代表实验否证。

## Thesis
具体方法（未验证）：

1. 在抽样student状态上取得少量teacher短action，与同状态student动作组成来源分类数据。
2. 训练条件判别器，使用其logit近似teacher与当前student的action密度比。
3. 以该比值提供OPD信号并结合真实奖励；随student更新刷新负样本，监督作用于可执行action。

猜测：分布层监督能保留teacher的多种有效策略，并支持无logits、异tokenizer教师。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
GAD §2已覆盖teacher/student判别器、在线负样本与策略奖励；动态agent场景本身不足形成新算法。

原始风险：判别器可能识别语言风格而非决策质量；稀疏状态监督造成比值偏差。

最小验证：同teacher样本预算比较ActionOPD、teacher-action SFT及密度比方法；若模式覆盖与成功率无收益，分布匹配假设失败。

成本：仅抽样状态请求1—2个短action，加小判别器；不执行teacher续轨，成本随查询率线性增长。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

