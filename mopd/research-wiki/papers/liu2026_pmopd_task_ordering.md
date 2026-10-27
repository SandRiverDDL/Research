---
type: paper
node_id: paper:liu2026_pmopd_task_ordering
title: "PMOPD: Task Ordering, Cycling, and Parameter-Update Subspace Protection in Multi-Teacher On-Policy Distillation"
authors: ["Youzhi Liu", "Ruobing Zheng", "Boyuan Tong", "Tianqi Li", "Pingqi Li", "Hanbo Bi", "Yi Yuan", "Jingdong Chen"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.34605"
  doi: null
  s2: null
tags: ["core", "update-protection"]
added: 2026-10-15T03:47:15Z
---

# PMOPD: Task Ordering, Cycling, and Parameter-Update Subspace Protection in Multi-Teacher On-Policy Distillation

## One-line thesis

PMOPD 结合 task ordering/cycling 与累计更新子空间投影，保护已学习领域能力。

## Problem / Gap

【作者问题】多个 teacher 对共享参数更新产生 capability seesaw。

## Method

【事实】task blocks 内做 reverse-KL；从二维参数矩阵的 block cumulative displacement 提取 rank-16 right-singular basis，QR 合并 memory；投影梯度 G−GMMᵀ 和 Adafactor update U−UMMᵀ。每 cycle 清空重建 memory；conflict probe 选顺序（§4 Eq.4–12）。

## Key Results

【作者报告】三域、每域 600 prompts、四 cycles、三 runs：Qwen2.5-7B Avg 66.97 vs MOPD 64.43；Llama-3.1-8B 41.04 vs 38.95（Tables 2–3）。同 schedule ablation：无投影 63.85、梯度投影 66.22、再投影 optimizer update 66.97（Table 4）。

## Assumptions

共同初始化 teachers、任务可分 block、矩阵参数及可维护低秩 memory。

## Limitations / Failure Modes

评测为 NuminaMath/orca_math、CommonsenseQA、APPS，非通用全能力整合。未找到完整 SVD/probe overhead 量化；排序和 cycles 是论文设置，非项目约束。

## Reusable Ingredients

【解释】累计 realized update memory、同 schedule 的梯度与 optimizer-update 投影分离消融。

## Open Questions

【开放问题】在更强的 mixed-batch baseline 下，保护收益能否覆盖 SVD、memory 和顺序搜索成本？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心更新保护方法；不把其诊断直接当作所有 MOPD 的统一 failure mode。

读取：2026-10-15，2609.34605v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.34605v1#S4)；[元数据](https://arxiv.org/abs/2609.34605v1)。发现来源：seed-sources.md。未保存本地 PDF。
