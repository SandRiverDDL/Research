---
type: paper
node_id: paper:sang2026_composing_what_each
title: "Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation through Teacher-Relative Shifts"
authors: ["Hejian Sang", "Zhengze Zhou", "Shayan Mohajer Hamidi", "Xiaomin Li", "Rohit Jain", "Alborz Geramifard"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2610.10460"
  doi: null
  s2: null
tags: ["core", "target-construction", "reference"]
added: 2026-10-15T03:47:15Z
---

# Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation through Teacher-Relative Shifts

## One-line thesis

Δ-MOPD 将 teacher 相对各自 precursor 的 logit shift 重新锚定到冻结 student initialization，替代 endpoint target。

## Problem / Gap

【作者问题】endpoint 同时携带 post-training 增益和 inherited base pull，组合时可能扭曲目标。

## Method

【事实】z_C=z_A+Σ_selected(z_Ti−z_Bi)，一次 softmax；student prefixes 上 reverse-KL。同域用全部 teachers，跨域路由用一个，固定 selection 比较 endpoint；B_i=A 时两目标完全相同（§2–3 Eq.2–6）。

## Key Results

【作者报告】BigMath 三 teacher composition、step100 greedy：Math macro 29.39→33.50，five-suite 24.24→26.19（Table 2）。两 phased orders 的 five-suite order gap 10.50→6.42（Table 3）。单 teacher acquisition matched capability allocated H100-hours 减 34.7%，但每 update 慢 27.3%（App.E.1，另一配置）。

## Assumptions

每 teacher 的准确 precursor、兼容 tokenizer 或显式 projection、冻结 student anchor。

## Limitations / Failure Modes

异源主要是同蒸馏 lineage 不同 scale。H100-hours 包含 forward/rollout/优化，排除 held-out eval；与 Table 2 的 H200 scaling run 不可混算。50-step checkpoint 间隔使 first-passage cost 是上界（§9/App.E）。

## Reusable Ingredients

【解释】selection 与 target construction 的正交比较、same-origin reduction。

## Open Questions

【开放问题】没有 precursor 时能否可靠估计 post-training shift？更广 teacher families 的 inherited pull 是否类似？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心 target 构造与组合方法；不把已有 shift 构造直接当新选题。

读取：2026-10-15，2610.10460v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2610.10460v1#S3)；[元数据](https://arxiv.org/abs/2610.10460v1)。发现来源：seed-sources.md。未保存本地 PDF。
