---
title: "Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe"
authors: [Yaxuan Li, et al.]
org: thunlp
year: 2026
venue: arxiv
arxiv_id: 2604.13016
url: https://arxiv.org/abs/2604.13016

confidence: 3
open_source: yes
verified: a

addresses:
  - teacher-pattern-mismatch
  - no-new-capability
  - flawed-prefix-trap

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: hardness
  extra: none
---

> **一句话**：OPD 成败条件与 token-overlap 机制分析。

## 核心做法

论文不是提出一个新 loss，而是把 OPD 是否成功拆成两个条件：teacher/student 要有 compatible thinking patterns；即使 pattern 一致，teacher 也必须提供 student 训练中没有见过的新能力。若条件不满足，推荐用 off-policy teacher rollout cold start 和 teacher-aligned prompt selection 先把 student 拉到可蒸馏区域。

$$\text{success}\approx \text{pattern compatibility}\ \land\ \text{new capability from teacher}$$

实操含义：OPD 不是“teacher 分数更高就能蒸”，必须先检查 teacher 在 student-visited states 上是否给出可利用的局部方向。

## 机制发现（可选）

- [作者 ack Abstract / §3]: 两个成败条件是 thinking-pattern consistency 与 teacher new capability；same-family 1.5B/7B teachers 从 student 视角可能分布不可区分。
- [作者 ack §4]: 成功 OPD 表现为 student-visited states 上 high-probability shared tokens 的 progressive alignment，少量 shared token set 承载 97%-99% probability mass。
- [作者 ack §6.1]: reward quality 随 trajectory depth 退化，instability 主要来自 later tokens，长程蒸馏的 dense reward 并非免费午餐。

## 谱系位置

- 上游：GKD / MiniLLM (2024) — 继承 student rollout + token-level teacher feedback 的基本 OPD 设置。
- 同期：Revisiting OPD (2026) — Revisiting 从 sampled-token estimator 与 special-token mismatch 解释不稳；本文从 teacher-student pattern/capability compatibility 解释成败。
- 同期：Trust Region OPD / TGPO (2026) — 都关注 teacher signal 在 student state 上是否可靠，本文给出更宏观的 teacher/prompt 选择准则。
- 下游：OPD recipe / verl 实现 — off-policy cold start 与 teacher-aligned prompt selection 可作为跑 OPD 前的 hygiene。

## 优缺点

- ✅ [作者 ack §3-5]: 把“teacher 更强但 OPD 仍失败”转化为可诊断条件，而不是继续调 loss。
- ✅ [作者 ack §4]: token-overlap mass 解释为什么 shared high-probability tokens 足以驱动有效 OPD。
- ⚠️ [作者 ack §6]: 长 trajectory 后段 teacher continuation 质量下降，OPD 的 dense reward 在 long-horizon 上仍有结构性成本。

## headline number

无 Table/Fig anchor 的机制性数字不放入 headline number；97%-99% overlap mass 仅作为机制证据保留。

<!-- pdf: arXiv HTML v2 Abstract / §3 / §4 / §5 / §6 -->
