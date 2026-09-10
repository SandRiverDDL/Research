---
title: "From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models"
authors: [Chenchen Zhang]
year: 2026
venue: arxiv
url: https://arxiv.org/abs/2604.09459
arxiv_id: 2604.09459

lane: survey
paper_type: survey
lifecycle_role: survey-seed
data_overlap: false

rl_axes:
  environment: mixed
  interaction_mode: online
  reward_signal: sparse
  optimizer: other
  credit_assignment: segment
  data_reuse: off-policy
  sft_warm_start: unclear
---

## 一句话

Agentic RL 的核心机制 seed：长轨迹 sparse reward 下如何分配 credit。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | mixed；示例覆盖 web、tool、code、multi-agent。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2604.09459_26_credit-assignment-rl-llms-survey.md` |
| Interaction loop | long-horizon multi-turn environment interaction。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2604.09459_26_credit-assignment-rl-llms-survey.md` |
| Reward / feedback | sparse terminal reward 是核心问题；process reward / verifier 是 reasoning side 的成熟路线。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2604.09459_26_credit-assignment-rl-llms-survey.md` |
| Optimizer / update | 覆盖 Monte Carlo、TD、model-based、game-theoretic、information-theoretic 等 CA 方法，不提出单一 optimizer。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2604.09459_26_credit-assignment-rl-llms-survey.md` |
| Credit assignment | 本文核心；granularity 包括 token、segment、step、turn、multi-agent。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2604.09459_26_credit-assignment-rl-llms-survey.md` |
| Exploration / replay | 不是主轴。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2604.09459_26_credit-assignment-rl-llms-survey.md` |
| Warm start / data | 非主轴。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2604.09459_26_credit-assignment-rl-llms-survey.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: 论文将 credit assignment 分成 reasoning RL 和 agentic RL 两个 regime；reasoning RL 主要处理单次 CoT 生成中的 token/step credit，agentic RL 处理 100+ turns、100K-1M tokens 的多轮环境交互。

**事实 [PDF abstract, p.1]**: 论文 survey 47 个 credit assignment methods，按 assignment granularity 与 methodology 建立二维 taxonomy；还给出 machine-readable inventory、reporting checklist 和 benchmark protocol specification。

**解释 [本项目判断]**: 这是比场景 lane 更稳的机制 seed。它能直接约束后续抽卡：只有真正改变 token/step/tool-call/turn/trajectory credit 的论文才进入 `credit-assignment` track。

## 谱系位置

- 上游：GRPO / process reward model / actor-critic / TD learning。
- 同期：GiGPO、Agent Lightning、RAGEN、SPA-RL、HiPER 等 agentic CA 方法。
- 下游：可以作为 `agentic-rl` 第一个强机制 track。

## 优缺点

- ✅ [PDF abstract, p.1]: 明确指出 agentic RL 的 credit assignment 与 reasoning RL 不同，因其有 stochastic transitions、partial observability、长 horizon。
- ✅ [PDF abstract, p.1]: 提供 paper inventory / checklist / benchmark protocol，适合后续建立高准入抽卡标准。
- ⚠️ [本项目判断]: 单作者 arXiv；需要对其方法覆盖和分类可信度做二次核查，不能直接当作完整权威 survey。

## Evidence

- paper brief: `_meta/briefs/surveys/2604.09459_26_credit-assignment-rl-llms-survey.md`
- PDF / HTML: `papers/2604.09459-credit-assignment-rl-llms.pdf`
- survey windows: seed
- PDF: `papers/2604.09459-credit-assignment-rl-llms.pdf`
- source anchors: abstract p.1; introduction p.1; scope/inclusion criteria; agentic CA discussion。

<!-- pdf: papers/2604.09459-credit-assignment-rl-llms.pdf -->

<!-- brief: _meta/briefs/surveys/2604.09459_26_credit-assignment-rl-llms-survey.md -->

<!-- survey: seed -->
