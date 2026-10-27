---
type: idea
node_id: idea:reversible-error-inoculation-on-policy
title: "可逆错误的交互式免疫训练"
stage: archived
outcome: pending
added: 2026-10-18T17:03:51Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G1"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "reserve"]
---

# 可逆错误的交互式免疫训练

**stage:** `archived`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：SOL-07；本轮暂不投入。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。archived仅表示本轮不推荐投入，不代表实验否证。

## Thesis
具体方法（未验证）：

1. teacher从环境暴露的可逆动作中选择一次有教学价值的偏离，如错误选项或绕路。
2. 在少量真实student轨迹中执行该偏离，随后由student自主恢复并接受teacher监督。
3. 注入动作不进入actor loss；根据实际恢复成功率调整错误类型，持续保留正常rollout。

猜测：自然on-policy采样对稀有、可恢复错误覆盖不足，导致部署时恢复能力脆弱。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
与recovery curriculum/扰动增广近邻；同环境步数随机扰动若等效则teacher选错机制不成立。

原始风险：表面可逆不代表任务预算内可恢复；teacher可能挑选过易错误。

最小验证：未见错误组合与正常成功率双测；等环境步数比较随机扰动。若随机扰动等效或正常表现下降，教学假设失败。

成本：例如10%轨迹额外2—4步；无需reset分叉，成本由注入率和恢复长度控制。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

