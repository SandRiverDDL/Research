# Qwen3 Distillation / Eval

```yaml
---
source_id: qwen3
section_type: distillation-eval
stage: post-training
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Strong-to-weak distillation 是 Qwen3 小模型 recipe 的核心：小模型不完整重跑四阶段，而是用大模型 teacher 缩短开发路径。[10, 12]
- Distillation 分两段：off-policy response distillation 建 basic reasoning 和 mode-switching；on-policy distillation 让 student 生成序列，再对齐 teacher logits 最小化 KL。[12]
- TR 直接对比了 direct RL 和 on-policy distillation：从同一 off-policy distilled 8B checkpoint 出发，distillation 用约 1/10 GPU hours 获得更好表现。[20-21]
- Eval 设计同时测 thinking/non-thinking，并显式区分 general、alignment、math/reasoning、agent/coding、multilingual。[12-15]

## Why It Matters

这对小规模 recipe 很有启发：如果有强 teacher，logit-level on-policy distillation 可能比直接 RL 更高效，尤其当目标是让小模型继承 exploration space 和 mode-control 行为。

## Mechanism Sketch

1. Teacher 用 `/think` 和 `/no think` 生成 outputs，student 做 off-policy response distillation。
2. Student on-policy 采样 prompts 并生成 thinking/non-thinking responses。
3. 对这些 student trajectories 查询 teacher logits，最小化 KL。
4. 用 pass@1/pass@64 和 GPU hours 判断“性能 + exploration potential + 成本”。

## Details / Evidence

- TR 报告 on-policy distillation 不只提高 pass@1，也提高 AIME pass@64；direct RL 则没有提升 pass@64。[20-21]
- Eval setting 对 thinking/non-thinking 使用不同 sampling 参数，并对 AIME 扩展 max output length 到 38,912 tokens。[13]
- ThinkFollow、ToolUse、LengthCtrl 等 in-house eval 用于检查 mode fusion、tool calling 和长度控制，而不只是公开 benchmark。[20-21]

## Gaps / Open Questions

- Teacher logits 的 serving cost、token subset、temperature、KL weighting 未充分披露。
- On-policy distillation 和 OPD/MOPD 的边界需要 lens 比较：Qwen3 更像 teacher-guided small-model transfer，MiMo/Nemotron 更像 multi-teacher capability consolidation。

## Lookup-only

- Table 21: RL vs on-policy distillation numbers and GPU hours。[20-21]
- Table 22: Stage 2/3/4 mode-fusion and General RL ablations。[21]

## Evidence Anchors

- 12: distillation phases.
- 13-15: eval suite and headline model comparison.
- 20-21: budget and distillation ablations.

