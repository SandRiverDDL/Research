---
type: paper
node_id: paper:qin2026_videomopd_multiteacher_onpolicy
title: "Video-MOPD: Multi-Teacher On-Policy Distillation for Video Understanding"
authors: ["Zhenxin Qin", "Peng Shi", "Cong Han", "Yinlong Qian", "Zequn Jie", "Lin Ma"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.09300"
  doi: null
  s2: null
tags: ["core", "multimodal", "filtering"]
added: 2026-10-15T03:47:15Z
---

# Video-MOPD: Multi-Teacher On-Policy Distillation for Video Understanding

## One-line thesis

Video-MOPD 以视频、时序定位、STEM 独立 experts 做领域路由蒸馏，并离线筛选可靠高差距数据。

## Problem / Gap

【作者问题】统一视频理解模型需要整合不同视觉 RL 专长。

## Method

【事实】三只 Qwen3-VL-8B experts 独立 RL；RAIS 让 teacher/initial student 每候选各采 K 次，先保留 teacher 全对，再优先 empirical accuracy gap 大的样本。按 Video/Image/Temporal 单 teacher 路由，默认 sampled-token PG reverse-KL（§3.2–3.3/App.D）。

## Key Results

【作者报告】8B 七 video benchmark Avg69.12 vs base63.68/参数平均67.28；temporal IoU61.98 vs base52.78/expert62.32（Table 1）。7493 samples、2epochs/178updates、32A800，仅训练 language model（App.A）。

## Assumptions

任务标签、task-specific correctness verifiers、离线2K候选 generations。

## Limitations / Failure Modes

本轮未核实 K 的具体值和 RAIS 单独增益消融，不能归因总提升于筛样。Avg 混合 IoU/native/judged metrics；长视频仍未来工作（§6）。

## Reusable Ingredients

【解释】initial empirical gap 的离线筛样与训练中 log-prob weighting 分开。

## Open Questions

【开放问题】筛样成本和 coverage 损失能否被更少训练步骤补偿？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增核心视觉 MOPD；三独立 experts 而非三个 context views。

读取：2026-10-15，2609.09300v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.09300v1#S3)；[元数据](https://arxiv.org/abs/2609.09300v1)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
