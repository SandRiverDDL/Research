---
type: paper
node_id: paper:fu2026_rethinking_onpolicy_distillation
title: "Rethinking On-Policy Distillation of Large Language Models II: One Training Example"
authors: ["Zixuan Fu", "Bingxiang He", "Yuxin Zuo", "Haohuan Huang", "Jinqian Zhang", "Ruhang Xiao", "Cheng Qian", "Qinyu Luo", "Huan-ang Gao", "Yudong Wang", "Zhiyuan Liu", "Ning Ding", "Chaojun Xiao"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.04172"
  doi: null
  s2: null
tags: ["evidence", "data"]
added: 2026-10-15T03:47:15Z
---

# Rethinking On-Policy Distillation of Large Language Models II: One Training Example

## One-line thesis

少量不同语义 queries 配合不断刷新的 student rollouts，可在固定预算下匹配部分全数据 MOPD。

## Problem / Gap

【作者问题】OPD 缺少问题数据，还是缺少有效吸收 teacher 监督的训练机制？

## Method

【事实】one-shot 反复同 query、每次新 rollout；16-shot 按 BGE-M3 semantic clusters 取代表。1.5B student、JustRL/math、Nemotron/code、UltraData-IF 三 teachers，固定 routing/sampled-token OPD（§6）。

## Key Results

【作者报告】同300 steps/rollout/optimization budget，1-shot/domain、16-shot/domain、full-data Avg50.1/52.9/52.8，base43.5（Fig.11）。101% 指 full-data gain 的恢复比例，非准确率。

## Assumptions

三领域可标注、teacher/student 概率兼容、持续重新 rollout。

## Limitations / Failure Modes

少 query 未减少训练计算。State coverage 是 teacher hidden states 的 PCA/Kmeans cluster occupancy proxy，不是精确 prefix coverage；单 teacher 71.5% coverage 不可当 MOPD 结果（§4/App.D）。

## Reusable Ingredients

【解释】固定 rollout budget 下 query-count 对照和 coverage proxy 的适用边界。

## Open Questions

【开放问题】吸收速度的具体因果机制是什么？复杂组合能力是否仍只需少量 queries？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增 MOPD data dependence 证据；与 DF-OPD 的 teacher 自生成问题设定区分。

读取：2026-10-15，2609.04172v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.04172v1#S6)；[元数据](https://arxiv.org/abs/2609.04172v1)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
