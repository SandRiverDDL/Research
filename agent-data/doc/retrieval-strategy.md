# Agent Post-Training Data Retrieval Strategy

> 本文档只规定本项目“怎么找论文”。“什么论文可以收 / 抽卡”写在 `doc/acceptance-rules.md`。通用流程仍以 `research-codex-workflow` 的 literature pipeline 为准。

## Recall Focus

候选必须以 agent post-training data mechanism 为主贡献或强相关贡献：

- trajectory / tool-call / observation-action data generation。
- synthetic agent trajectory / task / verifiable environment。
- real-world long-horizon supervision，例如 PR sequence、IDE / browser / GUI logs。
- verifier / judge / executable check / format validity 做 data selection。
- step-level masking、partial supervision、failure mining / repair。
- search / rollout / critic / process feedback 蒸馏到 SFT。
- curriculum / difficulty sampling / student-feedback data flywheel。

不默认纳入：

- 泛 LLM pretraining / corpus work。
- 普通 instruction tuning / alignment data，除非直接服务 agent trajectory / tool / environment。
- 纯 Agentic RL optimizer / reward / exploration。
- benchmark-only paper，除非 benchmark 改变 data collection 或 verifier protocol。

## Recall Sources

本项目使用三类召回：

1. **Seed survey recall**：从 data-centric post-training、tool-use survey、self-evolving agents survey 中抽取 data mechanism references。
2. **Known-item recovery**：用户或 comparison 已点名的 2026 方法先进入 queue，再核查 original paper。
3. **Adjacent project backflow**：从 `/Users/chy/Research/agentic-rl/` 的 queue / cards 中反向发现 data-overlap papers。

每个候选必须记录来源和 `recall_reason`，例如 step-mask trajectory curation、synthetic verifiable environment、real-world PR supervision、search-to-SFT distillation、metacognitive failure switching。

## Bounded Snowballing Loop

不要边搜边抽卡。每轮 recall 必须先产出候选表，再决定是否进入下载 / brief / card：

```text
seed / known-item
  -> source verification
  -> candidate classification
  -> apply doc/acceptance-rules.md
  -> collect PDF / HTML / brief
  -> write approved L1 cards
  -> validate
```

只有发现新术语族、新方法族或明显漏召回时，才插入一次 keyword direct search：

```text
new term family
  -> one-time keyword direct search
  -> queue candidate table
  -> return to seed / known-item loop
```

停止条件：连续两轮新增 `high-priority data-mechanism candidate` ≤ 2，即停止 recall，转入 comparison。

## Batch-First Admission

每轮候选先分类：

| candidate | class | reason | action |
|---|---|---|---|
| paper title | core-data / survey / benchmark-eval / rl-overlap / background / reject | 1 sentence | card / hold / ask user |

默认只抽满足 `doc/acceptance-rules.md` 的 `core-data`。以下情况先暂停、汇报、等用户确认，不直接写正式 L1：

- 新召回集中落入一个新分支，例如 metacognitive failure switching、skill memory、judge/eval infra。
- 方法核心是 RL update，不清楚 data pipeline 是否新。
- 候选只有 benchmark/eval，没有训练数据构造。
- 单轮候选超过 8 篇，先分类和去重，不下载 PDF。

每轮限制：

- 每篇 seed 最多提取 3-5 个 direct data-mechanism references；不召回泛泛 references。
- 只保留 method / survey / verifier-data papers；普通 benchmark、framework、prompt-only background 不计入 core 新增。
- Agent post-training data 注意时效性：除 canonical anchors 外，优先 2025Q4 之后，尤其是 2026 papers。
- 每轮最多写 3-5 张 L1 card；超过则先给用户候选表和抽卡顺序。

## Seed Selection

优先用近期 high-confidence data method 做 seed：

1. 2026 / 2025Q4、明确改 agent data pipeline 的 method paper。
2. 被近期 data method 反复对比或引用的 canonical anchor。
3. 近期 survey 中专门讨论 data generation / selection / verifier filtering / self-evolving data loop 的章节。

不作为强 seed：

- survey-only mention。
- application / benchmark / generic framework。
- pure RL optimizer。
- model release 或 prompt-only work。

## Candidate Log

具体候选、每轮新增、拒绝原因写到 `comparison/queue.md` 或专题 recall 文档，不要只留在聊天里。

每个候选至少记录：

| field | meaning |
|---|---|
| `source` | 哪个 seed / keyword / related work 找到 |
| `recall_reason` | 为什么可能是 data mechanism |
| `boundary_risk` | rl / eval / recipe / infra / none |
| `action` | card / queue-review / hold / reject |
