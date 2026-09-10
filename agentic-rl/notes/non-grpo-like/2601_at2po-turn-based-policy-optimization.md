---
title: "AT^2PO: Agentic Turn-based Policy Optimization via Tree Search"
authors: [Zefang Zong, Dingwei Chen, Yang Li, et al.]
year: 2026
venue: arxiv
url: https://arxiv.org/abs/2601.04767
arxiv_id: 2601.04767

lane: tool-rl
paper_type: core-rl-method
lifecycle_role: frontier-candidate
data_overlap: false

rl_axes:
  environment: tool
  interaction_mode: online
  reward_signal: sparse
  optimizer: policy-gradient
  credit_assignment: step
  data_reuse: none
  sft_warm_start: standard
---

## 一句话

用 turn-level tree search 同时做探索、credit 和 policy update。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | search-agent multi-turn benchmarks。 | 聚焦 tool interaction 里的 turn-level decision。 | `_meta/briefs/papers/2601.04767_at2po-turn-based-policy-optimization.md` |
| Interaction loop | interleaved reasoning/tool turns with observations from tool responses。 | turn 是 agent 与环境交互的自然训练单位。 | brief p.1 introduction |
| Reward / feedback | sparse outcome reward propagated through turn-level tree。 | 将终局 sparse feedback 转为 per-turn supervision。 | brief p.1-p.2 method window |
| Optimizer / update | Agentic Turn-based Policy Optimization with turn-level importance/clipping。 | 避免 token/sequence objective 与 multi-turn sampling process 错位。 | brief p.2 method window |
| Credit assignment | Turn-wise Credit Assignment。 | 给每个 turn 分配 fine-grained value/advantage。 | brief p.2 method window |
| Exploration / replay | Entropy-Guided Tree Expansion。 | 把 rollout budget 投到高不确定 turn，提升探索效率。 | brief p.2 and p.4 method windows |
| Warm start / data | 基于 search-agent RL pipeline；非数据机制论文。 | 贡献在 RL objective 和 rollout/search structure。 | brief p.1 front matter |

## 核心增量

**事实 [brief p.1]**: AT^2PO 直接针对 agentic RL 的 limited exploration diversity、sparse credit assignment、misaligned policy optimization 三个问题。

**事实 [brief p.2]**: 方法包含 Entropy-Guided Tree Expansion、Turn-wise Credit Assignment、Agentic Turn-based Policy Optimization 三部分；ATPO 可独立于 tree search 集成到 multi-turn RL pipeline。

**事实 [brief p.1-p.2]**: 论文报告在 7 个 search-agent benchmarks 上相对 state-of-the-art baseline 平均提升最高 1.84 个百分点，并用 ablation 验证组件贡献。

**解释 [本项目判断]**: 这是 Tree-GRPO 之后的 turn-level refinement：Tree-GRPO 用 agent step tree 构造过程信号，AT^2PO 进一步用 entropy 选择扩展节点，并把 policy update 显式改成 turn-level。

## 谱系位置

- 上游：GRPO、Tree-GRPO、Search-R1/R1-Searcher、ARPO。
- 同期：StepPO、APPO、AEPO。
- 下游：turn-level exploration budget allocation、turn-level clipping / advantage estimation。

## 优缺点

- ✅ [brief p.2]: 同时处理 exploration、credit、policy objective 三个 agentic RL 痛点。
- ✅ [brief p.1]: 官方代码公开。
- ⚠️ [本项目判断]: 当前主要在 search-agent benchmarks 验证，是否泛化到 GUI/code/web action space 还需后续 comparison。

## Evidence

- paper brief: `_meta/briefs/papers/2601.04767_at2po-turn-based-policy-optimization.md`
- PDF / HTML: `papers/2601.04767-at2po-turn-based-policy-optimization.pdf`
- survey windows: post-survey strict-core recall

<!-- pdf: papers/2601.04767-at2po-turn-based-policy-optimization.pdf -->
<!-- brief: _meta/briefs/papers/2601.04767_at2po-turn-based-policy-optimization.md -->
<!-- survey: post-survey strict-core recall -->
