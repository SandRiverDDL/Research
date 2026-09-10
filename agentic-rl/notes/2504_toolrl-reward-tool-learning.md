---
title: "ToolRL: Reward is All Tool Learning Needs"
authors: [Cheng Qian, Emre Can Acikgoz, Qi He, et al.]
year: 2025
venue: arxiv
url: https://arxiv.org/abs/2504.13958
arxiv_id: 2504.13958

lane: tool-rl
paper_type: environment-recipe
lifecycle_role: frontier-candidate
data_overlap: false

rl_axes:
  environment: tool
  interaction_mode: online
  reward_signal: tool-success
  optimizer: grpo-like
  credit_assignment: tool-call
  data_reuse: none
  sft_warm_start: standard
---

## 一句话

工具使用 RL 的 reward-design anchor：粗粒度 answer reward 不够。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | external tools / tool-integrated reasoning。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.13958_25_toolrl-reward-tool-learning.md` |
| Interaction loop | multi-step feedback-driven tool loop。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.13958_25_toolrl-reward-tool-learning.md` |
| Reward / feedback | 核心贡献；从 coarse answer matching 转向工具选择和应用的细粒度 reward。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.13958_25_toolrl-reward-tool-learning.md` |
| Optimizer / update | GRPO。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.13958_25_toolrl-reward-tool-learning.md` |
| Credit assignment | tool-call / temporal reward granularity。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.13958_25_toolrl-reward-tool-learning.md` |
| Exploration / replay | 非主轴。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.13958_25_toolrl-reward-tool-learning.md` |
| Warm start / data | SFT 是对照和 warm-start 背景。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2504.13958_25_toolrl-reward-tool-learning.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: 论文指出 SFT 学工具使用在 unfamiliar / complex tool-use scenarios 上泛化差；工具任务 reward design 有独特挑战，因为可能调用多个工具和多样参数，coarse answer matching 不能给足细粒度 feedback。

**事实 [PDF abstract, p.1]**: 论文系统探索 reward types、scales、granularity、temporal dynamics，并提出面向 tool selection / application 的 principled reward design，用 GRPO 训练 LLM。

**事实 [PDF abstract, p.1]**: 作者报告方法相对 base models 提升 17%、相对 SFT 提升 15%，并开源代码。

**解释 [本项目判断]**: 这张卡的价值是 reward/verifier 轴，而不是 tool benchmark 本身。后续应重点读 reward decomposition 和工具调用失败的反馈设计。

**收录依据 [queue/audit]**: survey 正文提到 + 官方开源 + 明确 RL mechanism，走 arXiv exception。代码：`https://github.com/qiancheng0/ToolRL`。

## 谱系位置

- 上游：Tool-integrated reasoning、GRPO、SFT tool-use。
- 同期：VerlTool、Tool-R0、Search-R1。
- 下游：tool-use RL reward / verifier design。

## 优缺点

- ✅ [PDF abstract, p.1]: 直接研究 tool-use RL reward granularity。
- ✅ [PDF p.1 footnote]: 官方代码开源。
- ⚠️ [本项目判断]: arXiv 版本；需要后续核查是否已有正式会议版本。

## Evidence

- paper brief: `_meta/briefs/papers/2504.13958_25_toolrl-reward-tool-learning.md`
- PDF / HTML: `papers/2504.13958-toolrl-reward-tool-learning.pdf`
- survey windows: Landscape / seed queue
- PDF: `papers/2504.13958-toolrl-reward-tool-learning.pdf`
- source anchors: abstract p.1; intro p.1-2。

<!-- pdf: papers/2504.13958-toolrl-reward-tool-learning.pdf -->

<!-- brief: _meta/briefs/papers/2504.13958_25_toolrl-reward-tool-learning.md -->

<!-- survey: Landscape / seed queue -->
