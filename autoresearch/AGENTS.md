# Autoresearch Research Workspace

> This file narrows `/Users/chy/Research/AGENTS.md`.
> Current directory is for **Autoresearch (the research topic)**: 研究自动化科研系统本身 —— 它现在做得到什么、做不到什么、怎么评、怎么改。

**注意命名冲突**：根 `~/Research/CLAUDE.md` 里 `autoresearch` 也是一个 **skill 名**（legacy literature pipeline 入口）。这里的 `autoresearch/` 是**研究主题目录**，不是 skill。写笔记引用 skill 时用反引号 `` `autoresearch` skill ``；引用本项目用「本项目」或「Autoresearch 项目」。

## Current Goal

Build a source-backed literature map for **自动化科研系统的机制、缺陷、评测与改进**, prioritizing:

- 现有 autoresearch pipeline（end-to-end / semi-autonomous）的**架构与机制**是什么，哪些环节靠 LLM，哪些靠人/工具
- 这些系统的**失败模式**：hallucinated novelty、weak experimental design、metric gaming、citation fabrication、reward hacking on reviewer models、reproducibility gap
- 如何**评测** autoresearch 产出：novelty / correctness / reproducibility / peer-review outcome / expert judgment
- 改进路径：verifier design、human-in-the-loop 结构、tool grounding、专业领域适配（ML / bio / material 等 domain-specific autoresearch）

This project is a research lens, not a mature community survey category. Do not force papers into this project if their core contribution belongs elsewhere (e.g. general LLM agent methods).

## Boundary

Include:

- 端到端 autoresearch agents（AI Scientist / AI Scientist-v2 / Sakana / AgentLaboratory 类）
- 子任务 autoresearch systems：autonomous literature review (STORM, PaSa, Elicit-like)、hypothesis generation、autonomous experimentation (chemistry/ML)、AI-driven peer review
- 评测 autoresearch 的 benchmark 与 protocol（ResearchBench、MLE-bench 中和科研直接相关的部分、reviewer-model eval）
- 关于 autoresearch 缺陷的批判性研究、reproducibility audit、position paper

Move or cross-link to neighboring projects:

- `agentic-rl/`: 只要 core contribution 是 RL 算法 / policy optimization，即便用在 research agent 上也归那边；本项目只在 autoresearch pipeline 中作为组件引用。
- `agent-data/`: 通用 agent trajectory / tool-call data 合成归那边；本项目只关心用于 autoresearch 训练/评测的**专用**数据。
- `foundation-model-systems/`: frontier model 的通用 capability 归那边；autoresearch 只关心它们在 research task 上的表现和被用作 backbone 时的适配。

Mixed papers:

- 如果核心贡献是 autoresearch mechanism / evaluation / critique，本项目写 L1。
- 如果 autoresearch 只是 downstream application，另一项目写主卡，本项目最多 queue 交叉引用。
- 双料（如"用 RL 训练一个 research agent"）：双登记，两边各写视角卡。

## Entry Points

Read in this order:

1. `doc/memory/STATE.md` — hot state and next actions.
2. `comparison/queue.md` — canonical script queue.
3. `doc/acceptance-rules.md` — what can enter queue / formal L1.
4. `doc/retrieval-strategy.md` — how to recall papers.
5. `doc/templates/l1-card.md` — L1 card template.
6. `doc/taxonomy/failure-modes.md` and `doc/taxonomy/design-knobs.md` — stable tag vocabulary.
7. `doc/memory/DECISIONS.md` and `doc/memory/OPEN-QUESTIONS.md` when scope or unresolved issues matter.
8. 仅在创建或审阅 open-source system dossier 时读 `doc/source-dossier-guidelines.md`，其中定义阅读深度、证据层级与验收标准。

## Language Hard Requirement

**IMPORTANT — MUST：本项目的 notes、dossiers、comparison、insights 与 memory 正文必须以中文为主。** 英文只保留技术术语、原始引文、代码、命令、schema、模型/skill/file 名称；不得因主要来源是英文而把研究笔记主体写成英文。

## Literature Pipeline Hard Gates

- Queue row is not a card.
- Survey mention is recall signal, not paper evidence.
- No original paper PDF / HTML / bounded brief, no formal L1 card.
- `notes/` root-level `*.md` only contains formal L1/L2 notes; the documented
  `notes/<system-slug>/` source-dossier exception is nested and never counts as L1.
- Run `scripts/autoresearch.py validate` before reporting completed cards.
- `scripts/autoresearch.py` handles hygiene / lookup / audit / pack only; Codex makes research judgments.

## Autoresearch-Specific Discipline

因为本项目研究对象本身就是"AI 做科研"，claim 特别容易被 hype 污染。额外纪律：

- **区分三档证据**：论文自报 metric / 第三方复现 / 独立 audit。三者不能混引。
- 任何 "AI scientist 做到 X" 的 claim 都要标注：是**端到端**做的还是**pipeline 中某一步**做的，是**人挑选后**展示还是**随机取样**。
- Reviewer-model eval 的结果**默认低置信**，除非配套人工审查或多 reviewer 一致。
- 复现 / 代码 / 产出物是否公开是硬指标；不公开的 claim 归 speculation。

## Directory Contract

- `doc/`: topic rules, templates, taxonomy, memory.
- `notes/`: root-level `*.md` are formal L1/L2 paper notes. A named open-source
  system may instead use `notes/<system-slug>/` as a source dossier, with
  `overview.md` as its only entry point; nested dossier notes are not formal L1,
  do not enter the card count, and do not require an extra `dossiers/` layer.
  Creation and review MUST follow `doc/source-dossier-guidelines.md`.
- `comparison/`: queue, seed sources, structured comparisons, synthesis reports.
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
