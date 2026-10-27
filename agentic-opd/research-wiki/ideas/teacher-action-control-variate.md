---
type: idea
node_id: idea:teacher-action-control-variate
title: "将 teacher 从优化目标改为无偏 RL 控制变量"
stage: proposed
outcome: pending
added: 2026-10-18T17:03:50Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G2", "gap:G5"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "recommended"]
---

# 将 teacher 从优化目标改为无偏 RL 控制变量

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：ASTRA-03；主候选2，高风险。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。

## Thesis
具体方法（未验证）：

1. 共同 OPD 热身后，用实际 returns 校准 teacher log-prob，使其预测 token 或 action 的后续收益。
2. 在策略梯度中减去该动作相关预测，并加入其在 student 分布下期望的解析梯度。
3. 交叉拟合校准器，保证 teacher 主要减少估计方差，而不持续改变目标最优策略。

猜测：teacher 信号与回报相关但存在系统偏差，适合作为控制变量。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
Q-Prop已有action-dependent control variate，vOPD已有OPD baseline。必须证明同总成本task梯度收益；on-policy、冻结且独立/交叉拟合c、精确或无偏期望是边界。PPO clipping、GRPO标准差归一化与忽略尾部不能自动继承无偏性。

原始风险：全零奖励阶段无法凭无偏估计创造学习信号；不能宣称替代早期探索引导。

最小验证：从相同热身 checkpoint 比较梯度方差、固定预算成功率和 teacher 错误继承；若相关性不足或方差上升，则否证。

成本：复用 teacher logits，加轻量校准器和词表期望；不增加环境 rollout，完整词表处理可能增加显存。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

