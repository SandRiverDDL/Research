---
type: paper
node_id: paper:wang2026_aclarena_agent_continual
title: "ACLArena: Agent Continual Learning in Multi-stage Post-training"
authors: ["Haixin Wang", "Xiaoxuan Wang", "Junkai Zhang", "Han Zhang", "Renliang Sun", "Alexander K Taylor", "Yidan Shi", "Haoran Deng", "Chenguang Wang", "Jason Cong", "Yizhou Sun", "Wei Wang"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.23989"
  doi: null
  s2: null
tags: ["evidence", "agent", "capability-preservation"]
added: 2026-10-15T03:47:15Z
---

# ACLArena: Agent Continual Learning in Multi-stage Post-training

## One-line thesis

ACLArena 比较顺序训练后 MOPD、离线 replay 与 merging，显示 Agent 多能力恢复仍有明显取舍。

## Problem / Gap

【作者问题】固定四阶段 Agent post-training 中如何恢复旧能力并保留新能力？

## Method

【事实】MMOPD 以四 sequential checkpoints 为 teachers，最终 checkpoint 为 student，平衡 stage prompts；reverse-KL 加 teacher 高熵 token 的 forward-KL。对比 SDFT/replay 与 checkpoint averaging；最终 MLE 使用独立 LoRA experts（§4–6）。

## Key Results

【作者报告】Qwen3-8B，Sequential→MMOPD：AIME26 10.21→21.25、NQ33.5→45.2、multi-hop25.0→32.8，但 MMLU/IF-Bench 略降（§5.2/Table 2）。

## Assumptions

固定 Math/Search/E-commerce/IF curriculum 与可交互环境；teacher 是顺序 checkpoint，并非全独立同源专家。

## Limitations / Failure Modes

最终 MLE 依赖可观察环境 context 路由，保留专家参数；不是已压缩到单一参数 student 的 MOPD 成果。限 Qwen3-8B 和一个训练顺序（§7）。

## Reusable Ingredients

【解释】完整 ID/OOD recovery/retention matrix、MMOPD 与 replay/merging 的共同设置。

## Open Questions

【开放问题】单一模型的容量瓶颈与训练干扰能否分离？不同顺序是否改变 trade-off？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增 Agent 直接对照；HTML 标题 Continual，搜索 metadata 曾为 Continue，以当前正文名记录。

读取：2026-10-15，2609.23989v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.23989v1#S4)；[元数据](https://arxiv.org/abs/2609.23989v1)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
