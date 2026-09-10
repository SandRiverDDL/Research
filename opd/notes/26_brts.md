---
title: "On-Policy Distillation with Best-of-N Teacher Rollout Selection"
authors: [Ke Zhang, et al.]
org: jhu-tiktok
year: 2026
venue: arxiv
arxiv_id: 2605.09725
url: https://arxiv.org/abs/2605.09725

confidence: 3
verified: a

addresses:
  - teacher-pattern-mismatch
  - flawed-prefix-trap

decisions:
  rollout: mixed
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: verifier-pass
  extra: none
---

> **一句话**：teacher rollout 选择的可靠性路线。

## 核心做法

BRTS 把 teacher rollout 本身也当作需要筛选的对象：先做 correctness- and alignment-aware trajectory curation，再用 teacher-context supervision 补充 standard student-context OPD。它还区分 Top-K direction 中 student-confident 与 teacher-confident 的监督方向。

$$y^{T,*}=\arg\max_{y^T_i}\{\mathrm{correct}(y^T_i),\mathrm{align}(y^T_i,y^S)\}$$

实操含义：teacher 不是生成一次就可信，teacher-context 轨迹本身也需要 selection。

## 机制发现（可选）

- [作者 ack paper brief §3.2]: trajectory curation 同时考虑 correctness 和 student alignment，不默认 teacher rollout 全部可用。
- [作者 ack paper brief §3.3]: teacher-context supervision 是对 student-context OPD 的补充，目标是提供更可靠的 teacher-side states。
- [作者 ack paper brief §3.4]: Top-K direction 区分 student-confident 与 teacher-confident token，避免把所有 teacher 偏好同质化。

## 谱系位置

- 上游：TGPO (2026) — 都关注 teacher 与 student 分布差距下如何提供可执行指导。
- 同期：Trust Region OPD (2026) — 都在选择 teacher signal 的可信区域；BRTS 在 teacher rollout 侧做选择。
- 同期：ReNIO (2026) — BRTS 选择可靠正向 teacher 轨迹，ReNIO 强调错误 student trajectory 的信息量。

## 优缺点

- ✅ [作者 ack paper brief §3]: 把 teacher trajectory selection、teacher-context supervision 和 token direction 组合成一条 teacher-reliability 路线。
- ⚠️ [作者 ack paper brief §4]: Best-of-N 需要额外 teacher sampling，适用性取决于 inference budget 和 selection proxy 质量。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv HTML brief §3 / §4 -->
