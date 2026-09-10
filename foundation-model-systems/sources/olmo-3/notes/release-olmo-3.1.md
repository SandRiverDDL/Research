# Olmo 3.1 Release Delta

```yaml
---
source_id: olmo-3
section_type: stage-note
stage: release-delta
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Olmo 3.1 Think 32B 不是新 recipe，而是在 Olmo 3 Think 最佳 RL run 上继续训练：额外 21 天、224 GPUs，并对 Dolci-Think-RL 数据增加 epochs。[blog-release]
- Olmo 3.1 Instruct 32B 把原来 7B Instruct 的 SFT/DPO/RL 路线扩到 32B，填补 fully-open general chat/tool-use 的 scale gap。[blog-release]
- Olmo 3.1 同时刷新 RL-Zero 7B Code 与 Math checkpoints，官方将提升归因于更长、更稳定的训练 run。[blog-release]

## Why It Matters

这是一个少见的公开“继续同一 RL run”案例，可用于研究长 schedule 是否仍有收益、训练稳定性如何随时间变化，以及 recipe 从 7B 扩到 32B 时是否保持。它应该作为 Olmo 3 lineage delta，而不是重建独立 dossier。

## Mechanism Sketch

1. 从 Olmo 3 32B Think 的最佳 RL checkpoint 恢复。
2. 在相同 Dolci-Think-RL family 上延长训练并增加 epochs。
3. 同时把 Instruct recipe 从 7B 扩到 32B。
4. 对 RL-Zero Code/Math 运行更长、更稳定的训练并发布 checkpoints。[blog-release]

## Details / Evidence

- 官方报告 Think 32B 在 math、reasoning、instruction following、coding 与 multi-step tasks 上继续提升；这些数字是 release eval，不应替代 run logs 与 variance。[blog-release]
- 该 delta 保持 Olmo 的 fully-open model-flow framing：data、code、weights 与 checkpoints 仍可追踪。[blog-release]
- 3.1 说明原始 Olmo 3 recipe 仍有 schedule headroom，但不能由单次 continuation 推出无限 scaling。

## Gaps / Open Questions

- 继续训练过程中是否改变 learning rate、sampling policy、data order 或 reward mix，blog 没有完整列出。
- 需要进一步对照 released logs/checkpoints，分离“更多 compute”和“更稳定 implementation”的贡献。
- 32B Instruct 是否完全复用 7B mixture/weights，还是做了 scale-specific 调整。

## Lookup-only

- 训练时长、GPU 数与 headline improvement：`[blog-release]`。

## Evidence Anchors

- `[blog-release]`: https://allenai.org/blog/olmo3 （Update 12/12: Announcing Olmo 3.1）。
