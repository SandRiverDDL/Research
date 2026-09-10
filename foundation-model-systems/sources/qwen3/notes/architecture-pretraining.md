# Qwen3 Architecture / Pretraining

```yaml
---
source_id: qwen3
section_type: architecture-pretraining
stage: pretraining
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Qwen3 覆盖 dense 与 MoE 两条线，从 0.6B 到 235B；旗舰 Qwen3-235B-A22B 是 235B total / 22B active 的 MoE。[2-3]
- Dense 结构延续 Qwen2.5，但去掉 QKV bias，引入 QK-Norm 稳定训练；MoE 使用 fine-grained expert segmentation，128 total experts / 8 active experts，并取消 shared experts。[3]
- Pretraining 是 36T tokens、119 languages/dialects、三阶段：general 30T -> STEM/code knowledge intensive -> long-context 4K 到 32K。[2-3]
- 数据扩展依赖 Qwen2.5-VL 做 PDF text extraction，Qwen2.5-Math/Qwen2.5-Coder 生成 synthetic math/code data。[2]

## Why It Matters

Qwen3 是理解“开放大模型家族工程化”的基础样本：同一个 TR 同时覆盖小 dense、旗舰 dense、小 MoE 和大 MoE，后续 coder/VL/agent 分支都可回到这个 base recipe。

## Mechanism Sketch

1. 架构层保持成熟 Transformer 组件：GQA、SwiGLU、RoPE、RMSNorm、QK-Norm。
2. MoE 层采用 128 experts / 8 active，fine-grained expert segmentation，无 shared experts。
3. 数据层扩大多语言和领域覆盖，用 VL 模型抽 PDF，用专业模型合成 math/code。
4. 三阶段 pretraining 逐步从 general knowledge 转到 STEM/code，再转到 long-context。

## Details / Evidence

- TR 明确将 36T tokens 和 119 languages/dialects 作为相对 Qwen2.5 的关键扩展。[2-3]
- QK-Norm 被用于 attention stability；MoE 的 global-batch load balancing loss 被用于 expert specialization。[3]
- Long-context stage 将最大上下文从 4,096 扩展到 32,768。[2]

## Gaps / Open Questions

- 具体 cleaning、dedup、synthetic data 质量控制和 contamination audit 披露不细。
- 需要后续和 Olmo 3 对比：Qwen3 更强、更大，但开放性显著弱于 fully-open model flow。

## Lookup-only

- 各模型 layer/head/context/expert 数看 Table 1/2。[3]

## Evidence Anchors

- 2-3: pretraining overview and architecture.
- 3-9: pretraining details and base eval.

