# LongCat-2601 Robust RL / Heavy Thinking

```yaml
---
source_id: longcat-flash-thinking-2601
section_type: robust-training-test-time-scaling
stage: post-training
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Robust RL 把真实世界环境缺陷显式注入训练，而不是假设部署时模型自然泛化到 noisy tools/users。[15-16]
- 噪声主要分两类：instruction noise 表示用户交互的模糊和变体；tool noise 表示工具失败、不一致响应和 partial results。[16]
- 噪声 curriculum 逐步增加 difficulty/diversity，目标是缩小 perfect vs imperfect environment 的性能差。[16]
- Heavy Thinking 通过多个 independent thinkers 并行探索，再由 summary/refinement 聚合，扩展 reasoning width 和 depth。[16-17]

## Why It Matters

这部分说明 agentic 模型不能只在干净 benchmark 上训练。对真实产品，用户和工具都不稳定；robustness 应该变成训练 distribution 的一部分。

## Mechanism Sketch

1. 在不破坏 solvability 的前提下注入 instruction/tool imperfections。
2. 根据模型当前鲁棒性逐步提高噪声复杂度。
3. 在 Heavy Thinking 中，多个 thinkers 独立生成 reasoning paths。
4. Summary LLM 汇总共识、指出冲突，并生成 final answer。
5. 额外 RL 阶段强化聚合和 refinement 能力。

## Details / Evidence

- Table 1 显示 w/ Noise 训练在 noisy VitaBench / Tau2Bench 上相对 w/o Noise 明显更强，同时标准环境不降或略升。[15-16]
- Heavy Thinking 的流程图显示并行 thinkers、context memory、summary 和 final output 的结构。[16]

## Gaps / Open Questions

- Heavy Thinking 是否使用同一模型自调用、不同采样参数、还是额外 summary model，细节不完全清楚。
- 噪声注入的具体分布、级别和 curriculum gate 未公开。

## Lookup-only

- Table 1 各 benchmark 数字只在做 robustness comparison 时查。[15-16]

## Evidence Anchors

- 15-16: robust noisy environment training.
- 16-17: Heavy Thinking mode.

