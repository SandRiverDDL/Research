---
type: paper
node_id: paper:xie2026_rethinking_selfdistillation_multiteacher
title: "Rethinking Self-Distillation for Multi-Teacher Capability Merging"
authors: ["Roy Xie", "Dan Friedman", "Feng Nan", "Yukun Huang", "Zhichao Xu", "Chengjiu Zhang", "Jun Xu", "Manaal Faruqui", "Vivek Rathod", "Bhuwan Dhingra"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2610.04272"
  doi: null
  s2: null
tags: ["evidence", "fair-baselines", "cost"]
added: 2026-10-15T03:47:15Z
---

# Rethinking Self-Distillation for Multi-Teacher Capability Merging

## One-line thesis

独立调参和高质量 teacher 数据下，SFT/Soft-KD 可匹配部分 MOPD ID recovery，OOD retention 与运行成本仍有差异。

## Problem / Gap

【作者问题】on-policy 优势是否来自公平不足的 off-policy baseline，完整 student interaction 的收益和成本是什么？

## Method

【事实】共享 prompts/teachers，分别调 LR；比较 teacher-token SFT、teacher-context forward-KL Soft-KD、固定 teacher history 的 Offline-MOPD，以及完整 student interaction 的 online MOPD。四模型、两个三 teacher compositions（§3 Eq.1–6/§4）。

## Key Results

【作者报告】Qwen3-8B MIA 三 seeds ID recovery：SFT 98.2±5.6%、MOPD 97.9±1.8%（Table 1）。三 Agent ID 为 99.0±1.7%/99.3±1.0%，OOD delta 为 −2.0±.2/+0.6±.4 pp。8 B200 完整运行：MIA MOPD/SFT 383.32/25.90 GPU-h，Agent 415.80/18.00（Tables 18–19）。

## Assumptions

有 rejection-sampled teacher corpus、各方法独立 LR tuning；主模型 1.7B–8B。

## Limitations / Failure Modes

运行成本排除一次性 teacher trajectory generation，也不含全部 tuning search。并未证明任意规模、teacher family 或数据质量下 off-policy 必然等价（App.H）。

## Reusable Ingredients

【解释】强 SFT/Soft-KD、offline/on-policy history 分解，以及 ID/OOD/成本同时报告。

## Open Questions

【开放问题】更多样 teacher pool 或真正组合任务上，公平调参后的 on-policy 独特收益是否扩大？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

直接证据与公平对照，限制其他方法仅对 vanilla MOPD 增益的归因；此文不是新 routing 方法。

读取：2026-10-15，2610.04272v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2610.04272v1#S3)；[元数据](https://arxiv.org/abs/2610.04272v1)。发现来源：seed-sources.md。未保存本地 PDF。
