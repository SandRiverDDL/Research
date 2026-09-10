---
title: "Less is More: Early Stopping Rollout for On-Policy Distillation"
authors: [Zhou Ziheng, et al.]
org: ucla-biga
year: 2026
venue: arxiv
arxiv_id: 2605.27028
url: https://arxiv.org/abs/2605.27028

confidence: 3
verified: a

addresses:
  - flawed-prefix-trap
  - sgo-generation-cost
  - compounding-error

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: support-truncation
  extra: none
---

> **一句话**：early-stop rollout 的效率路线。

## 核心做法

论文诊断 Off-policy Teacher Decay：后缀 token 的上下文来自 student 早期轨迹，对 teacher 来说逐渐 off-policy，teacher corrective score 会退化成预训练式 token completion。ESR 直接限制 rollout 到前 N 个 response tokens。

$$\mathcal{L}_{\mathrm{ESR}}=\sum_{t\le\tau(x)}D(\pi_T(\cdot|y_{<t})\|\pi_\theta(\cdot|y_{<t}))$$

实操含义：长推理任务里的“多生成一些再蒸馏”未必更好，后缀监督可能同时更贵、更脏。

## 机制发现（可选）

- [作者 ack paper brief Abstract / §2]: Off-policy Teacher Decay 是 ESR 的核心 failure mode，后期 token 的 teacher corrective score 会衰减。
- [作者 ack paper brief §3]: ESR 的干预很简单，只生成并蒸馏前 N 个 response tokens。
- [作者 ack paper brief §5]: 论文用 Cascading Alignment 和 Sub-mode Commitment 解释 ESR 为什么可能超过 full rollout。

## 谱系位置

- 上游：GKD / MiniLLM (2024) — 默认用 student 自生成序列做监督。
- 同期：Are Full Rollouts Necessary (2026) — 都挑战完整 rollout，本篇更强调 early response tokens 的可靠性。
- 同期：When Are Teacher Tokens Reliable (2026) — 都把位置作为 teacher-token reliability 信号。

## 优缺点

- ✅ [作者 ack paper brief Abstract / §4.4]: ESR 同时针对 GPU efficiency、training stability 和 cross-family teacher decay。
- ⚠️ [作者 ack paper brief §7 Limitations]: position-based truncation 是粗控制，未必适合所有需要长程过程监督的任务。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv HTML brief Abstract / §2 / §3 / §4 / §5 / §7 -->
