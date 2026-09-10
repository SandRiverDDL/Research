# Step 3.5 Flash Architecture / Inference Co-design

```yaml
---
source_id: step-3.5-flash
section_type: architecture
stage: architecture
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Step 3.5 Flash 的架构目标是 agentic latency：大量 prefilling + prolonged multi-turn decoding，因此把 attention、MoE、MTP 一起做系统协同。[5]
- 196B total / 11B active sparse MoE，45 layers，其中前 3 个 dense FFN，后 42 个 MoE；每 MoE layer 有 288 routed experts + 1 shared expert，top-8 active。[6]
- 3:1 SWA/full attention 降低 long-context attention 成本；GQA-8 对齐 8-GPU tensor parallelism。[5-7]
- 增加 SWA query heads 和 head-wise gated attention，用很小开销补回 naive SWA 的质量损失。[7-8]
- MTP-3 是为 speculative decoding 服务的低延迟组件，多数阶段只训 MTP-1，最后克隆/联合微调 MTP-2/3。[7]

## Why It Matters

Step 的重点是“active parameter / latency density”。如果你未来想做基模系统，这类设计训练你看架构时不只问 benchmark，还问 agent workflow 的 wall-clock、KV cache、speculative decoding 和部署节点约束。

## Mechanism Sketch

1. 用 sparse MoE 保持大容量但只激活 11B 参数。
2. 用 SWA/full hybrid 避免全 attention 在长上下文下的 cost。
3. 用 GQA-8 对齐常见 8-GPU server。
4. 用 head-wise gated attention 解决 SWA 无有用窗口信息时的 sink/吸收问题。
5. 用 MTP heads 让 speculative decoding 更有效。

## Details / Evidence

- TR 直接将 agentic workloads 描述为 extensive context prefilling + prolonged multi-turn interactive decoding。[5]
- S3F1+Head 相比 naive S3F1 质量更好且几乎不增加 attention cost；S1F1 质量更强但 cost 高约 60%，因此最终选择 S3F1+Head。[8]
- MTP heads 只增加约 0.81B 参数，约 0.41%。[7]

## Gaps / Open Questions

- MTP 在真实服务中的 acceptance rate、latency gain、与 vLLM/SGLang speculative decoding 的配合没有充分展开。
- Head-wise gated attention 与 sink token 的长期训练稳定性还需要 appendix 细读。

## Lookup-only

- 具体 layers、experts、heads、FLOPs ablation 需要时查 Figure 2、Table 1 和 appendix。[6-8]

## Evidence Anchors

- 5-8: architecture and ablation.
- 27-30: architecture appendix.

