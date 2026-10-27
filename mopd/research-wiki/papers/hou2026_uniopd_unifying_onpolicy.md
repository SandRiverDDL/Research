---
type: paper
node_id: paper:hou2026_uniopd_unifying_onpolicy
title: "Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe"
authors: ["Wenjin Hou", "Shangpin Peng", "Weinong Wang", "Zheng Ruan", "Yue Zhang", "Zhenglin Zhou", "Mingqi Gao", "Yifei Chen", "Kaiqi Wang", "Hongming Yang", "Chengquan Zhang", "Zhuotao Tian", "Han Hu", "Yi Yang", "Fei Wu", "Hehe Fan"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2605.03677"
  doi: null
  s2: null
tags: ["core", "recipe", "verification"]
added: 2026-10-15T03:47:15Z
---

# Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe

## One-line thesis

Uni-OPD 同时改善 student 探索与 teacher outcome 排序的一致性，并验证多 teacher 文本/多模态整合。

## Problem / Gap

【作者问题】student 探索不足和 teacher supervision 不符合 outcome 排序限制 OPD。

## Method

【事实】离线增采中等难度 prompt，在线平衡正确/错误 trajectories；最差正确 return−最好错误 return 低于 δ 时 mask 或给正确轨迹 δ−margin 修正（§3）。

## Key Results

【作者报告】多 teacher Qwen3-4B math48.5 vs OPD47.0、code63.6 vs60.2（Table 1）；VL4B multi-teacher math61.0 vs57.9（Table 2）。在线组件 <1% iteration wall-clock（App.C.6）。

## Assumptions

outcome 可验证，组内有正负样本，能够做离线 difficulty sampling。

## Limitations / Failure Modes

<1% 不涵盖离线 difficulty 数据准备；更大模型和长程 agents 未验证（§5）。

## Reusable Ingredients

【解释】outcome margin 与 teacher log-prob return 的一致性检查。

## Open Questions

【开放问题】没有可靠 outcome verifier 时该 recipe 哪些部分仍有效？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增直接相关 recipe；DN-MOPD 明确复用其实现。

读取：2026-10-15，2605.03677v2 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2605.03677v2#S3)；[元数据](https://arxiv.org/abs/2605.03677v2)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
