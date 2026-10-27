---
type: paper
node_id: paper:ma2026_mopd_multiteacher_onpolicy
title: "MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training"
authors: ["Wenhan Ma", "Jianyu Wei", "Liang Zhao", "Hailin Zhang", "Bangjun Xiao", "Lei Li", "Qibin Yang", "Bofei Gao", "Yudong Wang", "Rang Li", "Jinhao Dong", "Zhifang Sui", "Fuli Luo"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2606.30406"
  doi: null
  s2: null
tags: ["core", "routed-opd", "recipe"]
added: 2026-10-15T03:47:15Z
---

# MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training

## One-line thesis

独立训练领域 RL teachers，再在 student 自采样轨迹上做 domain-routed reverse-KL 蒸馏，实现能力整合。

## Problem / Gap

【作者问题】联合或串行多域 RL 存在能力互扰，离线蒸馏受 exposure bias 影响。

## Method

【事实】共同 SFT 初始化；冻结各领域 teacher，按 prompt domain 选择 teacher，在 student prefixes 上提供监督。PG 实现采用 stopgrad(log π_teacher−log π_student)，默认双侧 clip ±5；teacher-top-64 generalized KL 含截断修正项。见 §3.1–3.3、Eq.1–5、App.A。

## Key Results

【作者报告】Qwen3-30B-A3B 的 Math/IF/SWE normalized headroom recovery 为 0.9373，Mix-RL 为 0.8818；SWE-bench Verified 50.40%，对应 specialist 51.20%（Table 2）。309B MiMo-V2-Flash 的 AIME25 为 94.1%，teacher 93.9%（Table 3）。

## Assumptions

领域标签、teacher 概率访问、共同初始化与兼容 tokenizer。

## Limitations / Failure Modes

§4.4.2 中换用更强但异源的 math teacher 后训练不稳定，不能外推至任意 teacher pool。§3.3 的低 wall-clock overhead 依赖异步 prefill 部署，仍有 teacher compute。

## Reusable Ingredients

【解释】共同初始化、独立 RL teachers、routed student rollouts 可作为整合方法的基本对照。

## Open Questions

【开放问题】异源 teachers 的兼容性和 teacher 制备在总成本中的占比，仍需独立核算。

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心起点；与单 teacher OPD 背景分开。本页仅定向核查方法和主要实验。

读取：2026-10-15，2606.30406v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2606.30406v1#S3)；[元数据](https://arxiv.org/abs/2606.30406v1)。发现来源：seed-sources.md。未保存本地 PDF。
