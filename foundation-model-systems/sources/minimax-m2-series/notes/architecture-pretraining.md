# MiniMax-M2 Architecture / Pretraining

```yaml
---
source_id: minimax-m2-series
section_type: stage-note
stage: architecture-pretraining
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- MiniMax-M2 的 architecture 主线是“mini activations”：229.9B total / 9.8B active MoE，用小 active compute 服务高频 agentic workloads。[1-3]
- 与 MiniMax-Text-01 的 hybrid attention 不同，M2 回到 full GQA attention；TR 解释是 hybrid / SWA 在复杂 multi-hop reasoning 和 agent tasks 上质量不足。[3-6]
- MTP 被纳入 pretraining / inference 设计：先训练 MTP，再扩展到多个 MTP modules，用 main model verification 做 speculative decoding。[5-6]
- Pretraining 仍是大规模基础：29.2T tokens，constant + decay 两段，long-context extension 从 8K 到 32K 再到 192K。[6-7]

## Why It Matters

MiniMax 的重点不是追求最大 active parameters，而是把有限 active compute 投到 agentic data、Forge RL、interleaved thinking 和 self-evolution。对于关注后训练的人，这比单纯大模型 scaling 更贴近“如何让较小 active model 做真实任务”。

## Mechanism Sketch

1. Decoder-only MoE backbone，fine-grained experts + sigmoid gating + expert bias。
2. 选择 full attention / GQA，放弃质量不稳定的 hybrid/SWA。
3. Pretraining 后做 long-context extension，加入 code concatenation、long PDFs、thematically related packing。
4. MTP 为 speculative decoding 和 agent serving latency 服务。

## Details / Evidence

- M2 是 62-layer decoder-only Transformer，256 fine-grained experts，GQA，192K context，MTP。[2-6]
- TR 明确称 SWA variants 在 32K+ context 和 agent tasks 上更差，因此采用 full attention。[5-6]
- Pretraining 数据包括 web、academic literature、books、code、QA，并用 model-based reward scoring / classifiers 做质量筛选，upsample code/math/STEM。[6-7]
- Long-context extension 使用 code concatenation、long PDFs 和 thematically related packing。[6-7]

## Gaps / Open Questions

- 具体 pretraining mixture、quality threshold、dedup、contamination control 披露有限。
- “小 active footprint + agentic data”到底在哪些任务上比更大 active model 更 cost-effective，需要结合 deployment cost 比较。

## Lookup-only

- 完整 architecture table 和参数回查 `[3-6]`。
- 具体 benchmark progression 图回查 `[28-29]`。

## Evidence Anchors

- 1-7: architecture and pretraining.
- 28-30: within-series progression and conclusion.
