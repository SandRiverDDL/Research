---
title: The AI Scientist - Towards Fully Automated Open-Ended Scientific Discovery
year: 2024
venue: arxiv
paper_type: core-method
lifecycle_role: canonical-anchor
boundary_risk: none

failure_modes: [hallucinated-novelty, reviewer-model-hacking, cherry-picked-showcase, weak-experimental-design, reproducibility-gap, verifier-blind-spot, code-execution-fake-success]
design_knobs: [pipeline-scope, stage-decomposition, agent-role-organization, verifier-type, iteration-control, code-execution-env, reproducibility-artifact]
---

## 一句话定位

端到端 autoresearch pipeline 的命名事件：LLM 从 idea 到 paper 到 review 全流程自动，$15/paper。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `hallucinated-novelty` | 无系统性 novelty check，只靠 LLM 内部 prompt 判断 | 自动 reviewer 给 score 高就算通过 | novelty 主要靠 LLM self-eval [abstract] |
| `reviewer-model-hacking` | "papers exceed acceptance threshold as judged by our automated reviewer"——被自评的 reviewer 打过关 | 声称 automated reviewer 与人类 near-human 一致 | 与人类 near-human 是**本文自己评估的**，第三方复现 gap 大 |
| `weak-experimental-design` | 生成 paper 覆盖三个 subfield（diffusion、transformer LM、learning dynamics），每 idea 都执行实验 | 端到端跑代码 + 出图 | 后续 Si 2025b 类 execution audit 揭示这类 idea 落地时崩溃 |
| `cherry-picked-showcase` | 展示 acceptance-threshold 论文，未系统报告失败率分布 | $15/paper cost 数字很诱人 | 未报告成功产出 vs 失败迭代的比例 |
| `code-execution-fake-success` | 代码执行由 pipeline 自己 sandbox 跑 | 有代码验证步骤 | 后续社区复现发现许多产出的实验结果与 claim 不匹配 |
| `verifier-blind-spot` | 只有 LLM reviewer 做终审 | automated reviewer + iterative refine | verifier 与生成器同源，共盲区 |
| `reproducibility-gap` | 声明开源（GitHub SakanaAI/AI-Scientist）| 开源代码 + prompts | 生成产出的可复现性、依赖 API 版本、seed 敏感度未系统评估 |

## 方法机制

- Pipeline stages：**idea generation → 代码 → 实验执行 → 可视化 → 全文写作 → 自动 review**，全 LLM 驱动，可迭代 [abstract]。
- Domain 覆盖：diffusion modeling、transformer-based LM、learning dynamics 三个 ML 子领域。
- 成本 claim：每篇论文 <$15 [abstract]，作为经济可行性论据。
- 评测方式：**Automated reviewer 内部评分**，声称与人类近似；用"是否超 top ML 会议 acceptance threshold"作为 claim（**由本 reviewer 打分**）。
- 关键设计：LLM 承担了所有环节，人类只在 pipeline 设置阶段介入。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| Baek 2025 (ResearchAgent) 等 | 只做子任务 ideation | 首个真正端到端 | 每个环节都被削弱以适配自动化 |
| Boiko 2023 (Coscientist) | 化学 domain，实验硬件驱动 | 纯软件 ML 域 | ML domain 实验难度低但更容易 game |
| Si 2025a | Ideation-only 严格评测 | 全流程 demo | ideation 阶段的 novelty claim 已被 Si 2025b 打破 |
| AI Scientist v2 / Sakana 后续 | 本文的直接迭代 | 是 v1 的**批判对象和基线** | 本卡定位 canonical anchor，非 SOTA 参考 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `pipeline-scope` | End-to-end（idea → paper → review） | Sub-task specialized |
| `stage-decomposition` | Linear: idea → code → exp → viz → write → review | Iterative refine loop / DAG |
| `agent-role-organization` | 单一 LLM 承担多角色，通过 prompt 切换 | Multi-agent role-specialized |
| `verifier-type` | LLM-as-automated-reviewer（自评） | Human / execution-based / hybrid |
| `iteration-control` | Fixed rounds + reviewer score threshold | Human accept gate / budget |
| `code-execution-env` | Notebook-like sandbox | Container / real hardware |
| `reproducibility-artifact` | 开源 code + generated papers | Prompts only / closed |

## 方法优缺点 / 适用边界

- 优势：
  - **canonical anchor 例外保留**（超 12 个月 cutoff）：后续所有 end-to-end autoresearch 工作都在回应它，砍掉读者失去背景。
  - 首个把 pipeline 六个环节都串起来的公开工作，成本 claim（$15/paper）激励了后续大量迭代。
  - 开源代码 + prompt 完整，便于第三方 audit——这正是它成为 critique target 的前提。
- 不足 / 风险：
  - 几乎所有 failure mode 都在此论文集齐（hallucinated-novelty、reviewer-model-hacking、cherry-picked-showcase、code-execution-fake-success、verifier-blind-spot、reproducibility-gap）——本卡的价值在于**列清它是什么的靶子**。
  - 自评 reviewer + 自评 threshold 的循环论证：'passes top-conf threshold' 只在其自建 reviewer 语义下成立。
  - 未报告失败案例分布、seed 稳定性、跨 domain 泛化。
  - v2 及后续社区复现显示大量生成 paper 存在 citation fabrication、实验与 claim 不符。这些属于后续论文的 finding，不改本文定位。

<!-- meta:
authors: [Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha]
url: https://arxiv.org/abs/2408.06292
arxiv_id: 2408.06292
pdf: papers/2408.06292-the-ai-scientist.pdf
brief: _meta/briefs/papers/2408.06292.md
survey: measuring-gap-human-llm-research-ideas
-->
