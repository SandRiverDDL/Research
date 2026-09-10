---
title: Black-Box On-Policy Distillation of Large Language Models
authors: [Tianzhu Ye, Li Dong, Zewen Chi, Xun Wu, Shaohan Huang, Furu Wei]
org: microsoft-research
year: 2025
venue: arxiv
arxiv_id: 2511.10643
url: https://arxiv.org/abs/2511.10643
zotero_key:

confidence: 2
open_source: no
verified: a

addresses:
  - api-only-teacher
  - teacher-staleness

decisions:
  rollout: student
  loss: advantage
  signal: outcome
  iteration: continuous
  filter: none
  extra: rm
---

> **一句话**：black-box teacher 场景的动态判别器蒸馏路线。

## 核心做法
仅用 teacher 生成的文本（无 logits）实现 on-policy 蒸馏：将 student 视为 GAN 的 generator，额外训练一个 discriminator 区分 teacher/student 回复，构成 minimax 对抗训练。discriminator 的输出作为 on-policy reward，驱动 generator 通过 GRPO 更新。与 RLHF 中固定 reward model 不同，discriminator 与 student 同步更新，持续对齐当前策略的分布，理论上规避 reward hacking。

## 谱系位置
相比 SeqKD（teacher response SFT，off-policy），GAD 引入了 on-policy 采样 + 动态 discriminator 作为 reward，无需白盒 logits；相比 MiniLLM/DistiLLM（sequence-level RKL），这是首个在纯 black-box 场景下做 on-policy 优化的方法，不依赖 teacher 概率空间。discriminator co-evolve 的设计比 SPIN（self-play，无 teacher 导向）多了一个显式的 teacher–student 排序监督。


## Method
1. **数据**：从 LMSYS-Chat-1M 采样 200K 条，用 teacher（GPT-5-Chat）生成回复构建 `T={(x, y_t)}`。
2. **Warmup（1 epoch）**：generator 用 CE loss 在 `y_t` 上 SFT；discriminator 用 Bradley-Terry 损失 `min_D E[-log σ(D(y_t) - D(G(x)))]` 初始化。
3. **GAD 迭代**：student 采样 `G(x)`，discriminator 打分 `D(G(x))` 作为 reward；GRPO 更新 generator；同步用 BT 损失更新 discriminator（参数来自 student + 额外标量 head）。
4. **实现**：基于 verl 框架，GRPO 作为 policy gradient 算法，batch size 256，3 epochs，约 2400 步。

## 优缺点

- ✅ [作者 ack §2]: 不需要 teacher logits，只要 teacher 文本即可构造动态判别器 reward。
- ⚠️ [作者 ack §3.2]: 主要评测依赖 GPT-4o judge，teacher 数据来自闭源 GPT-5 API，复现链条受限。

## headline number

- Qwen2.5-3B+GAD 48.9 vs Qwen2.5-7B+SeqKD 49.2 on LMSYS GPT-4o evaluation（§3.2 Table 2）

## Evidence
- TL;DR 数字（48.9/49.2）来自 §3.2 Table 2，LMSYS 列
- "Qwen2.5-3B+GAD matches Qwen2.5-7B+SeqKD" 来自 §3.2 Automatic Evaluation
- "SeqKD yields marginal or negative improvements on OOD" 来自 §3.2 Automatic Evaluation

<!-- pdf: §2 Method / §3.2 Automatic Evaluation -->
