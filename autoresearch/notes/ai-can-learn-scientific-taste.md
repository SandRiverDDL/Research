---
title: AI Can Learn Scientific Taste
year: 2026
venue: arxiv
paper_type: core-method
lifecycle_role: critique-anchor
boundary_risk: none

failure_modes: [reviewer-model-hacking, metric-gaming, benchmark-contamination, evidence-tier-mixing]
design_knobs: [reward-signal, verifier-type, novelty-check, training-source, demonstration-corpus]
---

## 一句话定位

用 700K 篇高低引论文配对 + RL 训一个"科研品味"判官和政策模型，反 measuring-gap 的对立命题。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `reviewer-model-hacking` | 通用 LLM reward model 不懂 research taste，训出来的政策 idea 是 reviewer-friendly 但社群不认 | 用**引用数**作为社群实际偏好信号，绕开人工 rubric | 引用受时代/领域/网络效应污染，非纯品味 |
| `metric-gaming` | novelty 打分可被 LLM prompt 优化，但 citation 是"外部真实反馈" | Scientific Judge 训在 field/time 匹配的高低引 pair 上，减轻引用时效偏差 | 高引 ≠ 高质量（明星作者、话题热度） |
| `benchmark-contamination` | 政策模型可能背下训练时期论文 | 加了 future-year test（训练截止后发表的论文）泛化实验 | future-year 论文本身在网上可能已泄漏 |
| `evidence-tier-mixing` | 用 GPT-5.2 / Gemini 3 Pro 作 baseline，未区分 API 判官 vs 训练判官 | SciJudgeBench 提供第三方 benchmark | benchmark 是本文自建，外部独立复现少 |

## 方法机制

- **RLCF (Reinforcement Learning from Community Feedback)**：把引用数当社群偏好信号，替代 RLHF 的人工 rating [PDF §1]。
- **SciJudgeBench**：700K field-and-time-matched 高低引 abstract pair，做偏好建模训练集与 benchmark [PDF §1]。
- **Scientific Judge**：generative reward model，用 GRPO 训，读两篇 abstract 说哪个 taste 更好；泛化到未见年份、未见领域、peer-review preference 上都过 SOTA LLM baseline（GPT-5.2、Gemini 3 Pro）[PDF §1, Fig 1]。
- **Scientific Thinker**：policy model，用 Scientific Judge 当 reward 做 RL；输入某 paper 的 title+abstract，输出 follow-up idea；ensemble evaluation 下 win rate 高于未训 base policy。
- 关键机制：把"scientific taste"操作化成"能被高引论文暗含的社群偏好"，用 pair-wise preference learning + GRPO 训。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| Measuring-Gap (Chen 2026) | 说 LLM taste 系统性偏窄、无法学 | 直接反驳：taste 可训、可对齐社群 | 训完的 idea 分布仍可能收敛到高引模板 |
| RLHF 通用对齐 | reward 是人工标注 helpfulness / harmlessness | reward 是社群 citation，绕开人工 rubric | citation 本身有系统性偏差 |
| Si 2025a 人类 blind review | 一次性评审，无 policy | 学出可持续 propose idea 的 policy | policy 泛化到 execution 未验证 |
| AI Scientist v1 (Lu 2024) | prompt LLM 生成 idea，无 taste 训练 | 用 RL + Scientific Judge 显式对齐 | 训练 corpus 700K 高引 pair，成本极高 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `reward-signal` | citation-derived pairwise preference（community feedback） | 人工 rubric / LLM judge / self-consistency |
| `verifier-type` | Trained generative reward model (Scientific Judge) | LLM-as-reviewer / rule-based / peer review |
| `novelty-check` | 隐含在 taste reward 中 —— 高引论文的 taste distribution | embedding similarity / prompt-based novelty check |
| `training-source` | GRPO on preference pair | SFT / DPO / prompt only |
| `demonstration-corpus` | 700K field/time-matched high-vs-low citation abstracts | 人写 gold idea / expert demonstration |

## 方法优缺点 / 适用边界

- 优势：
  - **和 measuring-gap 是直接对立命题**——一个说"LLM taste 分布系统性窄且训不动"，一个说"用社群信号可以训出人级 taste"。必须并列读，是本项目 idea evaluation 争论的双端。
  - 用 citation 做 reward 巧妙：绕开人工标注瓶颈，能拿到 700K 级数据。
  - Future-year generalization 测试是这类工作里少见的严肃泛化实验。
- 不足 / 风险：
  - **citation ≠ taste**。高引可能来自话题热度、作者名气、时代红利；用它对齐等于让政策学"如何写出热点论文"，正是 reviewer-model-hacking 的高维版本。
  - Scientific Thinker 的评测靠 Scientific Judge 自己 ensemble——**同源污染严重**，win rate 高不等于人类真觉得 idea 好。
  - 未做 execution 侧验证（对比 Si 2025b 的做法），policy 产出的 idea 落到实验会不会崩不清楚。
  - 若和 measuring-gap 结论一起看：可能训出来的政策 taste 更"高引 template"化，即 bridge/synthesis 依然占大头，只是包装更精致。这个 hypothesis 值得对本文 policy 输出跑一遍 taste taxonomy 分布分析（后续可写为 comparison 报告或 idea hook）。

<!-- meta:
authors: [Jingqi Tong, Mingzhe Li, et al.]
url: https://arxiv.org/abs/2603.14473
arxiv_id: 2603.14473
pdf: papers/2603.14473-ai-can-learn-scientific-taste.pdf
brief: _meta/briefs/papers/2603.14473.md
survey: measuring-gap-human-llm-research-ideas
-->
