---
title: "Stabilizing On-Policy Distillation for MLLM Reasoning with Global Normalization"
authors: [Dongze Hao, Zhiwei Jin, Chen Chen, Haonan Lu]
org: oppo
year: 2026
venue: arxiv
arxiv_id: 2606.09091
url: https://arxiv.org/abs/2606.09091
zotero_key:

confidence: 4
open_source: yes
verified: a

addresses:
  - large-policy-divergence
  - policy-gradient-variance

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: none
  extra: none
---

> **一句话**：多模态 OPD 的 batch 归一化稳定路线。

## 核心做法

观察：naive OPD 用 reverse KL `log π_θ / π_teacher` 作 token reward，当 student 生成 teacher 给低概率的 OOD token 时 log-ratio 爆炸，少数 token 主导梯度→训练不稳。
方案：把 raw token-level KL reward 在 batch 内 z-score 归一化得到 `Â^norm`，再走 importance-sampling RL objective。当极端 reward 出现时，batch std 自动膨胀→等效梯度步长被自动缩小。

## 谱系位置

vs. Thinking Machines OPD (Lu 2025) 直接把 reverse KL 当 token reward：GNDPO 在此之上加 batch-level mean/std 归一化，本质是把 GRPO 的 group-relative advantage 思想从 sequence-level 移到 token-level distillation reward。
vs. GSPO：从 sparse outcome reward 升级到 dense token-level KL 信号但保持 stable。

## Method

Reward: `Â_{i,t} = -(log π_θ(o_t) - log π_teacher(o_t))`（reverse KL，§2.2 Eq.3）。
归一化: `Â^norm_{i,t} = (Â_{i,t} - mean_B(A)) / (std_B(A) + ε)`（§3.2 Eq.4，B 为整 batch 所有 token）。
Setup: VERL 框架；teacher = InternVL3.5-8B，student = 1B/2B/4B；Geometry3K 训练；G=16 rollouts，bs=32，lr=1e-6 Adam constant，max ctx 24576，8×H20。

## 优缺点

- ✅ [作者 ack §3.1-3.2]: batch z-score 自动压缩 OOD token 引发的极端 KL reward，缓解梯度尖峰。
- ⚠️ [作者 ack §4]: 验证集中在 InternVL3.5/Geometry3K，多模态数学单域外泛化仍弱。

## headline number

- InternVL3.5-4B Overall 54.5 vs OPD 53.9 / GSPO 52.5 / Base 49.4 across seven MLLM reasoning benchmarks（§4.2 Table 1）

## Evidence

- TL;DR Overall 54.5 / 53.9 / 52.5 / 49.4 来自 §4.2 Table 1 (InternVL3.5-4B 行)
- "raw KL log-ratio 在 OOD token 上爆炸" 来自 §3.1 Motivation
- 归一化公式 Eq.4 来自 §3.2
- code 释放来自 abstract (github.com/OPPO-Mente-Lab/GNDPO)

<!-- pdf: §3 Motivation and Method / §4.2 Experiments -->
