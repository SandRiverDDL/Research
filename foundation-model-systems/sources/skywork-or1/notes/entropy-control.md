# Skywork-OR1 Entropy Control

```yaml
---
source_id: skywork-or1
section_type: rl-training
stage: post-training
substage: rl-training
depth: deep
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Premature policy-entropy collapse 被当作与 held-out performance 下降相关的 failure mode，而不是抽象的 token-distribution 美学问题。[18-26]
- Adaptive entropy control 只在 entropy 低于 target 时启动，而不是整段训练持续添加固定 entropy bonus。[16-18, 24-26]
- 增加 SGD reuse/off-policy distance 会加快 collapse；更多 fresh rollouts 往往比在相同 trajectories 上多更新几次更有价值。[20-30]
- Compute 允许时，扩大 rollout batch/group size 可以提高最终表现；单纯增加同一数据上的 gradient steps 反而可能伤害 exploration。[20-30]

## Why It Matters

Entropy 同时是 diagnostic 与 controlled variable。可迁移原则是把 entropy 与 test performance、policy lag、data reuse 一起监控，而不是照搬一个 universal target。

## Mechanism Sketch

1. 全程记录 token entropy。
2. 比较 collapse timing 与 held-out eval。
3. 保持 rollout on-policy，并限制 trajectory reuse。
4. Entropy 低于 target 时才加入控制项。
5. 增加资源时优先购买 fresh rollout diversity，而不是重复 SGD。[16-30]

## Details / Evidence

- 实验分别改变 rollout batch、group size、mini-batches、SGD steps 与 reuse，以区分 diversity 和 policy-distance effects。[19-25]
- 仅增加 rollout diversity 并不能抵消 off-policy updates；freshness 是独立轴。[20-24]
- Target-entropy 效果对 coefficient 与 threshold 敏感，应该根据 development set 调整。[24-26]

## Gaps / Open Questions

- Entropy 与 capability 的因果关系仍被 update magnitude、policy lag 等因素混杂。
- Token-average entropy 可能掩盖 domain-specific 或 position-specific collapse。
- Agentic multi-turn trajectory 可能需要 action/tool entropy，而不是只看语言 token entropy。

## Lookup-only

- Ablation configurations 与 hardware allocation：第 19-30 页。
- Target entropy 与 coefficient：第 24-26、35-36 页。

## Evidence Anchors

- 16-18：adaptive entropy mechanism。
- 18-26：collapse studies。
- 27-30：resource-allocation studies。
