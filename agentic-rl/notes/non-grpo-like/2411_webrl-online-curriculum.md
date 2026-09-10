---
title: "WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning"
authors: [Zehan Qi, Xiao Liu, Iat Long Iong, et al.]
year: 2025
venue: ICLR 2025
url: https://arxiv.org/abs/2411.02337
arxiv_id: 2411.02337

lane: web-rl
paper_type: environment-recipe
lifecycle_role: canonical-anchor
data_overlap: true

rl_axes:
  environment: web
  interaction_mode: online
  reward_signal: outcome
  optimizer: policy-gradient
  credit_assignment: trajectory
  data_reuse: curriculum
  sft_warm_start: standard
---

## 一句话

Web agent RL anchor：用 online curriculum 处理稀疏反馈和 policy drift。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | WebArena-Lite web interaction。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2411.02337_25_webrl-online-curriculum.md` |
| Interaction loop | online web trajectories。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2411.02337_25_webrl-online-curriculum.md` |
| Reward / feedback | outcome-supervised reward model。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2411.02337_25_webrl-online-curriculum.md` |
| Optimizer / update | online curriculum RL；具体实现需 L2 再核。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2411.02337_25_webrl-online-curriculum.md` |
| Credit assignment | trajectory-level sparse feedback。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2411.02337_25_webrl-online-curriculum.md` |
| Exploration / replay | 核心贡献；从 unsuccessful attempts 生成新任务。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2411.02337_25_webrl-online-curriculum.md` |
| Warm start / data | 有 SFT / BC baseline 和初始化问题。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2411.02337_25_webrl-online-curriculum.md` |

## 核心增量

**事实 [PDF p.1]**: WebRL 是 ICLR 2025 会议论文，提出 self-evolving online curriculum RL 训练 open LLM web agents。

**事实 [PDF abstract, p.1]**: 论文把 web agent 训练的三个关键挑战定义为 training tasks scarcity、sparse feedback signals、policy distribution drift。

**事实 [PDF abstract, p.1]**: 方法包含 self-evolving curriculum、outcome-supervised reward model、adaptive RL strategies；在 WebArena-Lite 上把 Llama-3.1-8B 从 4.8% 提到 42.4%，GLM-4-9B 从 6.1% 提到 43%。

**解释 [本项目判断]**: 这是 web lane 的强 anchor，但机制重点应放在 curriculum / reward model / online learning stability，不展开网页任务细节。

**收录依据 [queue/audit]**: survey 正文提到 + ICLR 2025 + 官方代码/模型/数据公开，直接抽卡。代码：`https://github.com/THUDM/WebRL`。

## 谱系位置

- 上游：WebArena / behavior cloning web agents。
- 同期：RAGEN、WebAgent-R1。
- 下游：web/GUI multi-turn RL、online curriculum RL。

## 优缺点

- ✅ [PDF p.1]: ICLR 2025 + code/model/data public。
- ✅ [PDF abstract, p.1]: 明确针对 sparse feedback 和 policy drift。
- ⚠️ [本项目判断]: curriculum 机制和 data generation 可能混在一起，后续 L2 需要分清 RL update 与 task generation。

## Evidence

- paper brief: `_meta/briefs/papers/2411.02337_25_webrl-online-curriculum.md`
- PDF / HTML: `papers/2411.02337-webrl-online-curriculum.pdf`
- survey windows: GFCR / Landscape
- PDF: `papers/2411.02337-webrl-online-curriculum.pdf`
- source anchors: abstract p.1; figure 1 p.1; introduction p.1-2。

<!-- pdf: papers/2411.02337-webrl-online-curriculum.pdf -->

<!-- brief: _meta/briefs/papers/2411.02337_25_webrl-online-curriculum.md -->

<!-- survey: GFCR / Landscape -->
