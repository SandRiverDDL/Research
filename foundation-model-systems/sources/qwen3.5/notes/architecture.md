# Qwen3.5 Architecture

```yaml
---
source_id: qwen3.5
section_type: architecture
stage: architecture
substage: none
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Qwen3.5 使用 3:1 hybrid stack：每三层 Gated DeltaNet 后接一层 Gated Attention；这不是 Qwen3 的轻量 release delta。[hf-small]
- Dense 与 MoE variants 共用 Qwen3.5 family；旗舰 397B-A17B 以较低 active ratio 换取 serving efficiency。[blog-qwen35, hf-flagship]
- Native multimodal early fusion、扩大后的 tokenizer、MTP 与 long-context support 共同服务 text/vision/video 和 agent workload。[hf-small]

## Why It Matters

对 post-training 来说，architecture 决定 rollout 成本、可承载 context 和 multimodal environment 的训练边界。这里应作为 agentic RL 的 system constraint，而不是主研究结论。

## Mechanism Sketch

1. Gated DeltaNet 处理大部分序列层，降低长上下文 attention cost。
2. 周期性 Gated Attention 保留 full-attention path。
3. Vision encoder 与 language backbone 从预训练阶段融合 multimodal tokens。
4. MTP 为 speculative decoding 提供训练基础。[hf-small]

## Details / Evidence

- Qwen3.5-4B model card 给出 32 layers 与明确的 `8 × (3 Gated DeltaNet + 1 Gated Attention)` layout。[hf-small]
- 原生 context 为 262,144，可配置扩展到约 1.01M；可扩展能力不等于所有训练都在 1M context 上完成。[hf-small]

## Gaps / Open Questions

- Flagship training ablation、data scale 与 multimodal mixture 没有公开。
- MTP 对 planning/reasoning 的独立贡献没有可用消融。

## Lookup-only

- Hidden size、head count、vocabulary 与 context metadata：`[hf-small]`。

## Evidence Anchors

- `[hf-small]`: Qwen3.5-4B 官方 model card。
- `[hf-flagship]`: 397B-A17B 官方 model card。
