---
type: idea
node_id: idea:evidence-separated-decision-target
title: "切断错误 reasoning 对 teacher 决策的反向污染"
stage: proposed
outcome: pending
added: 2026-10-18T17:03:50Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G2"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "reserve"]
---

# 切断错误 reasoning 对 teacher 决策的反向污染

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：ASTRA-01；靶点验证储备。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。

## Thesis
具体方法（未验证）：

1. 固定真实交互历史，仅改变student自产reasoning，先测teacher目标是否被带偏。
2. 仅当靶点成立，teacher看真实证据视图、student保留完整历史，训练action目标并结合task RL。
3. 与SOPD、随机reasoning dropout、等长摘要匹配成本，暂不叠加一致性模块。

猜测：部分低 disagreement 来自 teacher 被错误解释诱导，而非双方都缺少行动能力。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
SOPD/GC-OPD/ActionOPD近邻；先固定真实交互、改变reasoning测teacher action漂移。若只是短上下文或dropout收益，不足方法成篇。

原始风险：删掉正确推断也会丢信息；不能把事实视图偷偷构造成完整可观测状态。

最小验证：固定真实 action/observation，仅改写错误 reasoning；测 teacher action 漂移和训练收益。若漂移很小或清理后收益消失，则否证。

成本：每 turn 一份事实视图与一次 teacher target；可用更短上下文替代原评分，避免环境分叉。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

