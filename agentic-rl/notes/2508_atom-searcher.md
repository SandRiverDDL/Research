---
title: "Atom-Searcher: Enhancing Agentic Deep Research via Fine-Grained Atomic Thought Reward"
authors: [Yong Deng, Guoqing Wang, Zhenzhe Ying, et al.]
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2508.12800
arxiv_id: 2508.12800

lane: tool-rl
paper_type: environment-recipe
lifecycle_role: frontier-candidate
data_overlap: true

rl_axes:
  environment: web
  interaction_mode: online
  reward_signal: process
  optimizer: grpo-like
  credit_assignment: segment
  data_reuse: curriculum
  sft_warm_start: standard
---

## 一句话

Deep research reward card：Atomic Thought + process reward 缓解稀疏 outcome。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | web search / deep research。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.12800_25_atom-searcher.md` |
| Interaction loop | multi-turn reasoning-search-synthesis。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.12800_25_atom-searcher.md` |
| Reward / feedback | process-level Atomic Thought Reward + outcome reward。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.12800_25_atom-searcher.md` |
| Optimizer / update | GRPO-like RL framework。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.12800_25_atom-searcher.md` |
| Credit assignment | segment / thought-unit level。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.12800_25_atom-searcher.md` |
| Exploration / replay | process reward to outcome reward schedule。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.12800_25_atom-searcher.md` |
| Warm start / data | standard。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.12800_25_atom-searcher.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: Atom-Searcher 指出 agentic deep research 中 outcome-based RL 有 conflicting gradients 和 reward sparsity 问题。

**事实 [PDF abstract, p.1]**: 论文提出 Atomic Thought，将 reasoning 分解为 fine-grained functional units，并由 Reasoning Reward Models 提供 Atomic Thought Rewards。

**事实 [PDF abstract, p.1]**: Atom-Searcher 使用 curriculum-inspired reward schedule，先 prioritizing process-level ATR，再 transition 到 outcome rewards。

**解释 [本项目判断]**: 这是 deep-research lane 的 reward-verifier 卡，和 DeepResearcher 的 real-web end-to-end RL 互补。

**收录依据 [queue/audit]**: Landscape search/deep-research table 标 GitHub；arXiv + 官方代码 + 明确 fine-grained reward mechanism。代码：`https://github.com/antgroup/Research-Venus`。

## 谱系位置

- 上游：
- 同期：
- 下游：

## 优缺点

- ✅ [paper]:
- ⚠️ [本项目判断]:

## Evidence

- paper brief: `_meta/briefs/papers/2508.12800_25_atom-searcher.md`
- PDF / HTML: `papers/2508.12800-atom-searcher.pdf`
- survey windows: Landscape
- PDF: `papers/2508.12800-atom-searcher.pdf`
- source anchors: abstract p.1; figure 1 p.1。

<!-- pdf: papers/2508.12800-atom-searcher.pdf -->

<!-- brief: _meta/briefs/papers/2508.12800_25_atom-searcher.md -->

<!-- survey: Landscape -->
