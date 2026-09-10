---
title: "HDPO: Hybrid Distillation Policy Optimization via Privileged Self-Distillation"
authors: [Ken Ding]
org: nvidia
year: 2026
venue: arxiv
arxiv_id: 2603.23871
url: https://arxiv.org/abs/2603.23871

confidence: 3
verified: a

surveys:
  song-2026: "§5.3 privileged information self-distillation; self-distillation table"

addresses:
  - cliff-prompt-zero-gradient
  - compounding-error

decisions:
  rollout: student
  loss: jsd
  signal: logit
  iteration: continuous
  filter: verifier-pass
  extra: privileged-info
---

> **一句话**：cliff-prompt 修补型自蒸馏。

## 核心做法

GRPO 在 all-fail prompt 上 advantage 没有差异，policy gradient 近似消失；HDPO 在这些 cliff prompt 上用同一个模型携带 ground truth 条件生成 privileged rollouts，并把成功轨迹的分布蒸回无 ground-truth student。

$$\mathcal{L}_{\mathrm{HDPO}}=\mathcal{L}_{\mathrm{GRPO}}+\lambda\,\mathcal{L}_{\mathrm{JSD}}(\pi_{\mathrm{GT\text{-}cond}}\|\pi_\theta)$$

实操含义是主训练仍走 GRPO，只在 batch 中检测到全失败 prompt 时注入 JSD self-distillation 辅助梯度。

## 谱系位置

- 上游：GRPO (2024) — HDPO 修补 GRPO 在 all-fail group 上无有效梯度的问题
- 上游：OPSD (2026) — 同属 ground-truth-conditioned privileged self-distillation
- 同期：PACED (2026) — PACED 通过 curriculum 避开 pass-rate≈0 的低 SNR prompt，HDPO 直接给这些 prompt 加信号
- 下游：GATES / π-Distill (2026) — survey 将其放在放宽 ground-truth PI 与统一 PI 理论的前序位置

## 优缺点

- ✅ [song-2026 §5.3]：JSD self-distillation 在能力边界提供非零梯度，不需要限制 problem distribution
- ✅ [作者 ack §3.4]：same-model privileged teacher 缩小 cross-model realizability gap，R=1 filtering 与 KL-regularized optimum 有形式联系
- ⚠️ [作者 ack §6]：实验规模集中在 Qwen2.5-Math-1.5B / OpenMathInstruct-2，提升主要体现在 pass@k 而非 pass@1

<!-- pdf: §3 Method / §3.4 Theoretical Analysis / §4.2 Results / §6 Limitations -->
<!-- song-2026: §5.3 Privileged Information / self-distillation table -->
