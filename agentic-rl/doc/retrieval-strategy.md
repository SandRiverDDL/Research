# Agentic RL Retrieval Strategy

> 本文档只规定本项目“怎么找论文”。“什么论文可以收 / 抽卡”写在 `doc/acceptance-rules.md`。通用流程仍以 `research-codex-workflow` 的 literature pipeline 为准。

## Strict Core Recall

`strict core` 候选必须以训练 LLM agent policy 的 RL 机制为主贡献：

- policy optimization objective / optimizer
- reward / verifier-to-policy update
- multi-turn / long-horizon credit assignment
- exploration, replay, off-policy, tree search, model-based or world-model RL loop
- environment interaction learning loop for tool / web / GUI / code / multi-turn tasks

不默认纳入：

- 纯 application recipe
- benchmark / environment / generic framework
- data generation / filtering / repair / curriculum
- reasoning-only credit assignment，除非明确迁移到 agentic environment trajectory

## Recall Sources

Strict core 检索使用三类召回，但它们不是每轮都跑：

1. **Seed related recall**：从已抽卡的 high-confidence core method 的 related work、direct competitors、baseline table、ablation references 往前 / 往后找。
2. **Keyword direct search**：阶段开始时跑一轮 recent paper search；后续只在发现新术语族时补跑，例如从 SPEAR 发现 `self-imitation / replay / entropy control`。
3. **Codex hypothesis**：只能提出候选；必须用 arXiv / OpenReview / venue page / project page / GitHub / PDF 验证后才能进 queue。

候选必须记录来源和 `recall_reason`，例如 direct algorithmic competitor、same optimizer family、same credit problem、same environment loop、same reward design、newer follow-up。

## Bounded Snowballing Loop

Strict core recall 使用有限循环，不无限扩散。循环里默认只做 seed related recall，不重复跑 broad keyword search：

```text
carded strict-core papers
  -> related work / direct competitors
  -> batch candidate classification
  -> confirm strict-core boundary
  -> apply doc/acceptance-rules.md
  -> download / brief / write approved cards
  -> repeat
```

只有发现新术语族、新方法族或明显漏召回时，才插入一次 keyword direct search：

```text
new term family
  -> one-time keyword direct search
  -> queue candidate table
  -> return to seed related recall loop
```

停止条件：连续两轮新增 `high-priority strict-core candidate` ≤ 2，即停止 strict-core recall，转入 comparison。

### Batch-First Admission

不要边搜边抽卡。每轮 recall 必须先产出候选表，再决定是否进入下载 / brief / card：

| candidate | class | reason | action |
|---|---|---|---|
| paper title | strict-core / skill-overlap / reasoning-adjacent / framework / data / reject | 1 sentence | card / hold / ask user |

默认只抽满足 `doc/acceptance-rules.md` 的 `strict-core`。以下情况先暂停、汇报、等用户确认，不直接写正式 L1：

- 新召回集中落入一个新分支，例如 skill/internalization、instruction/prompt co-evolution、memory evolution。
- 候选只有 reasoning RL，没有 tool/web/GUI/code/environment interaction loop。
- 方法核心是 data / skill bank / memory / prompt，不清楚 RL update 是否是主贡献。
- 单轮候选超过 8 篇，先分类和去重，不下载 PDF。

每轮限制：

- 只从 `canonical-anchor` / `frontier-candidate` strict-core cards 的 related work 召回。
- 每篇最多提取 3-5 个 direct competitors；不召回泛泛 references。
- 只保留 method paper；benchmark、framework、data mechanism、reasoning-only background 不计入 strict-core 新增。
- Agentic RL method 注意时效性：除经典 / 高影响力方法外，优先 2025 年之后，尤其是 GRPO/RLVR 范式之后的方法。
- 每轮最多写 5-8 张 L1 card；超过则先给用户候选表和抽卡顺序。

## Seed Selection

优先用近期 high-confidence core method 做 seed：

1. 2026 / 2025 下半年、已抽卡、明确改 RL training loop 的 core method。
2. 被近期 core paper 反复对比的 strong baseline / canonical anchor。
3. 新发现的术语族 seed，例如 SPEAR 引出的 `self-imitation / replay / entropy control`。

不作为强 seed：

- survey-only mention。
- application / recipe / benchmark / framework。
- substrate-only 方法，例如原始 GRPO / DAPO / Dr.GRPO；它们用于背景，不用于无限扩散。
- data-only / prompt-only / model release。

## Candidate Log

具体候选、每轮新增、拒绝原因写到 `comparison/strict-core-recall.md` 或 `comparison/queue.md`，不要只留在聊天里。

每个候选至少记录：

| field | meaning |
|---|---|
| `source` | 哪个 seed / keyword / related work 找到 |
| `recall_reason` | 为什么可能是 core method |
| `boundary_risk` | data / recipe / reasoning / infra / none |
| `action` | card / queue-review / hold / reject |
