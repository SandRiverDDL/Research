# Mistral 3 Cascade Distillation

```yaml
---
source_id: mistral-3
section_type: training-recipe
stage: pretraining
substage: distillation
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Ministral 3 不从头分别训练 14B/8B/3B，而是从 Mistral Small 3.1 依次做 `prune -> distill -> repeat`，把一次 data stream 同时变成模型缩小和 continued pretraining 过程。[3]
- 每一级先做 16K short-context distillation，再做 256K long-context extension；short-context child 又成为下一次 pruning 的输入。[3-5]
- Distillation 只使用 forward-KL logit objective，报告称比混合 next-token prediction loss 更好。[4]
- 这套方法的核心是 compute efficiency 和 capability retention，不应误标成 post-training innovation。

## Why It Matters

- 对后训练的直接启发是 checkpoint provenance：同样的 SFT/RL recipe 落在“pruned + distilled” base 上，failure mode 会随尺寸显著变化。
- Teacher selection 不是简单选择 benchmark 最强者；student/teacher 距离、训练阶段和 teacher 是否经过 preference tuning 都会改变效果。[9]

## Mechanism Sketch

1. 从 Mistral Small 3.1 Base 初始化。
2. 按 activation statistics 做 layer、hidden-dimension 和 FFN pruning。
3. 用 parent logits 做 16K context forward-KL distillation。
4. 用 YaRN 和 position-based temperature scaling 扩到 256K，并继续 distillation。
5. 对 14B -> 8B -> 3B 重复以上过程，同时避免重复消费同一段 data mix。[3-5]

## Details / Evidence

- Layer importance 使用 input/output activation norm ratio；hidden dimension 用跨层 activation PCA；FFN dimension 用 gated activation magnitude 排序。[4]
- Vision encoder 从 Mistral Small 3.1 复制并冻结，每个 size 重新训练 projection。[3-5]
- Pretraining teacher 始终采用 Mistral Small 3.1；更强的 Medium 3 反而较差。报告的解释空间包括 teacher/student capacity gap 和目标分布不匹配，但没有完整因果拆解。[9]
- Post-training SFT 则相反：更强 teacher 有益，且 preference-tuned teacher 优于只做 SFT 的 teacher。[9]

## Gaps / Open Questions

- 未公开 data mix、token 数、训练 FLOPs 和每一级 pruning/distillation 成本，无法验证端到端 FLOP efficiency。
- 只有 Mistral family 内部 teacher/student 实验，能否迁移到不同 tokenizer/architecture 不清楚。
- 没有从头训练的严格 compute-matched 全套对照。

## Lookup-only

- sizes: 14B / 8B / 3B。
- context schedule: 16,384 -> 262,144。
- vision encoder: frozen 410M ViT。

## Evidence Anchors

- 3-5: Cascade Distillation、pruning、forward-KL 和 context extension。
- 9: teacher-selection / preference-tuned-teacher ablations。
