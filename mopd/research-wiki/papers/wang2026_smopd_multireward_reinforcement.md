---
type: paper
node_id: paper:wang2026_smopd_multireward_reinforcement
title: "SMOPD: Multi-Reward Reinforcement Learning via Specialize-and-Merge Online Policy Distillation"
authors: ["Wen Wang", "Jiahua Bao", "Tu Yongsiqi", "Yihao Liu", "Haotian Zhou", "Haoxuan Ma", "Mengyu Zhou", "Wenkui Fan", "Junwei He", "Xiaoxi Jiang", "Guanjun Jiang"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2608.03092"
  doi: null
  s2: null
tags: ["core", "reward-specialists", "aggregation"]
added: 2026-10-15T03:47:15Z
---

# SMOPD: Multi-Reward Reinforcement Learning via Specialize-and-Merge Online Policy Distillation

## One-line thesis

SMOPD 训练 reward-priority specialists，再以 arithmetic teacher mixture 的 forward-KL 和 GDPO anchor 整合。

## Problem / Gap

【作者问题】同一 prompt 上多个 reward 的冲突不能用 domain routing 分离。

## Method

【事实】先用 .9/.1 等 reward-priority GDPO 训练 experts，再在 student trajectories 均匀混合 teacher distributions，用 component-top16 近似 target；forward-KL+equal-weight GDPO，默认 λ=1（§2.2–3）。

## Key Results

【作者报告】Qwen2.5-1.5B tool calling：RLLA2.740 vs GDPO1.849，format97.5% vs8.8%（Table 1）；7B conflicting-reward Overall5.646 vs5.498（Table 2）。

## Assumptions

可评 reward、全部 teacher scoring、兼容 token distributions；额外多 teacher 训练。

## Limitations / Failure Modes

两个 reward settings；API-Bank 用 LLM-judge 救回 exact-match failures，须保留 metric 条件。未核得完整 wall-clock；distillation 仍带在线 reward optimization。

## Reusable Ingredients

【解释】同 prompt reward specialists、arithmetic mixture 和无标签 domain routing 分开考虑。

## Open Questions

【开放问题】expert reward 强度如何影响目标冲突与超越单一 teacher 的空间？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增核心同域多 reward 整合；forward-KL 与 reverse-KL 的 target geometry 不同。

读取：2026-10-15，2608.03092v2 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2608.03092v2#S3)；[元数据](https://arxiv.org/abs/2608.03092v2)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
