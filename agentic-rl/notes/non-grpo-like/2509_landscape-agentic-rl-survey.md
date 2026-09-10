---
title: "The Landscape of Agentic Reinforcement Learning for LLMs: A Survey"
authors: [Guibin Zhang, Hejia Geng, Xiaohang Yu, et al.]
year: 2026
venue: TMLR
url: https://arxiv.org/abs/2509.02547
arxiv_id: 2509.02547

lane: survey
paper_type: survey
lifecycle_role: survey-seed
data_overlap: true

rl_axes:
  environment: mixed
  interaction_mode: online
  reward_signal: verifier
  optimizer: other
  credit_assignment: trajectory
  data_reuse: replay
  sft_warm_start: unclear
---

## 一句话

Agentic RL 总入口：把 LLM RL 从单步 MDP 扩展到长时域 POMDP。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | mixed；覆盖 tool、web、code、embodied、多模态等环境。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2509.02547_26_landscape-agentic-rl-survey.md` |
| Interaction loop | 多轮 observation-action loop；论文用 POMDP 描述 agent receives observations from state。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2509.02547_26_landscape-agentic-rl-survey.md` |
| Reward / feedback | 讨论 rule-based verifier、reward model、environment feedback、process/outcome reward。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2509.02547_26_landscape-agentic-rl-survey.md` |
| Optimizer / update | 综述级，不提出新 optimizer；覆盖 PPO、GRPO、actor-critic、Q-learning 等。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2509.02547_26_landscape-agentic-rl-survey.md` |
| Credit assignment | 明确把 long-horizon credit assignment 作为 Agentic RL 相比 PBRFT 的区别之一。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2509.02547_26_landscape-agentic-rl-survey.md` |
| Exploration / replay | 作为 open challenge 和部分方法族讨论。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2509.02547_26_landscape-agentic-rl-survey.md` |
| Warm start / data | 不是本文核心变量。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2509.02547_26_landscape-agentic-rl-survey.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: 论文发表于 TMLR 2026-01，明确把 Agentic RL 描述为从 conventional LLM RL 到 autonomous decision-making agents 的范式变化，并对比 single-step MDP 与 temporally extended POMDP。

**事实 [PDF abstract, p.1]**: 论文给出两套 taxonomy：一套按 agentic capabilities，包括 planning、tool use、memory、reasoning、self-improvement、perception；另一套按 application domains，并整理 open-source environments、benchmarks、frameworks。

**解释 [本项目判断]**: 它适合做 `agentic-rl` 的边界 seed，但不适合直接变成抽卡全集。它 synthesis over 500 works，覆盖太广，后续只能从中抽机制相关文献。

## 谱系位置

- 上游：LLM RL / RLHF / reasoning RL / autonomous agents survey。
- 同期：credit assignment survey、GFCR rollout survey、environment scaling survey。
- 下游：RAGEN、ToolRL、WebRL、GiGPO、Agent Lightning、VerlTool 等机制论文的总索引。

## 优缺点

- ✅ [PDF abstract, p.1]: 明确提出 Agentic RL 与 PBRFT/传统 LLM RL 的形式化差异。
- ✅ [PDF p.1]: TMLR 2026-01，适合作为稳定引用。
- ⚠️ [本项目判断]: 太全景，容易把 project scope 拉成 generic agent survey；只作为边界和查漏 seed。

## Evidence

- paper brief: `_meta/briefs/surveys/2509.02547_26_landscape-agentic-rl-survey.md`
- PDF / HTML: `papers/2509.02547-landscape-agentic-rl-survey.pdf`
- survey windows: seed
- PDF: `papers/2509.02547-landscape-agentic-rl-survey.pdf`
- source anchors: abstract p.1; introduction p.1; reward/function discussion; algorithms section; environments/benchmarks tables。

<!-- pdf: papers/2509.02547-landscape-agentic-rl-survey.pdf -->

<!-- brief: _meta/briefs/surveys/2509.02547_26_landscape-agentic-rl-survey.md -->

<!-- survey: seed -->
