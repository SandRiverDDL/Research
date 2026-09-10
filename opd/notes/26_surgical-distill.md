---
title: "Surgical Post-Training: Cutting Errors, Keeping Knowledge"
authors: [Wenye Lin, Kai Han]
org: visual-ai
year: 2026
venue: arxiv
arxiv_id: 2603.01683
url: https://arxiv.org/abs/2603.01683
zotero_key:

confidence: 3
open_source: partial
verified: a

addresses:
  - capacity-gap
  - reward-hacking

decisions:
  rollout: mixed
  loss: preference
  signal: outcome
  iteration: one-shot
  filter: trajectory-level
  extra: privileged-info
---

> **一句话**：最小编辑偏好数据的 surgical post-training 路线。

## 核心做法
灾难性遗忘的决定性因素不是数据分布偏移（SFT+ 在近分布数据上仍然遗忘），而是优化目标中是否存在 KL 约束的隐式奖励——其梯度系数 λ = 1−σ(r_θ) 在模型饱和时自动归零，充当逐样本的 early stopping。SPoT 把这一机制拆解出来，设计了两个组件：(1) Oracle 最小编辑数据流水线，产出与学生分布高度重叠的 (y⁻, y⁺) 对；(2) 解耦 BCO loss，对正负样本独立分类，消除 DPO 相对排序导致的"只压 y⁻ 不拉 y⁺"问题和 SFT 的"pull-up 效应"。

## 谱系位置
相比 DPO：指出其"相对排名"优化路径允许通过 collapse y⁻ 而非提升 y⁺ 来最小化 loss，对 reasoning（正确/错误二元）不合适；改用解耦 BCE，正负各自对 sigmoid(r) 分类。
相比 SFT/蒸馏（含 SPIN）：SPIN 用模型自采样作负例；本文用教师最小编辑版作正例，并通过 LCS ratio 硬过滤保证 token 级近邻性，使梯度集中于分歧 token。


## Method
1. **Error Elicitation**：从当前策略采样，保留答案错误的 (x, y⁻)。
2. **Oracle 最小编辑**：Gemini 2.5 Pro 仅修改错误推理步骤，保留原始风格，得到 y⁺。
3. **LCS 过滤**：R_LCS = 1 − |LCS(y⁻,y⁺)|/|y⁺| > 0.6 的对被丢弃；确保 y⁺/y⁻ 共享大多数 token 轨迹。
4. **SPoT-BCE loss**：−E[log σ(r(x,y⁺)) + log σ(−r(x,y⁻))]；隐式奖励 r = β log(π_θ/π_ref)。
5. **SPoT-BCO（推荐）**：加 EMA 动态 reward shift δ，防止正例 sigmoid 饱和过早停止；β=0.1，4k 对样本，28 分钟。

## 优缺点

- ✅ [作者 ack §3.2]: sigmoid 梯度衰减提供逐样本 early stopping，解释 DPO 知识保持来源。
- ⚠️ [作者 ack §4.5]: 最小编辑正例依赖强 oracle，当前验证规模偏小且集中在数学域。

## headline number

- Qwen3-8B average +6.2% and IFEval +1.8% with 4k samples / 28 minutes（§4.5 Table 1）

## Evidence
- TL;DR 数字 +6.2% 来自 §4.5 Table 1（Qwen3-8B+SPoT avg=53.3 vs baseline 47.1）
- TL;DR IFEval +1.8% 来自 §4.5 Table 1（84.8 vs 83.0）
- "λ ≈ 4.5×10⁻⁵" 来自 §3.2 Eq. 示例（r_θ=10 时）
- "SFT+ 仍遗忘" 来自 §3.1 Figure 2（IFEval 单调下降）

<!-- pdf: §3 Mechanism / §4.5 Experiments -->
