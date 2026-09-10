---
title: "Scaling Generalist Data-Analytic Agents"
year: 2025
venue: iclr-2026
paper_type: synthetic-verifiable-data
lifecycle_role: frontier-candidate
boundary_risk: rl

failure_modes: [coverage-gap, difficulty-mismatch, long-horizon-drift]
data_knobs: [task-generation, difficulty-curriculum, teacher-rollout, success-filtering]

agent_domain: mixed
data_object: trajectory
data_source: synthetic
selection_signal: verifier
adaptivity: curriculum
failure_use: discard
training_consumer: sft
---

## 一句话

数据分析 agent 的合成训练 recipe。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `coverage-gap` | open-source models 难处理多格式、大文件、长程数据分析。 | 细粒度任务 taxonomy + DataMind-12K trajectory set。 | 是否覆盖用户 benchmark 的 xlsx/csv/doc 工作流需核查。 |
| `difficulty-mismatch` | 数据分析 query 难度和多样性不足。 | recursive easy-to-hard task composition。 | 合成难度是否对应真实失败 slice 需要验证。 |

## 核心做法

DataMind 是你当前最弱 slice（数据处理与分析）的高价值 seed。它提出 fine-grained task taxonomy、recursive easy-to-hard task composition、knowledge-augmented trajectory sampling，再用 model-based 和 rule-based filtering 清洗轨迹。[arXiv abstract] 训练上还包含 dynamically adjustable SFT + RL objective 和稳定 code-based multi-turn rollout。[Brief] 摘要称 DataMind-14B 在多个数据分析 benchmarks 平均 71.16%，超过 DeepSeek-V3.1 和 GPT-5；7B 模型也达到 open-source 最优 68.10%。[Brief]

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `task-generation` | 细粒度 taxonomy + easy-to-hard composition。 | 平铺式 synthetic query。 |
| `success-filtering` | model-based + rule-based filtering。 | 只靠 teacher 生成。 |
| `difficulty-curriculum` | 显式构造难度梯度。 | 随机混合任务。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| prompt-only data agent | proprietary model prompt engineering 难迁移到开源模型。 | 合成数据 + 训练 recipe。 | RL objective 混入，需拆 data-only 贡献。 |

## 谱系位置

- 上游：data-analysis agent benchmark、code-based rollout。
- 同期：SWE-Master、ACC、S1-DeepResearch。
- 下游：用户数据处理类 bad case 的 task synthesis / filtering 模板。

## 和 Agentic RL 的关系

- agentic_rl_overlap: true
- 本项目只读 taxonomy、trajectory sampling、filtering 和 SFT data；RL loss 视角可 cross-link。
- 需要后续确认是否登记到 `agentic-rl`。

## 优缺点

- 优势：直接对应用户最弱的“数据处理与分析”benchmark slice。
- 不足 / 风险：摘要级证据无法拆分 SFT、RL、rollout framework 各自贡献。

<!-- meta:
authors: [Shuofei Qiao, et al.]
url: https://arxiv.org/abs/2509.25084
arxiv_id: 2509.25084
pdf:
brief: _meta/briefs/papers/2509.25084_datamind.md
survey: Codex HF/arXiv recall
agentic_rl_overlap: true
agentic_rl_queue: pending
-->
