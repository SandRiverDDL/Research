---
title: "VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use"
authors: [Dongfu Jiang, Yi Lu, Zhuofeng Li, et al.]
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2509.01055
arxiv_id: 2509.01055

lane: tool-rl
paper_type: infra-interface
lifecycle_role: frontier-candidate
data_overlap: true

rl_axes:
  environment: tool
  interaction_mode: online
  reward_signal: verifier
  optimizer: grpo-like
  credit_assignment: trajectory
  data_reuse: none
  sft_warm_start: standard
---

## 一句话

Tool-use RL system-interface seed：把 VeRL 扩展到多工具多轮 ARLT。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | code/search/SQL/vision/web/software engineering tool environments。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2509.01055_25_verltool.md` |
| Interaction loop | multi-turn tool trajectories。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2509.01055_25_verltool.md` |
| Reward / feedback | verifiable rewards / task-specific verifier。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2509.01055_25_verltool.md` |
| Optimizer / update | PPO/GRPO in VeRL workflow。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2509.01055_25_verltool.md` |
| Credit assignment | trajectory-level；主要通过统一 trajectory schema 回流。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2509.01055_25_verltool.md` |
| Exploration / replay | 非主轴。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2509.01055_25_verltool.md` |
| Warm start / data | standard。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2509.01055_25_verltool.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: 论文指出 RLVR 成功增强 LLM reasoning，但主要局限在 single-turn interaction without tool integration；Agentic RL with Tool use 需要处理 multi-turn tool interactions。

**事实 [PDF abstract, p.1]**: VerlTool 提供 upstream alignment with VeRL、unified tool management、asynchronous rollout execution、6 个 ARLT domains 的评测。

**事实 [PDF abstract, p.1]**: 论文将 ARLT formalize 为 multi-turn trajectories with multi-modal observation tokens，覆盖 code execution、search、SQL、vision processing 等工具。

**解释 [本项目判断]**: 这篇更偏 training system / interface，但因为它定义 ARLT rollout interface，对本项目的 environment-interface 轴有用。

**收录依据 [queue/audit]**: survey 正文提到 + 官方开源 + 明确 ARLT mechanism，走 arXiv exception；有 model-system overlap。代码：`https://github.com/TIGER-AI-Lab/verl-tool`。

## 谱系位置

- 上游：VeRL、RLVR、ToolRL、Search-R1。
- 同期：Agent Lightning、RAGEN。
- 下游：tool-augmented RL infra / unified ARLT experiments。

## 优缺点

- ✅ [PDF abstract, p.1]: 明确 formalize ARLT multi-turn trajectories。
- ✅ [PDF abstract, p.1]: 官方开源，并解决 rollout execution bottleneck。
- ⚠️ [本项目判断]: 主要贡献可能是系统工程；不要让它主导方法谱系。

## Evidence

- paper brief: `_meta/briefs/papers/2509.01055_25_verltool.md`
- PDF / HTML: `papers/2509.01055-verltool.pdf`
- survey windows: GFCR / Landscape
- PDF: `papers/2509.01055-verltool.pdf`
- source anchors: abstract p.1; figure 1 p.1; introduction p.1-2。

<!-- pdf: papers/2509.01055-verltool.pdf -->

<!-- brief: _meta/briefs/papers/2509.01055_25_verltool.md -->

<!-- survey: GFCR / Landscape -->
