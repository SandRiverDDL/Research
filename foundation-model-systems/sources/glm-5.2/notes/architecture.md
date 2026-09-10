# GLM-5.2 Architecture / 1M Context

```yaml
---
source_id: glm-5.2
section_type: stage-note
stage: architecture
substage: 1m-context
depth: working
confidence: medium
need_expert_review: true
---
```

本 note 只覆盖 GLM-5.2 release blog 披露的 1M context / serving 增量；没有覆盖 GLM-5 TR 的完整 MoE、DSA 和 training pipeline。

## Core Design / Innovation

- 核心设计不是“支持 1M tokens”本身，而是让 1M context 在 coding-agent 长轨迹里可用：模型要处理大规模实现、自动化研究、性能优化、复杂 debugging，而不是只在 synthetic long-context benchmark 上撑住。[blog-glm-52]
- IndexShare for DSA：每 4 个 sparse attention layers 共享一个 lightweight indexer，复用 top-k indices，减少 1M context 下 indexer dot product 和 top-k operation 的开销。[blog-glm-52]
- MTP 增量服务 speculative decoding：在 MTP layer 中复用 IndexShare/KVShare，减少 draft model 成本并提高 acceptance length；配合 rejection sampling 和 end-to-end TV loss，blog 披露 coding scenario acceptance length 提升约 20%。[blog-glm-52]
- Serving 侧把 bottleneck 从单纯 FLOPs 转到 KV-cache capacity、long-context kernels、cache transfer、CPU-side scheduling；GLM-5.2 的系统叙事是 architecture 和 inference engine co-design。[blog-glm-52]

## Why It Matters

值得内化的是这个 taste：长上下文模型不能只看 context window 数字。1M context 会把瓶颈转移到 KV-cache、prefill/decode pipeline、CPU scheduling、request routing 和 agent trace management。对未来基模/后训练工作来说，long-context training、inference infra 和 agentic eval 必须一起看。

随查随用的是具体 FLOPs、acceptance length、kernel/serving 名称；它们重要，但不是你现在最需要记住的直觉。

## Mechanism Sketch

1. 在 DSA sparse attention 中，不让每层都独立计算 indexer；改成每 4 层共享一次 indexer/top-k selection。
2. 从 128K sequence length 的 mid-training 开始训练 IndexShare，让模型适应这个 sparse attention index reuse。
3. 对 MTP speculative decoding 也做类似 reuse：MTP 多步共享 indices 和 KV cache，减少训练/推理 discrepancy。
4. Serving 侧围绕 1M context 做 KV-cache 容量、cache transfer、long-context kernel、CPU scheduling 和 GPU pipeline bubble 的优化。

## Details / Evidence

- Blog 明确说 GLM-5.2 每 4 个 transformer layers 共享一个 lightweight indexer；indexer 放在 4 层中的第一层，top-k indices 被后续 4 层复用，因此 3/4 layers 避免 indexer dot product 和 top-k operation。[blog-glm-52]
- GLM-5.2 从 128K sequence length 的 mid-training 开始使用 IndexShare，并声称在更低 computation 下超过 GLM-5.1 long-context benchmarks。[blog-glm-52]
- MTP 侧的关键问题是 GLM-5.1 中 training-inference discrepancy：后续 MTP step 的 KV cache 可能混合 target model hidden states 和 MTP layer hidden states；GLM-5.2 通过复用 first MTP step 的 KV/top-k indices 来减少 discrepancy。[blog-glm-52]
- MTP ablation 披露 baseline acceptance length 4.56，加入 IndexShare/KVShare、rejection sampling、end-to-end TV loss 后到 5.47，提升约 20%。[blog-glm-52]
- 1M serving 的三类优化是：更细粒度 memory management / parallelization 增加 usable KV-cache space；优化随 context length 增长的 kernels 并配合 cache transfer；优化 CPU-side cache management、request scheduling 和 runtime paths 以减少 GPU pipeline bubbles。[blog-glm-52]

## Gaps / Open Questions

- 没有披露完整 architecture table：layer count、experts、active params、attention layout、positional encoding 等需要从 GLM-5 TR / model config 回查，且要确认是否等同于 GLM-5.2。
- IndexShare 的质量损失边界、不同层组大小 ablation、不同 context length 上的效果没有在 blog 中完整披露。
- Serving throughput 图没有转成可复现 setup；硬件、batching、concurrency、request length distribution、engine version 都需要补。
- 1M-context training data composition 没披露，只说 expanded coding-agent scenarios。

## Lookup-only

- Model card / GitHub README 标注 GLM-5.2 为 744B total / 40B active、BF16/FP8 weights；但这属于 model metadata，architecture 细节仍需 config/TR 核对。[github-readme]
- MTP ablation exact values：4.56 -> 5.10 -> 5.29 -> 5.47 acceptance length。[blog-glm-52]
- Serving frameworks: transformers、vLLM、SGLang、xLLM、ktransformers。[blog-glm-52]

## Evidence Anchors

- `[blog-glm-52]`: Introduction, Architecture for 1M Context, IndexShare for DSA, MTP with IndexShare and KVShare, Efficiently Serving 1M Context Length。
- `[hf-model-card]`: model card mirror and model usage metadata。
- `[github-readme]`: GLM-5 series download table and release overview。
