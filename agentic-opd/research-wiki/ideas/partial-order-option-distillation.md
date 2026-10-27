---
type: idea
node_id: idea:partial-order-option-distillation
title: "将 teacher 指导编译为可复用的子目标依赖程序"
stage: archived
outcome: pending
added: 2026-10-18T17:03:50Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G5", "gap:G6"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "reserve"]
---

# 将 teacher 指导编译为可复用的子目标依赖程序

**stage:** `archived`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：ASTRA-04；本轮暂不投入；与SOL-04机械合并。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。archived仅表示本轮不推荐投入，不代表实验否证。

## Thesis
具体方法（未验证）：

1. teacher 从已有 student 成功与失败轨迹提取子目标、前置条件和终止条件，形成小型依赖图。
2. student 学习生成该图，并用 option policy 执行当前可满足的子目标。
3. 环境反馈更新子目标完成状态；RL 优化具体路线，teacher 只修订失效的程序片段。

猜测：可迁移的教师知识主要是前置关系，而非固定动作顺序。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
与options、GC-OPD和项目旧时序契约方向近；人工契约验证与跨域schema成本可能主导收益。

原始风险：teacher 从轨迹推断的前置关系未必具有因果性，错误程序可能系统性阻止有效行为。

最小验证：训练已见子目标组合，测试新顺序与新组合；对照普通计划文本。若不能提高组合泛化或减少 teacher 调用，则否证。

成本：按任务簇生成、按失败片段修订，成本随独特程序数量增长；推理期程序和执行器均由 student 提供。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

