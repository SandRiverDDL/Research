---
title: "Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation"
authors: [Yecheng Wu, Song Han, Han Cai]
org: nvidia
year: 2026
venue: arxiv
arxiv_id: 2604.13010
url: https://arxiv.org/abs/2604.13010
zotero_key:
confidence: 2
open_source: yes
verified: r

addresses:
  - sgo-generation-cost
  - teacher-staleness

decisions:
  rollout: offline
  loss: advantage
  signal: logit
  iteration: one-shot
  filter: none
  extra: none
---

> **一句话**：offline OPD 的 teacher consistency 约束路线。

## 核心做法

OPD 有两个 teacher：SFT 生成轨迹的和 OPD 打分的。**Teacher consistency** 要求二者同一模型；违反则 importance weight w=π_θ/π_ref 与 π_T 不对齐 → gradient bias（offline 更严重）。满足后可证 J_off 与 J_on 同一最优点 + 梯度差有界 + 隐式正则防 drift（§3.2 Thm 1-3）。

## 谱系位置

- vs **TAID**（同为 offline rollout）：本文给出 teacher consistency 的理论充要条件，TAID 无此分析。
- vs **MiniLLM/GKD**（online OPD）：指出 SFT-OPD teacher mismatch 是此前被忽略的设计 bug。

## Method

## 优缺点

- ✅ [作者 ack §3.2]: 明确 SFT teacher 与 OPD scoring teacher 必须一致，否则 offline objective 出现 bias。
- ⚠️ [作者 ack §3.2]: 适用前提是 teacher consistency 成立；不满足时离线复用 log-prob 会放大 mismatch。

## headline number

- 4× efficiency and Qwen3-8B AIME 2024 69.9% with 30 GPU hours（§1 Figure 1）

① SFT：π_T 生成轨迹 → π_ref；② 预算：π_ref 采样，π_T **一次**打分存 D_OPD；③ 训练：J_off = E_{x∼π_ref}[ΣA_t(θ)]，全程无 live teacher server。支持 MoE（单节点 8×H100）。

## Evidence

- 4× 效率 + 69.9% AIME 2024：§1 Figure 1（Qwen3-8B-Base, 30 GPU hours）
- MoE 71.0% AIME / 60.8% LCB-v5：§1
- Bias 证明：§3.2 Proposition 1 + Theorem 1

<!-- pdf: §1 Figure 1 / §3.2 Theory / §4 Experiments -->
