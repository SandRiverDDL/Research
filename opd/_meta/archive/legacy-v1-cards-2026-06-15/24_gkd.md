---
title: "On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes"
authors: [Rishabh Agarwal, Nino Vieillard, Yongchao Zhou, Piotr Stanczyk, Sabela Ramos, Matthieu Geist, Olivier Bachem]
org: gdm
year: 2024
venue: iclr-2024
arxiv_id: 2306.13649
url: https://arxiv.org/abs/2306.13649
zotero_key:

confidence: 1
open_source: unknown
verified: a

decisions:
  rollout: student
  loss: forward-kl
  signal: logit
  iteration: continuous
  filter: none
  extra: none
---

> **TL;DR**: 让 student 自己采样序列、teacher 在这些 on-policy rollout 上给 token-level 概率作为标签，可在 forward-KL / reverse-KL / JSD(β) 之间任选 divergence；相对 supervised KD 在 XSum / WMT / GSM8K 上把 student 提升 2.1× / 1.7× / 1.9×（averaged across T5 students）。

## Core Idea

把 auto-regressive KD 框成 interactive-expert imitation learning：用 student 自己 rollout 解决 train-inference distribution mismatch（exposure bias），teacher 只提供 token-level logits 作 expert label。GKD 把 student data fraction λ ∈ [0,1] 与 divergence 𝒟（forward-KL / reverse-KL / JSD(β)）解耦成两个独立超参，不 backprop 通过采样过程，所以比 MiniLLM 的 policy gradient 稳定。

## What's Actually New

vs. MiniLLM (Gu et al. 2023, 同期)：MiniLLM 用 reverse-KL + policy gradient 还要一堆 stabilizing tricks（length bias、reward hacking）；GKD 不 backprop through sampling，更接近 supervised training。vs. ImitKD (Lin 2020)：ImitKD 只到 λ=0.5 mix、固定 forward-KL，不探索纯 on-policy 也不接 RL；GKD 把 ImitKD/f-distill 都涵盖为特例。GKD 还首次把 distillation 和 RLAIF 同时联合优化（teacher 替代 SFT 作 KL anchor）。

## Method

GKD 损失：L = (1−λ)·E_{(x,y)~D}[𝒟(p_T‖p_S)(y|x)] + λ·E_{x~X, y~p_S}[𝒟(p_T‖p_S)(y|x)]，每 step 以概率 λ 用 student rollout 否则用 ground-truth。Algorithm 1 是 mixture sampling。Sweep：λ∈{0,0.5,1}、𝒟∈{forward-KL, reverse-KL, JSD(0.1/0.5/0.9)}。Models：T5-small/base/large/XL（77M/250M/800M/3B）作 student，supervised-FT T5-XL 作 teacher。Tasks：XSum (ROUGE-2)、WMT en-de (BLEU)、GSM8K (4-shot CoT acc)、FLAN2021 instruction tuning (MMLU/BBH 几何平均)。还做了 GKD + REINFORCE 的 RLAIF 实验（textual entailment reward）。

## Verdict

- 升 L2？yes
- 理由：on-policy distillation 的开山参考之一，几乎所有后续 OPD/DistiLLM/SKL/GAD 论文的主 baseline，必须复现 + 精读

## Evidence

- TL;DR 数字 2.1×/1.7×/1.9× 来自 §1 Introduction (Figure 1 caption)
- "λ=1 on-policy 未被先前探索" 来自 §4 Experiments → GKD Variants
- "不 backprop through sampling 比 MiniLLM 稳定" 来自 §5 Related Work (MiniLLM 段)
- task-dependent divergence: WMT 用 JSD(0.1)，instruction tuning 用 reverse-KL，summarization/GSM8K 用 forward-KL —— 来自 Figure 1 caption + §4.4 Results
