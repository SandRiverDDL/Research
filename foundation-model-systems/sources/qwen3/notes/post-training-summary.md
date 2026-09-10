# Qwen3 Post-training Summary

```yaml
---
source_id: qwen3
stage: post-training
summary_role: classic-mainline-anchor
priority_for_post_training: A
confidence: high
---
```

## Verdict

Qwen3 是统一 thinking/non-thinking behavior 的经典开放recipe：通过 Long-CoT cold start、reasoning RL、thinking-mode fusion和general RL把深推理与快速回答装进同一policy；小模型则使用strong-to-weak、student-on-policy logit distillation降低完整RL成本。[10-12, 20-21]

## Pipeline

```text
Stage 1: Long-CoT cold-start SFT
-> Stage 2: reasoning RL
-> Stage 3: thinking-mode fusion
-> Stage 4: general RL
```

- Cold start建立长reasoning格式与初始能力，reasoning RL提升math/code等可验证任务。[10-12]
- Mode fusion让同一模型在template/budget控制下输出thinking或non-thinking behavior。
- General RL修instruction following、helpfulness、format与更广任务，避免reasoning specialization覆盖普通聊天。

## Core Mechanisms

### Thinking Budget / Mode Fusion

- Runtime可以选择thinking mode并控制budget，训练必须同时维护两种行为分布。
- 统一policy降低部署/维护成本，但引入mode interference：non-thinking可能变啰嗦，thinking可能过早停止或被general alignment压制。

### Strong-to-weak Distillation

- 小模型不完整重复四阶段，而是从强teacher蒸馏；on-policy distillation使用student自己生成的sequences对齐teacher logits。[12, 20-21]
- 这降低teacher-trace distribution mismatch，并报告比直接RL更高效；但teacher serving和logit access仍是成本。

## Failure Modes / Controls

- Long-CoT cold start可能把verbosity/style artifacts固化到policy。
- Mode fusion需要分别测thinking/non-thinking regression，不能只看综合平均。
- Budget control可能被模型绕过，例如输出隐式长推理或在低budget下质量骤降。

## Openness and Evidence

- Open weights + full TR，四阶段flow清楚；训练data、reward implementation和distillation configs不fully open。
- 仍是后续Qwen coder/VL/agent分支的lineage anchor，但current branch practice需读各自TR。

## Transfer to Current Work

- 构建双模式eval matrix：同prompt下比较quality、tokens、latency、format和mode leakage。
- 小模型baseline应包含direct RL、teacher-trace SFT和student-on-policy logit distillation。
- General RL后必须回归reasoning pass-rate与thinking length distribution。

## Evidence Anchors

- [post-training.md](post-training.md): pages 10-12。
- [distillation-eval.md](distillation-eval.md): distillation pages 12, 20-21 与 thinking/non-thinking eval settings。
- [../README.md](../README.md): Qwen3 lineage verdict。
