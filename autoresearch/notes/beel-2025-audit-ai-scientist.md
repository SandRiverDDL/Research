---
title: Evaluating Sakana's AI Scientist for Autonomous Research - Wishful Thinking or an Emerging Reality
year: 2025
venue: arxiv
paper_type: critique-audit
lifecycle_role: critique-anchor
boundary_risk: none

failure_modes: [hallucinated-novelty, code-execution-fake-success, reviewer-model-hacking, citation-fabrication, cherry-picked-showcase, weak-experimental-design, reproducibility-gap, human-in-the-loop-hidden, verifier-blind-spot]
design_knobs: [pipeline-scope, verifier-type, novelty-check, human-intervention-point, reproducibility-artifact]
---

## 一句话定位

本项目唯一 independent audit 卡：亲手复现 Sakana AI Scientist v1，把 self-report 与实际能力落差用硬数字揭穿。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `hallucinated-novelty` | Semantic Scholar API 只做 keyword search 判 novelty，10 生成 idea + 2 seed 全部判 novel，实际 micro-batching SGD / adaptive LR / hybrid MF / e-fold CV 都已发表 [§2.3] | 逐条列出与已存在文献的重合 | 需要 semantic synthesis 而非 keyword 匹配的替代 novelty check |
| `code-execution-fake-success` | e-fold CV 实验：pipeline 声称 test e={2,3,4,5} 实际固定 e=2；同时漏跑 k-fold baseline 让 e-fold 看起来"更好"（物理不可能，e-fold 设计上不可能超 k-fold 准确度）[§2.4] | 逐 idea 检查代码变化，Table 1 列出每次迭代字符增量 | AI Scientist v2 tree search 是否改善此问题未 audit |
| `reviewer-model-hacking` | Reviewer agent 对 7 篇自产 manuscript 全 recommend reject，但只提"single small dataset"表层问题；**没发现任何 hallucinated result / logical 矛盾 / duplicate section**——同源盲区 [§2.6] | 用 10 篇 OpenReview 真论文对照：拒 9/10（含 4 篇真接收），揭示 conservative bias + 与人类判断脱节 | 需要**异源** verifier 方案（不同架构 / 结构化 rubric / 人类 fallback） |
| `citation-fabrication` | Manuscript 中位数 5 citations，34 总 ref 只有 5 (14.7%) 来自 2020 后；e-fold CV manuscript **漏引所有真正的 e-fold CV 已发表工作** despite Semantic Scholar 可搜到 [§2.5] | 逐篇 ref 年份统计 + 关键漏引案例 | 未测 ref hallucination 率（是否引用不存在的 paper） |
| `cherry-picked-showcase` | Sakana claim $15/paper 端到端 autonomy，但复现显示需 5h setup + 15h template impl + 10h brainstorm/review = **25h 人力**（3.5h/manuscript）[§2.7] | 逐环节计时 report | Sakana 未公开自己使用的人力时间做直接对照 |
| `weak-experimental-design` | 5/12 idea 因 coding error 失败；跑通的 4/7 有 hallucinated 数字；一篇 claim "energy-efficient 算法"但训练 116→115s + RMSE 更好 + 内存**增加**，逻辑自相矛盾 [§2.4-2.5] | 手工检查每篇产出的实验设计 | 未系统统计跨 domain 表现 |
| `reproducibility-gap` | Sakana 开源代码，但产出 manuscript 的 seed 敏感度、API 版本依赖未 audit；本 audit 提供 Singularity 容器完整复现 | 提供 code.isg.beel.org 完整复现镜像 | Sakana v2 未 audit |
| `human-in-the-loop-hidden` | "autonomous" 需要 user 提供 template（prompts.json + experiment.py + plot.py + LaTeX），限制真正 autonomy 范围 [§2.2] | 明确列出所有 user-defined component | 未对比"更少 user input"能否运作 |
| `verifier-blind-spot` | Reviewer agent 检不出 duplicate section / "Conclusions Here" placeholder / hallucinated 数字 [§2.6] | 定性证据 | 与 SoundnessBench 的 74% FPR 统计证据形成互补 |

## 方法机制

- **复现设定**：单主题 (Green Recommender Systems + FunkSVD + MovieLens-100k)，刻意换域测泛化（非 Sakana 官方三个 ML 子域）；base model gpt-4o-2024-05-13；third-year CS undergrad 执行以估**下限** effort。
- **12 idea × 5 iteration 逐条追踪** [§2.4, Table 1]：每次 iteration 通过 Aider 修改 experiment.py，字符净变化在 0~1173 之间，5/12 全流程失败；平均首轮增量仅 8%——"reworking 而非 devising"。
- **Manuscript 手工审计** [§2.5]：结构、citation 年份分布、hallucinated 数字、logical 一致性逐篇检查。
- **Reviewer 双向测试** [§2.6]：既让 reviewer agent 评自产 paper，又让它评 10 篇 OpenReview 论文，暴露 self-review 盲区 + 与人类判断脱节。
- **成本 vs 人力对照** [§2.7]：Sakana $15/paper claim 复核为 $6/paper（一致），但补足 25h 人力时间 —— "autonomy" 概念被拆穿。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| Lu 2024 (AI Scientist v1) | Self-report metric，声称 "near-human reviewer"、"autonomous" | 独立复现 + 手工审计 12 idea + 7 manuscript + 10 human paper reviewer 对照 | 只测 v1 单域单模型，非 large-N 统计 |
| SoundnessBench (Ho 2026) | 统计层面 1099 例，但只测 base LLM classification | 定性单点，追踪完整 pipeline 每一环节的具体失败 | 无统计功效 |
| HindSight (Jiang 2026) | Post-hoc 用未来 citation 做 ground truth | 前向 audit 系统内部机制 | 不评 idea 未来 impact |
| Si 2025b (execution gap) | 43 专家 × 100h 大规模但只测 idea→execution 一环 | 覆盖 idea/execution/manuscript/review 四环 | 只测一个 pipeline |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `pipeline-scope` | Audit：全 pipeline（idea + code + exp + write + review） | 单环节 benchmark |
| `verifier-type` | Human researcher 手工审计 + 复现代码 + 定性 cross-check | LLM-Judge / benchmark automated metric |
| `novelty-check` | 手工对照 Semantic Scholar / 已发表文献 | Keyword search / embedding similarity |
| `human-intervention-point` | 显式量化每环节人力时间（setup / template / brainstorm / review） | 只 report 总 API cost |
| `reproducibility-artifact` | Singularity 容器 + GitHub 完整复现镜像 | Code only / prompts only |

## 方法优缺点 / 适用边界

- 优势：
  - **本项目 evidence tier 3（independent third-party audit）唯一档**：其余卡都是 self-report 或 replication，Beel 填补最缺的证据层。
  - 数字硬（5/12 fail、8% char/iter、5 citation/paper median、34 ref 中仅 5 篇 2020 后、25h 人力）——每个 failure mode 从 speculation 升级为 evidence。
  - 完整复现容器（Singularity）+ code 公开，方法学可复用。
  - Min-Yen Kan (NUS WING) 参与，可信度档位高于典型 arxiv-only critique。
- 不足 / 风险：
  - **只测 v1 版本**——v2 tree search + VLM reviewer 是否改善关键 failure mode 未 audit（这是本项目最需要跟进的 gap，AI Scientist v2 卡应该显式标出这个未复现）。
  - 单域（recsys）+ 单 base model (gpt-4o-2024-05-13)：外部效度有限，Sakana 原 3 domain 未复测。
  - 定性单点非统计：结论强度靠 SoundnessBench 类工作提供 statistical backing。
  - IR/SIGIR 视角写作，AI Scientist 后续社区 audit 未汇入。

<!-- meta:
authors: [Joeran Beel, Min-Yen Kan, Moritz Baumgart]
url: https://arxiv.org/abs/2502.14297
arxiv_id: 2502.14297
pdf: null
brief: _meta/briefs/papers/2502.14297.md
survey: AI-Scientist-v2-RW
-->
