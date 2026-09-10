---
title: "SCOPE: Signal-Calibrated On-Policy Distillation Enhancement with Dual-Path Adaptive Weighting"
authors: [Binbin Zheng, et al.]
org: other
year: 2026
venue: arxiv
arxiv_id: 2604.10688
url: https://arxiv.org/abs/2604.10688

confidence: 4
verified: a

surveys:
  song-2026: "§6.1 token and sample weighting; Table 9"

addresses:
  - flawed-prefix-trap
  - coarse-credit-assignment

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: one-shot
  filter: trajectory-level
  extra: none
---

> **一句话**：按 rollout correctness 分流的双路径 OPD。

## 核心做法

SCOPE 先按 on-policy rollout 是否正确分成两条 supervision path：错误轨迹用 teacher-perplexity-weighted KL，优先让 teacher 确实有 corrective capability 的样本提供监督；正确轨迹用 student-perplexity-weighted MLE，把强化集中在学生低置信但已到能力边界的样本上。

$$\mathcal{L}=\mathbf{1}_{\mathrm{wrong}}w_T\mathcal{L}_{\mathrm{KL}}+\mathbf{1}_{\mathrm{correct}}w_S\mathcal{L}_{\mathrm{MLE}}$$

实操含义：不把所有 rollout 放进同一种 token-level KL，而是用 trajectory correctness 先做 coarse routing，再在每条 path 内做 group-level normalization。

## 谱系位置

- 上游：OPD / GRPO — OPD 给 dense KL，GRPO 给 sparse outcome；SCOPE 把二者按 correctness 分流。
- 同期：TIP (2026) — TIP 细粒度 token selection，SCOPE 选择更粗的 trajectory-level path routing。
- 同期：SOD (2026) — SOD 认为 tool-call cascade 需要 step-level；SCOPE 更适合整条 trajectory 信号质量分化明显的场景。

## 优缺点

- ✅ [作者 ack Abstract]: incorrect path 用 teacher perplexity 抑制 unreliable guidance，correct path 用 student perplexity 避免过度强化已掌握样本。
- ✅ [song-2026 §6.1]: coarse routing 对 flawed-prefix trap 更稳，因为单个坏 token 不会污染整条梯度。
- ⚠️ [song-2026 §6.1]: trajectory-level routing 会牺牲局部 token/step 的信号保真度。

## headline number

无 Table/Fig anchor 的 abstract 数字不放入 headline number。

<!-- pdf: arXiv abstract -->
<!-- song-2026: §6.1 Token and Sample Weighting / Table 9 -->
