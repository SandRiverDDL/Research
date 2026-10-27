# MoE-Aware RL Optimization Acceptance Rules

> This document defines what can enter queue / formal L1. Retrieval rules live in `doc/retrieval-strategy.md`.

## Basic Principles

- Queue can be broad; formal L1 must be strict.
- Application domain alone does not determine inclusion.
- Judge by the reusable contribution to `针对 MoE 模型结构特性设计或验证的 RL 优化算法：重要性采样、路由不一致、梯度估计及 router / expert 更新`.
- When unsure, use `queue / review` rather than writing a formal card.

## Hard Gates

Formal L1 cards require:

- Original paper PDF / HTML / source brief.
- A clear mechanism relevant to `针对 MoE 模型结构特性设计或验证的 RL 优化算法：重要性采样、路由不一致、梯度估计及 router / expert 更新`.
- At least one reusable design knob from `doc/taxonomy/design-knobs.md`.

## Time / Venue Gate

Prioritize:

- 按机制相关性优先，覆盖经典 anchor 与近期工作；不设僵硬日期门槛。
- strong venue / strong lab / code / data / project page
- papers that directly affect current novelty risk

Older papers enter only if they are canonical anchors, repeated baselines, or unavoidable for comparison.

## Core Mechanism Gate

Include if the core contribution changes:

- 针对 MoE 路由特性设计的 RL objective、importance weighting、clipping 与梯度估计。
- router-aware policy optimization、routing replay / correction 及 router / expert 更新规则。
- GSPO 等通用 RL 算法：有明确 MoE 动机、机制分析或实验证据时纳入核心对照。

Do not automatically include:

- 仅使用 MoE backbone、没有结构相关算法或证据的 RL 应用。
- 纯 MoE 预训练、推理加速、通信调度，以及模型级多 agent routing。

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
