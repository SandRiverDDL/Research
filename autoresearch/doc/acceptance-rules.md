# Autoresearch Acceptance Rules

> This document defines what can enter queue / formal L1. Retrieval rules live in `doc/retrieval-strategy.md`.

## Basic Principles

- Queue can be broad; formal L1 must be strict.
- Application domain alone does not determine inclusion (LLM 用在科研 ≠ autoresearch 系统研究)。
- Judge by the reusable contribution to **自动化科研系统的机制、缺陷、评测与改进**。
- When unsure, use `queue / review` rather than writing a formal card.

## Hard Gates

Formal L1 cards require:

- Original paper PDF / HTML / source brief.
- A clear mechanism, evaluation protocol, critique, or reusable finding relevant to autoresearch systems.
- At least one reusable design knob from `doc/taxonomy/design-knobs.md`, **or** at least one documented failure mode from `doc/taxonomy/failure-modes.md`（本项目允许 critique-only 卡）。

## Time / Venue Gate

Base priorities:

- strong venue / strong lab / code / data / project page
- 有第三方复现、audit、或独立评测的 claim 优先
- 明确讨论 failure modes / limitations 的 position paper 优先

### Cutoff by paper_type

方法迭代快，分析与评测迭代慢。按 `paper_type` 分档设置时效 cutoff（相对当前日期）：

| paper_type | cutoff | 说明 |
|---|---|---|
| `core-method` | 约 12 个月 | 端到端 pipeline / 子任务系统更新极快，老方法很快被吸收；超期只留 canonical anchor 或 critique target。 |
| `benchmark-eval` | 约 18 个月 | 评测基础设施迭代慢，老 benchmark 在横向对比时仍有用。 |
| `critique-audit` | 不设 cutoff | 失败模式的**类型**变化远慢于方法本身；观点仍被引用即保留。 |
| `position` | 不设 cutoff | 同上。 |
| `survey` | 不设 cutoff | 只作 recall 信号，从不写卡，时效无关。 |
| `background` / `adjacent` | 约 24 个月 | 只在明确支撑某个 anchor 或 critique 时保留。 |

### 例外：canonical anchor / critique target

超过 cutoff 的 `core-method` 若满足以下任一，仍进入：

- **canonical anchor**：该项目命名了一个支线（例如 AI Scientist、Boiko 2023 的 autonomous chemistry），后续论文引用它是为了定位自己而非复用方法。
- **critique target**：正被一年内的 critique/audit 论文当作靶子；砍掉会使批判读者失去背景。

在 queue note 或卡的 `lifecycle_role` 里显式标 `canonical-anchor`；不这样标就按 cutoff 处理。

### 老于 2023 的工作

仅当作为上述 canonical anchor（例如 early autoresearch surveys、经典 hypothesis generation systems、human-vs-LLM 分布距离方法学祖先）时入选。

## Core Mechanism Gate

Include if the core contribution changes:

- 端到端 autoresearch pipeline 架构（planner / executor / reviewer / iterator 组织方式）
- Autoresearch 子任务的关键机制：novelty check、hypothesis generation、experiment design、result interpretation、paper writing、peer review
- Autoresearch 的评测方法（benchmark 设计、reviewer model、人工评审 protocol）
- Autoresearch 的**失败模式研究**（reproducibility audit、citation fabrication 分析、reward hacking 演示）

Do not automatically include:

- 通用 LLM agent 方法（工具调用、planning、reasoning），除非明确聚焦 research task
- 单一领域的 autonomous experimentation（除非 mechanism 可迁移到 general autoresearch）
- Prompt engineering tricks for research writing without evaluation

## Boundary Handling

Common boundary risks:

- `boundary_risk: none` — clearly about autoresearch systems
- `boundary_risk: adjacent` — general agent method demo'd on research task
- `boundary_risk: eval` — benchmark 涉及 research 但主要贡献是通用 eval methodology
- `boundary_risk: recipe` — model recipe 顺带做了 research task eval
- `boundary_risk: infra` — 工具 / 平台层，非 pipeline mechanism

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
