---
type: idea
node_id: idea:budget-neutral-random-horizon-opd
title: "随机化交互预算，恢复被截断的深层学习信号"
stage: archived
outcome: pending
added: 2026-10-18T17:03:51Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G5"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "reserve"]
---

# 随机化交互预算，恢复被截断的深层学习信号

**stage:** `archived`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：ASTRA-07；本轮暂不投入。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。archived仅表示本轮不推荐投入，不代表实验否证。

## Thesis
具体方法（未验证）：

1. 在固定平均交互预算下，为组内 rollout 分配具有长尾的随机 horizon。
2. 记录每一步继续采样的已知概率，对深层 teacher 信号和完成回报做存活概率校正。
3. 联合优化经过校正的 OPD 与 RL，避免将被预算截断的轨迹直接视作完整失败。

猜测：部分深层能力缺口来自训练数据的截断机制，而非深层 turn 本身缺少权重。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
随机截断与重要性校正已有；长尾方差及同步成本可能抵消深状态覆盖优势。

原始风险：若任务本身定义硬 deadline，则延长 horizon 改变任务；不能以此声称原任务收益。

最小验证：固定总环境步数和 teacher token，比较长任务成功率；若优势在同等 horizon 覆盖对照下消失，则否证。

成本：期望 rollout 成本不变，但长尾 episode 增加并行等待；校正权重需要控制方差。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

