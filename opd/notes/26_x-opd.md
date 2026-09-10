---
title: "X-OPD: Cross-Modal On-Policy Distillation for Capability Alignment in Speech LLMs"
authors: [Di Cao, et al.]
org: microsoft
year: 2026
venue: interspeech-2026
arxiv_id: 2603.24596
url: https://arxiv.org/abs/2603.24596

confidence: 2
verified: s

surveys:
  song-2026: "§7.4 multimodal / cross-modal OPD; Table 9"

addresses:
  - cross-tokenizer
  - exposure-bias
  - teacher-pattern-mismatch

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: none
  extra: privileged-info
---

> **一句话**：speech LLM 对齐 text teacher 的 cross-modal OPD。

## 核心做法

X-OPD 让 speech LLM 在自身 speech/multimodal distribution 上 rollout，再由 text-based teacher 对这些轨迹提供 token-level feedback，把文本推理能力蒸进 speech LLM 的多模态表示。关键不是让 teacher 看音频，而是把 text reasoning structure 当成 modality-agnostic scaffold。

$$y\sim\pi_{\theta}^{\mathrm{speech}}(\cdot|x_{\mathrm{audio}}),\quad \pi_T^{\mathrm{text}}(\cdot|y_{<t})\rightarrow \text{token feedback}$$

实操含义：cross-modal OPD 需要先解决 student rollout 与 text teacher distribution 的距离，否则 teacher feedback 在 speech state 上不可用。

## 谱系位置

- 上游：VOLD (2025) — VOLD 用 text-only teacher 指导 VLM reasoning；X-OPD 把同一原则移到 speech LLM。
- 同期：SimCT / VOLD — 都在放宽 OPD 的同 tokenizer/同 modality 假设。
- 下游：cross-modal / latent-space OPD — 为连续信号空间中的 OPD 提供 empirical starting point。

## 优缺点

- ✅ [作者 ack Abstract]: SFT/RL 无法完全弥合 E2E speech LLM 与 text counterpart gap，X-OPD 直接针对能力对齐。
- ✅ [song-2026 §7.4]: text-only teacher 可作为跨模态 reasoning scaffold，但需要 SFT cold-start 对齐。
- ⚠️ [song-2026 §7.4]: cross-modal OPD 理论基础仍弱，teacher 不看视觉/语音输入时依赖 reasoning structure 可迁移这一假设。

## headline number

无 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv abstract -->
<!-- song-2026: §7.4 Cross-Modal OPD / Table 9 -->
