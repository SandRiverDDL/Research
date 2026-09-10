---
title: "Skill-Conditioned Gated Self-Distillation for LLM Reasoning"
authors: [Jiazhen Huang, Xiao Chen, Xiao Luo, Yong Dai, Senkang Hu, Yuzhi Zhao]
org: tsinghua
year: 2026
venue: arxiv
arxiv_id: 2605.28791
url: https://arxiv.org/abs/2605.28791
zotero_key:

confidence: 3
open_source: yes
verified: a

addresses:
  - privileged-context-gap
  - flawed-prefix-trap

decisions:
  rollout: student
  loss: reverse-kl
  signal: logit
  iteration: continuous
  filter: verifier-pass
  extra: privileged-info
---

> **一句话**：skill bank privilege 的多 teacher 校验路线。

## 核心做法

把 skill-based SD 重新表述为 **teacher hypothesis validation**：retrieve 一组 skill-mistake pair 构造多 teacher pool，teacher 看 skill+plain prompt，student 只看 plain prompt，所有 teacher 对同一条 student rollout 打 logit。verifier 给最终答案对/错 → 推断每个 teacher 当前 stance 是否有用：rollout 成功且 teacher support 给正信号，rollout 失败且 teacher support 给反向信号，misleading teacher 会被反转，uncertain teacher (ρ_k=0) 被丢掉。

## 谱系位置

vs OPSD（Zhao 2026）：OPSD 用 reference answer 当 PI、单一 teacher、unconditional imitation；SGSD 用更弱的 PI（可能误导的 skill bank）+ 多 teacher polarity 校验 + gated 而非直接 KL。skill bank 路线 vs 直接答案蒸馏路线的首次正面对照。

## Method

(1) cold-start 用历史 mistake 抽 skill 入 bank，online 持续维护；(2) Qwen3-Embedding-0.6B 检索 top-8 skill pair；(3) student（disable thinking）从 plain prompt rollout 一次，K 个 skill-conditioned teacher（enable thinking）逐 token 打 full-vocab logit；(4) verifier outcome × teacher support 决定 ρ_k ∈ {+1, -1, 0}；(5) gated loss = bounded 函数 of teacher-student log-prob gap，理论上 local 等价于 sampled-token reverse-KL（§3）。Base：Qwen3-1.7B/4B/8B；训练集 DAPO-Math-17K English；评测 AIME24/AIME25/HMMT25 avg@12。

## 优缺点

- ✅ [作者 ack §2.3]: verifier outcome 给每个 skill-conditioned teacher 判定 polarity，避免盲目模仿误导 skill。
- ⚠️ [作者 ack §4.2]: 8B 上仍弱于 OPSD，收益主要集中在小模型，scale-up 稳定性有限。

## headline number

- Qwen3-1.7B AIME24/25+HMMT25 average 37.4 → 43.7, +6.2 vs GRPO and +1.7 vs OPSD（§4.2 Table 3）

## Evidence

- TL;DR 数字（37.4→43.7、+6.2、+1.7）来自 §4.2 + Table 3，正文第 1297 行
- "verifier validates polarity, opposite stance reversed" 来自 Abstract + §2.3 Table 2
- "gated loss locally approximates reverse-KL，extreme gaps 被 exponentially damp" 来自 §3 / §2.5
- 8B 上 SGSD 仍 underperform OPSD，仅小模型反超：§4.2 Table 3
- code: https://github.com/walawalagoose/SGSD（abstract 末尾）

<!-- pdf: §2 Method / §3 Theory / §4.2 Experiments -->
