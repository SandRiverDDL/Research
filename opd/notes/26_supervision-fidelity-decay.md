---
title: "Your Teacher Can't Help You Here: Combating Supervision Fidelity Decay in On-Policy Distillation"
authors: [Yanjiang Liu, et al.]
org: cas-xiaohongshu
year: 2026
venue: arxiv
arxiv_id: 2605.30833
url: https://arxiv.org/abs/2605.30833

confidence: 4
verified: a

addresses:
  - flawed-prefix-trap
  - compounding-error
  - teacher-pattern-mismatch

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: iterative
  filter: trajectory-level
  extra: none
---

> **一句话**：supervision fidelity decay 诊断。

## 核心做法

论文提出 Supervision Fidelity Decay：随着 student-generated prefixes 变长，teacher next-token distribution 变得 less confident / less discriminative，reverse-KL corrective signal 弱化，student drift 在长推理链上复合。LGR 用 one-step lookahead teacher confidence 作为 supervision signal。

$$\mathrm{Fidelity}(t)=\mathrm{sim}(\pi_T(\cdot|y^S_{<t}),\pi_T(\cdot|y^T_{<t}))$$

实操含义：teacher 的强能力不保证它能修复任意 student prefix；越长的错误上下文越可能让 teacher signal 变成噪声。

## 机制发现（可选）

- [作者 ack paper brief Abstract / §2.2]: SFD 被形式化为 supervision capability functional 随 student trajectory 下降。
- [作者 ack paper brief §2.3-2.4]: 论文从 signal collapse、compounding drift 和 supervision boundary contraction 解释恶性循环。
- [作者 ack paper brief §3.1-3.3]: Lookahead Group Reward 评估 student top-K candidate tokens 在下一步诱导的 teacher confidence，并给出 group-normalized reward。

## 谱系位置

- 上游：Revisiting OPD (2026) — flawed-prefix trap 的更一般长程版本。
- 同期：Prefix Teach Suffix Fade (2026) — 都描述 teacher signal 在 suffix / long-prefix 上衰减。
- 同期：Trust Region OPD / KL Agreement Trap (2026) — 都要求显式判断 teacher signal 的可信区间。

## 优缺点

- ✅ [作者 ack paper brief §2-3]: 同时给出 SFD 机制诊断和 LGR 干预，信息量高于只做 rollout truncation。
- ⚠️ [作者 ack paper brief Appendix E]: tree attention / segmentation 等高效计算设计说明 LGR 有额外系统复杂度。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv HTML brief Abstract / §2 / §3 / §4 / Appendix E-F -->
