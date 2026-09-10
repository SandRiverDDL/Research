---
title: "SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution"
authors: [Hanlin Wang, Chak Tou Leong, Jiashuo Wang, Jian Wang, Wenjie Li]
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2505.20732
arxiv_id: 2505.20732

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: frontier-candidate
data_overlap: false

rl_axes:
  environment: mixed
  interaction_mode: online
  reward_signal: sparse
  optimizer: policy-gradient
  credit_assignment: step
  data_reuse: none
  sft_warm_start: standard
---

## 一句话

把 final reward 分解成每一步 progress contribution 的 reward redistribution。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | WebShop、ALFWorld、VirtualHome。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.20732_25_spa-rl-stepwise-progress.md` |
| Interaction loop | multi-step external environment interaction。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.20732_25_spa-rl-stepwise-progress.md` |
| Reward / feedback | final delayed reward redistributed into fine-grained intermediate rewards。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.20732_25_spa-rl-stepwise-progress.md` |
| Optimizer / update | RL with estimated per-step reward。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.20732_25_spa-rl-stepwise-progress.md` |
| Credit assignment | stepwise progress attribution。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.20732_25_spa-rl-stepwise-progress.md` |
| Exploration / replay | 非主轴。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.20732_25_spa-rl-stepwise-progress.md` |
| Warm start / data | standard。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2505.20732_25_spa-rl-stepwise-progress.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: SPA-RL 针对 agentic tasks 的 delayed rewards，提出 Stepwise Progress Attribution，把 final reward 分解成 stepwise contributions。

**事实 [PDF abstract, p.1]**: 方法训练 progress estimator，使它在 trajectory 上累积 stepwise contributions 并匹配 task completion；policy optimization 时结合 per-step contribution 与 environment action grounding signal。

**事实 [PDF abstract, p.1]**: 在 WebShop、ALFWorld、VirtualHome 上，SPA-RL 相比 SOTA 平均提升 success rate 2.5%、grounding accuracy 1.9%。

**解释 [本项目判断]**: SPA-RL 是 reward redistribution / progress-estimation 路线，与 BEACON 的 milestone segmentation 和 HCAPO 的 hindsight critic 可并列比较。

**收录依据 [queue/audit]**: Landscape / Credit Assignment survey 正文提到；arXiv + 官方代码 + 明确 stepwise credit mechanism。代码：`https://github.com/WangHanLinHenry/SPA-RL-Agent`。

## 谱系位置

- 上游：
- 同期：
- 下游：

## 优缺点

- ✅ [paper]:
- ⚠️ [本项目判断]:

## Evidence

- paper brief: `_meta/briefs/papers/2505.20732_25_spa-rl-stepwise-progress.md`
- PDF / HTML: `papers/2505.20732-spa-rl-stepwise-progress.pdf`
- survey windows: Credit Assignment / Landscape
- PDF: `papers/2505.20732-spa-rl-stepwise-progress.pdf`
- source anchors: abstract p.1; introduction p.1。

<!-- pdf: papers/2505.20732-spa-rl-stepwise-progress.pdf -->

<!-- brief: _meta/briefs/papers/2505.20732_25_spa-rl-stepwise-progress.md -->

<!-- survey: Credit Assignment / Landscape -->
