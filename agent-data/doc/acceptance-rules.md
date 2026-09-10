# Agent Post-Training Data Acceptance Rules

> 本文档只规定本项目“什么论文可以进入 queue / 抽正式 L1 card”。“怎么找论文”写在 `doc/retrieval-strategy.md`。这些是项目本地规则，不写入全局 skill。

## 基本原则

- Queue 可以宽，formal L1 card 要严。
- `SFT / RL / tool / GUI / SWE / web` 只是应用场景，不自动决定是否收录。
- 真正判断看论文是否改了 agent post-training data pipeline 的可迁移设计位点。
- 不确定时先 `queue / review`，不要直接抽卡。

## Hard Gates

正式 L1 card 必须满足：

- 有 original paper PDF / HTML / source brief。
- 有明确 data mechanism，不只是 benchmark、prompt trick、模型发布或普通 training recipe。
- 至少能定位到一个可复用的 data design knob，例如 trajectory curation、step masking、verifier filtering、environment synthesis、real-log mining、search-to-SFT distillation。

不开源只允许进入 `queue / review`，除非满足以下例外之一：

- 大厂 / frontier lab 论文，存在保密或产品化理由。
- 被多个近期方法反复作为 baseline / direct related work。
- 有明确社区影响力背书。
- 公开了数据构造流程、数据统计或 evaluation protocol，足以支持 data-mechanism card。

## Time / Venue Gate

### 2025Q4 之后

优先接受：

- 2026 paper 或 2025Q4 paper。
- data mechanism 明确的新 arXiv。
- strong venue / 大厂背书 / 代码或数据公开。
- 能直接解释 2026 agent post-training data recipe 的论文。

新 arXiv 可以没有稳定 venue，但需要 Codex 判断可靠性：

- 方法 delta 清楚。
- data construction 可追踪。
- verifier / filtering / masking / curriculum 不是空泛描述。
- baselines 合理，没有明显数据泄漏、reward hacking 或 weak baseline。

### 2025Q3 之前

默认不新增正式 card，除非是：

- canonical anchor，例如 FireAct / STeP / InSTA 这类 agent trajectory data 起点。
- 被近期 2026 papers 反复引用。
- 对当前 comparison 不可替代的 data mechanism。

## Core Data Mechanism Gate

算本项目 core 的条件：论文主贡献改了可迁移的 agent data pipeline 设计位点，例如：

- trajectory generation / curation / repair / masking。
- tool-call / action-schema / observation-action data construction。
- synthetic task / trajectory / executable environment generation。
- real-world logs / PR / GUI / browser history mining。
- verifier / judge / rule / unit test / format validity 用于 selection 或 reweighting。
- failed trajectory mining、contrast、partial supervision。
- search / rollout / critic / process feedback 蒸馏成 SFT / pre-RL data。
- curriculum / difficulty sampling / student-feedback data generation。

不自动算 core：

- 只是用一批 SFT warm-start data 后做 RL。
- 只是把普通 synthetic instruction tuning 跑到 agent benchmark。
- 主要贡献是 benchmark、环境、prompt、workflow、model release。
- 核心是 RL objective / reward design / online exploration / credit assignment。

## Boundary Handling

边界项必须写清：

- 为什么可能是 data mechanism。
- 为什么可能只是 RL / benchmark / recipe / eval / infra。
- 需要核查什么证据。

常见边界：

- `boundary_risk: rl`：数据管线和 RL update 都强；本项目只写 data 视角，RL 视角登记到 `agentic-rl`。
- `boundary_risk: eval`：benchmark / judge / verifier 有价值，但不一定是训练数据方法。
- `boundary_risk: recipe`：像 training recipe，但 data curation 或 verifier filtering 可能可迁移。
- `boundary_risk: infra`：环境或日志系统是基础设施，只有改变数据生成 / 验证时才抽卡。

## Queue vs Card

进入 queue 的最低条件：

- 有可靠来源可验证。
- 有一句明确 `recall_reason`。
- 有初步 `paper_type`、`boundary_risk` 和 `agent_domain`。

写正式 L1 card 的最低条件：

- 通过 hard gates。
- 通过 time / venue gate 或有明确 exception。
- 通过 core data mechanism gate，或者明确标成 survey / benchmark / background 等非 core 类型。
- 有 bounded original paper brief。

## One-Line Checklist

抽卡前按顺序问：

1. 有原文和 source verification 吗？
2. 是 2025Q4 / 2026 吗？如果不是，是否 canonical anchor？
3. 它改变的是 data pipeline，还是只是 optimizer / reward / benchmark？
4. 数据对象是什么：task、trajectory、tool-call、observation、environment、replay？
5. selection / filtering / masking / verification 信号是什么？
6. failure trajectory 是丢弃、mask、修复、对比、挖掘还是忽略？
7. 是否需要同时登记到 `/Users/chy/Research/agentic-rl/`？
