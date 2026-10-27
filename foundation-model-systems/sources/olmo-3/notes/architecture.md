# Olmo 3 Architecture

```yaml
---
source_id: olmo-3
section_type: architecture
stage: architecture
depth: working
confidence: high
need_expert_review: false
---
```

## 问题

Scope：7B / 32B dense backbone 的架构继承与主要改动。
- 是否直接采用某个其他模型的架构或权重？
- 与 OLMo 2 相比改了什么？
- attention、normalization、position encoding 的具体选择是什么？
- 哪些属于成熟组件，哪些是本报告的研究重点？

## Core Design / Innovation

- **事实**：TR 明确说 modeling/training largely follows OLMo 2；采用 decoder-only Transformer，7B / 32B 都是 dense，非 MoE。[html-architecture]
- **事实**：相对 OLMo 2，pretraining / midtraining context 从 4K 增到 8K；每四层中三层采用 4K-window SWA，一层 full attention，最后一层保持 full attention。[html-architecture]
- **解释**：它采用成熟组件并在自身 lineage 上迭代；原文不支持“直接照搬 Qwen/Llama 某个 checkpoint 或完整架构”的说法。

## Why It Matters

**解释**：Olmo 3 的主要研究价值在完整 model flow、数据选择、评测和后训练；架构应理解为稳定、成本可控的底座，而不是新 attention / MoE 架构的展示。

## Mechanism Sketch

- **事实**：局部 SWA 限制多数层的 attention 范围；间隔的 full-attention 层保留跨窗口信息访问。报告将引入 SWA 的动机明确写为长序列训练可扩展性和 inference cost。[html-architecture]
- **事实**：7B 使用 MHA；32B 使用 GQA。两者使用 SwiGLU、QK-Norm、RMSNorm；Table 33 指定 layer norm applied to outputs，不能机械画成所有现代模型通用的 pre-norm block。[html-architecture-table]
- **事实**：long-context 阶段从 8,192 扩到 65,536 tokens；YaRN 用于 full-attention layers。[html-long-context; html-architecture-table]

## Details / Evidence

- **事实**：tokenizer 沿用 OLMo 2，derived from OpenAI cl100k；这是 tokenizer 继承，不是权重继承。[html-architecture]
- **事实**：SWA 引用 Beltagy et al. (2020)，GQA 引用 Ainslie et al. (2023)，表中其他组件亦为已有方案；SWA/full 的具体搭配是 Olmo 3 的 recipe choice。[html-architecture; html-architecture-table]
- **事实**：base training 使用 OLMo-core，报告描述 BF16、torch.compile、custom kernels 和 asynchronous metrics/checkpoints。[html-architecture]

## Gaps / Open Questions

- **开放问题**：§3.2 没有提供足以独立量化 SWA/full 配比收益的 architecture ablation；不能由采用该配置推断它是最优设计。
- **解释**：成熟组件的组合与自己从头训练可以同时成立；要区分 architecture reuse、teacher-generated supervision 和 pretrained-weight reuse。
- 本轮按官方 HTML §3.2、§3.6、Table 33 核验；旧 bundle 的 macOS 本地 PDF 路径在本机不存在，未重新验证 PDF 页码或图示。

## Lookup-only

- hidden size、head count、FFN dimension、RoPE 参数：Table 33。
- optimizer / LR / batch / stage schedule：Table 35；不要把架构与 optimizer 选择混为同一个问题。

## Evidence Anchors

- Source [html-architecture]: https://arxiv.org/html/2512.13961v2#S3.SS2
- Source [html-architecture-table]: https://arxiv.org/html/2512.13961v2#Ax2.T33
- Source [html-long-context]: https://arxiv.org/html/2512.13961v2#S3.SS6
