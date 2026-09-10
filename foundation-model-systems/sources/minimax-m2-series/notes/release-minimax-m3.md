# MiniMax-M3 Release Delta

```yaml
---
source_id: minimax-m2-series
section_type: stage-note
stage: release-delta
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- M3 是 MiniMax 当前 model line：约 428B total / 23B active、native multimodal、1M context，并引入 MiniMax Sparse Attention（MSA）。[m3-model-card]
- MSA paper 是 architecture/serving source，不是完整 M3 post-training TR；M3 的 coding/cowork 能力与三种 thinking modes 已公开，但训练 recipe 没有同步公开。[m3-model-card, m3-msa]
- M3 与 M2 应写成“current-practice model delta + M2 lineage-reference”，不能默认继承 M2 的 Forge、self-evolution 或 interleaved thinking。[m3-blog, m3-model-card]

## Why It Matters

M3 改变了 MiniMax 当前系统约束：native multimodality、million-token context 与 sparse attention 会改变 agent rollout、long-context data 和 serving cost。对 post-training 工作，更重要的结论是公开不足，不能从能力榜单补 recipe。

## Mechanism Sketch

1. 从训练开始混合 text/image/video tokens，形成 native multimodal base。[m3-model-card]
2. MSA 的 index branch 选择 KV blocks，main branch 再执行 block-sparse attention。[m3-msa]
3. 模型暴露 `enabled`、`adaptive`、`disabled` 三种 reasoning modes。[m3-model-card]
4. Release materials 强调 coding、cowork 与 long-horizon agent capability，但 SFT/RL/data/consolidation 未披露。[m3-blog]

## Details / Evidence

- 官方 model card 给出相对 M2 的 1M-context prefill/decode speedup；这是同厂 serving measurement，不是独立 quality ablation。[m3-model-card]
- MSA 通过 indexer/main-branch 对齐与 sparse kernel 支撑长上下文，适合放入 architecture lens。[m3-msa]
- MaxProof 是 M3 series 的 math-proof expert/workstream，但仅凭该材料无法重建 M3 最终 expert merge。[maxproof]

## Gaps / Open Questions

- 是否继承 M2 的 Forge/self-evolution、具体 agent environment 与 rollout system。
- Multimodal SFT/RL mixture、reward/verifier、expert consolidation 与 safety alignment。
- Adaptive thinking 是训练出的 mode policy、prompt routing 还是 inference controller，未公开。
- M3 release blog 曾承诺后续 technical report；截至本次核查，官方关联论文主要仍是 MSA，而非完整 training TR。

## Lookup-only

- 参数量、context、reasoning mode 与部署参数：`[m3-model-card]`。
- MSA 公式、kernel 与效率表：`[m3-msa]`。

## Evidence Anchors

- `[m3-blog]`: https://www.minimax.io/blog/minimax-m3
- `[m3-model-card]`: https://huggingface.co/MiniMaxAI/MiniMax-M3
- `[m3-msa]`: https://arxiv.org/abs/2606.13392
- `[maxproof]`: https://arxiv.org/abs/2606.13473
