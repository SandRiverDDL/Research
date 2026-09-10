---
title: "DistiLLM: Towards Streamlined Distillation for Large Language Models"
authors: [Jongwoo Ko, et al.]
org: kaist
year: 2024
venue: icml-2024
arxiv_id: 2402.03898
url: https://arxiv.org/abs/2402.03898

confidence: 3
open_source: yes
verified: s

surveys:
  song-2026: "§2.3 comparative synthesis (GKD/MiniLLM/DistiLLM tradeoff triangle); §4.1 Fixed-Divergence Objectives Table 3, Eq.10"

addresses:
  - exposure-bias
  - kld-gradient-explosion
  - sgo-generation-cost

decisions:
  rollout: mixed
  loss: skl
  signal: logit
  iteration: iterative
  filter: none
  extra: none
---

> **一句话**：OPD fixed-divergence 路线三篇开山之一（KAIST + MSR, ICML 2024），与 GKD / MiniLLM 并列。

## 核心做法

标准 KLD 在 q_θ→0 时梯度系数 r_{p,q_θ} 无界（梯度爆炸）；连续 on-policy SGO 生成占训练时间高达 80%（§2.2）。SKL 以混合分布替换分母使梯度有界，adaptive replay buffer 缓存旧 SGO 降低实时生成频率。

$$D_{\text{SKL}}^{(\alpha)}(p, q_\theta) = D_{\text{KL}}\!\left(p,\; \alpha p + (1-\alpha)q_\theta\right)$$
$$D_{\text{SRKL}}^{(\alpha)}(p, q_\theta) = D_{\text{KL}}\!\left(q_\theta,\; (1-\alpha)p + \alpha q_\theta\right)$$

α=0 退回标准 KLD；α=0.1（§3.1 理论与实验推荐）使分母下界 ≥ 0.1·p，梯度系数压为 (1−α)·r_{p,q̃}，无需 RL policy gradient。

## 谱系位置

- 上游：GKD (Agarwal 2024) — 共享 SGO 框架；DistiLLM 将 divergence 从 JSD 换为 skew-KL，将连续 on-policy 换为 adaptive off-policy
- 同期：MiniLLM (Gu 2024) — 同样 on-policy 但选 reverse-KL + REINFORCE policy gradient
- 下游：DistiLLM-2 (Ko 2025) — 对 teacher-generated / student-generated 数据分别用 forward/reverse SRKL（asymmetric loss per source）

## 优缺点

- ✅ [song-2026 §4.1]: skew 操作把梯度系数从无界 r_{p,q_θ} 压为 (1−α)·r_{p,q̃}，避免 q_θ≈0 时梯度爆炸，无需 RL policy gradient
- ✅ [song-2026 §2.3]: 相比 GKD 无需手选 divergence；相比 MiniLLM 无 REINFORCE 高方差
- ⚠️ [作者 ack §Limitation]: SFT-only 设计，未扩展至 preference optimization（DPO/RLHF），作者标注为 future work
- ⚠️ [song-2026 §2.3]: replay buffer + adaptive scheduler 引入额外超参复杂度

## headline number

- SRKL ROUGE-L 25.21 vs JSD 24.34 on Dolly Eval, GPT-2 XL→GPT-2（§Table 1）
- 2.5–4.3× training speedup vs MiniLLM / GKD（§Fig 2 / Abstract）

<!-- pdf: §Abstract / §2.2 Pitfalls / §3.1 Skew KLD / §6 Related Work / §7 Conclusion -->
<!-- song-2026: §2.3 comparative synthesis / §4.1 Fixed-Divergence Objectives -->
