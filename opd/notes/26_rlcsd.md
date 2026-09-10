---
title: "RLCSD: Reinforcement Learning with Contrastive On-Policy Self-Distillation"
authors: [Leyi Pan, Shuchang Tao, Yunpeng Zhai, Lingzhe Zhang, Zhaoyang Liu, Bolin Ding, Aiwei Liu, Lijie Wen]
org: tsinghua
year: 2026
venue: arxiv
arxiv_id: 2606.11709
url: https://arxiv.org/abs/2606.11709
zotero_key:

confidence: 3
open_source: yes
verified: a

addresses:
  - privileged-context-gap
  - coarse-credit-assignment

decisions:
  rollout: student
  loss: advantage
  signal: logit
  iteration: continuous
  filter: none
  extra: privileged-info
---

> **一句话**：privileged hint 的正负对照去偏路线。

## 核心做法

OPSD 用 e_c,t = log π_T(y|x,y_c*,·) − log π_S(y|x,·) 提供 dense token signal，但作者发现 conditioning on 正解会让 teacher 系统性地偏向更短、更直接的 style token（style 平均 |e| = 0.263 vs task = 0.083），训练要么 length 爆炸要么坍缩。RLCSD 同时在 correct hint 和 wrong hint 下算 e_c, e_w，相减得到 e_ctr，对称模板下 style 部分被 cancel，剩下的是 task-bearing 信号。

## 谱系位置

vs OPSD/SDPO/SRPO（一边倒只用 positive privileged context）和 RLSD（同样用 sampled-token modulation 但只有 e_c）：第一次显式做 correct/wrong hint 的 symmetric contrast 来抵消 style drift，并加上 K-marginalized negative hints + 排除 target rollout 自己当 hint（避免 self-referential collapse）这两个 refinement。

## Method

正负 hint 都从同 group 的 student rollouts 里取（数据集少有反例）；symmetric prompt template 让 style component 在 e_c − e_w 中可消去；e_ctr 经 soft normalize + sign-preserving clamp 后作为 per-token modulation 乘到 GRPO 的 A_ORM 上（modulation only, 不反转 sign）；two-path loss aggregation；实验用 Qwen3 1.7B/4B/8B + Olmo-3-7B-Think，AMC23/AIME24/AIME25 + K&K (id/ood-easy/medium/hard)，对比 GRPO/OPSD/SDPO/SRPO/RLSD。

## 优缺点

- ✅ [作者 ack §3.1]: correct/wrong hint 对照能抵消 privilege-induced style drift，保留 task-bearing signal。
- ⚠️ [作者 ack §3]: 需要同 group 中可用的 correct/wrong rollouts；当采样缺少反例时负 hint 构造会变弱。

## headline number

- Qwen3-8B math+logic seven-benchmark average +14.4 over GRPO/OPSD/SDPO/SRPO/RLSD（§4.2 Table 1）

## Evidence

- "+14.4 avg / +21 (KK-ood-hard) / +20 (KK-ood-medium) on Qwen3-8B" 来自 §4.2 Table 1
- "style 0.263 vs task 0.083 per-rollout |e_c,t|" 来自 §3.1 Figure 2
- code release at github.com/THU-BPM/RLCSD 来自 §1 paper header
- decomposition + cross-model OPD 推广 来自 §4.5

<!-- pdf: §3 Mechanism / §4.2 Experiments / §4.5 Analysis -->
