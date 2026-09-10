---
title: "SOD: Step-wise On-policy Distillation for Small Language Model Agents"
authors: [Qiyong Zhong, et al.]
org: nju
year: 2026
venue: arxiv
arxiv_id: 2605.07725
url: https://arxiv.org/abs/2605.07725

confidence: 3
open_source: yes
verified: a

surveys:
  song-2026: "§6.1 token and sample weighting; Table 9"

addresses:
  - tool-call-cascade
  - flawed-prefix-trap
  - coarse-credit-assignment

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: one-shot
  filter: step-level
  extra: none
---

> **一句话**：tool-integrated reasoning 的 step-level OPD 路线。

## 核心做法

TIR agent 的错误 tool call 会把 corrupted observation 注入后续上下文，使 teacher-student divergence 在 step 边界后阶跃式放大；SOD 不再对所有 token 均匀蒸馏，而是按 accumulated step-level divergence 自适应调弱高 divergence step 的 distillation strength。

$$w_s=f\!\left(\sum_{t\in \mathrm{step}\ s}D(\pi_T(\cdot|h_t)\|\pi_\theta(\cdot|h_t))\right)$$

实操含义：把 granularity 从 token/trajectory 中间插入 step，既能保留 well-aligned step 的 dense guidance，又能避免错误 tool observation 后的 teacher signal 继续污染训练。

## 谱系位置

- 上游：TIP (2026) — token-level weighting 太细，无法识别 tool-call 后的状态突变。
- 同期：SCOPE (2026) — trajectory-level routing 更稳但太粗，可能丢掉部分 trajectory 中仍可靠的 step。
- 下游：GEAR / multi-turn OPD — 进一步把固定 step 粒度推广到 adaptive segment granularity。

## 优缺点

- ✅ [song-2026 §6.1]: step-level granularity 填补 TIP 的 token 级与 SCOPE 的 trajectory 级之间的缺口。
- ✅ [作者 ack Abstract]: 在 math/science/code benchmarks 上最高超过第二强 baseline 20.86%，0.6B student 在 AIME 2025 avg@32 达 26.13%。
- ⚠️ [song-2026 §6.1]: 适用动机强依赖 TIR step 边界；纯文本 reasoning 是否需要 step granularity 仍取决于能否定义稳定边界。

## headline number

无 Table/Fig anchor 的 abstract / survey 数字不放入 headline number。

<!-- pdf: arXiv abstract -->
<!-- song-2026: §6.1 Token and Sample Weighting / Table 9 -->
