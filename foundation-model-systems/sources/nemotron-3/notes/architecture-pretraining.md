# Nemotron 3 Architecture / Pretraining

```yaml
---
source_id: nemotron-3
section_type: architecture
stage: architecture
substage: hybrid-mamba-latentmoe-nvfp4
depth: working
confidence: medium
need_expert_review: true
---
```

## Core Design / Innovation

- Super 的 architecture 三件套是 LatentMoE、MTP、Hybrid Mamba-Attention；目标是提高 accuracy per FLOP / parameter / byte，而不是单纯扩 active params。[Super:3-8]
- LatentMoE 是 hardware-aware MoE 设计，显式考虑 low-latency serving 的 memory bandwidth、throughput serving 的 all-to-all routing 和 sharding overhead。[Super:4-5]
- MTP 不只是 auxiliary objective，也服务 native speculative decoding；这和 MiMo / Qwen 的 rollout/inference co-design 形成同一趋势。[Super:5-7]
- Super 是 25T token pretraining，并披露 NVFP4 pretraining、data mixture ordering、long-context extension 和 base eval。[Super:8-18]
- Ultra 沿用 Super recipe 并扩到 550B-A55B，报告更强调 pretraining stability diagnostics，例如 dead experts 和 residual norm imbalance。[Ultra:3-15]

## Why It Matters

Nemotron 3 的开源价值在于它把硬件约束写进 model system：MoE 不是抽象 sparsity，而是 memory bandwidth、all-to-all、quantization、Blackwell/Hopper serving 的共同设计。对未来基模方向，这比单个模型分数更值得学。

## Gaps / Open Questions

- 具体 pretraining data release 和 filtering thresholds 需要进一步审计 artifacts。
- Ultra 相比 Super 的 recipe adjustments 第一版还没有逐项展开。
- Hybrid Mamba-Attention 的质量/速度 tradeoff 需要结合推理 benchmark 和硬件环境看。

## Lookup-only

- Super: 120B total / 12B active, 25T tokens。[Super:1, 3]
- Ultra: 550B / 55B active。[Ultra:1]

## Evidence Anchors

- Super 3-8: architecture。
- Super 8-18: pretraining / data / long context。
- Ultra 3-15: Ultra pretraining and stability。
