# Harness RL Research Workspace

> This file narrows `/home/chy/notes/Research/AGENTS.md`.
> Current directory is for **Harness RL**: 面向一个或多个 agent harness 进行 RL 后训练，使模型学会相应的工具调用、信息处理、记忆 / 上下文管理和任务推进，并研究适配、混合训练与跨 harness 泛化.

## Current Goal

Build a source-backed literature map for `面向一个或多个 agent harness 进行 RL 后训练，使模型学会相应的工具调用、信息处理、记忆 / 上下文管理和任务推进，并研究适配、混合训练与跨 harness 泛化`, prioritizing:

- RL 如何让模型适应目标 harness 的工具协议、返回信息和控制流？
- 单 harness 适配提升来自哪些可学习行为，是否迁移到其他 harness？
- 多个 harness 如何联合或混合 RL，如何选择配比并识别迁移与干扰？
- 收益能否跨 harness / 任务迁移，并在等预算下成立？

This project is a research lens, not necessarily a mature community survey category. Do not force papers into this project if their core contribution belongs elsewhere.

## Boundary

Include:

- 在目标 harness 下用 RL 训练模型使用工具、理解返回信息、管理状态并完成任务；不要求修改 harness 或提出新的 RL objective。
- 多个 harness 的联合 / 混合 RL、配比或调度，以及专用适配与通用能力之间的迁移 / 干扰。
- 已见和未见 harness 上的泛化、训练部署一致性，以及支撑这些目标的 rollout / optimization 机制；compaction 是具体子问题。

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

用户进一步明确：在某些 harness 下训练 RL，使模型适应其工具调用、信息处理等运行方式；同时询问多个 harness 混合 RL 的现状。此前以 harness 编辑或分段优化为中心的解释过窄，现以模型的 harness 适配、混合训练与泛化为主线。

只在用户要求时启动调研、idea 生成或实验规划；不在此处跑训练。原文有版本一致的 HTML 时优先 HTML。
