# Nemotron 3 Infra / Quantization

```yaml
---
source_id: nemotron-3
section_type: infra
stage: infra
substage: quantization-rollout
depth: working
confidence: medium
need_expert_review: true
---
```

## Core Design / Innovation

- Quantization 是 Nemotron 3 system 的一等公民：Super 提供 FP8 for Hopper 和 NVFP4 for Blackwell；Ultra 进一步给 layer/operator precision recipe。[Super:33-37], [Ultra:41-47]
- Ultra 的 quantization recipe 区分 embedding/MTP/BF16、MoE routed experts/NVFP4、shared experts/FP8、Mamba linears/FP8、KV cache/FP8、Mamba SSM cache/FP16 stochastic rounding。[Ultra:41]
- Super / Ultra 都把 rollout generation、MTP acceleration、RL infra scaling 与模型 release 绑定；这说明 open frontier recipe 不只是训练 loss，而是 deployment + RL throughput stack。[Super:28-33], [Ultra:31-33]

## Why It Matters

对真正可用的 open frontier model，低精度训练/量化、rollout speed 和部署硬件是 recipe 的一部分。Nemotron 3 比很多 TR 更明确地把 Hopper/Blackwell 作为 design target。

## Gaps / Open Questions

- 量化校准数据、AutoQuantize sensitivity analysis 和实际质量损失需要深读 tables。
- 非 NVIDIA 硬件上的迁移性有限；这是 open recipe 和 hardware ecosystem 绑定的典型例子。

## Evidence Anchors

- Super 33-37: FP8/FP4 quantization。
- Ultra 41-47: NVFP4 quantization recipe。
