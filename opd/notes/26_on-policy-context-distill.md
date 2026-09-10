---
title: On-Policy Context Distillation for Language Models
authors: [Tianzhu Ye, Li Dong, Xun Wu, Shaohan Huang, Furu Wei]
org: microsoft-research
year: 2026
venue: arxiv
arxiv_id: 2602.12275
url: https://arxiv.org/abs/2602.12275
zotero_key:

confidence: 2
open_source: no
verified: a

addresses:
  - privileged-context-gap
  - experience-internalization

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: one-shot
  filter: none
  extra: privileged-info
---

> **一句话**：context distillation 的 OPD 化框架。

## 核心做法
传统 context distillation 用 forward KL + off-policy 数据，有 exposure bias 和 mode-covering 问题。
OPCD 将 on-policy 蒸馏（MiniLLM 范式）移植到 context distillation：student 在无 context 条件下生成轨迹 $y$，teacher 读 $[c; x; y]$ 提供 target distribution，以 token-level reverse KL 作为训练信号。
Teacher 可以是不同大小的模型（teacher-student）或同一模型共享权重但输入不同（self-distillation）。
两大应用：(1) 将历史 solution trace 提炼的经验知识 $c$ 内化；(2) 将优化好的 system prompt $c$ 内化，推理时去掉 context 开销。

## 谱系位置
相对 MiniLLM：损失形式相同（on-policy reverse KL），但 teacher 不是更大的模型，而是**同一模型加 privileged context**；压缩对象从"知识"变成"上下文行为"。
相对传统 context distillation（Askell 2021 / Snell 2022）：将 off-policy forward KL 替换为 on-policy reverse KL，解决 exposure bias 和 mode averaging 问题。
相对并发 privileged-information 工作（RLSD/Self-distilled Reasoner）：支持 cross-size teacher-student 蒸馏，小模型可吸收大模型在 context 上的行为。


## Method
**Loss（Eq. 1）**：$\mathcal{L}(\theta) = \mathbb{E}_{y \sim \pi_\theta(\cdot|x)} \left[ \frac{1}{|y|} \sum_t D_\text{KL}(\pi_\theta(\cdot|x,y_{<t}) \| \pi_\text{teacher}(\cdot|c,x,y_{<t})) \right]$
实现时用 student top-$k$ token 近似解析 KL，避免全词表求和。
训练规模极轻：50 steps，batch 128，max length 16384（math）/ 512（system prompt）。
经验知识蒸馏分三步：①模型对 validation 问题自生成 solution trace；②提炼 experience items 并累积为上下文 $c$；③用 OPCD 将 $c$ 内化，推理时无需 context。

## 优缺点

- ✅ [作者 ack §3]: teacher 通过 context-conditioned 分布提供监督，student 推理时无需携带 context。
- ⚠️ [作者 ack §3-4]: 依赖 privileged context 本身可被参数内化；实例级、不可恢复 context 可能退化为 shortcut。

## headline number

- Qwen3-8B math OPCD 80.9% vs off-policy context distillation 79.5%（§4.3 Table 2）

## Evidence
- "80.9% OPCD vs 79.5% Context Distill" 来自 §4.3 Table 2（filtered, Qwen3-8B, Math）
- "OPCD can surpass the original model with experiential knowledge in the context" 来自 §4.3 §4.SS3.SSS0.Px1.p2
- Token-level reverse KL loss 来自 §3 Eq. 1–2 及 Algorithm 1

<!-- pdf: §3 Method / §4.3 Experiments -->
