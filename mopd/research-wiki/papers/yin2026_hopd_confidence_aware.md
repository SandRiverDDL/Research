---
type: paper
node_id: paper:yin2026_hopd_confidence_aware
title: "H-OPD: Confidence Aware Heterogeneous Multi-Teacher Multimodal On-policy Distillation"
authors: ["Qixiang Yin", "Huanjin Yao", "Yuchen Cai", "Jianghao Chen", "Ziyi Wang", "Fei Su", "Zhicheng Zhao"]
year: 2026
venue: "arXiv; authors report EMNLP 2026 (not independently verified)"
external_ids:
  arxiv: "2607.02592"
  doi: null
  s2: null
tags: ["core", "multimodal", "token-routing"]
added: 2026-10-15T03:47:15Z
---

# H-OPD: Confidence Aware Heterogeneous Multi-Teacher Multimodal On-policy Distillation

## One-line thesis

H-OPD 以逐 token 预测熵融合独立 VL/text teachers，替代静态样本路由。

## Problem / Gap

【作者问题】同一 multimodal trajectory 不同位置对模态专长的需求不同。

## Method

【事实】VL teacher 离线生成 description 供 text teacher；两者评分同一 student prefix，合并 top-k support、缺席 token 补零，负 entropy 经 softmax 形成权重，mixed target 上 reverse-KL（§3.3–3.4 Eq.7–10）。

## Key Results

【作者报告】VL4B+text4B→Qwen3-VL-2B：11 benchmarks Avg53.5 vs单 VL OPD51.1（Table 1）；LogicVista uniform31.3、sample routing42.5、H-OPD49.4（App.C Table 8）。MathVerse-200 best checkpoint GPU-h173.6 vs145.2（Table 5），质量也不同。

## Assumptions

可比较 token distributions、额外 description 与两个 teacher forwards。

## Limitations / Failure Modes

description 质量、截断 entropy 与过度自信限制 proxy（§6）；未测试32B/MoE。非等质量成本数字，不能写成绝对节省算力。

## Reusable Ingredients

【解释】异模态 teacher-pair、uniform/sample/token 三层比较。

## Open Questions

【开放问题】entropy calibration 能否可靠跨模型、跨模态使用？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增核心异构多模态方法；v3 七位作者，arXiv comments 声称 EMNLP2026，未独立核实接收。

读取：2026-10-15，2607.02592v3 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2607.02592v3#S3)；[元数据](https://arxiv.org/abs/2607.02592v3)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
