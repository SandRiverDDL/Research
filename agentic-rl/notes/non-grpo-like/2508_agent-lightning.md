---
title: "Agent Lightning: Train ANY AI Agents with Reinforcement Learning"
authors: [Xufang Luo, Yuge Zhang, Zhiyuan He, et al.]
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2508.03680
arxiv_id: 2508.03680

lane: environment-rl
paper_type: infra-interface
lifecycle_role: frontier-candidate
data_overlap: true

rl_axes:
  environment: mixed
  interaction_mode: online
  reward_signal: outcome
  optimizer: actor-critic
  credit_assignment: segment
  data_reuse: off-policy
  sft_warm_start: unclear
---

## 一句话

系统/机制交界卡：把任意 agent execution 解耦成可训练 MDP transitions。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | mixed；existing agents / dynamic workflows / multi-agent scenarios。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.03680_25_agent-lightning.md` |
| Interaction loop | agent execution trace 被转换为 MDP transitions。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.03680_25_agent-lightning.md` |
| Reward / feedback | outcome-based environment feedback；具体 reward 依赖任务。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.03680_25_agent-lightning.md` |
| Optimizer / update | LightningRL，hierarchical RL；摘要强调 credit assignment module。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.03680_25_agent-lightning.md` |
| Credit assignment | trajectory-to-transition decomposition 是核心。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.03680_25_agent-lightning.md` |
| Exploration / replay | 非主轴。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.03680_25_agent-lightning.md` |
| Warm start / data | 不清楚。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2508.03680_25_agent-lightning.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: Agent Lightning 目标是让 RL-based training 可用于任意 AI agent；它强调 decoupling agent execution and training，避免现有方法把 RL training 与 agent 紧耦合或依赖 sequence concatenation with masking。

**事实 [PDF abstract, p.1]**: 论文把 agent execution 形式化为 MDP，定义统一 data interface，并提出 hierarchical RL algorithm LightningRL，其中包含 credit assignment module，用于把任意 agent 生成的 trajectories 分解成 training transitions。

**事实 [PDF abstract, p.1]**: 系统设计上提出 Training-Agent Disaggregation architecture，并把 observability framework 引入 agent runtime；实验覆盖 text-to-SQL、RAG、math tool-use。

**解释 [本项目判断]**: 这篇一半属于 `agentic-rl`，一半属于未来 `model-system`。在本项目只保留机制视角：agent trace 如何被形式化、切分、回流到 RL update。

**收录依据 [queue/audit]**: survey 正文提到 + 官方代码 + 明确 MDP / hierarchical RL / credit assignment mechanism，走 arXiv exception；标记 `model-system` cross-link。代码：`https://github.com/microsoft/agent-lightning`。

## 谱系位置

- 上游：multi-turn RL / agent frameworks / RLHF infra。
- 同期：RAGEN、GiGPO、VerlTool。
- 下游：通用 agent RL training interface / training-agent disaggregation。

## 优缺点

- ✅ [PDF abstract, p.1]: 明确提出 MDP formulation、unified data interface、credit assignment module。
- ✅ [PDF abstract, p.1]: 解决 real-world agent execution 与 RL training 的耦合问题，适合作为 system-interface seed。
- ⚠️ [本项目判断]: 容易滑向 training system / recipe；后续抽卡只保留 RL loop 机制，不展开工程细节。

## Evidence

- paper brief: `_meta/briefs/papers/2508.03680_25_agent-lightning.md`
- PDF / HTML: `papers/2508.03680-agent-lightning.pdf`
- survey windows: Credit Assignment / Landscape
- PDF: `papers/2508.03680-agent-lightning.pdf`
- source anchors: abstract p.1; introduction p.1。

<!-- pdf: papers/2508.03680-agent-lightning.pdf -->

<!-- brief: _meta/briefs/papers/2508.03680_25_agent-lightning.md -->

<!-- survey: Credit Assignment / Landscape -->
