---
title: "Segment-Level On-Policy Distillation for Long-Horizon Agents"
authors: [Anonymous]
org: other
year: 2026
venue: acl-arr-2026-may
arxiv_id: openreview-KONaKYIBWv
url: https://openreview.net/attachment?id=KONaKYIBWv&name=pdf

confidence: 4
verified: a

addresses:
  - tool-call-cascade
  - coarse-credit-assignment
  - compounding-error

decisions:
  rollout: student
  loss: advantage
  signal: verifier
  iteration: iterative
  filter: step-level
  extra: none
---

> **一句话**：long-horizon agent 的 segment 粒度路线。

## 核心做法

OpenReview PDF 中的方法名显示为 CHOP，核心问题是 token-level supervision 与 sequence-level return misalignment。它先定义 alignment coefficient 诊断 teacher local token reward 是否与最终成功一致，再用在线 proxies 做 routing，而不是对整条 long-horizon agent trajectory 使用同质监督。

$$\mathcal{L}=\sum_{k}A_kD(\pi_T(\cdot|s_{k})\|\pi_\theta(\cdot|s_{k}))$$

实操含义：长程任务的 OPD 应该按 route segment 定位错误，否则 early action、tool call 和后续 observation 会混成一个粗信号。

## 机制发现（可选）

- [作者 ack paper brief §3]: 标准 OPD 在 teacher local token reward 与 sequence-level return 不一致时失败。
- [作者 ack paper brief §3.1]: alignment coefficient 用来度量 local supervision 与 trajectory success 的一致性。
- [作者 ack paper brief §3]: CHOP 使用 online proxies 做 routing，服务于长程 agent / segment 条件监督。

## 谱系位置

- 上游：SOD (2026) — step-wise supervision 处理 agent token/tool granularity。
- 同期：GEAR / long-horizon OPD 分支 — 都从 response-level 转向局部 credit。
- 同期：Trajectory-Refined Distillation (2026) — 一个聚焦 trajectory correction，一个聚焦 agent segment credit。

## 优缺点

- ✅ [作者 ack paper brief §3]: 把 long-horizon agent failure 具体化为 local token reward 与 sequence return 的 misalignment。
- ⚠️ [作者 ack paper brief §3-4]: 标题/队列名与 PDF 中 CHOP 命名存在差异，后续引用前应核对 OpenReview 元数据和最终标题。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached OpenReview PDF brief §3 / §4 -->
