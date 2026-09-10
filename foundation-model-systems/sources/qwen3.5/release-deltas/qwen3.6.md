# Qwen3.6 Release Delta

```yaml
---
delta_id: qwen3.6
parent_source: qwen3.5
release_date: 2026-04-15
role: release-delta
confidence: high
status: section-notes
---
```

## 定位

Qwen3.6-35B-A3B 是建立在 Qwen3.5 model type 上的高稀疏 MoE release，主要增量是 agentic coding、reasoning 与 multimodal capability，而不是新的 architecture-level 换代。[qwen36-blog, hf-doc]

## 核心 delta

- 官方定位强调相对 Qwen3.5-35B-A3B 的 agentic coding 与 reasoning 提升。[qwen36-blog]
- 35B total / 3B active，继续沿用 Qwen3.5 architecture/model type；没有证据显示更换 attention、tokenizer 或 native multimodal backbone。[qwen36-blog, hf-doc]
- 继续支持 multimodal thinking/non-thinking modes；这属于 capability/release fact，不代表公开了新的 post-training recipe。[qwen36-blog]
- 官方 benchmark 使用具体 agent scaffold 与自测设置，应保留 setup caveat，而不是只抄分数。[qwen36-blog]

## Source

- 官方 release blog: https://qwen.ai/blog?id=qwen3.6-35b-a3b
- Model organization: https://huggingface.co/Qwen
- Architecture documentation: https://huggingface.co/docs/transformers/en/model_doc/qwen3_5
- 历史 baseline: `sources/qwen3.5/README.md`

## 未公开

- 没有新的 pretraining/post-training mixture、RL objective、reward、environment composition 或 infra ablation。
- 因此不能从 capability gain 反推“Thinking Preservation”或具体 long-horizon training mechanism。

## 升级 trigger

只有出现完整 TR、architecture-level 改动，或足够支撑至少两个独立 stage notes 的 training disclosure，才升级为独立 dossier。

## Evidence Anchors

- `[qwen36-blog]`: Qwen 官方 Qwen3.6-35B-A3B release。
- `[hf-doc]`: Qwen3.5/3.6 model type 与 architecture 关系。
