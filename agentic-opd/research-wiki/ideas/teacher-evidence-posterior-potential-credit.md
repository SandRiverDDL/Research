---
type: idea
node_id: idea:teacher-evidence-posterior-potential-credit
title: "Teacher证据后验的势函数蒸馏"
stage: archived
outcome: pending
added: 2026-10-18T17:03:51Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G5"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "reserve"]
---

# Teacher证据后验的势函数蒸馏

**stage:** `archived`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：SOL-05；本轮暂不投入。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。archived仅表示本轮不推荐投入，不代表实验否证。

## Thesis
具体方法（未验证）：

1. 在有训练答案的Search-QA中，teacher评分正确答案在少量prefix下的条件概率，训练student状态势函数。
2. 用前后势函数差形成逐turn奖励，终点势设零，并训练对应的residual critic。
3. 结合环境奖励优化查询与停止决策；每次rollout冻结势函数，保持奖励望远镜抵消。

猜测：teacher对证据充分性的知识比其具体查询策略更容易传递，并能改善长程credit。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
potential shaping为经典机制；若V_new=V−Phi则TD residual逐项相同。剩余贡献只能来自更好的价值先验或优化，不是新信用分配。

原始风险：teacher先验知识可能掩盖证据作用；势函数近似误差会影响有限样本优化。

最小验证：查询上限4/8/16，加入无关检索；比较ATOD加普通critic、teacher初始化critic。若普通critic等效，方法贡献不足。

成本：每轨迹抽两个prefix评分答案；增加小value head，无teacher环境续跑。成本随答案长度和抽样边界数增长。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

