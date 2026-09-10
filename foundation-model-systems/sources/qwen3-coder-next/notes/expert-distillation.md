# Qwen3-Coder-Next Expert Distillation

```yaml
---
source_id: qwen3-coder-next
section_type: sft-distillation
stage: post-training
substage: expert-distillation
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Post-training 从高质量 agentic coding SFT checkpoint 出发，训练多个 expert models，再把能力 distill 回统一模型。[2, 6-11]
- Experts 覆盖 web development、user experience focused coding、single-turn QA、software engineering 等 domain；这是 specialist-to-generalist consolidation 的 coding-agent 版本。[6-11]
- 和 MiMo/Nemotron 的 MOPD 相比，Qwen 披露更偏工程流程和 expert domains，公式/OPD objective 披露较少。[11]

## Why It Matters

这条线说明 2026 coding-agent model 也在走 specialist consolidation：不是一个模型直接吃所有任务，而是先把 WebDev、UX、SWE、QA 等专家训练出来，再压回 unified model。后续值得和 MiMo MOPD / Cascade MOPD / GLM parallel OPD 做横向 lens。

## Method Blocks

### Expert distillation

- 官方披露：多个 expert models 被训练并 distill 回 unified model。[6-11]
- 合理解释：这是 coding-agent 领域的 multi-teacher consolidation，但不一定是 MiMo 式 token-level MOPD。
- 未披露 / 不能下结论：exact loss、teacher weighting、student sampling policy、filtering 和是否 on-policy 尚需深读或查 repo。

## Gaps / Open Questions

- Distillation objective 不够明确。
- 各 expert 的训练数据、reward 和 selection criteria 仍需细读。
- 需要确认是否有公开训练数据或只开放 weights/repo。

## Evidence Anchors

- 2: high-level expert model consolidation。
- 6-11: expert models and distillation。
