# Kimi K2.5 Multimodal Training

```yaml
---
source_id: kimi-k2.5
section_type: stage-note
stage: multimodal-training
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Kimi K2.5 的多模态核心是 joint text-vision optimization：视觉不是后挂的 adapter，而是在 pretraining 和 RL 中共同优化。[2-4]
- TR 的关键结论是早期、低比例视觉融合比 late/high-ratio visual data 更好；这说明多模态能力要尽早进入 scaling ladder，而不是最后补数据。[2-3]
- Zero-vision SFT 是最值得记的设计：SFT 只用 text trajectories，依靠 pretraining 对齐激活视觉 agent 能力，同时避免人工视觉轨迹带来的泛化问题。[3-4, 8]
- MoonViT-3D 统一 image/video encoder，使用 native resolution、NaViT packing、4-frame video grouping 和 temporal compression 支撑长视频/多帧输入。[7]

## Why It Matters

这对后训练很有启发：如果 pretraining 已经完成跨模态对齐，SFT 阶段未必需要堆人写的视觉轨迹，反而可能因为格式和行为分布不自然而伤害泛化。对基模方向，视觉比例、加入时机、视频压缩和训练效率是核心 taste。

## Mechanism Sketch

1. 从 Kimi K2 text MoE base 出发，接入 MoonViT-3D 和 projector。
2. 先训练 vision encoder，再进行 15T 级 vision-text joint pretraining。
3. Long-context midtraining 把 context 从 32K 扩到 262K。
4. SFT 阶段主要用 text traces，强化 instruction/tool/reasoning 行为。
5. RL 阶段恢复 joint text-vision optimization，用 visual rewards 和 general rewards 同时训练。

## Details / Evidence

- K2.5 使用 1.04T total / 32B active Kimi K2 foundation，384 experts、8 active experts。[6-7]
- Vision encoder 从 SigLIP-SO-400M 初始化，支持 patch packing；video 使用 4-frame grouping 和 temporal pooling，实现 4x temporal compression。[7]
- TR 报告 joint pretraining 15T vision-text tokens，long-context midtraining 500B -> 200B tokens，context 32,768 -> 262,144。[7-8]
- 作者认为人工视觉轨迹 SFT 会损害 generalization，因此用 zero-vision SFT 让文本 SFT 激活已对齐的视觉 agent 能力。[3-4, 8]

## Gaps / Open Questions

- 视觉数据的具体来源、清洗、比例搜索和“早期融合”ablation 细节仍需要回 appendix/figures。
- Zero-vision SFT 是否适用于 weaker base / poorer visual pretraining 的模型，不应直接外推。

## Lookup-only

- Vision/text ratio ablation figure 回查 `[21-23]`。
- 具体 multimodal benchmark scores 回查 `[12-13]`。

## Evidence Anchors

- 2-4: joint optimization and zero-vision SFT.
- 7-10: MoonViT-3D, pretraining, SFT/RL, DEP.
