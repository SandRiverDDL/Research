# MoE-Aware RL Optimization Research Workspace

> This file narrows `/home/chy/notes/Research/AGENTS.md`.
> Current directory is for **MoE-Aware RL Optimization**: 针对 MoE 模型结构特性设计或验证的 RL 优化算法：重要性采样、路由不一致、梯度估计及 router / expert 更新.

## Current Goal

Build a source-backed literature map for `针对 MoE 模型结构特性设计或验证的 RL 优化算法：重要性采样、路由不一致、梯度估计及 router / expert 更新`, prioritizing:

- MoE 的离散路由如何影响 RL 的概率比与 off-policy 校正？
- rollout / training 路由变化如何影响梯度估计与稳定性？
- 如何联合或分别更新 router 与 experts，同时保留有效探索和专长？
- 算法收益是否来自 MoE 结构，并能跨模型规模和任务成立？

This project is a research lens, not necessarily a mature community survey category. Do not force papers into this project if their core contribution belongs elsewhere.

## Boundary

Include:

- 针对 MoE 路由特性设计的 RL objective、importance weighting、clipping 与梯度估计。
- router-aware policy optimization、routing replay / correction 及 router / expert 更新规则。
- GSPO 等通用 RL 算法：有明确 MoE 动机、机制分析或实验证据时纳入核心对照。

Move or cross-link to neighboring projects:

- `agentic-rl/`: 通用 agent RL 的 reward、credit assignment 与优化算法；本项目只写当前 lens 的专门机制。
- `foundation-model-systems/`: 模型 TR / recipe 的完整 dossier；本项目抽取与当前算法问题直接相关的证据。

Mixed papers:

- If this project's mechanism is the core contribution, write this project's perspective card.
- If another project owns the core contribution, only add a queue / cross-link row here.
- If both are substantial, dual-register and write separate perspective cards.

## Entry Points

Read in this order:

1. `doc/memory/STATE.md` — hot state and next actions.
2. `synthesis/queue.md` — canonical script queue.
3. `doc/acceptance-rules.md` — what can enter queue / formal L1.
4. `doc/retrieval-strategy.md` — how to recall papers.
5. `doc/templates/l1-card.md` — L1 card template.
6. `doc/taxonomy/failure-modes.md` and `doc/taxonomy/design-knobs.md` — stable tag vocabulary.
7. `doc/memory/DECISIONS.md` and `doc/memory/OPEN-QUESTIONS.md` when scope or unresolved issues matter.

## Literature Pipeline Hard Gates

- Queue row is not a card.
- Survey mention is recall signal, not paper evidence.
- No original paper PDF / HTML / bounded brief, no formal L1 card.
- `notes/` root only contains formal L1/L2 notes.
- Run `scripts/autoresearch.py validate` before reporting completed cards.
- `scripts/autoresearch.py` handles hygiene / lookup / audit / pack only; Codex makes research judgments.

## Directory Contract

- `doc/`: topic rules, templates, taxonomy, memory.
- `notes/`: formal L1/L2 paper notes.
- `synthesis/`: queue, seed sources, structured comparisons, bottleneck reconstruction, and idea synthesis.
- `papers/`: PDF mirrors or temporary downloads.
- `_meta/`: generated or bounded source artifacts; do not manually maintain generated files.
- `scripts/autoresearch.py`: project-local helper.

## L1 Card Metadata

New L1 cards use short YAML plus a trailing `<!-- meta: ... -->` block.

Required frontmatter is defined in `doc/triage-rules.json`. Keep human-useful, Obsidian-filterable fields in YAML; put low-frequency source metadata such as authors, URL, PDF, and brief paths in the trailing meta block.

## Constraints

- L1 is a research index, not a full paper summary.
- Strong claims require source anchors.
- Reports must label fact / interpretation / conjecture / open question.
- Do not add new workflow fields unless they can be validated or maintained.

## 本次授权与范围说明

用户已明确：关注针对 MoE 模型做针对性优化的 RL 算法，类似 GSPO；不以泛化的 MoE 后训练 recipe 或多专家 agent 为核心。

只在用户要求时启动调研、idea 生成或实验规划；不在此处跑训练。原文有版本一致的 HTML 时优先 HTML。
