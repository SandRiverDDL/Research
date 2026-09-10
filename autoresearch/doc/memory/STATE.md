# Autoresearch Current State

> Hot memory for Codex. Keep only what the next session must read.

## Current Goal

L1 卡池保持 12 张。2026-07-22 已完成两个 open-source system source dossiers；下一阶段仍可做跨卡 comparison，但不把 dossier 误计为 L1。

## Source Dossiers

- `notes/aris/overview.md` — 首版完成；后续缺口：独立 benchmark、完整 run denominator、audit precision/recall 与真实投稿结果。
- `notes/researchstudio-idea/overview.md` — 首版完成；后续缺口：第三方运行复现、human expert blind eval、compute-matched ablation 与 taxonomy stability。

## Current Boundary

Include:

- 端到端 / 子任务 autoresearch systems
- Autoresearch benchmark 与 evaluation protocol
- Autoresearch failure mode 的实证研究和 critique

Move / cross-link:

- `agentic-rl/`: RL 算法本身归那边，即使被用在 research agent 里。
- `agent-data/`: 通用 agent trajectory 数据归那边。
- `foundation-model-systems/`: frontier model 通用 capability 归那边。

## Current Workflow

- Canonical queue: `comparison/queue.md`.
- Formal cards require original PDF / HTML / bounded brief.
- Helper: `scripts/autoresearch.py status | validate | lookup | audit | pack`.
- 特别注意：**区分三档证据**（self-report / third-party / audit），写卡时 mechanism 段落必须标出证据档位。

## Next Actions

1. **comparison 综合（未启动）**：按 `verifier-type` × `evidence-tier` × `domain` 交叉列出 12 张卡，产出 idea hooks（本项目最缺的 verifier 结构是什么）。
2. **应用 LLM-Judge 使用规则**（DECISIONS.md 2026-07-15）：任何未来卡在写 mechanism 段落时标 verifier 是否同源、reward signal 是否非同源。
3. Queue 剩余 medium-priority 抽卡（MLE-Bench high / Divergent Thinking / ResearchBench / IdeaBench / SciArena / Boiko 2023）可以慢来，不急。
4. AI Scientist v2 未被 Beel-style 独立 audit——是本项目最关键的开放 gap，将来若见到 v2 audit 立刻入 queue high。

## Current Seed Status

- Queue 现有 17 项：10 cardified + 7 待抽（详见 `comparison/queue.md`）
- L1 卡 12 张：measuring-gap 6 张 + 26 年新抽 6 张
- Brief 6 份（26 年新抽的均有 brief，历史 6 张为 shortcut 未补 brief——可延后）
- **关键跨卡综合**：`comparison/insights-2026-llm-judge-and-novelty.md`

## Key Files

- `AGENTS.md`: topic scope.
- `comparison/queue.md`: canonical queue.
- `doc/acceptance-rules.md`: admission rules.
- `doc/retrieval-strategy.md`: retrieval loop.
- `doc/review-checklist.md`: 论文汇报/证据审查 protocol（Tier A 每卡 human-in-the-loop-hidden 强制，Tier B 红旗触发 6 项）。
- `doc/templates/l1-card.md`: card template.
- `doc/taxonomy/failure-modes.md`: failure vocabulary.
- `doc/taxonomy/design-knobs.md`: design vocabulary.
- `scripts/autoresearch.py`: local helper.
