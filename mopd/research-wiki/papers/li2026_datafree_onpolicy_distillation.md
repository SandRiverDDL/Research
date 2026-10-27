---
type: paper
node_id: paper:li2026_datafree_onpolicy_distillation
title: "Data-Free On-Policy Distillation: How Far Can We Go Without External Data?"
authors: ["Gengsheng Li", "Mao Zheng", "Mingyang Song", "Jie Sun", "Zeyuan Liu", "Ruiqi Liu", "Tianyu Yang", "Qiyong Zhong", "Haiyun Guo", "Junfeng Fang", "Shiming Xiang", "Jinqiao Wang", "Tat-Seng Chua"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.14193"
  doi: null
  s2: null
tags: ["evidence", "data", "recipe"]
added: 2026-10-15T03:47:15Z
---

# Data-Free On-Policy Distillation: How Far Can We Go Without External Data?

## One-line thesis

teacher 自生成少量固定问题可支持 MOPD 能力恢复，但空 prompt 的成功强依赖 student 行为。

## Problem / Gap

【作者问题】OPD 对外部训练问题的数量与内容究竟依赖多大？

## Method

【事实】teacher 按 domain/topics 预生成固定 question pool，仅提取、格式检查、去重，不以正确性筛选；student 自采样后沿原 routed OPD 更新。多域维持真实数据领域比例；再以 empty prompts 对照（§4.1–5）。

## Key Results

【作者报告】Open-MOPD SmolLM3-3B 三 teacher：真实7458 questions Overall31.18/recovery96.6%，自生成1000为31.31/98.5%，64为30.33/84.8%（Table 1，peak-Overall checkpoint）。空 prompt MOPD 仅保留 full-data gain 的26.7%（§5）。

## Assumptions

领域标签、teacher generation 和 scoring；data-free 指没有外部问题，不指无领域知识或无训练计算。

## Limitations / Failure Modes

少问题不意味着 compute 更少，仍反复 rollout/query。覆盖 teacher/student、模型规模和预算有限（§7）；旧版题名及作者名单有变化，采用 v4。

## Reusable Ingredients

【解释】自生成/真实/空 prompt、固定领域比例的逐项比较。

## Open Questions

【开放问题】组合能力与长程 Agent 场景需要多少问题覆盖？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增 MOPD 数据依赖证据；不能把单 teacher 八问题结果当多 teacher 结果。

读取：2026-10-15，2609.14193v4 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.14193v4#S4)；[元数据](https://arxiv.org/abs/2609.14193v4)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
