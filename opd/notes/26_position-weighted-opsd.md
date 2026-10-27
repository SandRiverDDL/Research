---
title: "When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning"
authors: [Xiaogeng Liu, et al.]
org: jhu-uw-ntu
year: 2026
venue: neurips-2026
arxiv_id: 2605.21606
url: https://arxiv.org/abs/2605.21606

confidence: 3
verified: a

addresses:
  - sampled-token-imbalance
  - flawed-prefix-trap
  - compounding-error

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: support-truncation
  extra: none
---

> **一句话**：teacher-token reliability 的位置加权路线。

## 核心做法

论文问 teacher tokens 何时可靠，并把答案落到 position 和 branch viability 上：同一 rollout 内不同位置的 teacher signal 不应等权处理。PW-OPSD 在 OPSD 框架中加入 position-weight schedule，并提供 branch-viability protocol 与 reliability-weighted surrogate 解释。

$$\mathcal{L}_{\mathrm{PW}}=\sum_t w(t)D(\pi_T(\cdot|y_{<t})\|\pi_\theta(\cdot|y_{<t}))$$

实操含义：teacher token reliability 不只由 entropy 决定，序列位置和 branch viability 也可能更关键。

## 机制发现（可选）

- [作者 ack paper brief §3.2]: branch-viability protocol 用于检验 token-position 是否预测 teacher reliability。
- [作者 ack paper brief §3.3]: reliability-weighted distillation 给 position weighting 提供理论解释。
- [作者 ack paper brief §3.4]: PW-OPSD 是在 OPSD 上加入 position-weighted auxiliary signal。

## 谱系位置

- 上游：OPSD (2026) — 在 self-distillation rollout 上加位置可靠性权重。
- 同期：Revisiting OPD (2026) — 都诊断 sampled-token OPD 脆弱性。
- 同期：Less is More / Prefix Teach Suffix Fade (2026) — 都把位置和后缀可靠性作为核心变量。

## 优缺点

- ✅ [作者 ack paper brief §3]: 把 teacher-token reliability 从 entropy-only 推向 position / branch-viability diagnostic。
- ⚠️ [作者 ack paper brief §5]: 作者把未来工作指向更 adaptive 的 schedule，说明固定位置权重不是最终形态。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv HTML brief §3 / §4 / §5 / Appendix A-G -->

<!-- venue verified 2026-10-04: https://neurips.cc/Downloads/2026 ; official entry: https://neurips.cc/virtual/2026/poster/148618 -->
