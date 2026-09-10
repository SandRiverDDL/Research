# Kimi K3 Architecture

```yaml
---
source_id: kimi-k3
section_type: stage-note
stage: architecture
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- K3 的 architecture 不是单点换 attention，而是同时扩展 sequence、depth、width 三个 information-flow axis：3:1 KDA/Gated MLA hybrid、Attention Residuals、Stable LatentMoE。[2-3]
- 2.78T total / 104.2B active 的容量扩展靠 LatentMoE 才能承受：routed expert 在 3584 latent width 中运行，16/896 experts active；两个 full-width shared experts 保留 common path。[6-11]
- 极端稀疏带来的关键问题不是“expert 数够不够”，而是 internal activation explosion 与 load imbalance；RMSNorm、SiTU-GLU、Quantile Balancing 是一组稳定性设计。[6-9]
- native vision 与 language backbone 从训练开始共同优化；MoonViT-V2 从零 next-token training，报告的 gradient-norm ablation 支持它比 SigLIP initialization 更稳定。[9-10]

## Why It Matters

K3 最值得内化的 architecture taste 是：超长 context 和超大 sparse width 不能分别处理。linear attention 降低 sequence-state 成本后，会暴露 recurrent kernel/parallelism 问题；expert pool 放大后，会暴露 routing、activation 与 communication 问题；更深网络则需要跨层信息通道。K3 用 architecture-system co-design 一起解决这些二阶瓶颈。

## Mechanism Sketch

```text
visual/text tokens
-> MoonViT-V2 + projector (vision only)
-> shared embedding
-> repeated [KDA x3 + Gated MLA x1]
-> each attention layer followed by Stable LatentMoE
-> AttnRes retrieves embedding / prior block representations
-> final global Gated MLA
```

## Details / Evidence

### Hybrid KDA / Gated MLA

- 每个 block 为 3 个 KDA + 1 个 Gated MLA，backbone 末尾再放一个 Gated MLA，确保最后一层有 global attention。[4-5]
- KDA 是带 channel-wise forget gate 的 delta recurrence；K3 将 log-decay 改为 lower-bounded scaled sigmoid，使 16-token tile 的 reciprocal rescaling 保持在 BF16 dynamic range 内，因而 diagonal/off-diagonal tiles 都可用 dense Tensor Core path。[4-5]
- MLA 采用 NoPE；KDA 提供 position-sensitive/recency-aware mixing，周期性 MLA 提供 unrestricted global content interaction，也避免 1M extension 时 retune RoPE/YaRN。[5]

### Attention Residuals

- AttnRes 将 depth 类比 sequence attention：当前 layer 不只接收累积 residual，而对 embedding 与前序 layer/block representations 做 learned weighted retrieval。[6]
- K3 使用 Block AttnRes，将 93 layers 分为 8 个 12-layer blocks（加 embedding 共 9 sources），把 state/memory/communication 从 layer-level 降到 block-level。[6]
- 报告引用外部 AttnRes work 的经验结论，但 K3 report 内没有独立 ablation 将 K3 增益单独归因到 AttnRes。

### Stable LatentMoE

- 896 routed experts、16 selected/token、2 shared experts；latent width 3584 是 hidden width 7168 的一半。[6-11]
- routed aggregation 后、up-projection 前加入 RMSNorm，降低不同 expert/route scale 对 full-width merge 的敏感性。[6-7]
- SiTU-GLU 对 gate/up 两支分别 soft-cap，保持 near-origin SwiGLU-like response，同时限制大正值相乘导致的 outlier。[7-8]
- Quantile Balancing 从 global-batch margin histogram 估计每个 expert 的目标 quantile，并在下一 step 更新 dispatch bias；bias 不进入 mixture weights，推理时冻结。[8-9]

### Native Vision / Optimizer

- MoonViT-V2 为 27-layer、约 401M parameter ViT，image/video share parameters；spatial/temporal attention factorized，2×2 pixel shuffle 将 visual token 降 4×。[9-10]
- 从零 next-token training 的 vision tower gradient norms 更低、更少 spike，并在作者 eval 中匹配 SigLIP-initialized baseline；这是方向性 ablation，不是完整 benchmark/variance report。[9]
- Per-Head Muon 对 Q/K/V momentum 按 head 分块做 Newton-Schulz orthogonalization，避免大-scale head 主导 shared update，并稍降 optimizer overhead。[10]

## Gaps / Open Questions

- `2.5× scaling efficiency` 将 architecture、data、optimizer 和 recipe 合并，缺少 component-wise ablation。
- KDA:MLA 3:1、AttnRes block size、896×16 experts、latent width 0.5× 的选择过程与替代设计比较未公开。
- MoonViT-V2 的“匹配 SigLIP init”没有给完整表格、error bars 或不同 scale 的复现。
- weights 已开放，但 KDA/AttnRes/LatentMoE 的完整 training implementation 与 K3 config 并未随 report 形成 fully reproducible recipe。

## Lookup-only

- 93 layers、hidden 7168、96 heads、160K vocab、69 KDA + 24 MLA、1M context。[10-11]
- SiTU soft caps `β1=4`, `β2=25`; KDA `gmin=-5`。[5, 8]
- QB histogram estimator与误差界回查 9、Appendix D。

## Evidence Anchors

- 2-3: three-axis architecture overview。
- 4-5: KDA lower-bounded decay, gated MLA。
- 6: AttnRes and LatentMoE。
- 7-9: SiTU-GLU, Quantile Balancing, vision ablation。
- 10-11: MoonViT-V2, Per-Head Muon, architecture comparison。
