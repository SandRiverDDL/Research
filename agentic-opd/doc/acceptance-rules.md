# Agentic OPD Acceptance Rules

> This document defines what can enter queue / formal L1. Retrieval rules live in `doc/retrieval-strategy.md`.

## Basic Principles

- Queue can be broad; formal L1 must be strict.
- Application domain alone does not determine inclusion.
- Judge by the reusable contribution to `student 自采样轨迹上的 teacher 监督，如何在多轮环境交互中可靠地转化为 Agent 能力`.
- When unsure, use `queue / review` rather than writing a formal card.

## Hard Gates

Formal L1 cards require:

- Original paper PDF / HTML / source brief.
- A clear mechanism relevant to `student 自采样轨迹上的 teacher 监督，如何在多轮环境交互中可靠地转化为 Agent 能力`.
- At least one reusable design knob from `doc/taxonomy/design-knobs.md`.

## Time / Venue Gate

Prioritize:

- 优先近期直接相关工作；不设硬日期截止，保留必要的早期方法和 baseline。
- strong venue / strong lab / code / data / project page
- papers that directly affect current novelty risk

Older papers enter only if they are canonical anchors, repeated baselines, or unavoidable for comparison.

## Core Mechanism Gate

Include if the core contribution changes:

- Student rollout / state coverage、teacher query 或介入策略。
- Agent 蒸馏信号、loss 分配、工具 action 与多轮 credit allocation。
- Agentic OPD 的可靠性、训练成本与评测协议。

Do not automatically include:

- 仅使用 teacher 离线生成固定数据、没有 on-policy 机制贡献的 Agent SFT。
- 与蒸馏机制无关的纯 RL 算法、Agent 应用或工程框架。

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
