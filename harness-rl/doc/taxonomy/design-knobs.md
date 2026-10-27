# Harness RL design-knobs

分析标签，须按原文核查具体机制。

- `context-compaction`: 摘要生成、触发规则与上下文重建。
- `segment-credit-assignment`: 跨压缩段的奖励与 advantage 传播。
- `rollout-training-alignment`: 真实生成 token、loss mask 与 log-prob 的一致性。
- `state-externalization`: policy 与 runtime 的状态管理分工。
- `cross-harness-evaluation`: 跨 harness 的迁移评测。
- `harness-conditioning`: 工具协议、观察格式、控制流与训练中 harness 的选择。
- `multi-harness-mixing`: 多 harness 的采样配比、batch 构造与更新调度。
