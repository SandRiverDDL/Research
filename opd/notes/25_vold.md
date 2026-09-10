---
title: "VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation"
authors: [Walid Bousselham, et al.]
org: inria
year: 2025
venue: arxiv
arxiv_id: 2510.23497
url: https://arxiv.org/abs/2510.23497

confidence: 3
verified: a

surveys:
  song-2026: "§7.4 multimodal / cross-modal OPD"

addresses:
  - teacher-pattern-mismatch
  - exposure-bias
  - capacity-gap

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: none
  extra: privileged-info
---

> **一句话**：text-only teacher 指导 VLM reasoning 的 cross-modal OPD。

## 核心做法

VOLD 将 GRPO 与 OPD 结合：VLM student 在视觉推理任务上产生 on-policy reasoning traces，text-only teacher 不看图像但提供 reasoning-structure supervision，引导 student 的推理轨迹。论文强调 SFT cold-start 对 cross-modal distribution alignment 必要，否则 student rollout 离 text teacher 支持集太远，OPD 不收敛。

$$y\sim\pi_{\theta}^{\mathrm{vlm}}(\cdot|x_{\mathrm{image}}),\quad \pi_T^{\mathrm{text}}(\cdot|y_{<t})\rightarrow \text{reasoning feedback}$$

实操含义：跨模态 OPD 的关键前提是先把 student 拉到 teacher 可评价的分布附近。

## 谱系位置

- 上游：OPD / GRPO — VOLD 把 dense teacher feedback 加到 VLM on-policy RL 上。
- 同期：X-OPD (2026) — 从 VLM reasoning 扩展到 speech LLM capability alignment。
- 下游：cross-modal OPD — 证明 text reasoning scaffold 可跨 modality 迁移，但仍依赖 cold-start alignment。

## 优缺点

- ✅ [song-2026 §7.4]: 说明 text-only teacher 可以指导 VLM student，而 teacher 不必直接观察视觉输入。
- ✅ [作者 ack Abstract]: VOLD 在 MMMU-Pro、MathVision、MathVista、LogicVista 等 benchmark 上显著优于 baseline。
- ⚠️ [song-2026 §7.4]: 没有 cold-start alignment 时 teacher/student 分布距离过大，on-policy distillation 不能提供有效 guidance。

## headline number

无 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv abstract -->
<!-- song-2026: §7.4 Cross-Modal OPD -->
