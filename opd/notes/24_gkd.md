---
title: "On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes"
authors: [Rishabh Agarwal, et al.]
org: gdm
year: 2024
venue: iclr-2024
arxiv_id: 2306.13649
url: https://arxiv.org/abs/2306.13649

confidence: 1
verified: s

surveys:
  song-2026: "§1 Introduction; §2.1 Classical KD; §2.3 Unified Framework"

addresses:
  - exposure-bias

decisions:
  rollout: mixed
  loss: forward-kl
  signal: logit
  iteration: continuous
  filter: none
  extra: none
---

> **一句话**：和 MiniLLM 同期（2023 年中）把 OPD 带入 LLM 时代的开山参考之一。

## 核心做法

针对 train-inference distribution mismatch（exposure bias），将蒸馏框架化为 imitation learning：student 自己 rollout，teacher 在 student 生成序列上给 token-level logits；divergence 𝒟 与 mixture rate λ 正交，可独立选择，不 backprop through sampling。

$$\mathcal{L}_{\mathrm{GKD}}(\theta) := (1-\lambda)\,\mathbb{E}_{(x,y)\sim(X,Y)}\bigl[\mathcal{D}(p_T \| p_S^\theta)(y|x)\bigr] + \lambda\,\mathbb{E}_{x\sim X}\Bigl[\mathbb{E}_{y\sim p_S(\cdot|x)}\bigl[\mathcal{D}(p_T \| p_S^\theta)(y|x)\bigr]\Bigr]$$

λ→1 = 纯 on-policy；λ=0 退回 supervised KD；ImitKD / f-distill 均为 GKD 特例。

## 谱系位置

- 上游：Seq-KD (Kim & Rush 2016) — 放松到 sequence-level 但仍静态数据（off-policy assumption 未破）
- 上游：ImitKD (Lin 2020) — 首识 KD-IL 连接但固定 λ=0.5、只用 forward-KL，未探索纯 on-policy
- 同期：MiniLLM (Gu 2024) — 同样 on-policy 但选 reverse-KL + REINFORCE，需多种稳定 tricks
- 下游：DistiLLM (Ko 2024) — 以 skew-KL mixture target 修复 KLD 梯度不稳，加 replay buffer

## 优缺点

- ✅ [作者 ack §3.1]：不 backprop through sampling，训练稳定且计算高效
- ✅ [song-2026 §2.3]：divergence-agnostic 设计成为后续 OPD 方法的通用脚手架
- ⚠️ [song-2026 §2.3]：divergence 选择缺乏理论指导，最优 𝒟 随任务而异，需经验调参
- ⚠️ [DistiLLM 2024]：标准 KL 在 q_θ≈0 处存在 zero-division 梯度不稳（kld-gradient-explosion），DistiLLM 以 skew-KL mixture target 改进

<!-- pdf: §3.1 GKD / §3.2 RL Fine-tuning / §5 Related Work / §6 Conclusion -->
<!-- song-2026: §1 Introduction / §2.1 Classical KD / §2.3 Unified Framework -->
