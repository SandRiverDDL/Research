---
title: "SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution"
authors: [Yuxiang Wei, Olivier Duchenne, Jade Copet, et al.]
year: 2025
venue: NeurIPS 2025
url: https://arxiv.org/abs/2502.18449
arxiv_id: 2502.18449

lane: coding-rl
paper_type: environment-recipe
lifecycle_role: frontier-candidate
data_overlap: true

rl_axes:
  environment: code
  interaction_mode: offline-rollout
  reward_signal: verifier
  optimizer: policy-gradient
  credit_assignment: trajectory
  data_reuse: curriculum
  sft_warm_start: standard
---

## 一句话

软件工程 RL anchor：用 open software evolution 和 rule reward 训练 reasoning model。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | software evolution / issue resolution tasks。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2502.18449_25_swe-rl-open-software-evolution.md` |
| Interaction loop | offline software trajectories / generated solutions。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2502.18449_25_swe-rl-open-software-evolution.md` |
| Reward / feedback | rule-based verifier / similarity reward。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2502.18449_25_swe-rl-open-software-evolution.md` |
| Optimizer / update | RL post-training。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2502.18449_25_swe-rl-open-software-evolution.md` |
| Credit assignment | trajectory-level。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2502.18449_25_swe-rl-open-software-evolution.md` |
| Exploration / replay | data scaling through software evolution。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2502.18449_25_swe-rl-open-software-evolution.md` |
| Warm start / data | Llama 3 base / prior SFT context。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2502.18449_25_swe-rl-open-software-evolution.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: SWE-RL 将 RL-based LLM reasoning 扩展到 real-world software engineering，使用 open-source software evolution data。

**事实 [PDF abstract, p.1]**: 方法使用 lightweight rule-based reward，例如 ground-truth 与 LLM-generated solutions 的 similarity score。

**事实 [PDF abstract, p.1]**: Llama3-SWE-RL-70B 在 SWE-bench Verified 上达到 41.0% solve rate，并出现 out-of-domain generalized reasoning gains。

**解释 [本项目判断]**: 这篇有明显 Agent Data overlap，因为核心资源是 software evolution data；但它也符合 coding-agent RL / verifier reward anchor，应在本项目保留机制卡。

**收录依据 [queue/audit]**: Landscape/GFCR 提到 + NeurIPS 2025 + 官方代码。代码：`https://github.com/facebookresearch/swe-rl`。

## 谱系位置

- 上游：
- 同期：
- 下游：

## 优缺点

- ✅ [paper]:
- ⚠️ [本项目判断]:

## Evidence

- paper brief: `_meta/briefs/papers/2502.18449_25_swe-rl-open-software-evolution.md`
- PDF / HTML: `papers/2502.18449-swe-rl-open-software-evolution.pdf`
- survey windows: Landscape / GFCR
- PDF: `papers/2502.18449-swe-rl-open-software-evolution.pdf`
- source anchors: abstract p.1; introduction p.1。

<!-- pdf: papers/2502.18449-swe-rl-open-software-evolution.pdf -->

<!-- brief: _meta/briefs/papers/2502.18449_25_swe-rl-open-software-evolution.md -->

<!-- survey: Landscape / GFCR -->
