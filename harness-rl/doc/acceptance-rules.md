# Harness RL Acceptance Rules

> This document defines what can enter queue / formal L1. Retrieval rules live in `doc/retrieval-strategy.md`.

## Basic Principles

- Queue can be broad; formal L1 must be strict.
- Application domain alone does not determine inclusion.
- Judge by the reusable contribution to `面向一个或多个 agent harness 进行 RL 后训练，使模型学会相应的工具调用、信息处理、记忆 / 上下文管理和任务推进，并研究适配、混合训练与跨 harness 泛化`.
- When unsure, use `queue / review` rather than writing a formal card.

## Hard Gates

Formal L1 cards require:

- Original paper PDF / HTML / source brief.
- A clear mechanism relevant to `面向一个或多个 agent harness 进行 RL 后训练，使模型学会相应的工具调用、信息处理、记忆 / 上下文管理和任务推进，并研究适配、混合训练与跨 harness 泛化`.
- At least one reusable design knob from `doc/taxonomy/design-knobs.md`.

## Time / Venue Gate

Prioritize:

- 按机制相关性优先，覆盖经典 anchor 与近期工作；不设僵硬日期门槛。
- strong venue / strong lab / code / data / project page
- papers that directly affect current novelty risk

Older papers enter only if they are canonical anchors, repeated baselines, or unavoidable for comparison.

## Core Mechanism Gate

Include if the core contribution changes:

- 在目标 harness 下用 RL 训练模型使用工具、理解返回信息、管理状态并完成任务；不要求修改 harness 或提出新的 RL objective。
- 多个 harness 的联合 / 混合 RL、配比或调度，以及专用适配与通用能力之间的迁移 / 干扰。
- 已见和未见 harness 上的泛化、训练部署一致性，以及支撑这些目标的 rollout / optimization 机制；compaction 是具体子问题。

Do not automatically include:

- 仅在 harness 下评测、未训练或无可追踪训练说明的工作；可作背景，不据此当成 harness RL 证据。
- 纯 harness 工程且不涉及模型训练、适配或相关对照证据的项目。

## Boundary Handling

Common boundary risks:

- `boundary_risk: none`
- `boundary_risk: adjacent`
- `boundary_risk: eval`
- `boundary_risk: recipe`
- `boundary_risk: infra`

For each boundary item, write why it may belong here, why it may belong elsewhere, and what evidence would decide.

## Queue vs Card

Queue row minimum:

- verifiable source
- one-sentence `recall_reason`
- initial `paper_type` and `boundary_risk`

Formal L1 minimum:

- passes hard gates
- passes time / venue gate or has an exception
- has bounded original source input
- passes `scripts/autoresearch.py validate`
