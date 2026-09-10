---
title: "OPRD: On-Policy Representation Distillation"
authors: [Shenzhi Yang, Guangcheng Zhu, Bowen Song, Haobo Wang, Mingxuan Xia, Xing Zheng, Yingfan Ma, Zhongqi Chen, Weiqiang Wang, Gang Chen]
org: zju
year: 2026
venue: arxiv
arxiv_id: 2606.06021
url: https://arxiv.org/abs/2606.06021
zotero_key:

confidence: 3
open_source: partial
verified: a

addresses:
  - policy-gradient-variance
  - coarse-credit-assignment

decisions:
  rollout: student
  loss: mse
  signal: representation
  iteration: one-shot
  filter: none
  extra: privileged-info
---

> **一句话**：OPD 监督信号从输出空间转向表示空间。

## 核心做法
所有现有 on-policy distillation 变体（sampled-token、full-vocab、top-k）都在 **output space** 对 KL 做估计，受两个结构性限制：(1) token-level REINFORCE 估计器的方差在 p→q 时不消失，导致 late-stage 训练 plateau；(2) LM head 是信息瓶颈，teacher 的中间 hidden state 被 softmax projection 压缩丢弃。
OPRD 将蒸馏目标从 LM head **之后**移到 **之前**：在同一 on-policy rollout 上对 student 和 teacher 在选定层的 hidden state 做 normalized MSE，stop-gradient 到 teacher 侧。
这一改变同时解决两个问题：gradient 是确定性函数（条件方差 = 0），且监督信息量按 (L × T × d) 维度展开而非被投影压缩。

## 谱系位置
相比所有 output-space OPD 变体（包括 DeepSeek-V4、Qwen3 使用的 sampled-token reverse KL），OPRD **首次**在 on-policy regime 引入 representation-level 监督，证明（Thm 1）hidden-state MSE gradient 的条件方差为零，而任意 output-space OPD 的方差由 score function term 主导且不随训练收敛而衰减。
相比离线 feature distillation（FITNET 等），OPRD 作用在 student 自采样的 on-policy trajectory 上，避免 exposure bias，且不需要静态 teacher rollout。


## Method
**Loss**（Eq. 6）：对 on-policy rollout (x, ŷ) 上，选取层集合 L_layer 和位置集合 P(ŷ)（默认 last k=2000 tokens），计算
$$\mathcal{L}_\text{OPRD} = \mathbb{E}\left[\frac{1}{|L_\text{layer}|}\sum_l \frac{1}{\sum_t m_t}\sum_t m_t \frac{1}{d}\|h_{\theta,t}^{(l)} - \text{sg}(h_{T,t}^{(l)})\|_2^2\right]$$
student 与 teacher 维度不同时接一个线性 projector（本实验中 d_s = d_T = 1536，省略）。
实验配置：Qwen2.5-1.5B backbone（L=28，d=1536，|V|≈151K），teacher=JustRL-1.5B，student=R1-distill-1.5B，DAPO-Math-17K prompt set，AdamW lr=1e-5，500 steps，8×A100 80G FSDP。

## 优缺点

- ✅ [作者 ack §3.2]: hidden-state MSE 的 conditional gradient variance 为零，直接避开 output-space score-function 方差。
- ⚠️ [作者 ack §4]: 主要实验在同架构/同 hidden size setting，cross-architecture projector 与 layer selection 仍需额外验证。

## headline number

- AIME24 Avg@16 OPRD 49.8 vs OPD top-16 47.1（§4.2 Table 2）
- Training speed 1.44× and actor-update memory -54%（§1 Figure 1）

## Evidence
- "AIME24 OPRD=49.8 vs. OPD top-16=47.1" 来自 §4.2 Table 2
- "1.44× faster, 54% less memory" 来自 §1 Fig 1 caption
- "Var[ĝ_OPRD | x, ŷ] = 0" 来自 §3.2 Theorem 1 (Eq. 8)

<!-- pdf: §3 Method / §4.2 Experiments -->
