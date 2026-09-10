---
title: "Trajectory-Refined Distillation"
authors: [Li Jiang, et al.]
org: mcgill-ut-austin
year: 2026
venue: arxiv
arxiv_id: 2606.08432
url: https://arxiv.org/abs/2606.08432

confidence: 4
verified: a

addresses:
  - flawed-prefix-trap
  - compounding-error
  - coarse-credit-assignment

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: iterative
  filter: trajectory-level
  extra: none
---

> **一句话**：trajectory correction 的路线代表。

## 核心做法

TRD 把 prefix failure 定义为 token-level OPD 的 common failure mode：错误 prefix 会诱导 teacher mixture / fragmented gradients，即使局部 token 被修正，也未必回到正确 trajectory。TRD 先构造 refined trajectory，再蒸馏修正后的路径。

$$\tilde y=\mathrm{Refine}(y^S;\pi_T),\qquad \mathcal{L}=D(\pi_{\tilde y}\|\pi_\theta)$$

实操含义：当错误来自整条 reasoning path，局部 token 加权不如先修正轨迹再蒸馏。

## 机制发现（可选）

- [作者 ack paper brief §4.1-4.3]: prefix failure 被拆成 mixture of distribution、perfect teacher 是否能 recover correction path、empirical validation 三个诊断。
- [作者 ack paper brief §5]: Trajectory-Refined Distillation 从 token-level interventions 转向 trajectory-level refinement。
- [作者 ack paper brief Appendix B]: refinement 会 compress trajectory、raise verifier accuracy，并呈现 monotonically corrective 趋势。

## 谱系位置

- 上游：Revisiting OPD / TIP (2026) — 关注局部 token 支持和重要性。
- 同期：Near-Future Guidance (2026) — 都从 trajectory consequence 判断监督价值。
- 同期：Segment-Level OPD (2026) — 都提升监督粒度，只是 TRD 面向 reasoning trajectory，Segment-Level 面向 agent route。

## 优缺点

- ✅ [作者 ack paper brief §4-5]: 将 OPD 失败从局部 token loss 解释提升到 trajectory path 修正。
- ⚠️ [作者 ack paper brief Appendix B.3]: TRD 对 filtering / trajectory subset 敏感，不能简单等同于“筛掉坏轨迹”。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv HTML brief §4 / §5 / §6 / Appendix A-B -->
