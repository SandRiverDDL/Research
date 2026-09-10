---
title: "Scaling Reasoning Efficiently via Relaxed On-Policy Distillation"
authors: [Jongwoo Ko, et al.]
org: kaist-microsoft
year: 2026
venue: icml-2026
arxiv_id: 2603.11137
url: https://arxiv.org/abs/2603.11137

confidence: 2
verified: r

surveys:
  song-2026: "§4.3 RL-augmented objectives; Table 5; §7 operational guidelines"

addresses:
  - policy-gradient-variance
  - entropy-collapse
  - capacity-gap

decisions:
  rollout: student
  loss: advantage
  signal: logit
  iteration: iterative
  filter: score-threshold
  extra: none
---

> **一句话**：DistiLLM 系列的 RL 化延伸。

## 核心做法

把 OPD 的 teacher-student log-likelihood ratio 解释成 fixed token reward，用 stop-gradient 得到 policy optimization 视角；再用 reward clipping、entropy token sampling 和 exploration-to-refinement schedule 稳定训练。

$$\hat{R}_{i,t}=\max(\mathrm{sg}[\log\pi_T(o_{i,t})-\log\pi_\theta(o_{i,t})],\log\lambda/(1-\lambda))$$

实操含义是不过度相信极端 teacher signal，只在高不确定 token 或 reward-threshold token 上更新，减少 negative transfer 和 premature entropy collapse。

## 谱系位置

- 上游：DistiLLM (2024) — 同作者线从 stabilized KL 出发，REOPOLD 转为 log-ratio reward / policy optimization
- 上游：DistiLLM-2 (2025) — DistiLLM-2 按数据源分流，REOPOLD 进一步诊断 reward 分布病因
- 同期：G-OPD (2026) — survey 将二者都放进 OPD ↔ KL-constrained RL 的统一视角
- 下游：RLKD / CoDistill-GRPO (2026) — survey 把 REOPOLD 作为 dense token reward 到结构化 reward / co-distillation 的中间点

## 优缺点

- ✅ [作者 ack §3.1]：stop-gradient 使 OPD 可按 policy gradient 诊断，梯度范数更稳定
- ✅ [song-2026 §4.3]：把 teacher-student log-ratio 作为 token reward，连接 KD dense gradient 与 RL exploration
- ⚠️ [song-2026 §4.3]：仍保留 token-level KL/logit signal，若 teacher expertise 更像 step structure，RLKD 这类结构奖励可能更合适

## headline number

- 6.7–12x sample efficiency over recent RL approaches（§5.1 Figure 1a）
- 7B student matches 32B teacher in visual reasoning with ~3.3x inference speedup（§5.2 Table 5）

<!-- pdf: §3.1 Policy Optimization View / §4 REOPOLD / §5.1-5.2 Results -->
<!-- song-2026: §4.3 RL-Augmented Objectives / §7 Operational Guidelines -->
