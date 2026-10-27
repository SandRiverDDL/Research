---
type: paper
node_id: paper:lu2026_beyond_best_teacher
title: "Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold"
authors: ["Songshuo Lu", "Zhi Chen", "Yaohua Tang"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2607.27770"
  doi: null
  s2: null
tags: ["core", "teacher-construction", "verification"]
added: 2026-10-15T03:47:15Z
---

# Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold

## One-line thesis

RGRPO 逐轮训练互补 teachers，TU-OPD 以质量加权与 winner residual 压缩其可解题并集。

## Problem / Gap

【作者问题】单一 RL teacher 的可解区域有限，已有 teacher pool 聚合没有主动扩大覆盖。

## Method

【事实】每轮从共同初始化训练 teacher，16 次 verifier rollouts 识别已覆盖样本并移除；可靠 teachers 的 success rate 经 softmax 加权 sampled-token reverse-KL；winner top8 相对 peers 的正残差归一化成 CE target，以 .05 系数加入（§3）。

## Key Results

【作者报告】Qwen3-1.7B 七 math Avg@8：best teacher16.37、student16.70、benchmark-wise envelope17.74（Table 1）；同四 teachers uniform/base15.81→quality/base15.99→加 residual16.70（Table 3）。

## Assumptions

可验证任务、重复 teacher rollouts、多轮 RL teacher preparation。

## Limitations / Failure Modes

各 task domain 分别构建四 teachers，不证明同一 student 三域联合整合。未见等总 compute 或端到端计时；oracle union 不是部署模型。

## Reusable Ingredients

【解释】teacher construction 与 compression 共同设计，以及固定 teacher pool 的 weighting/residual 消融。

## Open Questions

【开放问题】互补性增益能否覆盖重复 teacher 训练成本，并超过强单 teacher 的等预算训练？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增核心 teacher 冗余/互补性方法。

读取：2026-10-15，2607.27770v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2607.27770v1#S3)；[元数据](https://arxiv.org/abs/2607.27770v1)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
