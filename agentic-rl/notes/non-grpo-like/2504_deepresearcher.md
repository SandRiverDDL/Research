---
title: "DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments"
authors: [Yuxiang Zheng, Dayuan Fu, Xiangkun Hu, et al.]
year: 2025
venue: EMNLP 2025
url: https://arxiv.org/abs/2504.03160
arxiv_id: 2504.03160

lane: tool-rl
paper_type: environment-recipe
lifecycle_role: frontier-candidate
data_overlap: true

rl_axes:
  environment: web
  interaction_mode: online
  reward_signal: outcome
  optimizer: policy-gradient
  credit_assignment: trajectory
  data_reuse: none
  sft_warm_start: standard
---

## 一句话

Deep research lane anchor：真实开放网页环境中的 end-to-end RL。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | real open web search/browsing。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.03160_25_deepresearcher.md` |
| Interaction loop | multi-step search / browse / synthesize。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.03160_25_deepresearcher.md` |
| Reward / feedback | task outcome / model-based evaluation。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.03160_25_deepresearcher.md` |
| Optimizer / update | end-to-end RL。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.03160_25_deepresearcher.md` |
| Credit assignment | trajectory-level。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.03160_25_deepresearcher.md` |
| Exploration / replay | real-web interaction scaling。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.03160_25_deepresearcher.md` |
| Warm start / data | standard。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.03160_25_deepresearcher.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: DeepResearcher 认为 prompt engineering 脆弱，controlled RAG-based RL 不能捕捉真实交互复杂性；提出在 real-world web environments 中 end-to-end training deep research agents。

**事实 [PDF abstract, p.1]**: 方法训练 agents navigate noisy, unstructured, dynamic open web，并实现 browsing agents 处理多种网页结构。

**事实 [PDF abstract, p.1]**: 作者报告相对 prompt engineering baseline 最高 +28.9 points、相对 RAG-based RL agents 最高 +7.2 points。

**解释 [本项目判断]**: 这篇应作为 deep-research lane anchor，但需防止和未来 `model-system` 项目重叠；本项目只保留 RL-in-real-web-environment 视角。

**收录依据 [queue/audit]**: Landscape search/deep-research table 标 GitHub；EMNLP 2025 + 官方代码。代码：`https://github.com/GAIR-NLP/DeepResearcher`。

## 谱系位置

- 上游：
- 同期：
- 下游：

## 优缺点

- ✅ [paper]:
- ⚠️ [本项目判断]:

## Evidence

- paper brief: `_meta/briefs/papers/2504.03160_25_deepresearcher.md`
- PDF / HTML: `papers/2504.03160-deepresearcher.pdf`
- survey windows: Landscape
- PDF: `papers/2504.03160-deepresearcher.pdf`
- source anchors: abstract p.1; figure 1 p.1。

<!-- pdf: papers/2504.03160-deepresearcher.pdf -->

<!-- brief: _meta/briefs/papers/2504.03160_25_deepresearcher.md -->

<!-- survey: Landscape -->
