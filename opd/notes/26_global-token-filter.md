---
title: "Filter, Then Reweight: Rethinking Optimization Granularity in On-Policy Distillation"
authors: [Yuying Li, Leqi Zheng, Yongzi Yu, Wenrui Zhou, Xuchang Zhong, Xing Hu, Jing Jin, Huangjie Yuan, Tao Feng]
org: tsinghua
year: 2026
venue: arxiv
arxiv_id: 2606.02684
url: https://arxiv.org/abs/2606.02684
zotero_key:

confidence: 3
open_source: partial
verified: a

addresses:
  - flawed-prefix-trap
  - coarse-credit-assignment

decisions:
  rollout: student
  loss: adaptive-kl
  signal: logit
  iteration: one-shot
  filter: trajectory-level
  extra: none
---

> **一句话**：trajectory 过滤与 token 软加权的双粒度路线。

## 核心做法
标准 OPD 对所有 trajectory 和 token 施加均匀 KL 监督，FiRe-OPD 在两个粒度上做选择性优化：
1. **Trajectory 过滤**：计算 teacher 在 student 生成轨迹上的平均 log-prob `s(y)`，丢弃 batch 内底部 20% 的 rollout（teacher 与 student 分布差距太大时监督不可靠）。
2. **Token 软加权**：对保留轨迹，令 `w_t = (1 + α·c_t^T)(1 + β·c_t^S)`，其中 `c_t^T` 为 teacher 置信度（1 - 归一化熵），`c_t^S` 为 student 困惑度（归一化熵），乘积后 trajectory 内归一化再乘回 advantage。
关键发现：trajectory 级**硬过滤**优于软加权；token 级**软加权**优于硬截断。

## 谱系位置
相比 EOPD/TIP/REOPOLD 只做 token 级、ExOPD 只做 trajectory 级（且不用 teacher 置信度），FiRe-OPD 是首个**同时在两个粒度**联合建模的方法，且 token 级用乘积软权重取代了 TIP 的硬截断，避免了信息丢失和梯度不稳定。


## Method
- **Trajectory 得分**：`s(y) = (1/T) Σ log π*(y_t|x,y_{<t})`，过滤 batch 内底部 `p=20%`
- **Teacher 置信度**：`c_t^T = 1 - H(π*_t) / max_batch H(π*)`
- **Student 困惑度**：`c_t^S = H(π_θ_t) / max_batch H(π_θ)`
- **Token 权重**：`w_t = (1 + α·c_t^T)(1 + β·c_t^S)`，α=β=1.0，trajectory 内均值归一化
- **损失**：标准 PPO-clip 但 advantage 替换为 `ã_t = (w_t / mean_w) · a_t`

## 优缺点

- ✅ [作者 ack §3.2]: trajectory 级硬过滤与 token 级软加权分工明确，避免把两种粒度混成同一个 selection rule。
- ⚠️ [作者 ack §3.2]: 依赖 teacher log-prob 评估 rollout 质量，teacher-student 差距大时过滤阈值可能带来选择偏差。

## headline number

- AIME2024 +6.25 vs standard OPD in Qwen3-30B→4B strong-to-weak setting（§3.1 Table 2）
- Multi-teacher Miner +18.81 vs standard OPD（§3.2 Table 4）

## Evidence
- "+6.25 on AIME 2024 in strong-to-weak" 来自 §3.1 Table 2 Δ vs OPD 行
- "+18.81 on Miner in multi-teacher" 来自 §3.2（含 Table 4）Δ vs OPD 行
- "p=20%, α=β=1.0" 来自 §3.2 Method 正文（Eq. 4-9）

<!-- pdf: §3 Method / §3.1-3.2 Experiments -->
