# DeepSeek-R1 SFT and Distillation

```yaml
---
source_id: deepseek-r1
section_type: sft-distillation
stage: post-training
substage: sft-distillation
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Cold-start SFT 是第一段 R1 RL 前的小规模行为 scaffold，不是主要的 reasoning supervision 来源。[6]
- Rejection-sampling SFT 是 capability consolidation：从 reasoning policy 采样，保留正确且可用的 traces，再与 non-reasoning assistant data 混合。[6-8]
- 小模型 distillation 主要使用约 800K 条 R1 生成数据做 behavior cloning，并没有完整复刻 R1 的多阶段 RL。[60-62]

## Why It Matters

R1 把 supervised data 的三种作用拆开了：初始化可读 policy、固化已经训练出的能力、把大模型行为迁移给小模型。这比笼统的“SFT 然后 RL”更值得保留。

## Mechanism Sketch

1. 收集数千条 human-aligned long-CoT，作为 cold start。
2. 运行 reasoning RL。
3. 从 reasoning checkpoint 采样并验证回答。
4. 将约 600K reasoning 样本与约 200K non-reasoning 样本混合。
5. 在 base checkpoint 上再次 SFT。
6. 用同类 trace corpus SFT 多个 Qwen/Llama 小模型。[6-8, 60-62]

## Details / Evidence

- 第二次 SFT 用于修复 narrow reasoning RL 没覆盖的写作和 open-domain 行为。[6]
- Distillation 结果说明：对小模型，强 teacher traces 可能比直接照搬大模型 RL recipe 更有效。但这是特定 scale 与 initialization 下的经验，不能推广成“小模型不该做 RL”。[60-62]

## Gaps / Open Questions

- Cold-start 数据的人工参与程度、收集过程和过滤 rubric 披露不足。
- Rejection threshold、diversity control 与 contamination audit 不足以精确复现。
- 800K corpus 和 generation pipeline 没有开放。

## Lookup-only

- Reasoning/non-reasoning 数量与训练安排：第 6-8、60-62 页。

## Evidence Anchors

- 6-8：cold start 与 rejection-sampling SFT。
- 60-62：student distillation 设置与对比。
