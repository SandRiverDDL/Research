---
type: idea
node_id: idea:semantic-quotient-action-distillation
title: "在可证明等价的行动类上蒸馏"
stage: archived
outcome: pending
added: 2026-10-18T17:03:51Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G2"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "reserve"]
---

# 在可证明等价的行动类上蒸馏

**stage:** `archived`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：ASTRA-08；本轮暂不投入。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。archived仅表示本轮不推荐投入，不代表实验否证。

## Thesis
具体方法（未验证）：

1. 利用工具 schema、参数规范化和环境规则，将等价调用归入同一 action class。
2. 将 teacher 的行动建议聚合为类分布，student 学习选类，并独立生成合法调用和 reasoning。
3. 类间进行蒸馏，类内由执行反馈优化，允许学生保留不同表述及实现。

猜测：部分 disagreement 来自序列实现差异，而不是决策错误。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
ASL与ActionOPD覆盖行动语义/转移等价；schema能证明的部分可能只剩格式规范化。

原始风险：真实等价关系可能难以确定；自由文本搜索不能仅凭语义相似就合并为同一行动。

最小验证：改变合法 alias、工具参数顺序与等价接口，测跨接口迁移；若原收益仅来自降低格式错误，则否证核心假设。

成本：有限行动集可批量评分；开放工具需采样 teacher 行动，成本随候选数增长；无需环境恢复。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

