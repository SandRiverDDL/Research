---
type: idea
node_id: idea:teacher-plan-portfolio-exploration
title: "蒸馏可执行策略组合，而不是单一路径偏好"
stage: archived
outcome: pending
added: 2026-10-18T17:03:50Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G2"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "reserve"]
---

# 蒸馏可执行策略组合，而不是单一路径偏好

**stage:** `archived`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：ASTRA-02；本轮暂不投入。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。archived仅表示本轮不推荐投入，不代表实验否证。

## Thesis
具体方法（未验证）：

1. 每个任务由外部 teacher 提出少量不同的高层计划，使用固定长度结构表示。
2. student 学习计划分布，自采样计划并完成全部交互；组内 outcome 分别更新计划选择和执行策略。
3. teacher 定期纠正 student 自产计划的缺失步骤，保留多个有效计划的概率质量。

猜测：小 student 的探索瓶颈包含策略同质化；token 熵不能保证组内策略多样性。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
层次options与计划数据增广已有；需超越同teacher tokens、同rollout数的普通计划多样化。

原始风险：计划可能束缚执行；推理时计划必须由 student 生成，避免隐含 teacher 依赖。

最小验证：固定 rollout、teacher token 总额，比较成功策略覆盖与全零奖励组比例；若只增加语言多样性而不增加有效探索，则否证。

成本：每组一次短 teacher 计划生成，随计划数和长度增长；执行仍为原有 G 条 student rollout。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

