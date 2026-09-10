---
title: "On the Geometry of On-Policy Distillation"
authors: [Zhennan Shen, et al.]
org: hkust
year: 2026
venue: arxiv
arxiv_id: 2606.07082
url: https://arxiv.org/abs/2606.07082

confidence: 4
verified: a

addresses:
  - no-new-capability
  - capacity-gap

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: none
  extra: none
---

> **一句话**：OPD 参数空间几何解释。

## 核心做法

论文比较 OPD 在参数空间中的位置，使用 update sparsity、principal-angle rotation、spectral drift 和 update-mask overlap 等 diagnostics。它把 OPD 描述成 relaxed off-principal regime，并提出 subspace locking：早期更新进入低维 update band 后具有功能充分性。

$$\Delta\theta_{1:T}\in \mathrm{span}(U_k),\qquad k\ll d$$

实操含义：OPD 的优势可能来自状态分布和更新子空间共同作用，而不是单纯因为 teacher 分布更密集。

## 机制发现（可选）

- [作者 ack paper brief §3.1-3.2]: 论文用 update sparsity、principal-angle rotation、spectral drift 和 update-mask overlap 定位 OPD。
- [作者 ack paper brief §3.3]: relaxed three-gate account 把 signal granularity、model geometry、precision realization 作为 OPD 几何解释。
- [作者 ack paper brief §4-5]: subspace locking 是低维 update band 的早期形成和功能充分性现象，runtime perturbations 仍能保留 lock。

## 谱系位置

- 上游：GKD / DistiLLM (2024) — 定义 OPD 目标但不解释参数几何。
- 同期：Dense Supervision, Sparse Updates (2026) — 都解释 OPD 更新为何不是普通 dense rewrite。
- 同期：Post-Training is About States (2026) — 一个从 parameter geometry 看，一个从 state distribution 看。

## 优缺点

- ✅ [作者 ack paper brief §3-5]: 提供跨 SFT/RLVR/OPD 的几何解释，可服务总结报告里的“为什么 OPD 不只是 dense KD”。
- ⚠️ [作者 ack paper brief Appendix C-G]: 结论依赖具体 training setup、diagnostic implementation 和 rank-constrained controls。

## headline number

未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

<!-- pdf: cached arXiv HTML brief §3 / §4 / §5 / Appendix C-G -->
