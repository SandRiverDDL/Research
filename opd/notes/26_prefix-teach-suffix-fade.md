---
title: "Prefix Teach, Suffix Fade: Local Teachability Collapse in Strong-to-Weak On-Policy Distillation"
authors: [Kaiyuan Liu, et al.]
org: zju-meituan
year: 2026
venue: arxiv
arxiv_id: 2605.13643
url: https://arxiv.org/abs/2605.13643

confidence: 4
verified: a

addresses:
  - flawed-prefix-trap
  - teacher-pattern-mismatch
  - compounding-error

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: support-truncation
  extra: none
---

> **一句话**：strong-to-weak teachability collapse 诊断。

## 核心做法

论文研究 strong-to-weak OPD 的 local teachability：teacher supervision 可能在 prefix 有用，但随着 student trajectory 偏离，suffix positions 上 teacher token 逐渐不再可教。它把这一现象诊断为 local teachability collapse，并引入 trajectory-specific release rule。

$$r_t=\mathrm{Reliability}(\pi_T(\cdot|y^S_{<t}),\pi_\theta(\cdot|y^S_{<t}))$$

实操含义：strong teacher 并不自动意味着全序列都可教，后缀位置可能是最不可靠的监督源。

## 机制发现（可选）

- [作者 ack paper brief §3]: local teachability analysis 把 strong-to-weak gap 落到 token position / trajectory state 层面。
- [作者 ack paper brief §3]: trajectory-specific release rule 表明不是所有 suffix token 都应继续被 teacher 约束。
- [作者 ack paper brief Abstract / §3]: prefix teach、suffix fade 是 full-rollout OPD 的直接风险。

## 谱系位置

- 上游：TGPO / TAID (2025-2026) — 都处理 teacher-student 差距。
- 同期：Less is More (2026) — ESR 是应对后缀失真的训练策略，本篇偏机制诊断。
- 同期：When Are Teacher Tokens Reliable (2026) — 都把 position 作为 reliability 关键变量。

## 优缺点

- ✅ [作者 ack paper brief §3]: 把 capacity gap / teacher-student gap 细化为局部、位置相关的 teachability。
- ⚠️ [作者 ack paper brief §4-5]: release rule 是否泛化到不同任务和 teacher/student size，需要依赖实验部分判断。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv HTML brief Abstract / §3 / §4 / §5 -->
