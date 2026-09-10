# Mistral 3 Claims and Gaps

```yaml
---
source_id: mistral-3
section_type: claims-and-gaps
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- 可信：Ministral 3 的 model lineage、Cascade Distillation、Instruct/Reasoning post-training flow 和局部 ablations 在 TR 中披露清楚。[3-10]
- 可信：Mistral 3 family 权重采用 Apache 2.0，Large 3 和 Ministral 3 均提供开放权重。[blog-mistral-3]
- 不足：Large 3 的 post-training 只有“after post-training”能力 claim，没有 method disclosure，不能进入 recipe comparison。
- 不足：Ministral 3 是开放权重与高层 recipe，不是 fully-open training project。

## Why It Matters

- 这个 source 最有价值的是阶段化 teacher/distillation/alignment 决策，而非官方 leaderboard positioning。
- 对用户当前工作，可信机制集中在 3B/8B/14B；Large 3 主要是 openness/serving reference。

## Details / Evidence

- 官方对 base/instruct/reasoning variants 使用内部统一 harness 重跑对照，优于直接拼接不同来源榜单，但仍缺 variance、完整 prompts 和外部 reproduction。[6-8]
- Teacher-selection、long-CoT mixture 和 post-RL ODPO 有方向性 ablation，足以支持 recipe judgment，但不足以估计绝对贡献和成本。[9-10]

## Gaps / Open Questions

- Large 3：pretraining tokens/data、multimodal alignment、SFT、preference/RL、reward 和 safety training 全部缺失。
- Ministral 3：训练 data/config/code/logs、compute budget、reward model 和 rubric judge 缺失。
- 发布时所称 frontier / best cost-performance 主要依赖官方 eval，需独立复现。

## Lookup-only

- Large 3: 675B total / 41B active，NVFP4 checkpoint，Apache 2.0。
- Ministral 3: 3B/8B/14B，每个 size 有 base/instruct/reasoning。

## Evidence Anchors

- 3-10: Ministral 3 TR。
- `[blog-mistral-3]`: family release and Large 3 claims。
