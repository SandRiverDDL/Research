# MoE-Aware RL Optimization Retrieval Strategy

> This document defines how to find papers. Admission rules live in `doc/acceptance-rules.md`.

## Recall Focus

Candidates must primarily contribute to `针对 MoE 模型结构特性设计或验证的 RL 优化算法：重要性采样、路由不一致、梯度估计及 router / expert 更新`:

- 针对 MoE 路由特性设计的 RL objective、importance weighting、clipping 与梯度估计。
- router-aware policy optimization、routing replay / correction 及 router / expert 更新规则。
- GSPO 等通用 RL 算法：有明确 MoE 动机、机制分析或实验证据时纳入核心对照。

Do not default-include:

- 仅使用 MoE backbone、没有结构相关算法或证据的 RL 应用。
- 纯 MoE 预训练、推理加速、通信调度，以及模型级多 agent routing。

## Recall Sources

Use:

1. **Seed survey recall**: extract direct method references from relevant survey sections.
2. **Known-item recovery**: user-named or project-named papers enter queue, then source verification.
3. **Neighbor backflow**: inspect neighboring projects for overlap papers.
4. **Keyword direct search**: one-time search only when discovering a new term family or obvious coverage gap.

## Bounded Snowballing Loop

```text
seed / known-item
  -> source verification
  -> candidate classification
  -> apply doc/acceptance-rules.md
  -> collect PDF / HTML / brief
  -> write approved L1 cards
  -> validate
```

Stop recall when two consecutive rounds add <= 2 high-priority candidates.

## Batch-First Admission

Classify candidates before writing cards:

| candidate | class | reason | action |
|---|---|---|---|
| paper title | core / survey / benchmark-eval / adjacent / background / reject | 1 sentence | card / hold / ask user |

Do not write more than 3-5 L1 cards in one batch without validation.

## Candidate Log

Write candidates to `synthesis/queue.md` or a focused synthesis document. Do not leave recall state only in chat.

Each candidate row should include:

- `source`
- `recall_reason`
- `boundary_risk`
- `action`

## 初始关键词

MoE reinforcement learning policy optimization; GSPO; routing mismatch importance sampling; router-aware RL
