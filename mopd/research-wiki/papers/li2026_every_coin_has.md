---
type: paper
node_id: paper:li2026_every_coin_has
title: "Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy Distillation of Large Language Models"
authors: ["Zhaoyi Li", "Deyang Kong", "Yuan Wei", "Evan Yang", "Ranran Shen", "Mahardika Krisna Ihsani", "Ming Yang", "Wei Zhang", "Chuan Hao", "Jian Yang", "Ran Tao", "Bryan Dai", "Shikun Zhang", "Wei Ye", "Ying Wei", "Defu Lian"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2608.16647"
  doi: null
  s2: null
tags: ["evidence", "interference", "reference"]
added: 2026-10-15T03:47:15Z
---

# Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy Distillation of Large Language Models

## One-line thesis

OPD 可跨 prompt 域传递 teacher 偏好，固定 domain routing 并不能隔离 teacher 对其他能力的影响。

## Problem / Gap

【作者问题】泛化与能力 seesaw 对数据域、语言、horizon 和 teacher origin 有何依赖？

## Method

【事实】sampled-token PG OPD；固定总量改变 teacher/domain mixture，交换 teacher-task assignment，并用 cascaded OPD 分离时间影响（§2/4）。

## Key Results

【作者报告】1.5B、step200 五 math benchmark Avg@K：JustRL教math时 J/N=25/8、1/1、2/25 得19.6/19.1/17.4%；JustRL仅教science/IF、J/N=25/0 仍17.5%，balanced15.8%（App.C.4 Table 6）。

## Assumptions

两 teacher、固定路由、最多200 steps，长度 cap40K–96K。

## Limitations / Failure Modes

Avg@K 非 pass@K；没有统一成本匹配。Origin→whole-policy alignment 是解释，非因果保证；未验证大 teacher pool/adaptive routing。

## Reusable Ingredients

【解释】交换 teacher-domain assignment、固定总 prompts 的 mixture 对照。

## Open Questions

【开放问题】能否把有益跨域泛化与 inherited-base pull 分离？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增直接干扰证据；Δ-MOPD 明确引用本篇。

读取：2026-10-15，2608.16647v2 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2608.16647v2#S4)；[元数据](https://arxiv.org/abs/2608.16647v2)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
