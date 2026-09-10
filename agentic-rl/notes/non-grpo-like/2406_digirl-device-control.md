---
title: "DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning"
authors: [Hao Bai, Yifei Zhou, Mert Cemri, et al.]
year: 2024
venue: NeurIPS 2024
url: https://arxiv.org/abs/2406.11896
arxiv_id: 2406.11896

lane: gui-rl
paper_type: environment-recipe
lifecycle_role: canonical-anchor
data_overlap: true

rl_axes:
  environment: gui
  interaction_mode: online
  reward_signal: verifier
  optimizer: actor-critic
  credit_assignment: trajectory
  data_reuse: curriculum
  sft_warm_start: standard
---

## 一句话

GUI/device-control RL anchor：offline RL 初始化后接 offline-to-online RL。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | Android GUI / device-control environment。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2406.11896_24_digirl-device-control.md` |
| Interaction loop | offline-to-online GUI action trajectories。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2406.11896_24_digirl-device-control.md` |
| Reward / feedback | VLM-based evaluator / task success。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2406.11896_24_digirl-device-control.md` |
| Optimizer / update | advantage-weighted RL。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2406.11896_24_digirl-device-control.md` |
| Credit assignment | trajectory/step via advantage estimation。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2406.11896_24_digirl-device-control.md` |
| Exploration / replay | automatic curriculum。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2406.11896_24_digirl-device-control.md` |
| Warm start / data | pre-trained VLM + static demonstrations。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2406.11896_24_digirl-device-control.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: DigiRL 针对 in-the-wild device control through GUIs，指出 static demonstrations 无法处理真实 GUI 的 stochasticity 和 non-stationarity。

**事实 [PDF abstract, p.1]**: 方法用两阶段训练：offline RL 初始化模型，再 offline-to-online RL；构建 parallelizable Android learning environment 和 VLM-based evaluator。

**事实 [PDF abstract, p.1]**: 论文采用 advantage-weighted RL，并增强 advantage estimators 以处理 stochasticity，同时使用 automatic curriculum 提取最大 learning signal。

**事实 [PDF abstract, p.1]**: 1.3B VLM 在 AitW 上从 17.7% 到 67.2%，绝对提升 49.5%。

**解释 [本项目判断]**: 这是 web/GUI lane 的 canonical anchor，和 WebRL/WebAgent-R1 形成 “browser web vs device GUI” 对照。

**收录依据 [queue/audit]**: Landscape web/GUI section 正文提到 + NeurIPS 2024 + 官方代码。代码：`https://github.com/DigiRL-agent/digirl`。

## 谱系位置

- 上游：
- 同期：
- 下游：

## 优缺点

- ✅ [paper]:
- ⚠️ [本项目判断]:

## Evidence

- paper brief: `_meta/briefs/papers/2406.11896_24_digirl-device-control.md`
- PDF / HTML: `papers/2406.11896-digirl-device-control.pdf`
- survey windows: Landscape
- PDF: `papers/2406.11896-digirl-device-control.pdf`
- source anchors: abstract p.1; introduction p.1。

<!-- pdf: papers/2406.11896-digirl-device-control.pdf -->

<!-- brief: _meta/briefs/papers/2406.11896_24_digirl-device-control.md -->

<!-- survey: Landscape -->
