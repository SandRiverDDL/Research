---
type: idea
node_id: idea:bayes-consistent-hindsight-belief-distillation
title: "用回看信息蒸馏信念更新，避免蒸馏全知动作"
stage: proposed
outcome: pending
added: 2026-10-18T17:03:50Z
based_on: ["paper:tan2026_atod_annealed_turnaware"]
target_gaps: ["gap:G2", "gap:G5"]
tags: ["agentic-opd", "method", "atod-2026-10-19", "recommended"]
---

# 用回看信息蒸馏信念更新，避免蒸馏全知动作

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-19 ATOD全文驱动：ASTRA-05；主候选1。same-family provisional，outcome pending；用户尚未选题。[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)。

## Thesis
具体方法（未验证）：

1. Student自主rollout；外部teacher回看真实轨迹，为prefix确定的任务变量输出后验分布。
2. Student只用当时历史，通过forward cross-entropy学习该belief；成功和失败均采样。
3. Actor在训练与部署都读取student自己预测的belief，用task reward训练行动。Teacher回看信息只进标签。

猜测：部分深层失败来自错误信念持续传播；合理的回看监督可训练更新规则。

[全文分析与最终方法版本](../../idea-stage/atod-ideas-2026-10-19.md)包含最近工作、公式条件和停止标准。

## Key risks
Privileged POMDP belief learning与Meta-RL task inference已存在；此方案延续旧ledger。teacher软后验校准、prefix确定schema、成功失败不偏采样与部署真实使用belief必须成立；未来标签本身不等于泄漏。

原始风险：teacher 后验错误会污染标签；不能把事后正确答案直接当成早期确定性 action target。

最小验证：控制关键证据出现时刻，测证据前校准和证据后更新；若提前表现为全知或仅靠答案泄漏获益，则否证。

成本：每条完成轨迹一次 teacher 标注，复用于多个 prefix；额外训练成本取决于抽样 prefix 数。 本轮无GPU计时或效果验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

