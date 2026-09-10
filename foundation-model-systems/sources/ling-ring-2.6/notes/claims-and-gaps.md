# Ling / Ring 2.6 Claims and Gaps

```yaml
---
source_id: ling-ring-2.6
section_type: claims-and-gaps
stage: claims-and-gaps
substage: none
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- 强证据：报告明确披露 Ling/Ring 两条 post-training objective、KPop 核心 criterion 和 asynchronous rollout 设计。[13-19, 28-31]
- 中等证据：token-efficient objectives 能在广泛 domain 中提升 capability-per-token 且不明显伤害质量。[14-26]
- 仅属产品/eval claim：在 agentic benchmarks 上达到 frontier parity；不同模型的 scaffold、tools、context 和自测设置并不一致。[20-26]

## Why It Matters

它的价值来自当前机制披露，而不是公司 tier 或 leaderboard 名次。正确的比较单位是“公开了什么设计、证据有多强、哪些 artifact 可取得”。

## Mechanism Sketch

1. Post-training claim 回到第 13-19 页。
2. Rollout-system claim 回到第 28-31 页。
3. HF 页面只用于 openness/deployment 证据。
4. 不从 checkpoint availability 反推未公开 data 或 exact recipe。

## Details / Evidence

- 论文声明开放全部 2.6 checkpoints，包括 base variants。[1, hf-ling, hf-ring]
- AEnvironment 是真实的 environment artifact，但不能复现内部 task mixture。[aenvironment]
- Limitations 明确承认复杂 tool use、知识型回答压缩、long-horizon robustness 与 benchmark coverage 的不足。[33]

## Gaps / Open Questions

- Training dataset 与 exact mixture weights。
- KPop 完整实现/config 和 per-domain ablation。
- Matched scaffold/token budget 下的独立评测。
- Long-horizon recovery、cost-aware planning 和 multilingual drift eval。

## Lookup-only

- Model sizes 与 benchmark tables：第 20-26 页。

## Evidence Anchors

- 13-19：post-training evidence。
- 20-26：evaluation 与 settings。
- 28-31：infrastructure。
- 33：明确限制。
