# Kimi K2.6 Source Dossier

```yaml
---
source_id: kimi-k2.6
source_type: blog-bundle
org: Moonshot AI
release_date: 2026-05-20
priority: A
status: section-notes
openness: open-weights
confidence: medium
lineage: kimi-k2
role: release-delta
base_source: kimi-k2.5
---
```

## 一句话

Kimi K2.6 目前更适合按 Kimi K2.5 之后的 release delta 记录：公开材料强调更强 agentic / multimodal / long-context 使用能力，但没有找到与 K2.5 同等完整的训练 TR。

## 为什么重要

它能帮助追踪 Kimi family 的产品化方向，但不应替代 Kimi K2.5 TR 做 method source。后续如果比较 Kimi 家族，K2.5 是 anchor，K2.6 是“新版本能力和接口边界”。

## 核心设计 / Takeaways

- K2.6 公开材料强调 text/image/video、长上下文、thinking/non-thinking 和 agent tasks。
- 目前证据形态更像 model card / docs / release notes，不足以独立支撑 data mixture、RL、Agent Swarm 或 architecture 方法总结。
- 任何 K2.6-specific innovation 都需要单独核查，不继承为 K2.5 TR 已证明的 method。

## Source Bundle

- model card / release: https://huggingface.co/moonshotai/Kimi-K2.6
- docs / API: https://platform.moonshot.ai/
- lineage TR: https://arxiv.org/abs/2602.02276
- local pdf: none for Kimi K2.6
- K2.7 Code announcement: https://forum.moonshot.ai/t/441
- K2.7 Code weights: https://huggingface.co/moonshotai/Kimi-K2.7-Code
- last checked: 2026-07-21

## Lineage / Delta

- lineage: Kimi K2
- role: release delta after `kimi-k2.5`
- base source: `sources/kimi-k2.5/`

## Citation Labels

- non-TR source labels:
  - `[hf-model-card]`
  - `[kimi-docs]`
  - `[k25-tr]`

## 最大证据缺口

- 没有独立 full TR；训练流程、数据、RL、reward、Agent Swarm 细节未公开。
- K2.7 Code 已有 release delta，但仍缺 full TR，不能替换 K2.5 的 method anchor。

## Lens Hooks

- release-delta: Kimi K2.5 -> K2.6 capability movement.
- eval: release benchmark and product capability claims.
- multimodal-agent: whether K2.6 changes the K2.5 Agent Swarm / vision recipe is unknown.

## 阅读入口

- `section-index.md`: source map。
- `notes/release-delta.md`: delta and gaps。
- `notes/release-kimi-k2.7-code.md`: K2.7 Code current release delta。
- `notes/claims-and-gaps.md`: comparison 前先读。
