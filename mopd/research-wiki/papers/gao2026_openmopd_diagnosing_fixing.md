---
type: paper
node_id: paper:gao2026_openmopd_diagnosing_fixing
title: "Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation"
authors: ["Huan-ang Gao", "Haohan Chi", "Yong Yan", "Shiyuan Feng", "Hanlin Wu", "Zheng Jiang", "Bingxiang He", "Wei-Ying Ma", "Ya-Qin Zhang", "Hao Zhou"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2608.19098"
  doi: null
  s2: null
tags: ["core", "recipe", "budget"]
added: 2026-10-15T03:47:15Z
---

# Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation

## One-line thesis

Open-MOPD 以开放三域 recipe 诊断 token 预算失衡，并结合 token-share、gap-aware allocation 和 reward refresh 改善整合。

## Problem / Gap

【作者问题】即使 oracle domain routing，单 student 仍落后于逐域 RouteOPD，IF 尤其明显。

## Method

【事实】student-top-16 log-ratio 经 student 概率重归一化形成 PPO position reward。w_share=g*/s_tok，再乘 clipped gap factor 并保持 token-weighted 总权重为 1；inner updates 重算 student reward、缓存 teacher。见 §2.1、§4 Eq.1–4/8–10。Refresh 不更新 rollout states。

## Key Results

【作者报告】SmolLM3-3B 的 Math/Code/IF Total 由 naive 28.05 升至 31.24；以 SFT→RouteRL 为分母的 recovery 35.6%→83.4%（Table 2）。IF 占约 20% prompts、1% gradient tokens（Fig.3）。

## Assumptions

共同 SFT、领域标签、可缓存 teacher scoring；主要 testbed 是 3B 三领域。

## Limitations / Failure Modes

§3.2 的 token-disagreement metric 中 c_t>1 nat 占 0.62%；这不能排除参数梯度冲突。摘要措辞更强，本页采用 HTML 及同版 PDF 正文限定。完整端到端成本须计 teacher RL 与 refresh。

## Reusable Ingredients

【解释】可复用开放 checkpoints、RouteOPD 上界参照以及 prompt/token/response 权重分解。

## Open Questions

【开放问题】长度差异较小、teacher 异源或规模更大时，预算修正是否仍为主要收益来源？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心可复现 recipe；用于识别预算不足和能力干扰的证据边界。HTML 主读，同版 PDF 局部核对 §3.2/Table 2。

读取：2026-10-15，2608.19098v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2608.19098v1#S4)；[元数据](https://arxiv.org/abs/2608.19098v1)。发现来源：seed-sources.md。未保存本地 PDF。
