# Qwen3.5 Post-training Disclosure

```yaml
---
source_id: qwen3.5
section_type: rl-training
stage: post-training
substage: rl-training
depth: surface
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- 官方只披露 RL 已扩展到 million-agent environments，并使用 progressively complex task distributions。[hf-small]
- Model card 同时提到 asynchronous RL frameworks、massive agent scaffolds 与 environment orchestration，但没有给出 objective、reward、rollout policy 或 data mixture。[hf-small]
- 这些材料足以把 Qwen3.5 标为 native multimodal agent-oriented model，但不足以作为可复用 RL recipe。[hf-small]

## Why It Matters

这个 note 的作用是划清 disclosure boundary。Qwen3.5 很可能代表重要 current practice，但不能用 Qwen3 的四阶段 post-training 去填补它没有公开的部分。

## Mechanism Sketch

1. 在大量 agent environments 上扩展 RL。
2. 随训练推进提高 task-distribution complexity。
3. 用 asynchronous framework 编排 agent scaffold、environment 与 trainer。
4. 具体 loss/reward/filter/consolidation 未公开。[hf-small]

## Details / Evidence

- “Million-agent environments”和“asynchronous RL”来自官方 model-card highlights。[hf-small]
- Qwen3.6 的公开增量是 agentic coding capability，并未补充上述训练细节。[qwen36-blog]
- Qwen3.7 当前只有 API metadata，不能补齐 Qwen3.5 recipe。[qwen-api]

## Gaps / Open Questions

- SFT/RL stage order、teacher/distillation、reward/verifier 与 environment taxonomy。
- “Million-agent”究竟指 environment 数量、trajectory 数量还是 scaffold instances，口径未定义。
- Async RL 的 staleness control、policy freshness 与 failure recovery。

## Lookup-only

- Agent benchmark values 与 prompt best practices：`[hf-small]`。

## Evidence Anchors

- `[hf-small]`: 官方 Qwen3.5 model-card highlights。
- `[qwen36-blog]`: 官方 Qwen3.6 release delta。
- `[qwen-api]`: Qwen3.7 API product metadata。
