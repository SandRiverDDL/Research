# Open-Reasoner-Zero Critic and Advantage

```yaml
---
source_id: open-reasoner-zero
section_type: rl-training
stage: post-training
substage: rl-training
depth: deep
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- ORZ 的核心主张是：即使只有 sparse terminal reward，learned critic 也能对进入 repetition/degeneration 的 token states 给出更低 value。[5, 10-11]
- GRPO 的 group-normalized response reward 没有 learned token-state baseline，因此正负信号无法针对局部行为细分。[5]
- 项目连 critic weights 一并开放，使 value estimation 成为可检查 artifact，而不是隐藏的训练组件。[3, repo]

## Why It Matters

Long-CoT RL 的关键不只是 optimizer 名称，而是 credit 沿 trajectory 如何分配。如果 critic 能在 terminal reward 到来前识别局部 failure pattern，其额外成本可能是值得的。

## Mechanism Sketch

1. 用最终 binary return 监督 `V(s_t)`。
2. 对成功回答，高 value state 的正 advantage 较小，意外恢复成功的 state 获得更大信号。
3. 对失败且重复的回答，critic 可以在结束前学到 value decline。
4. PPO 使用这些 token-wise advantages 更新 policy。[4-6, 10-11]

## Details / Evidence

- 论文展示了 repetition 附近的 critic/value estimate，并分析 advantage 是否能识别不良 pattern。[10-11]
- 这比单纯 benchmark 对比更有机制证据，但仍只覆盖一套 implementation 与 data distribution。

## Gaps / Open Questions

- 非平稳 long-horizon training 中的 critic calibration 未被充分刻画。
- Critic 的额外 memory/compute 应与更大 rollout group 或更多 fresh data 做等成本对比。
- Binary math/code reward 上的结论能否迁移到 multi-turn agent trajectory 仍未知。

## Lookup-only

- Critic curves 与案例：第 10-11 页。

## Evidence Anchors

- 5：PPO vs GRPO rationale。
- 10-11：critic 与 advantage 分析。
