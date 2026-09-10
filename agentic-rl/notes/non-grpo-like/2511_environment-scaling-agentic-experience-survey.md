---
title: "Environment Scaling for Interactive Agentic Experience Collection: A Survey"
authors: [Yuchen Huang, et al.]
year: 2025
venue: neurips-2025-workshop
url: https://arxiv.org/abs/2511.09586
arxiv_id: 2511.09586

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

data_axes:
  data_object: environment-episode
  data_source: environment-generated
  selection_signal: feedback
  adaptivity: environment-feedback
  failure_use: replay
  training_consumer: rl
---

## 一句话

把 environment 视为 agentic experience producer 的综述。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | 综述/原卡未单独拆出；见核心增量。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2511.09586_25_environment-scaling-agentic-experience-survey.md` |
| Interaction loop | 综述/原卡未单独拆出；见核心增量。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2511.09586_25_environment-scaling-agentic-experience-survey.md` |
| Reward / feedback | 综述/原卡未单独拆出；见核心增量。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2511.09586_25_environment-scaling-agentic-experience-survey.md` |
| Optimizer / update | 综述/原卡未单独拆出；见核心增量。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2511.09586_25_environment-scaling-agentic-experience-survey.md` |
| Credit assignment | 综述/原卡未单独拆出；见核心增量。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2511.09586_25_environment-scaling-agentic-experience-survey.md` |
| Exploration / replay | 综述/原卡未单独拆出；见核心增量。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2511.09586_25_environment-scaling-agentic-experience-survey.md` |
| Warm start / data | 见 frontmatter `data_overlap` 与 `sft_warm_start`。 | 用于定位该 survey 覆盖的 Agentic RL 维度。 | `_meta/briefs/surveys/2511.09586_25_environment-scaling-agentic-experience-survey.md` |

## 核心增量

综述认为静态 human-level datasets 昂贵且缺少 dynamism / realism，agent 需要与环境直接交互并从 experience 学习。它把过程形式化为 Generation-Execution-Feedback loop：环境生成任务，agent 执行时环境返回 observation，并对 rollout 给 feedback。

对本项目而言，它是 Agentic RL 的 environment / experience collection seed。它也有 data overlap，但当前保留在 Agentic RL，因为核心问题是 interactive experience 如何进入 agentic learning loop。

- data object: environment task、observation、rollout、feedback。
- source: environment-generated interactive experience。
- selection / filtering: feedback / rollout evaluation。
- adaptivity: environment-feedback。
- failure trajectory use: replay / feedback / learning from failed rollouts。
- training consumer: RL / agentic interactive learning。
- downstream effect: long-term decision-making and adaptive behavior。

## 谱系位置

- 上游：autonomous agents survey / tool-use environment papers。
- 同期：ToolGym、ASTRA、environment tuning。
- 下游：Agentic RL 方法谱系。

## 优缺点

- ✅ [arXiv Abstract]: 明确提出 GEF loop，把 environment 定义为 experiential data producer。
- ⚠️ [本项目判断]: 更偏 Agentic RL / environment scaling；如果只抽 data generation 视角，可 cross-link 到 `/Users/chy/Research/agent-data/`。

## Evidence

- paper brief: `_meta/briefs/surveys/2511.09586_25_environment-scaling-agentic-experience-survey.md`
- PDF / HTML: `arXiv abstract`
- survey windows: none
- arXiv: abstract / comments。

<!-- pdf: arXiv abstract -->

<!-- brief: _meta/briefs/surveys/2511.09586_25_environment-scaling-agentic-experience-survey.md -->

<!-- survey: none -->
