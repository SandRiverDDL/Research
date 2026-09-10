---
title: "Multi-Rollout On-Policy Distillation via Peer Successes and Failures"
authors: [Weichen Yu, et al.]
org: cmu
year: 2026
venue: arxiv
arxiv_id: 2605.12652
url: https://arxiv.org/abs/2605.12652

confidence: 3
open_source: no
verified: a

surveys:
  song-2026: "§6 dynamics; peer-conditioned multi-rollout weighting"

addresses:
  - cross-rollout-credit
  - coarse-credit-assignment

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: verifier-pass
  extra: none
---

> **一句话**：peer-conditioned rollout weighting 代表作。

## 核心做法

单条 rollout 的 OPD 只看当前 trajectory，无法利用同一 prompt 下其他成功/失败样本；MOPD 把同 prompt 多条 student rollouts 按 verifier 分组，用成功 peer 和失败 peer 构造 teacher context。

$$\mathcal{L}_{\mathrm{MOPD}}=\frac1N\sum_i\sum_t D(\pi_\theta(\cdot|x,y_{<t}^{(i)})\|q_\phi^{\mathrm{peer}}(\cdot|x,C_i,y_{<t}^{(i)}))$$

实操上，成功 peer 提供可模仿路径，失败 peer 提供 contrastive negative context，让 teacher signal 分解出 failure-specific residual。

## 谱系位置

- 上游：GKD / OPD (2024) — 仍是 student rollout 上做 token-level teacher guidance
- 上游：SDPO (2026) — 都做 self-distillation，但 MOPD 不依赖文本反馈，转向 rollout group 结构
- 同期：TIP / EGRSD (2026) — TIP 用 token entropy/divergence 做选择，MOPD 用 cross-rollout structure 做 credit assignment
- 下游：GEAR / CoPD (2026) — survey 将其放在 dynamics/stabilization 分支，与 granularity-adaptive weighting 和 co-evolution 相邻

## 优缺点

- ✅ [song-2026 §6]：peer conditioning 捕捉单 rollout 不可见的成功/失败对比结构，与 token-level entropy 或 step-level divergence 互补
- ✅ [作者 ack §4.2]：默认用成功与失败 peer 共同构造 context，把 positive imitation 与 contrastive signal 合并
- ⚠️ [作者 ack §G Limitation]：需要每 prompt 多 rollout 与 verifier 分组，计算和上下文长度开销高于单轨 OPD

## headline number

- AIME2024 mean@8 17.09 → 28.54 vs GRPO on Qwen3-4B（§5.2 Table 1）

<!-- pdf: §4 Multi-Rollout OPD / §5.2 Main Results / Appendix G Limitation -->
<!-- song-2026: §6 Dynamics / peer-conditioned multi-rollout weighting -->
