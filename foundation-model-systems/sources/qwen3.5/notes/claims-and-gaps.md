# Qwen3.5 Claims and Gaps

```yaml
---
source_id: qwen3.5
section_type: claims-and-gaps
stage: claims-and-gaps
substage: none
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- 高可信：official model card 给出的 architecture、context、license 与 checkpoint metadata。[hf-small, hf-flagship]
- 中可信：million-agent environments、progressive tasks 与 async RL 的存在；官方披露没有足够机制细节。[hf-small]
- 低可信或不可推出：具体 RL algorithm、reward composition、Qwen3.7 architecture，以及旧 stub 中无 primary anchor 的强 agent claim。

## Why It Matters

Qwen3.5 是 current-practice tracking source，但不是 full recipe anchor。Comparison 应允许“重要但未披露”，而不是用 Qwen3 历史 TR 自动补齐。

## Mechanism Sketch

1. Architecture/model facts 引用 model card。
2. RL 只保留官方 highlights 的直接陈述。
3. Qwen3.6 仅记录已核验 release delta。
4. Qwen3.7 仅记录 API product metadata。
5. 出现 TR 后再升级为 page-level dossier。

## Gaps / Open Questions

- Pretraining/post-training 数据、阶段顺序、RL objective、reward/verifier 与 infra 消融。
- Agent benchmark scaffold 与 matched-cost comparison。
- Qwen3.6/3.7 是否沿用相同 architecture 与 post-training stack。

## Lookup-only

- Benchmark tables 与部署参数：官方 model cards。

## Evidence Anchors

- `[hf-small]`、`[hf-flagship]`、`[qwen36-blog]`、`[qwen-api]`。
