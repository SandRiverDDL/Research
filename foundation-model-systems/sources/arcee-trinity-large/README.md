# Arcee Trinity Large Source Dossier

```yaml
---
source_id: arcee-trinity-large
source_type: model-tr
org: Arcee AI / Prime Intellect / DatologyAI
release_date: 2026-02-19
priority: A
status: section-notes
openness: open-weights
confidence: medium
lineage: trinity
role: full-tr
base_source: trinity-nano-mini
---
```

## 一句话

Arcee Trinity Large 是 400B total / 13B active 的开放 MoE pretraining TR，最值得看的是现代 MoE 架构组合、Muon 训练、17T token pretraining、SMEBU 专家负载稳定策略，以及小到大 scaling ladder 如何支撑一次大模型训练。[1-2, 5-9]

## 为什么重要

它不一定是最强模型，但很适合补“开放团队如何 from-scratch 训练 400B sparse MoE”的视角。和 Olmo 3 的 fully-open workflow 不同，Trinity 更偏大规模 MoE 稳定训练和架构工程。

## 核心机制 / Takeaways

- 架构组合：3:1 local/global attention、QK-Norm、gated attention、DeepSeekMoE-style experts、sigmoid routing、depth-scaled sandwich norm。[5-8]
- SMEBU 用 tanh soft-clamped magnitude-aware expert bias update + momentum，替代 sign-based aux-free update，目标是减少大 MoE router oscillation / instability。[7]
- Muon 是训练主线之一；QK-Norm 被用于控制 Muon 下 attention logits 稳定性。[5]
- 数据由 DatologyAI curated，Trinity Large 训练 17T tokens，20T mix 按 13:4:3 三阶段组织，含大量 synthetic web/code/STEM data。[9]
- Nano/Mini 不只是小模型发布，也是验证 data pipeline、architecture、recipe、infra 的 scaling ladder。[2]

## Source Bundle

- technical report: https://arxiv.org/abs/2602.17004
- tech-report-pdf: https://arxiv.org/pdf/2602.17004
- blog: https://www.arcee.ai/blog/trinity-large
- repo/pdf: https://github.com/arcee-ai/trinity-large-tech-report
- model hub: https://huggingface.co/arcee-ai
- local pdf: `/Users/chy/Research/foundation-model-systems/papers/arcee-trinity-large/arcee-trinity-large.pdf`
- last checked: 2026-06-23

## Lineage / Delta

- lineage: Trinity
- role: full TR for Trinity Large, with Nano/Mini as scaling ladder context.
- later release-delta candidate: Trinity-Large-Thinking if user wants agentic post-training follow-up.

## Citation Labels

- default TR pages: page-only anchors.
- non-TR labels: `[blog-trinity]`, `[hf-arcee]`, `[github-report]`.

## 最大证据缺口

- Post-training 细节很少；此 source 更像 base/pretraining/architecture source。
- 数据由 DatologyAI curated，但具体 cleaning/filtering/provenance 公开程度有限。

## Lens Hooks

- architecture: modern open MoE recipe.
- pretraining: Muon, SMEBU, synthetic data, scaling ladder.
- infra/stability: zero loss spike claim, expert load balancing.
- openness audit: open-weight vs fully-open difference.

## 阅读入口

- `notes/architecture-stability.md`: 架构与 SMEBU。
- `notes/pretraining-data.md`: 17T data / Muon / scaling ladder。
- `notes/claims-and-gaps.md`: 开放性和缺口。

