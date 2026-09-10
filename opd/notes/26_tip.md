---
title: "TIP: Token Importance in On-Policy Distillation"
authors: [Yuanda Xu, et al.]
org: princeton
year: 2026
venue: arxiv
arxiv_id: 2604.14084
url: https://arxiv.org/abs/2604.14084

confidence: 3
open_source: yes
verified: a

surveys:
  song-2026: "§6 training efficiency and stabilization; §6.1 token and sample weighting; Table 9"

addresses:
  - flawed-prefix-trap
  - coarse-credit-assignment

decisions:
  rollout: student
  loss: forward-kl
  signal: logit
  iteration: one-shot
  filter: score-threshold
  extra: none
---

> **一句话**：token weighting 分支代表作。

## 核心做法

TIP 把 OPD token 重要性拆成 student entropy 与 teacher-student divergence 两轴：高熵 token 提供不确定性信号，低熵高 divergence token 是 overconfident error，低熵低 divergence token 基本已学会。

$$s_t=\hat h_t+\hat\delta_t-\hat h_t\hat\delta_t$$

Soft-OR 分数无额外权重超参，top-k 选择后只在重要 token 上算 forward KL，从而同时保留 Q1/Q2 的 uncertain signal 与 Q3 的 overconfident-wrong signal。

## 谱系位置

- 上游：GKD / MiniLLM (2024) — 它们均匀使用所有 token 的 OPD signal
- 同期：EOPD (2026) — EOPD 用 teacher entropy 单轴 routing，TIP 指出 entropy-only 会漏掉 Q3 overconfident errors
- 同期：SCOPE / SelecTKD / AdaSwitch (2026) — survey 将 TIP 放在 fine-grained token weighting 端
- 下游：EGRSD (2026) — 将 entropy-guided gating 推到 self-distillation setting，并补充动态 entropy 演化视角

## 优缺点

- ✅ [song-2026 §6.1]：Q3 token 对 entropy-only weighting 结构性不可见，TIP 用 divergence 轴恢复覆盖
- ✅ [作者 ack §6]：Soft-OR 是 parameter-free 的 token selection rule，降低 selection hyperparameter 负担
- ⚠️ [song-2026 §6.1]：fine-grained token methods 依赖可靠 token-level teacher signals，在 flawed prefix 严重时信号本身会退化

## headline number

- 50% token selection matches full-token baseline with 47% lower peak memory（§1 / §7.4 Table 5）
- Q3-only <20% tokens outperforms full-token OPD on DeepPlanning Avg@16 12.6 vs 11.7（§7.5 Table 7）

<!-- pdf: §4 Token types / §6 Type-Aware Token Selection / §7 Experiments -->
<!-- song-2026: §6.1 Token and Sample Weighting / Table 9 -->
