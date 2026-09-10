# Qwen3.5 Source Dossier

```yaml
---
source_id: qwen3.5
source_type: blog-bundle
org: Alibaba Qwen Team
release_date: 2026-02-16
priority: S
status: section-notes
openness: open-weights
confidence: medium
lineage: qwen3
role: full-tr-equivalent
base_source: qwen3
---
```

## 一句话

Qwen3.5 是 Qwen 主线第一次把 architecture / tokenizer / 多模态训练目标整体换掉的版本：hybrid attention（Gated DeltaNet + Gated Attention，3:1）、高稀疏 MoE（397B-A17B，激活 ~4.3%）、native multimodal early fusion、多 token 预测（MTP），词表扩到 250k / 201 语言。它没有完整 TR，公开材料以 release blog 和 model card 为主。

## 为什么重要

- 它不是 Qwen3 的 release delta：attention 类型、MoE sparsity profile、tokenizer、多模态融合方式都换了。后续 Qwen3.6 / 3.7 都建立在这一代架构上。
- 高稀疏 MoE + 线性注意力组合是当下 frontier industrial system 的一个值得追的方向，需要单独和 GLM-5.x / DeepSeek V4 / Kimi K2.x / MiniMax M2 横向比较。
- 即使没有 TR，blog 披露的 design knob（3:1 ratio、激活比、MTP、early fusion、deployment cost claim）已经够支撑 architecture / serving / multimodal lens 的横向 insight。

## 核心机制 / Takeaways

- **Hybrid attention**：Gated DeltaNet 线性注意力 : Gated Attention 标准注意力 = 3:1；线性层负责长序列 O(n) 推理，标准层保留全局语义/精确推理；gating 充当信号过滤。
- **Sparse MoE**：旗舰 Qwen3.5-397B-A17B 总参 397B、激活 ~17B（约 4.3%）；blog 宣称相对 Qwen3-Max 部署显存 -60%、最大吞吐 ×19；价格做到 0.8 RMB / Mtoken（Qwen3.5-Plus）。
- **Native multimodal early fusion**：从预训练阶段就混合文本和视觉 token，不再走 post-fusion 适配器。
- **Multi-Token Prediction (MTP)**：官方 model card 明确记录 multi-step MTP training；它支持 speculative decoding，但公开材料不足以把 planning 提升单独归因给 MTP。[hf-small]
- **Tokenizer / 多语**：词表扩到 ~250k，覆盖 201 语言/方言，比 Qwen3 的 119 多。
- **Agent / 视觉 agent**：blog 强调 mobile/PC 操作、视觉编程、空间智能。
- **Lineup**：旗舰 397B-A17B 当天发，0.8B / 2B / 4B / 9B 在 2026-03-02 跟进；Apache 2.0。

> Architecture 与 model metadata 已由官方 model card 核对；post-training 只披露 million-agent environments、progressive task distributions 和 asynchronous RL infrastructure，具体 objective、reward、data mixture 仍为 unknown。[hf-small]

## Source Bundle

见 `source-bundle.md`。

## Lineage / Delta

- lineage: Qwen3
- role: full TR equivalent (基于 blog bundle + model card 而非完整 TR)
- base source: `sources/qwen3/`（仅作为前一代历史 baseline，不要把 Qwen3 训练流程当作 Qwen3.5 默认值）
- downstream（single-file release deltas，不独立成子目录）：
  - `release-deltas/qwen3.6.md` — 已核验的 agentic coding release delta
  - `release-deltas/qwen3.7-max-preview.md` — 仅保留 API product metadata，confidence low

## Caveats

- 没有 TR，所有 pretraining mixture / data scale / RL recipe / reward / infra 的细节默认 unknown，不能从 Qwen3 老 TR 推断。
- Architecture、context、license 与小模型 lineup 已有官方 model card；价格与厂商 benchmark 仍只作为 release claim。
- 多模态、agent benchmark 的 setup 和 fairness 没有 verifier 信息，写 lens / comparison 时按 claim audit 处理。

## Lens Hooks

- 架构：3:1 Gated DeltaNet/full attention、sparse MoE 与 MTP。
- 后训练：百万级 agent environment、渐进任务与 asynchronous RL 的披露边界。
- agent：native multimodal agent positioning 与 Qwen3.6 coding delta。
- eval：官方 benchmark setting 与 cross-model comparability。

## 阅读入口

- `section-index.md`：blog/model-card source map。
- `notes/architecture.md`：已核验的 architecture 与 context facts。
- `notes/post-training.md`：RL/agent disclosure 与不能推出的内容。
- `notes/claims-and-gaps.md`：Qwen3.5/3.6/3.7 的证据边界。
