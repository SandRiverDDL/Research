# Harness RL failure-modes

初始分析标签，表示待核查的机制维度，不代表已证实的普遍失效。

- `harness-overfitting`: policy 依赖训练期 harness，迁移后收益消失。
- `state-interface-mismatch`: 状态呈现或工具语义变化破坏训练部署一致性。
- `budget-confounding`: 工具次数、上下文长度或推理成本不一致造成混淆。
- `compaction-credit-break`: 分段训练丢失最终结果对早期动作或摘要的反馈。
- `token-alignment-error`: harness 变换后的上下文与真实采样 token / 概率对不齐。
- `harness-specific-overfitting`: 目标 harness 上适配但未见 harness 上迁移弱。
- `cross-harness-interference`: 多 harness 的更新相互干扰。
