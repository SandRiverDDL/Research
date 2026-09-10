# Agent Post-Training Data 当前状态

> Hot memory for Codex. 只放下一轮启动必须读的状态。

## 当前目标

调研 `Agent Post-Training Data`：LLM agent 后训练阶段的数据机制，重点是 trajectory / tool-call / observation-action / environment feedback / verifier signal 如何进入 SFT、pre-RL 或 RL pipeline。

这是 `llm-post-training-data` 下的 agent 子方向，不是假设社区已经有成熟的 “Agent Data” 或 “Agent SFT” 综述类目。当前项目是 goal-driven literature map：服务 30B A3B MoE agent SFT 的 benchmark-driven data improvement，不做完整领域综述。

## 当前边界

收录：

- task / prompt / trajectory / tool-call / observation-action data generation。
- synthetic agent traces / teacher traces / self-generated traces / real-world interaction logs。
- verifier / judge / format-validity / success signal 做 data selection。
- failed trajectory repair / filtering / masking / contrast / mining。
- curriculum / difficulty sampling / student-feedback data generation。
- search / rollout / critic / process feedback 蒸馏成 supervised data。
- RL training data pipeline，只要核心贡献是数据机制而不是 RL 算法。

迁出到 `/Users/chy/Research/agentic-rl/`：

- reward design / policy optimization / RL objective。
- online exploration / long-horizon credit assignment。
- on-policy/off-policy update mechanics。
- environment interaction protocol 主要服务 RL learning loop。

## 下一步

1. 使用 `scripts/autoresearch.py status` / `validate` 确认本地 helper 健康。
2. 当前已经有 18 张 formal L1 / 16 个 paper briefs；不要继续盲目扩 queue。
3. 已生成第一版 synthesis：`comparison/agent-sft-data-synthesis.md`。后续学习和数据决策优先从这里进入。
4. `comparison/benchmark-to-data-actions.md` 已升级为训练数据 backlog stub：每个数据包写明 source、selection signal、expected win、negative-transfer risk。
5. 已补充数据配比 comparison：`comparison/data-mixture-comparison.md`。它区分 static mixture、FastMix、target/general regularization、bilevel repair，并给出当前项目的 bucket / validation slice / 最小实验矩阵。
6. 下一步不要继续盲目扩 queue；按 synthesis 和 data-mixture comparison 的开放问题补证据，或把 backlog 展开成具体数据生成 / verifier / ablation 方案。
7. MARS / MIRROR 仍只作为 metacognitive scaffold / benchmark 边界项；FireAct / STeP / InSTA / MAG-V 等 canonical anchors 只在 synthesis 暴露 lineage 缺口时补。

## 当前 seed 状态

- 当前主目录有 2 张 current seed cards：
  - `notes/26_agentic-tool-use-survey.md`：只用 supervised tool learning / tool-call data 部分。
  - `notes/26_alignment-data-centric-survey.md`：提供 data-centric pipeline lens。
- `comparison/queue.md` 已初始化为脚本主队列，包含用户提供的 2026 agent post-training data 候选和 Codex recall seed。
- 2026-06-24 验证状态：18 formal cards、26 queue rows、16 paper briefs、0 validation errors / warnings。
- 第一批 Codex recall L1：
  - `notes/2605_acc-agent-context-compilation.md`
  - `notes/2510_agent-data-protocol.md`
  - `notes/2602_swe-master.md`
  - `notes/2606_open-swe-traces.md`
  - `notes/2606_denovoswe.md`
  - `notes/2509_datamind.md`
  - `notes/2505_pc-agent-e.md`
  - `notes/2606_procua-sft.md`
- 第二批 user-known core L1：
  - `notes/2601_swe-lego.md`
  - `notes/2601_astra.md`
  - `notes/2602_davinci-agency.md`
  - `notes/2602_proact.md`
- Supporting data-flywheel L1：
  - `notes/2606_fastmix.md`
  - `notes/2605_dr-post-training.md`
  - `notes/2508_data-mixing-optimization-sft.md`
  - `notes/2511_bilevel-data-curation.md`
- ID 修正：`daVinci-Agency` 是 arXiv `2602.02619`；`ProAct` 是 arXiv `2602.05327`。
- 旧 agent 总综述归档在 `notes/archive/historical-background/`，默认不读。
- `Environment Scaling for Interactive Agentic Experience Collection` 已迁移到 `/Users/chy/Research/agentic-rl/notes/`。

## 关键文件

- `AGENTS.md`: 主题规则。
- `comparison/queue.md`: 脚本主队列。
- `doc/acceptance-rules.md`: 准入 / 抽卡规则。
- `doc/retrieval-strategy.md`: 检索与 recall 流程。
- `doc/agent-data-scope.md`: Agent Post-Training Data 边界。
- `doc/templates/l1-card.md`: L1 card 模板。
- `doc/taxonomy/failure-modes.md`: data/failure 词表。
- `doc/taxonomy/design-knobs.md`: data pipeline design knob 词表。
- `comparison/seed-sources.md`: 当前 seed / anchor。
- `comparison/reading-plan.md`: core / supporting 阅读计划和优先级。
- `comparison/agent-sft-data-synthesis.md`: 第一版 comparison；学习入口，按方法家族、data action、ablation 和 guardrail 组织。
- `comparison/data-mixture-comparison.md`: 数据配比专门 comparison；按 bucket、validation slice、target/general、最小 mixture 实验组织。
- `comparison/benchmark-to-data-actions.md`: benchmark failure -> meta-skill -> data action 映射；后续最重要的训练数据决策文件。
- `comparison/data-mechanisms.md`: data mechanism 字段规范。
- `scripts/autoresearch.py`: 本地 hygiene / lookup / audit / pack helper。
- `/Users/chy/Research/agentic-rl/`: Agentic RL 独立项目。
