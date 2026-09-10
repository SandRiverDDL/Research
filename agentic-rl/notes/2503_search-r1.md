---
title: "Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning"
authors: [Bowen Jin, Hansi Zeng, Zhenrui Yue, et al.]
year: 2025
venue: COLM 2025
url: https://arxiv.org/abs/2503.09516
arxiv_id: 2503.09516

lane: tool-rl
paper_type: environment-recipe
lifecycle_role: canonical-anchor
data_overlap: false

rl_axes:
  environment: tool
  interaction_mode: online
  reward_signal: outcome
  optimizer: grpo-like
  credit_assignment: trajectory
  data_reuse: none
  sft_warm_start: standard
---

## 一句话

Search-as-tool RL anchor：训练模型在推理中主动多轮搜索。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | search engine / real-time retrieval。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.09516_25_search-r1.md` |
| Interaction loop | multi-turn search queries during reasoning。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.09516_25_search-r1.md` |
| Reward / feedback | simple outcome-based reward。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.09516_25_search-r1.md` |
| Optimizer / update | RL for reasoning framework；与 R1/GRPO 谱系相关。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.09516_25_search-r1.md` |
| Credit assignment | trajectory-level；retrieved token masking 是稳定化机制。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.09516_25_search-r1.md` |
| Exploration / replay | 非主轴。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.09516_25_search-r1.md` |
| Warm start / data | standard。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2503.09516_25_search-r1.md` |

## 核心增量

**事实 [PDF p.1]**: Search-R1 是 COLM 2025 会议论文。

**事实 [PDF abstract, p.1]**: 论文提出让 LLM 在 step-by-step reasoning 中通过 RL 学会 autonomously generate multiple search queries with real-time retrieval。

**事实 [PDF abstract, p.1]**: Search-R1 优化包含 multi-turn search interactions 的 reasoning trajectories，使用 retrieved token masking 稳定 RL training，并采用 simple outcome-based reward。

**事实 [PDF abstract, p.1]**: 论文报告在 7 个 QA datasets 上相对 RAG baselines 提升，并开源代码与 checkpoints。

**解释 [本项目判断]**: 这是 search/deep-research lane 的基础卡，但它更像 search tool interaction，不等于完整 deep research system。

**收录依据 [queue/audit]**: survey 正文提到 + COLM 2025 + 官方代码/ckpt，直接抽卡。代码：`https://github.com/PeterGriffinJin/Search-R1`。

## 谱系位置

- 上游：RAG、tool-use prompting、DeepSeek-R1/RL reasoning。
- 同期：ToolRL、R1-Searcher、WebRL。
- 下游：deep research / search agent RL。

## 优缺点

- ✅ [PDF p.1]: COLM 2025 + code/checkpoints。
- ✅ [PDF abstract, p.1]: 明确 multi-turn search interactions + outcome reward + masking。
- ⚠️ [本项目判断]: QA setting 与真正 long-horizon deep research 有距离；不要过度外推。

## Evidence

- paper brief: `_meta/briefs/papers/2503.09516_25_search-r1.md`
- PDF / HTML: `papers/2503.09516-search-r1.pdf`
- survey windows: GFCR / Landscape
- PDF: `papers/2503.09516-search-r1.pdf`
- source anchors: abstract p.1; introduction p.1-2。

<!-- pdf: papers/2503.09516-search-r1.pdf -->

<!-- brief: _meta/briefs/papers/2503.09516_25_search-r1.md -->

<!-- survey: GFCR / Landscape -->
