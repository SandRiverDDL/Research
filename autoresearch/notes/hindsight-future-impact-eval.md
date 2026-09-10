---
title: HindSight - Evaluating LLM-Generated Research Ideas via Future Impact
year: 2026
venue: arxiv
paper_type: benchmark-eval
lifecycle_role: critique-anchor
boundary_risk: eval

failure_modes: [reviewer-model-hacking, verifier-blind-spot, hallucinated-novelty, metric-gaming, evidence-tier-mixing]
design_knobs: [evaluation-protocol, evaluation-judge, novelty-check, evaluation-scope]
---

## 一句话定位

用**未来发表 + citation**做外部 ground truth 打破 LLM-as-Judge 的同源 verifier 循环。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `reviewer-model-hacking` | LLM-Judge 与 idea 生成器同源，倾向奖励"novel-sounding" | 用时间切片 + 真实 citation 做外部 metric | Judge 单模型（Qwen3-32B），未做多 Judge 对照 |
| `verifier-blind-spot` | LLM-Judge 在 RA vs vanilla 上 p=0.584，看不出差异 | HindSight 揭示 2.5× gap [Table 1] | 未测更多生成系统，200 sample 偏小 |
| `hallucinated-novelty` | LLM-Judge 打的"更 novel"idea 与真实未来论文更**不**匹配 [ρ=-0.29, p=0.003] | 用 SPECTER2 embedding 匹配 27,589 篇 post-T 论文 | conformity bias：真正 revolutionary 不在已发表分布中 |
| `metric-gaming` | 系统优化 LLM-Judge → 学会造"grand but vague"（Overhyped 象限：26% RA / 34% BL） | 换成 HindSight 后 metric 与真实 impact 挂钩 | HindSight 也可 game（照抄 recent title 提高 similarity），未做对抗 audit |
| `evidence-tier-mixing` | 明确区分 subjective (LLM-Judge) vs objective (future publication) 两档信号，建议两者并报 | 讨论章节明说互补 | ground truth pool 只 10 topic，其他 domain 假零分 |

## 方法机制

- **时间切片 (time-split)**：把 cutoff T=2023-06 定在 LLM 训练截止 (2023-12) 之前 6 个月，防信息泄露；用 T+30 个月的真发表论文做 ground truth pool（27,589 篇）[§3.2, §4.1]。
- **匹配 + 打分**：idea (problem⊕method) 与 paper (title⊕abstract) 用 SPECTER2 embedding + FAISS top-20 检索，cosine≥0.96 保留匹配集合 `M(i)`；`HindSight(i) = max_{p∈M(i)} h(p)`，其中 `h(p) = 0.6·norm(citation) + 0.4·1[top venue]` [§3.3-3.4]。
- **对比实验**：ResearchAgent (retrieval-augmented) vs vanilla prompt，各 100 idea，同 Llama-3.3-70B，跨 10 个 AI/ML topic [§4.2]。
- **相关性**：HindSight 与 LLM-Judge Novelty 相关 ρ=-0.29 (p=0.003)、与 Feasibility 相关 ρ=+0.25 (p=0.012) [Table 2] —— **novelty 与 anticipatory 反向**。
- 四象限分析：Hidden Gem（HindSight 高 / Judge 低）23% RA idea，多为"technically specific" 但被判 incremental；Overhyped（Judge 高 / HindSight 零）26% RA / 34% BL，多为"holistic framework / unified approach" [§6, Table 3]。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| LLM-as-Judge (Zheng 2023) | 主观、verbosity bias、self-preference、与真实 impact 无相关 | 换成时间切片 + 真发表 citation 作 ground truth | 只能评已进入 published 分布的 idea，反 revolutionary |
| Si 2025a (人类专家评审) | 昂贵、慢、novelty 上 inter-annotator agreement 低 | 完全自动化、可 scale | 依赖 embedding 质量、单 embedding 模型 |
| Si 2025b (ideation-execution gap) | 需要真跑 100h 实验 | 只需 SPECTER2 + Semantic Scholar API | 只评 idea 是否**被人做**过，不评是否**能做出来** |
| Measuring-Gap (Chen 2026) | 只测 idea 集合的分布形状 | Pointwise 打分且有外部 anchor | 分布信息丢失（每个 idea 独立打分） |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `evaluation-protocol` | Time-split + citation/venue impact | LLM-Judge / human panel |
| `evaluation-judge` | 无 judge，SPECTER2 embedding 匹配 | LLM / human |
| `novelty-check` | Embedding 相似 post-T 论文（**反直觉**：越像已发表越好） | LLM 判断 novelty / literature contrast |
| `evaluation-scope` | Idea 单点 × 未来 30 个月发表窗口 | 端到端产出 / 中间过程 |

## 方法优缺点 / 适用边界

- 优势：
  - 首次给 idea eval 一个**外部 ground truth**，破 same-source verifier 循环——本项目 evidence tier 上的关键补齐。
  - 揭示 novel-sounding ↔ actual-impact 反相关，为 LLM 优化 idea 时"往哪走"提供反面路标。
  - Threshold 敏感性 (θ=0.93→0.965 时 RA/BL 比 1.1→3.8) 稳健，方法学干净。
- 不足 / 风险：
  - **单作者 arxiv-only，无第三方复现**；200 idea / 10 topic，效应量中等，需按"方法学锋利 + 证据量弱"评估。
  - Conformity bias：奖励接近已发表 → 系统性低估真正 revolutionary，作者自认为可接受但项目要注意。
  - 单 Judge (Qwen3-32B) 单 embedding (SPECTER2)：换模型可能改变相关方向。
  - HindSight 分数也可 game：直接照抄 recent title 就能拉高，未做对抗测试。
  - Ground truth 30 个月窗口偏短，慢发酵领域被截尾。

<!-- meta:
authors: [Bo Jiang]
url: https://arxiv.org/abs/2603.15164
arxiv_id: 2603.15164
pdf: null
brief: _meta/briefs/papers/2603.15164.md
survey: arxiv-search-2026-idea-eval
-->
