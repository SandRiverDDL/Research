---
title: "The Many Faces of On-Policy Distillation: Pitfalls, Mechanisms, and Fixes"
authors: [Siqi Zhu, et al.]
org: uiuc-ruc-pku
year: 2026
venue: neurips-2026
arxiv_id: 2605.11182
url: https://arxiv.org/abs/2605.11182

confidence: 3
verified: a

addresses:
  - large-policy-divergence
  - privileged-context-gap
  - flawed-prefix-trap

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: support-truncation
  extra: privileged-info
---

> **一句话**：OPD/OPSD 适用边界的系统经验研究。

## 核心做法

论文系统比较 OPD 与 OPSD 什么时候有效、什么时候失败：数学 reasoning 上 OPD 对 teacher choice 与 loss formulation 高度敏感；OPSD 在 instance-specific privileged information 上失败，但当 PI 是 shared latent rule（system prompt、alignment preference）时有效。修复策略包括 stop-gradient TopK objectives、RLVR-adapted teachers 和 SFT-stabilized students。

$$\text{OPSD works better when PI is shared-rule-like, not instance-specific.}$$

实操含义：privileged-info OPD 不能只问“teacher 是否更强”，还要问 PI 在推理期是否可由参数化策略稳定内化。

## 机制发现（可选）

- [作者 ack Abstract]: OPD on math reasoning 对 teacher choice 和 loss formulation 敏感。
- [作者 ack Abstract]: OPSD 在 instance-specific PI 下失败，因为 student 最终学到的是 PI-free policy 对多个 PI-conditioned teachers 的聚合。
- [作者 ack Abstract]: 三个机制是 student-generated prefix 引起的 distribution mismatch、biased TopK reverse-KL gradient instability、以及 instance-specific PI 的推理期缺失。

## 谱系位置

- 上游：OPCD / OPSD / SDR (2026) — 这些方法展示 context/PI internalization 可行；Many Faces 给出何时失败的边界。
- 同期：Revisiting OPD (2026) — 两者都诊断 OPD instability；Many Faces 同时覆盖 OPSD 与 privileged information。
- 下游：privileged OPD variants — 需要把 PI 类型分成 shared latent rule vs instance-specific privilege，而不是统一当作 teacher context。

## 优缺点

- ✅ [作者 ack Abstract]: 给出 OPD 与 OPSD 的条件化结论，能直接指导候选方法是否可靠。
- ✅ [作者 ack Abstract]: 明确 shared latent rule 与 instance-specific PI 的差异，是 privileged-context-gap 的关键边界。
- ⚠️ [作者 ack Abstract]: 结论是 empirical study，仍需按任务/teacher/loss 复核，不能替代具体方法的复现实验。

## headline number

无稳定 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv Abstract / §1 / PDF snippet -->

<!-- venue verified 2026-10-04: https://neurips.cc/Downloads/2026 ; official entry: https://neurips.cc/virtual/2026/poster/153073 -->
