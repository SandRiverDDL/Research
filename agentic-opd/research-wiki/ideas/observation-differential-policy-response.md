---
type: idea
node_id: idea:observation-differential-policy-response
title: "观察差分策略蒸馏"
stage: archived
outcome: pending
added: 2026-10-18T17:03:51Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G2"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "reserve"]
---

# 观察差分策略蒸馏

**stage:** `archived`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：SOL-01；本轮暂不投入。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。archived仅表示本轮不推荐投入，不代表实验否证。

## Thesis
具体方法（未验证）：

1. 从自然rollout匹配同一页面或工具状态、关键属性不同的观察对，校验可用动作兼容。
2. 让teacher输出两侧短action分布，student学习动作概率变化；对无关属性变化学习不变性。
3. 把成对训练与原有OPD、terminal RL联合，真实交互继续由student采样。

猜测：部分错误来自策略忽略新证据；单点模仿不足以传递正确的观察响应。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
与旧观察差分候选延续；必须超越完全相同成对数据的普通OPD，不能将数据收益算成差分loss贡献。

原始风险：观察配对可能遗漏隐藏状态；teacher差分也可能错误。

最小验证：WebShop属性选择，对比ATOD、ActionOPD及普通成对增广。若收益完全由额外样本解释，差分机制被否证。

成本：每10条轨迹抽一对，每对两次短teacher动作预测；无环境分叉，额外成本随配对率和动作候选数增长。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

