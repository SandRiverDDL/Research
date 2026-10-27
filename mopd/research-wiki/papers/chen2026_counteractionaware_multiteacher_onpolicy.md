---
type: paper
node_id: paper:chen2026_counteractionaware_multiteacher_onpolicy
title: "Counteraction-Aware Multi-Teacher On-Policy Distillation for General Capability Recovery with Domain Preservation"
authors: ["Tianlei Chen", "Jiao Ou", "Ziyuan Liu", "Ruiming Tang", "Jian Liang", "Han Li"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2605.27115"
  doi: null
  s2: null
tags: ["core", "capability-preservation"]
added: 2026-10-15T03:47:15Z
---

# Counteraction-Aware Multi-Teacher On-Policy Distillation for General Capability Recovery with Domain Preservation

## One-line thesis

CaMOPD 用交替更新、gap-based selection 与监督缩放，恢复 general capability 并保留 domain specialization。

## Problem / Gap

【作者问题】specialization 后恢复一般能力，general teacher 原始分布未知；混合梯度抵消及低需求样本稀释监督。

## Method

【事实】general model 作 T_g，specialized initialization 同时作固定 T_d。sampled-token log-prob gap 经 detached importance-weighted loss；默认 3 general updates 后 1 domain update。general 按绝对 gap、domain 按正 gap，选累计 score mass 前缀，再以 2:1 advantage scale 更新（§3 Eq.1–7）。

## Key Results

【作者报告】4B role-play：general avg 49.07 vs Vanilla 43.78/Relaxed OPD 45.26，domain avg 45.00 vs teacher 41.08（Table 1）。8B medical：general 45.84 vs Vanilla 42.29，medical 54.71 vs teacher 54.54（Table 2）。

## Assumptions

proxy general prompts、specialization pipeline 的 domain prompts、teacher token log-probs。

## Limitations / Failure Modes

仅两个 4B/8B specialization 设置；回答 recovery/retention，不直接证明广泛组合泛化。selection 位于 rollout/scoring 后，选中率不能等同端到端 compute 节约。

## Reusable Ingredients

【解释】recovery/preservation 两 branch 与 selection/scaling/decoupling 的逐项消融。

## Open Questions

【开放问题】多个独立领域专家同时整合时，交替 schedule 和 selection 是否仍有效？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心 general recovery 方法；与 SF-MOPD 的 preservation 目标相关，干预层不同。

读取：2026-10-15，2605.27115v2 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2605.27115v2#S3)；[元数据](https://arxiv.org/abs/2605.27115v2)。发现来源：seed-sources.md。未保存本地 PDF。
