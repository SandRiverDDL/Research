---
title: "Stage-1 Controls the Entropy Regime, Not the Outcome"
authors: [Jianxiong Shen]
org: other
year: 2026
venue: arxiv
arxiv_id: 2606.09059
url: https://arxiv.org/abs/2606.09059

confidence: 4
verified: a

addresses:
  - entropy-collapse
  - no-new-capability

decisions:
  rollout: student
  loss: reward
  signal: outcome
  iteration: one-shot
  filter: none
  extra: none
---

> **一句话**：OPD warm-start 收益边界的反证。

## 核心做法

论文在 small-data VLM RL 设置中比较 SFT 与 OPD warm-start，结论是 Stage-1 强相关于 entropy regime，而不是最终 outcome。OPD 进入 RL 时 policy entropy 更高，初始化时 answer diversity / pass@16 更高，但 RL 后优势缩小或消失。

$$H(\pi_{\theta_0}^{\mathrm{OPD}})>H(\pi_{\theta_0}^{\mathrm{SFT}}),\qquad \Delta_{\mathrm{final}}\approx 0$$

实操含义：OPD 作为 warm-start 的价值可能在探索形态，而不一定转化为最终平均性能。

## 机制发现（可选）

- [作者 ack paper brief Abstract / §4-6]: 三种 warm-start 在 Geometry3K internal validation 上进入窄 endpoint band，Stage-1 改变 final in-domain endpoint 的证据弱。
- [作者 ack paper brief Abstract / §6.1]: OPD 进入 RL 时有更高 policy entropy，且 entropy gap 在可用 trajectories 中仍可见。
- [作者 ack paper brief Abstract / §6.3]: 初始化处的 diversity / pass@16 优势在 RL endpoint 和 MathVista OOD 上消失或变小。

## 谱系位置

- 上游：Internalize-the-Temperature (2026) — 关注 OPD/RL 中 entropy 维持。
- 同期：Post-Training is About States (2026) — 都在反思 post-training 阶段的真实作用。
- 下游：synthesis report — 可作为“OPD 不是万能 warm-start”的证据。

## 优缺点

- ✅ [作者 ack paper brief §6]: 提供“OPD warm-start 主要控制 entropy regime”的降温证据，避免把初始化探索收益误读成最终效果。
- ⚠️ [作者 ack paper brief §8]: 结论来自 small-data VLM RL 设置，不能直接推广到所有 LLM reasoning OPD。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv HTML brief Abstract / §4 / §5 / §6 / §8 -->
