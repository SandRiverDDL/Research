---
title: "R1-Searcher: Incentivizing the Search Capability in LLMs via Reinforcement Learning"
authors: [Huatong Song, Jinhao Jiang, Yingqian Min, et al.]
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2503.05592
arxiv_id: 2503.05592

lane: tool-rl
paper_type: environment-recipe
lifecycle_role: frontier-candidate
data_overlap: false

rl_axes:
  environment: tool
  interaction_mode: online
  reward_signal: outcome
  optimizer: policy-gradient
  credit_assignment: trajectory
  data_reuse: none
  sft_warm_start: none
---

## 一句话

两阶段 outcome-RL，让模型冷启动学会何时搜索、如何使用搜索。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | external search system。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.05592_25_r1-searcher.md` |
| Interaction loop | reasoning-time search invocation and use。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.05592_25_r1-searcher.md` |
| Reward / feedback | outcome-based。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.05592_25_r1-searcher.md` |
| Optimizer / update | two-stage RL。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.05592_25_r1-searcher.md` |
| Credit assignment | trajectory-level。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.05592_25_r1-searcher.md` |
| Exploration / replay | 两阶段训练本身是 curriculum-like。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.05592_25_r1-searcher.md` |
| Warm start / data | none / cold-start。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.05592_25_r1-searcher.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: R1-Searcher 是 two-stage outcome-based RL approach，用于增强 LLM 的 search capability，使模型在 reasoning 过程中自主调用 external search systems。

**事实 [PDF abstract, p.1]**: 框架完全依赖 RL，不需要 process rewards 或 cold-start distillation。

**事实 [PDF abstract, p.1]**: 作者报告方法显著超过 strong RAG methods，甚至与 closed-source GPT-4o-mini 比较。

**解释 [本项目判断]**: 这是 Search-R1 的相邻 anchor：Search-R1 训练 multi-turn search query generation，R1-Searcher 更强调 cold-start 搜索调用能力。

**收录依据 [queue/audit]**: Landscape survey search table 标 GitHub；arXiv + 官方代码 + 明确 search-tool RL mechanism。代码：`https://github.com/RUCAIBox/R1-Searcher`。

## 谱系位置

- 上游：
- 同期：
- 下游：

## 优缺点

- ✅ [paper]:
- ⚠️ [本项目判断]:

## Evidence

- paper brief: `_meta/briefs/papers/2503.05592_25_r1-searcher.md`
- PDF / HTML: `papers/2503.05592-r1-searcher.pdf`
- survey windows: Landscape
- PDF: `papers/2503.05592-r1-searcher.pdf`
- source anchors: abstract p.1; introduction p.1。

<!-- pdf: papers/2503.05592-r1-searcher.pdf -->

<!-- brief: _meta/briefs/papers/2503.05592_25_r1-searcher.md -->

<!-- survey: Landscape -->
