# Harness RL Retrieval Strategy

> This document defines how to find papers. Admission rules live in `doc/acceptance-rules.md`.

## Recall Focus

Candidates must primarily contribute to `面向一个或多个 agent harness 进行 RL 后训练，使模型学会相应的工具调用、信息处理、记忆 / 上下文管理和任务推进，并研究适配、混合训练与跨 harness 泛化`:

- 在目标 harness 下用 RL 训练模型使用工具、理解返回信息、管理状态并完成任务；不要求修改 harness 或提出新的 RL objective。
- 多个 harness 的联合 / 混合 RL、配比或调度，以及专用适配与通用能力之间的迁移 / 干扰。
- 已见和未见 harness 上的泛化、训练部署一致性，以及支撑这些目标的 rollout / optimization 机制；compaction 是具体子问题。

Do not default-include:

- 仅在 harness 下评测、未训练或无可追踪训练说明的工作；可作背景，不据此当成 harness RL 证据。
- 纯 harness 工程且不涉及模型训练、适配或相关对照证据的项目。

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

harness adaptation reinforcement learning; multi-harness RL; harness-native agent training; tool-use adaptation; unseen harness generalization; CompactionRL
