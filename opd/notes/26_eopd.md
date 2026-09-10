---
title: "Entropy-Aware On-Policy Distillation of Language Models"
authors: [Woogyeol Jin, et al.]
org: ibm
year: 2026
venue: icml-2026
arxiv_id: 2603.07079
url: https://arxiv.org/abs/2603.07079

confidence: 3
open_source: yes
verified: r

surveys:
  song-2026: "§4.2 adaptive divergence objectives; Table 4"

addresses:
  - mode-collapse-fwdkl
  - void-region-coverage

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: one-shot
  filter: score-threshold
  extra: none
---

> **一句话**：entropy-gated adaptive divergence 代表作。

## 核心做法

标准 OPD 的 reverse KL 在低熵 token 上精确，但在高熵 teacher distribution 上会丢多样性；EOPD 以 teacher entropy 为 gate，在高熵 token 额外加入 forward KL。

$$\mathcal{L}_{\mathrm{EA}}=\mathbb{E}_{y\sim p_\theta}\left[\sum_t D_{\mathrm{KL}}(p_\theta\|p_T)+\mathbb{I}[H_t>\tau_H]D_{\mathrm{KL}}(p_T\|p_\theta)\right]$$

实操含义是默认保留 OPD 的 mode-seeking 效率，只在 teacher 明显不确定的位置补 mode-covering 信号。

## 谱系位置

- 上游：MiniLLM / OPD (2024) — 继承 student rollout + reverse-KL / clipped-RKL 主线
- 上游：DistiLLM-2 (2025) — DistiLLM-2 按数据源分流，EOPD 推进到按 token entropy 分流
- 同期：ToDi (2025) — ToDi 用 teacher-student log-ratio 做细粒度 routing，EOPD 只看 teacher uncertainty
- 下游：AKL / AOPD (2026) — survey 将其放在“which divergence where”的 adaptive objective 转向中

## 优缺点

- ✅ [作者 ack §4]：在 high-entropy token 激活 forward KL，保留多种合理 continuation 的概率质量
- ✅ [song-2026 §4.2]：teacher entropy 是稳定 routing 信号，尤其适合 student distribution 尚不可靠的早期训练
- ⚠️ [song-2026 §4.2]：仍然优化到 teacher distribution；若 teacher 自身缺 reasoning path，adaptive divergence 只能匹配 teacher，难以超越 teacher

## headline number

- Pass@8 +1.37 / +2.39 / +5.05 on Qwen3-0.6B/1.7B/4B across six math benchmarks（§5 Table 2）

<!-- pdf: §3.1 Diversity degradation / §4 Entropy-Aware OPD / §5 Experiments -->
<!-- song-2026: §4.2 Adaptive Divergence Objectives / Table 4 -->
