---
title: "On-Policy Distillation of Language Models for Autonomous Vehicle Motion Planning"
authors: [Amirhossein Afsharrad, Amirhesam Abedsoltan, Ahmadreza Moradipari, Sanjay Lall]
org: stanford
year: 2026
venue: arxiv
arxiv_id: 2604.07944
url: https://arxiv.org/abs/2604.07944
zotero_key:

confidence: 3
open_source: no
verified: a
scope: off  # 自动驾驶 cs.RO domain mismatch

decisions:
  rollout: unknown
  loss: forward-kl
  signal: unknown
  iteration: unknown
  filter: unknown
  extra: unknown
---

> **TL;DR**: Qwen3-1.7B distilled from Qwen3-8B via on-policy JSD-GKD (β=0.5, λ=0.5) reaches 0.373 m STP-3 L2 on nuScenes—only 5% below the 8B teacher—while a REINFORCE-based RL distillation baseline using teacher log-prob rewards lands 55% worse at 0.579 m.

## Core Idea
Reformulates LLM-based AV motion planning (GPT-Driver framework, nuScenes) as an on-policy distillation problem. Teacher = Qwen3-8B (SFT); student = Qwen3-1.7B trained with GKD, generating its own rollouts and minimizing per-token JSD to the teacher's full vocabulary distribution. The key claim: full-distribution supervision beats scalar per-token reward for structured coordinate output because digit co-occurrence constraints are encoded in the teacher distribution, not in any single sampled token.

## What's Actually New
GKD (Sinha et al.) existed for NLP (summarization, MT, math); this paper is the first direct application to structured numeric trajectory output in AV planning. The controlled GKD vs. RL comparison (same on-policy rollouts, same models, only learning signal differs) isolates *information richness* of the distillation signal—full vocabulary distribution vs. scalar advantage—and shows the gap is severe (55% L2, 2.6× collision rate) for coordinate generation.


## Method
1. **Teacher**: SFT Qwen3-8B on nuScenes GPT-Driver dataset, `qwen3_nothink` template (disables extended thinking).
2. **GKD Student**: TRL `GKDTrainer`; each batch 50% on-policy student rollouts + 50% GT (λ=0.5); loss = mean per-token JSD^(β=0.5) between teacher and student distributions along student-generated prefixes; gradients stop through sampling.
3. **RL Baseline**: per-token advantage A_n = sg[log p_T(ŷ_n | ctx) − log p_S(ŷ_n | ctx)], REINFORCE update; no KL penalty to reference.
4. Both methods: Qwen3-1.7B, lr=5e-5, effective batch 8, 5 epochs on 8×H200.

## Verdict
- 升 L2？**no**
- 理由：纯应用论文，方法是直接套 TRL GKDTrainer；GKD vs. RL 的对比有参考价值，但无新 distillation 机制；nuScenes 是封闭 domain，结论泛化性待验证。

## Evidence
- TL;DR 数字（0.373 m, 0.579 m, 5%）来自 §VI-A Table I
- "GKD 2.6× safer than RL on collision rate" 来自 §VI-A（0.138% vs. 0.363%）
- "β=0.5, λ=0.5" 来自 §IV-B3 和 §V-B
