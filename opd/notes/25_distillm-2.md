---
title: "DistiLLM-2: A Contrastive Approach to On-Policy Distillation"
authors: [Jongwoo Ko, et al.]
org: kaist-microsoft
year: 2025
venue: arxiv
arxiv_id: 2503.07067
url: https://arxiv.org/abs/2503.07067

confidence: 3
open_source: yes
verified: a

surveys:
  song-2026: "§4.1 Fixed divergence objectives; Table 3"

addresses:
  - kld-gradient-explosion
  - source-divergence-mismatch

decisions:
  rollout: mixed
  loss: skl
  signal: logit
  iteration: iterative
  filter: curriculum
  extra: none
---

> **一句话**：DistiLLM 后续的 objective 分流代表作。

## 核心做法

针对 teacher-generated 与 student-generated 样本信号不同的问题，把 DistiLLM 的 stabilized divergence 拆成两支：teacher response 上用 SKL 拉近 teacher distribution，student response 上用 SRKL 压低 student 低质区域。

$$\mathcal{L}_{\mathrm{CALD}}=\tfrac12\left(D_{\mathrm{SKL}}^{(\alpha)}(x,y_t)+D_{\mathrm{SRKL}}^{(\alpha)}(x,y_s)\right)$$

实操含义是 divergence 不再全局固定，而是按数据来源分配；再用 α curriculum 从较强 smoothing 逐步衰减，提高后期对比信号。

## 谱系位置

- 上游：GKD (2024) — 给出 mixture-policy OPD 框架，DistiLLM-2 继续沿 token-level white-box objective 走
- 上游：DistiLLM (2024) — 继承 SKL/SRKL 稳定化，但从单一 loss 改成按数据来源分流
- 同期：AlignDistil (2025) — 同样追求 token 级监督，但 AlignDistil 从 preference/DPO reward 推 teacher distribution
- 下游：ToDi / AKL / EOPD (2026) — survey 称后续 adaptive methods 进一步从 sequence source 粒度推进到 per-token geometry

## 优缺点

- ✅ [作者 ack §3.1.2]：teacher response 用 mode-covering、student response 用 mode-seeking，显式利用数据来源与 divergence 的协同
- ✅ [song-2026 §4.1]：survey 将其列为 fixed-divergence 家族中 asymmetric loss per data source 的代表
- ⚠️ [song-2026 §4.1]：source-level 分流仍是粗粒度，同一 sequence 内不同 token 的分布几何仍可能需要不同 divergence

## headline number

- Evol-Instruct win rate 79.83% → 84.67% on Mistral student（§3.2 Table 1）

<!-- pdf: §3.1 Contrastive Approach / §3.2 Data Curation / §3.3 Curriculum-based Adaptive Learning -->
<!-- song-2026: §4.1 Fixed Divergence Objectives / Table 3 -->
