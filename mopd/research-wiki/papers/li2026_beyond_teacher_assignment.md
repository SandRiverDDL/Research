---
type: paper
node_id: paper:li2026_beyond_teacher_assignment
title: "Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation"
authors: ["Xin Li", "Hao Jiang", "Xin Gao", "Annan Wang", "Yuchen Xie", "Jinghao Guo", "Xingwei Qu", "Yichi Zhang", "Chau Yuen"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.35347"
  doi: null
  s2: null
tags: ["core", "feedback-scale"]
added: 2026-10-15T03:47:15Z
---

# Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation

## One-line thesis

DN-MOPD 保持领域路由，以 pooled/domain feedback dispersion 比值归一化各域蒸馏信号。

## Problem / Gap

【作者问题】正确 teacher assignment 并不保证反馈尺度平衡。

## Method

【事实】从 cached teacher−rollout-student log-ratio 的 valid tokens 计算 population std，w_d=clip(σ_all/σ_d,0.25,4)。当前 actor advantage 乘 detached 权重后进入 clipped loss，先每 response token-average、再 response-average。见 §2、Algorithm 1。

## Key Results

【作者报告】Qwen3.5-9B/4B/2B，80 updates、16K eval，六任务 Total 相对 Label 增益 +1.17/+2.24/+2.36 pp（App.C Table C.4）；三 student seeds 平均增益 +1.12/+1.97/+2.34 pp（Table C.10）。初始 4B IF 梯度贡献 94%→64%（Table D.3）。

## Assumptions

领域标签、batch 中可分域统计、同族 teacher pool；无额外 teacher call。

## Limitations / Failure Modes

固定近似权重在 9B/4B 可比；早期 Qwen3-4B 无明确收益。IF 常触及 0.25 下界；dispersion 不等于 teacher quality，也不保证梯度范数相等（§5/App.E.2）。

## Reusable Ingredients

【解释】基于已有 log-ratios 的尺度校准，以及固定权重对照。

## Open Questions

【开放问题】收益来自动态校准还是稳定的领域重加权？跨 teacher pool 是否成立？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心反馈尺度方法；与 Open-MOPD 的 mean-gap allocation 不同，应单独比较。

读取：2026-10-15，2609.35347v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.35347v1#S2)；[元数据](https://arxiv.org/abs/2609.35347v1)。发现来源：seed-sources.md。未保存本地 PDF。
