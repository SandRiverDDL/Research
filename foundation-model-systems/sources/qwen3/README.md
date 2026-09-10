# Qwen3 Source Dossier

```yaml
---
source_id: qwen3
source_type: model-tr
org: Alibaba Qwen Team
release_date: 2025-05-15
priority: S
status: section-notes
openness: open-weights
confidence: high
lineage: qwen3
role: full-tr
base_source: qwen2.5
---
```

## 一句话

Qwen3 是 Qwen 主线的核心 TR：它把 dense/MoE family、36T multilingual pretraining、thinking/non-thinking 双模式、thinking budget、四阶段 post-training 和 strong-to-weak distillation 串成一套开放模型家族 recipe。[1-3, 10-12]

## 为什么重要

你现在已有 `qwen3-coder-next`，但那是 coding-agent 分支。Qwen3 主 TR 是理解 Qwen 系列后续 coder/VL/omni/agent 分支的 base lineage，也是研究“同一个模型内融合 thinking 和 non-thinking”最直接的公开来源。

## 核心机制 / Takeaways

- Qwen3 的核心产品设计是一个模型同时支持 thinking mode 和 non-thinking mode，并通过 chat template 和 thinking budget 控制推理深度。[1-2, 10-12]
- Pretraining 规模是 36T tokens，覆盖 119 languages/dialects；三阶段训练从 general knowledge 到 STEM/code，再到 long-context extension。[2-3]
- Post-training 是四阶段：Long-CoT cold start -> reasoning RL -> thinking mode fusion -> general RL。[10-12]
- 小模型不是完整重跑四阶段，而是 strong-to-weak distillation；on-policy distillation 用 student on-policy sequences 对齐 teacher logits，报告比直接 RL 更高效。[12, 20-21]
- Eval 同时测 thinking/non-thinking，且对 agent/coding/multilingual 设置单独 benchmark，适合做模式融合和 budget 控制的比较。[12-15, 20-21]

## Source Bundle

- technical report: https://arxiv.org/abs/2505.09388
- tech-report-pdf: https://arxiv.org/pdf/2505.09388
- repo: https://github.com/QwenLM/Qwen3
- model hub: https://huggingface.co/Qwen
- local pdf: `/Users/chy/Research/foundation-model-systems/papers/qwen3/qwen3.pdf`
- last checked: 2026-06-23

## Lineage / Delta

- lineage: Qwen3
- role: full TR for main Qwen3 LLM family
- downstream related source already in project: `qwen3-coder-next`
- not safe to inherit: Qwen3-Coder-Next agentic training details into base Qwen3 unless explicitly stated.

## Citation Labels

- default TR pages: page-only anchors.
- non-TR labels: `[repo]`, `[hf]`.

## 最大证据缺口

- 数据清洗、合成数据比例、reward/verifier 实现、teacher logits serving 等关键工程细节披露有限。
- TR 主要是模型家族/训练流程报告，post-training 的具体 infra 细节不如 LongCat/Step/Nemotron 详细。

## Lens Hooks

- post-training: thinking/non-thinking fusion, thinking budget, four-stage post-training.
- distillation: strong-to-weak off-policy + on-policy distillation.
- pretraining: 36T multilingual data and staged context extension.
- eval: dual-mode eval and budget-scaling curves.

## 阅读入口

- `section-index.md`: 回 PDF 页码。
- `notes/architecture-pretraining.md`: architecture 和 pretraining。
- `notes/post-training.md`: 四阶段后训练与模式融合。
- `notes/distillation-eval.md`: strong-to-weak distillation 和 eval 设计。

