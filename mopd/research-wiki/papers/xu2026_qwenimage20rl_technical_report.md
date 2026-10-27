---
type: paper
node_id: paper:xu2026_qwenimage20rl_technical_report
title: "Qwen-Image-2.0-RL Technical Report"
authors: ["Yixian Xu", "Kaiyuan Gao", "Yuxiang Chen", "Yilei Chen", "Zecheng Tang", "Zihao Liu", "Zikai Zhou", "Deqing Li", "Hao Meng", "Kuan Cao", "Jiahao Li", "Jie Zhang", "Liang Peng", "Lihan Jiang", "Ningyuan Tang", "Shengming Yin", "Tianhe Wu", "Xiaoyue Chen", "Yan Shu", "Yanran Zhang", "Yi Wang", "Yu Wu", "Yujia Wu", "Zekai Zhang", "Zhendong Wang", "Xiao Xu", "Kun Yan", "Chenfei Wu"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2606.27608"
  doi: null
  s2: null
tags: ["system", "multimodal", "flow"]
added: 2026-10-15T03:47:15Z
---

# Qwen-Image-2.0-RL Technical Report

## One-line thesis

Qwen-Image-2.0-RL 以 student flow trajectories 的 velocity matching 整合 T2I 与 editing 专家。

## Problem / Gap

【作者问题】图像生成和编辑的 task-specialized RL policies 互有退化，需要统一部署。

## Method

【事实】分别 RL 两任务，student 从 base 初始化并保存自己 reverse-ODE 的完整 trajectory；按任务选择 teacher，逐点 velocity MSE，teacher 使用 CFG、student 不用。只激活当前 teacher，其他 CPU offload（§4.3 Eq.14）；完整 pipeline 包含 reward models 与 RL。

## Key Results

【作者报告】整体 pipeline 的 Qwen-Image-Bench Overall55.23→57.84，T2I Elo1115→1193、editing1256→1349（§5/Table 1）。这些包含前置 RL，不能单独归因于 MOPD。§4.3/Fig.3 提供 Mix-RL 对照。

## Assumptions

共享 flow states/velocity representation、任务标签、两冻结 task teachers；需保存 student trajectory。

## Limitations / Failure Modes

系统结果混合 reward modeling、RL 与 OPD，缺少本轮核实的完整 teacher 制备+OPD 成本表；CPU offload 缓解显存但不消除 teacher compute。

## Reusable Ingredients

【解释】连续状态下 student-visited velocity supervision，以及 CFG 兼并到 student 的工程做法。

## Open Questions

【开放问题】更多任务、异 latent spaces 的 teacher 能否用同一轨迹对齐？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增多模态系统证据；loss 为 velocity MSE，不能直接与文本 reverse-KL 数字横比。

读取：2026-10-15，2606.27608v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2606.27608v1#S4.SS3)；[元数据](https://arxiv.org/abs/2606.27608v1)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
