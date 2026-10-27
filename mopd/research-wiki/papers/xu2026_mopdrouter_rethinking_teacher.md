---
type: paper
node_id: paper:xu2026_mopdrouter_rethinking_teacher
title: "MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation"
authors: ["Tianze Xu", "Yanzhao Zheng", "Zhentao Zhang", "Yuanqiang Yu", "Chao Ma", "Jihuai Zhu", "Lelun Wu", "Lyumanshan Ye", "Pengfei Liu", "Baohua Dong", "Hangcheng Zhu", "Ruohui Huang", "Gang Yu"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.30837"
  doi: null
  s2: null
tags: ["core", "token-routing", "reference"]
added: 2026-10-15T03:47:15Z
---

# MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation

## One-line thesis

MOPD-Router 用 teacher 专长方向与其对 student 的纠正方向对齐度，分配无标签 token 级 OPD 信号。

## Problem / Gap

【作者问题】固定领域路由不能利用未标注 mixture 与跨域互补监督。

## Method

【事实】每 token 聚合各 teacher sampled-token log-ratio advantage，PPO-style 更新。ExpertAlign 在 student top-k 支持比较 e=log teacher−log base 与 d=log teacher−log student，正对齐 teacher 被保留并按 cosine 加权；另比较 Entropy/Novelty metrics（§3 Eq.1/4/10–11）。k=1 有单独 product 实现。

## Key Results

【作者报告】Qwen3-4B 无标签九 benchmark Overall：Mean47.88→ExpertAlign53.76（Table 1）；有标签数据但不用标签：standard MOPD50.63→54.58（Table 2）。未把这些当三域等权 macro。

## Assumptions

共同 pre-RL base、兼容概率支持、每位置查询整个 teacher pool。

## Limitations / Failure Modes

对齐是 proxy，不是 outcome 认证。多个 teacher retained 不意味着少 scoring；研究主要 Qwen3 的 same-size/strong-to-weak，k=32 相对 plateau 表现下降（App.5）。

## Reusable Ingredients

【解释】Entropy/Novelty/ExpertAlign 同接口比较，uniform positive selection 与 cosine weighting 分离。

## Open Questions

【开放问题】异源 reference 与更多 teachers 下，alignment 与最佳监督的相关性如何？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增核心 routing 方法；与 TrustMOPD 同属 reference-based allocation，但指标和loss实现不同。

读取：2026-10-15，2609.30837v2 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.30837v2#S3)；[元数据](https://arxiv.org/abs/2609.30837v2)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
