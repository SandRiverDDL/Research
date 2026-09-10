---
title: "DP-OPD: Differentially Private On-Policy Distillation for Language Models"
authors: [Fatemeh Khadem, et al.]
org: other
year: 2026
venue: arxiv
arxiv_id: 2604.04461
url: https://arxiv.org/abs/2604.04461

confidence: 4
verified: a

surveys:
  song-2026: "§8.3 privacy and evaluation methodology; Table 9"

addresses:
  - privacy-leakage
  - exposure-bias

decisions:
  rollout: student
  loss: forward-kl
  signal: logit
  iteration: one-shot
  filter: none
  extra: none
---

> **一句话**：带 record-level privacy guarantee 的 OPD。

## 核心做法

DP-OPD 在 student 侧用 DP-SGD 执行 on-policy generalized KD，teacher 保持冻结并在 student-generated continuations 上提供 dense token targets；与 DP synthetic text 或 teacher/student 双侧 DP 相比，它避免了离线合成流水线，也不把 DP 噪声施加到大 teacher。

$$y\sim\pi_\theta,\quad \nabla_\theta\mathcal{L}_{\mathrm{GKD}} \xrightarrow{\mathrm{clip+noise}} \mathrm{DP\mbox{-}SGD}$$

实操含义：privacy 约束下，on-policy rollout 可以减少 DP noise 与 exposure bias 的复合误差。

## 谱系位置

- 上游：GKD / OPD — 继承 student-generated trajectory 上的 dense teacher targets。
- 同期：系统级 OPD — DP-OPD 把 OPD 从性能优化扩展到 privacy/trust 维度。
- 下游：private self-distillation — 综述指出 scaling 到 reasoning-capable LLM 与 self-distillation 仍是开放问题。

## 优缺点

- ✅ [作者 ack Abstract]: 只在 student 上施加 DP-SGD，teacher frozen，避免 DP-optimizing large teacher。
- ✅ [song-2026 §8.3]: on-policy formulation 适合 DP，因为 self-generated prefixes 能降低 DP noise 导致的 compounding errors。
- ⚠️ [song-2026 §8.3]: 目前是 early principled framework，扩展到 reasoning-capable LLM 与 self-distillation 仍未解决。

## headline number

无 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv abstract -->
<!-- song-2026: §8.3 Privacy and Evaluation Methodology / Table 9 -->
