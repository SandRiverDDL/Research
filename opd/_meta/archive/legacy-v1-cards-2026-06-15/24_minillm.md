---
title: "MiniLLM: Knowledge Distillation of Large Language Models"
authors: [Yuxian Gu, Li Dong, Furu Wei, Minlie Huang]
org: tsinghua
year: 2024
venue: iclr-2024
arxiv_id: 2306.08543
url: https://arxiv.org/abs/2306.08543
zotero_key:

confidence: 3
open_source: yes
verified: a

decisions:
  rollout: mixed
  loss: reverse-kl
  signal: logit
  iteration: continuous
  filter: none
  extra: none
---

> **TL;DR**: 用 **reverse-KL + on-policy policy gradient**（teacher-mixed sampling α=0.2 + length-norm + single-step decomposition）替代 sequence-level forward-KL；GPT-2 760M student 在 DollyEval GPT-4 score 54.7 vs SeqKD 52.0，OPT/LLaMA 1.3B–7B 学生在 S-NI/UnNI 上 Rouge-L 反超 teacher。

## Core Idea

White-box KD for generative LLM 时 forward-KL 让学生覆盖 teacher 全部 mode，导致它把概率分到 teacher 的 void region（生成低质量文本）。改成 **reverse-KL** `KL[q_θ‖p]` 让学生 mode-seeking，专注 teacher 的主 mode。优化用 policy-gradient on-policy 推导（学生自己 rollout，把 `log p/q_θ` 当 reward），形式上等价 RLHF。

## What's Actually New

vs. **sequence-level KD / Alpaca / Vicuna**（都最小化 forward-KL，要么 teacher-forcing token-level 要么直接 SFT teacher 文本）：MiniLLM 改 reverse-KL + 把 KD 当成 on-policy RL，学生从自己分布采样而非 fit teacher 样本，缓解 exposure bias 和 reward hacking。同期 concurrent work GKD（Agarwal 2023）也走 KL 变体方向但 framing 不同。

## Method

目标 `min_θ KL[q_θ‖p]`，policy-gradient 推导得 `∇L = -E[Σ(R_t-1)∇log q_θ]`，`R_t = Σ log p/q_θ`。三个稳定 trick：(1) **single-step decomposition** 把 r_t 直接 expectation over vocab 降方差，(2) **teacher-mixed sampling** `p̃ = αp + (1-α)q_θ` α=0.2 抑制 reward hacking，(3) **length normalization** 防 short-output 偏置。加 PPO clip + LM-loss 正则。Student：GPT-2 (120M–760M)、OPT (1.3B–6.7B)、LLaMA-7B；teacher：1.5B/13B。数据：databricks-dolly-15k 12.5K 训练。

## Verdict

- 升 L2？yes
- 理由：是 on-policy distillation 的 founding paper，OPD 项目的核心 baseline + 直接 competitor，必须复现 reverse-KL + teacher-mixed sampling 这套配方。

## Evidence

- TL;DR GPT-2 760M 数字 54.7/52.0 来自 §3.2 Table 1 (DollyEval GPT4)
- "学生 Rouge-L 反超 teacher" 来自 §3.2 Table 1（带 * 标记，例如 OPT-6.7B MiniLLM S-NI 32.5 > teacher 30.4）
- ablation 解读基于 §3.4 Table 4：去掉 length-norm Valid R-L 27.4→17.4，去 teacher-mixed →22.3
- α=0.2 / clip 配置来自 §3.1 + Algorithm 1
- reverse-KL motivation toy 实验来自 §2.1 Figure 2
