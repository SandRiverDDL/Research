---
type: paper
node_id: paper:sun2026_distill_what_you
title: "Distill What You Trust: Reliability-Aware Multi-Teacher On-Policy Distillation"
authors: ["Jie Sun", "Mao Zheng", "Mingyang Song", "Zeyuan Liu", "Gengsheng Li", "Houcheng Jiang", "Yilin Cheng", "Bichuan Feng", "Yuchen Cai", "Junfeng Fang", "Xiang Wang"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.23697"
  doi: null
  s2: null
tags: ["core", "token-routing", "reference"]
added: 2026-10-15T03:47:15Z
---

# Distill What You Trust: Reliability-Aware Multi-Teacher On-Policy Distillation

## One-line thesis

TrustMOPD 用 teacher 相对共同 pre-RL reference 的位移校准无标签 token 级监督分配。

## Problem / Gap

【作者问题】prompt 级单 teacher 路由依赖标签，无法适应生成中能力需求变化。

## Method

【事实】每个 student prefix 上计算 centered log-ratio L2 displacement ρ，以 calibration mean μ_k 校准；(ρ/μ)^γ 归一化为 token weights，加权 reverse-KL，teacher/reference/weights detached。student-top-128 实现；mixed log-target 对应归一化 geometric mean（§3 Eq.2–6、App.B.4）。

## Key Results

【作者报告】SmolLM3-3B、五 seeds：SingleCap Overall 30.04±0.47，label-MOPD 30.18±0.25；MultiCap 30.41±0.60，recovery 98.0%，最强 label-free baseline 54.5%（Table 1）。相对 Uniform measured GPU training/evaluation cost +7.3%（Table 12）。

## Assumptions

共同 pre-RL reference 与一次性 calibration；每 token 要所有 teachers 加 reference scoring。

## Limitations / Failure Modes

Displacement 是 reliability proxy；理论 utility 解释依赖 optimal KL-regularized teachers。MultiCap 为程序化构造，评测 3B/7B，不覆盖异源 teachers（App.F）。

## Reusable Ingredients

【解释】校准前后 reliability、token-level 与 response-level allocation、uniform geometric target 是关键对照。App.C.4.1 的 response-level 对照保持每条 response 的 teacher 总权重、去掉位置变化。

## Open Questions

【开放问题】reference 不共享或 teacher pool 扩大时，proxy 质量和 scoring 成本如何变化？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心无标签 token allocation；不应描述成只调用一个 teacher 的稀疏 router。当前核查 v3（2026-10-11）。

读取：2026-10-15，2609.23697v3 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.23697v3#S3)；[元数据](https://arxiv.org/abs/2609.23697v3)。发现来源：seed-sources.md。未保存本地 PDF。
