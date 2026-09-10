---
title: "PACED: Distillation and On-Policy Self-Distillation at the Frontier of Student Competence"
authors: [Yuanda Xu, et al.]
org: princeton
year: 2026
venue: arxiv
arxiv_id: 2603.11178
url: https://arxiv.org/abs/2603.11178

confidence: 3
verified: a

surveys:
  song-2026: "§7.1 curriculum and difficulty adaptation; Table 9"

addresses:
  - capacity-gap
  - cliff-prompt-zero-gradient

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: one-shot
  filter: hardness
  extra: none
---

> **一句话**：按 student pass rate 采样能力边界的 curriculum OPD。

## 核心做法

PACED 认为 uniform distillation 浪费在两端：student 已掌握的问题梯度小，完全不会的问题 gradient SNR 也塌陷；它用 student empirical pass rate 估计 prompt difficulty，并按 Beta-kernel 权重集中训练在 competence boundary。

$$w(p)=p^\alpha(1-p)^\beta,\quad \alpha=\beta=1\Rightarrow w(p)=p(1-p)$$

实操含义：在 generation 前选择合适 prompt，而不是在 generation 后才靠 token/trajectory weighting 修补信号质量。

## 谱系位置

- 上游：TAID / curriculum distillation — 都控制 teacher signal 难度；PACED 控制 prompt 难度。
- 同期：Uni-OPD (2026) — Uni-OPD 把 PACED 的 pass-rate criterion 扩展到 difficulty + correctness 双准则。
- 下游：long-horizon OPD curriculum — pass-rate SNR 给 cliff prompt / too-easy prompt 提供统一解释。

## 优缺点

- ✅ [song-2026 §7.1]: Beta family 是 bounded misspecification 下 leading-order minimax-optimal weighting，默认 p(1-p) 捕获多数收益。
- ✅ [作者 ack Abstract]: 不需要架构修改或额外超参，只需 student rollouts 估计 pass rate。
- ⚠️ [song-2026 §7.1]: 单次 pass-rate 估计可能 stale；iterative recomputation 可有增益但增加成本。

## headline number

无 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv abstract -->
<!-- song-2026: §7.1 Curriculum and Difficulty Adaptation / Table 9 -->
