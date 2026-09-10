# Olmo 3 Eval

```yaml
---
source_id: olmo-3
section_type: eval
stage: evaluation
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- OlmoBaseEval 的定位是 development decision system，而不是最终 leaderboard；它服务 small-scale experiment、stage transition 和 data-mix 决策。[4]
- Eval 设计承认小模型 / 小实验 benchmark 噪声很大，因此通过 task clusters、proxy metrics、增加样本或移除 noisy tasks 提高信噪比。[4-5]
- Fully-open release 让 eval 和 decontamination 也可审计，这比单纯报告分数更有价值。[1, 95-101]

## Why It Matters

Olmo 3 值得学的是 eval 如何参与训练决策。对于 model TR 阅读，具体分数随时间会过期，但“如何避免被 noisy eval 带偏 data/midtraining 决策”是可迁移的。

## Mechanism Sketch

1. 按 capability clusters 聚合 benchmark，降低单 benchmark 偶然性。
2. 为 small-scale models 设计 proxy metrics，避免随机水平任务污染判断。
3. 在 stage 切换时做 centralized integration tests，检查候选 mix 的 base quality 和 post-trainability。
4. 用 decontamination 工具和开放数据链路支撑可审计评估。

## Details / Evidence

- TR 在 model flow 章节明确说明 OlmoBaseEval 用于 compute-efficient base-model development，并列出三种提高小实验可靠性的策略。[4-5]
- Appendix 有 base eval、decontamination 和 post-training eval 的额外细节，first pass 尚未逐项抽取。[95-101, 114-118]

## Gaps / Open Questions

- 需要后续专项审计：OlmoBaseEval 任务选择是否会偏向 Olmo 目标能力，decontamination 对 Qwen/Gemma 等对照是否可比。

## Lookup-only

- 具体 benchmark 数字、cost、表格结果留作 lookup；除非做 fully-open vs open-weight comparison，不进入主线。

## Evidence Anchors

- 4-5: eval as base model development tool.
- 95-101: base eval and decontamination appendix.
- 114-118: post-training eval appendix.

