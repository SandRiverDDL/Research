---
type: idea
node_id: idea:teacher-knowledge-to-evidence-demand
title: "把 teacher 的参数知识转译为 student 的证据获取能力"
stage: archived
outcome: pending
added: 2026-10-18T17:03:51Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G6"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "reserve"]
---

# 把 teacher 的参数知识转译为 student 的证据获取能力

**stage:** `archived`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：ASTRA-06；本轮暂不投入。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。archived仅表示本轮不推荐投入，不代表实验否证。

## Thesis
具体方法（未验证）：

1. teacher 根据学生轨迹标出决策依赖但尚无外部证据支持的事实，生成短的证据需求。
2. student 学习将需求转成工具查询，并为使用的事实输出真实 observation 中的引用位置。
3. 蒸馏取证和证据绑定过程；最终回答由已有 outcome reward 优化。

猜测：小模型无法完整内化 teacher 知识，但能学习按需检索和核对。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
与普通query/evidence蒸馏和旧teacher-evidence-bottleneck差异不足；必须同检索预算比较。

原始风险：字符串引用不能证明证据蕴含结论；teacher 可能生成不可检索的证据需求。

最小验证：使用答案知识更新或长尾事实任务，匹配工具次数；若收益只来自增加搜索或直接泄漏答案，则否证。

成本：失败轨迹一次 teacher 需求标注；引用位置可机械核验，额外成本主要来自取证工具调用。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

