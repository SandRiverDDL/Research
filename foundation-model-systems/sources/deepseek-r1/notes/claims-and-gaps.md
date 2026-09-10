# DeepSeek-R1 Claims and Gaps

```yaml
---
source_id: deepseek-r1
section_type: claims-and-gaps
stage: claims-and-gaps
substage: none
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- 强证据：强 base model 可以在没有 reasoning SFT 的情况下，通过 outcome RL 同时提高 response length 与 benchmark performance。[2-5]
- 中等证据：R1 四阶段 pipeline 在保留 reasoning 的同时修复了可读性和通用 assistant 行为。[6-10]
- 弱因果证据：单个“aha moment”样例不能证明 RL 创造了新的 reasoning primitive；它首先是可观察的 token-pattern 变化。[5]

## Why It Matters

R1 应作为历史方法 anchor；缺失的算法消融由后续开放复现补充。开放 weights 很重要，但不能等同于可复现 training recipe。

## Mechanism Sketch

1. 主文训练流程和 within-run curves 可作为主要证据。
2. 跨模型 benchmark 需检查 sampling 与 model version。
3. 用 Open-Reasoner-Zero 检验 critic/algorithm 结论。
4. 用 Skywork-OR1 检验 entropy、data filtering 和 verifier 选择。
5. 当前 DeepSeek practice 应回到 DeepSeek-V4，而不是用 R1 覆盖。

## Details / Evidence

- Open weights 支持行为分析和 distillation，但不能复现原始训练 run。
- “Pure RL”指没有 post-training SFT warm start，不代表模型在没有预训练知识的情况下学会 reasoning。
- Response length 同时是能力表现和推理成本，做 comparison 时应单列。

## Gaps / Open Questions

- 完整 prompt/data mixture 与 decontamination。
- Training code、rollout system、verifier implementation 与 failure recovery。
- 多 seed 方差与对 base-model quality 的敏感性。
- 后续 DeepSeek 是否继续沿用相同 GRPO/reference-policy 配置。

## Lookup-only

- Headline benchmark tables：第 8-10 页。
- Safety/eval prompts：第 40-78 页。

## Evidence Anchors

- 2-10：主要方法和评测。
- 60-63：distillation 与限制。
