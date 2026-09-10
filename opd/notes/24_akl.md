---
title: "Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models"
authors: [Taiqiang Wu, et al.]
org: hku-tsinghua-tencent
year: 2024
venue: coling-2025
arxiv_id: 2404.02657
url: https://arxiv.org/abs/2404.02657

confidence: 3
open_source: yes
verified: s

surveys:
  song-2026: "§4.2 adaptive divergence objectives; Table 4"

addresses:
  - mode-collapse-fwdkl
  - void-region-coverage

decisions:
  rollout: offline
  loss: adaptive-kl
  signal: logit
  iteration: one-shot
  filter: none
  extra: none
---

> **一句话**：离线 KD 中自适应混合 FKL/RKL 的背景基线。

## 核心做法

AKL 反驳“RKL 在 LLM KD 中天然 mode-seeking、因此优于 FKL”的简单叙述：足够训练时 FKL/RKL 目标趋同，但早期训练 FKL 更关注 head，RKL 更关注 tail。AKL 根据 teacher/student 在 head/tail 区域的 gap 自适应分配 FKL/RKL 权重。

$$\mathcal{L}_{\mathrm{AKL}}=\lambda_tD_{\mathrm{KL}}(p_T\|p_S)+(1-\lambda_t)D_{\mathrm{KL}}(p_S\|p_T)$$

实操含义：AKL 不是 OPD 方法，但它是 EOPD/TIP/OPD+ 讨论 divergence choice 时的重要背景：divergence 方向的效果依赖训练阶段与 token 分布区域。

## 谱系位置

- 上游：MiniLLM / GKD — 这些方法把 divergence direction 当成 OPD 关键决策。
- 同期：DistiLLM-2 / EOPD — 都从固定 divergence 走向 adaptive divergence。
- 下游：PACED / OPD+ — PACED 用 AKL 作为强 baseline，OPD+ 将 divergence choice 放入更一般的 f-divergence 框架。

## 优缺点

- ✅ [作者 ack Abstract]: 指出 FKL/RKL 在 LLM KD 里不能简单套用 mean-seeking/mode-seeking 直觉。
- ✅ [song-2026 §4.2]: adaptive divergence 方法把 divergence 选择从全局常量变成随 token/statistics 变化的 routing 问题。
- ⚠️ [song-2026 §4.2]: AKL 是 offline KD 背景，不能直接解决 student rollout prefix 上 teacher signal 失真的 OPD 问题。

## headline number

无 Table/Fig anchor 的摘要数字不放入 headline number。

<!-- pdf: arXiv abstract / §4.2 Adaptive Kullback-Leiber Divergence -->
<!-- song-2026: §4.2 Adaptive Divergence Objectives / Table 4 -->
