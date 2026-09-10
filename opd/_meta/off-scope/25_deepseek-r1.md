---
title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
authors: [DeepSeek-AI]
org: deepseek
year: 2025
venue: arxiv
arxiv_id: 2501.12948
url: https://arxiv.org/abs/2501.12948
zotero_key:

confidence: 3
open_source: partial
verified: a
scope: off  # 综述 must-read seed，RL recipe 而非 OPD 方法

decisions:
  rollout: unknown
  loss: advantage
  signal: outcome
  iteration: unknown
  filter: unknown
  extra: unknown
---

> **TL;DR**: 纯 GRPO RL（无 SFT cold start）将 DeepSeek-V3-Base 在 AIME 2024 pass@1 从 15.6% 推至 71.0%，加 cold-start 后的 4-stage pipeline（R1）达 79.8%，并发现 rejection-sampling SFT 蒸馏到 7B 小模型即可超越 QwQ-32B-Preview（55.5% vs. ~50%）。

## Core Idea
RL 可以在无任何 SFT 数据的情况下激励 LLM 自发涌现 chain-of-thought、自我反思和验证行为（R1-Zero）。在此基础上加入少量 cold-start CoT 数据稳定训练，经历"cold start SFT → reasoning RL → rejection-sampling SFT → all-scenario RL"四阶段后得到 R1，性能比肩 o1-1217。蒸馏路径则是直接用 800k R1 输出 SFT 小模型，效果优于对小模型直接跑 RL。

## What's Actually New
相比 DeepSeek-V3 及此前 RL-for-reasoning 工作，R1-Zero 首次公开验证：**不需要 SFT warm-up，pure RL 即可从 base model 涌现可读的 long-CoT 和 aha-moment 反思行为**。相比 GKD / DistiLLM 等蒸馏方法，R1 蒸馏路径没有用 KL divergence loss，只做 rejection-sampled behavior cloning，但受益于 teacher 输出质量（reasoning traces with summaries），小模型增益超出预期。


## Method
1. **R1-Zero**：GRPO（group size G，baseline = group mean reward），rule-based reward = accuracy + format，无 SFT，base model 直接 RL。
2. **Cold Start**（R1 stage 1）：用数千条人工精筛的 long-CoT 数据 fine-tune base model，格式为 `<think>…</think><summary>`。
3. **Reasoning RL**（stage 2）：GRPO + accuracy reward + language consistency reward（目标语言词比例），跑至 reasoning benchmark 收敛。
4. **Rejection Sampling SFT**（stage 3）：从 stage 2 checkpoint 采样，保留正确输出；共 ~600k reasoning + ~200k non-reasoning，fine-tune 2 epochs。
5. **All-scenario RL**（stage 4）：rule-based reward（math/code/logic）+ neural RM（helpfulness/harmlessness），综合 reward 对齐人类偏好。
6. **Distillation**：直接用上述 800k 数据 SFT Qwen2.5/Llama3 系列（1.5B–70B），无额外 RL。

## Verdict
- 升 L2？**no**
- 理由：pipeline 描述完整，关键超参（GRPO group size、KL 系数 β、cold-start 数量、RL steps）未完全公开；作为 reasoning RL + distillation 的奠基 recipe，L1 足以做 baseline 对比参照。需要复现时再升。

## Evidence
- AIME 2024 15.6% → 71.0% 来自 §2.2.4 Figure 2 & Table 2
- cons@64 = 86.7% matching o1-0912 来自 §2.2.4 Table 2
- R1 AIME 79.8%, MATH-500 97.3% 来自 §1.2 Evaluation Summary
- Distill-Qwen-7B 55.5% AIME 来自 §1.1 Contributions（Distillation 段落）
- "direct distillation outperforms RL on small models" 来自 §2.4
