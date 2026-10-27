---
type: paper
node_id: paper:ma2026_one_student_many
title: "One Student, Many Teachers: Multi-Task On-Policy Distillation via Soft-Prompt Privileged Context"
authors: ["Yingzi Ma", "Zichen Zhu", "Ming Jiang", "Chaowei Xiao"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2607.18293"
  doi: null
  s2: null
tags: ["adjacent", "teacher-construction", "soft-prompt"]
added: 2026-10-15T03:47:15Z
---

# One Student, Many Teachers: Multi-Task On-Policy Distillation via Soft-Prompt Privileged Context

## One-line thesis

PromptSD 在共享冻结 backbone 上学习 task-specific soft-prefix teachers，再将其通过 OPD 压缩到无 prefix student。

## Problem / Gap

【作者问题】input-side privileged context 可能引发 post-hoc rationalization，weight-tuned teachers 还存在 drift/forgetting 与训练存储开销。

## Method

【事实】各任务(x,y_gold)上只训练 soft prefix 的 NLL，固定后按 task tag 单 teacher 路由；student 自采样、teacher 多看该 prefix，reverse-KL 训练一个 student；部署丢弃 prefix（§4 Eq.5–10）。

## Key Results

【作者报告】1.7B Science/Tooluse/Biology/Math target Avg56.2 vs multi-task SFT43.7/OPD-LoRA47.5，held-out utility51.7 vs base50.4（Table 2）。L400 teacher trainable参数 .82M=.048%（App.C Table 8）。

## Assumptions

监督数据可用、task tags、共享冻结 backbone 和任务特定 learned prefixes。

## Limitations / Failure Modes

不是独立 full-weight experts；小模型四任务。完整 backbone forward 仍需要，训练时间可接近 LoRA/FFT，每次 teacher 增加400/800 prefix位置（App.C/§7）。

## Reusable Ingredients

【解释】teacher 可用轻量参数而非完整 checkpoints 构造。

## Open Questions

【开放问题】learned prefixes 能否承载强 RL experts 的新能力，而非仅增强已有能力？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

邻近 teacher topology/低制备参数工作；不同于 AVSD 样本级 GT views 聚合。

读取：2026-10-15，2607.18293v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2607.18293v1#S4)；[元数据](https://arxiv.org/abs/2607.18293v1)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
