---
title: "DistiLLM: Towards Streamlined Distillation for Large Language Models"
authors: [Jongwoo Ko, Sungnyun Kim, Tianyi Chen, Se-Young Yun]
org: kaist
year: 2024
venue: icml-2024
arxiv_id: 2402.03898
url: https://arxiv.org/abs/2402.03898
zotero_key:

confidence: 3
open_source: yes
verified: a

decisions:
  rollout: mixed
  loss: skl
  signal: logit
  iteration: iterative
  filter: none
  extra: none
---

> **TL;DR**: 用 α=0.1 的 skew (R)KL 替代 KLD/RKLD/JSD + 一个 adaptive off-policy 的 SGO replay buffer（λ_R=ϕ(1−t/T)），相比 MiniLLM/GKD 拿到 2.5–4.3× 训练加速，SRKL 在 Dolly Eval 上 ROUGE-L 25.21 vs JSD 24.34。

## Core Idea

把 forward/reverse KL 换成 **skew KL**：D_SKL^(α)(p,qθ) = D_KL(p, αp+(1−α)qθ)，分母被 αp 抬起避免梯度爆炸；理论上界证明 α=0.1 在 gradient norm 与 L2 估计误差之间取折中。SGO 用 **adaptive scheduler + replay buffer** 处理：ϕ 按 validation loss 自适应调高，replay 概率 λ_R 随 t 线性衰减，前期多用 fresh SGO 减小 off-policy bias，后期多重用旧 SGO 省 generation 开销。

## What's Actually New

vs **GKD** (Agarwal 2024)：把 generalized JSD 换成 skew (R)KL（理论上更稳的梯度系数 (1−α)·r_{p,q̃}），并把 on-policy 的每步 SGO 换成 off-policy replay。
vs **MiniLLM** (Gu 2024)：不再用 policy gradient + RKLD，而是直接 token-level SKL + 自适应 SGO 比例，去掉 teacher rollout 开销。

## Method

Algorithm 1：每 iter 以概率 ϕ 用 SGO（从 D_R 采样）否则用 fixed dataset；以概率 λ_R = ϕ(1−t/T) 让 student 生成新 SGO 入 buffer；loss 用 D_SKL^(α) 或 D_SRKL^(α)，α=0.1，buffer size=1000，初始 ϕ=0。Teacher/student 设置：GPT-2 (XL→base)、OPT、OpenLLaMA-3B/7B；评测 instruction-following（databricks-dolly-15k → Dolly/Self-Instruct/Vicuna/Super-Natural/Unnatural Eval）+ 摘要 + 翻译，4×A100。

## Verdict

- 升 L2？yes
- 理由：直接 competitor — OPD 路线里的 logit-level SGO baseline，复现要对齐 SRKL+off-policy 配置；GKD/MiniLLM 的关键对照在此。

## Evidence

- TL;DR "2.5–4.3× speedup" 来自 §1 Contributions 与 §5/Fig. 7
- TL;DR "SRKL 25.21 vs JSD 24.34" 来自 §4 Table 1
- "α=0.1 最优" 来自 §3.1 末尾 + Table 6
- adaptive ϕ + λ_R=ϕ(1−t/T) 来自 §3.2 + Algorithm 1
