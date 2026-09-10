# Agentic RL Research Workspace

> 本文件收窄 `~/Research/AGENTS.md`。当前目录用于调研 **Agentic RL**：通过 environment interaction、reward、policy optimization、exploration 和 credit assignment 训练 agent。

## 当前目标

建立 Agentic RL 的独立文献地图，优先理解：

- environment rollout 如何进入 RL learning loop。
- reward / verifier / feedback 如何定义。
- tool-use RL、web/GUI/coding agent RL、multi-turn environment RL。
- long-horizon credit assignment、online exploration、replay / off-policy data。
- SFT warm start 与 RL upper bound / exploration 的关系。
- 哪些论文是 survey seed、strong baseline、frontier candidate、low-confidence novelty-risk。

## 和 Agent Data 的边界

迁到 `/Users/chy/Research/agent-data/`：

- 核心贡献是 training data generation / filtering / verification / repair / curriculum。
- RL 只是 data consumer，或者论文重点是 rollout selection / replay selection / data curation。

留在本项目：

- 核心贡献是 reward design、policy optimization objective、RL update mechanics。
- online exploration、long-horizon credit assignment、on/off-policy update。
- environment interaction protocol 主要服务 RL learning loop。

两边都有实质贡献时：本项目写 RL 视角卡；Agent Data queue 记录 data 视角。

## 当前入口

进入项目时先读：

1. `doc/memory/STATE.md` — 当前状态和下一步。
2. `comparison/queue.md` — 当前脚本主队列。
3. `doc/templates/l1-card.md` — L1 card 模板。
4. `doc/taxonomy/failure-modes.md` — failure mode 词表。
5. `doc/taxonomy/design-knobs.md` — design knob 词表。
6. `doc/retrieval-strategy.md` — 本项目怎么找论文。
7. `doc/acceptance-rules.md` — 本项目什么论文可以进 queue / 抽卡。

需要解释稳定选择时再读：

- `doc/memory/DECISIONS.md`
- `doc/memory/OPEN-QUESTIONS.md`
- `comparison/seed-queue.md`、`comparison/survey-derived-full-queue.md` — seed/source queue 历史与来源说明。

## Autoresearch 硬门槛

- Queue row 不是 card；survey mention 只是 recall signal，不是论文证据。
- `notes/` 根目录只放正式 L1/L2 note；survey-only formal card 是历史错误，必须移出正式 notes 或标成 invalid。
- `notes/provisional-survey-derived/` 是 legacy cleanup 隔离区，不是正常抽卡流程。
- 没有 original paper PDF/HTML brief，不写正式 L1 card。
- 大批量抽卡前后都运行 `scripts/autoresearch.py validate`；最终汇报必须说明 queue / brief / valid card / provisional 的计数。
- L1 card body 使用 `doc/templates/l1-card.md` 的机制表；不要再写 `Selection Basis`、`Bounded Brief`、`RL Mechanism`、`和 Agent Data 的关系` 这类旧栏目。

## 目录约定

- `doc/`: 主题规则、模板、taxonomy、memory。
- `notes/`: Agentic RL L1/L2 paper notes；不要放纯 Agent Data notes。
- `comparison/`: 结构化对比、seed queue、总结报告。
- `papers/`: PDF 镜像或临时下载。
- `_meta/`: 后续脚本生成物；不手动维护 generated files。
- `scripts/autoresearch.py`: 项目本地 hygiene helper；支持 `status`、`validate`、`lookup`、`audit`、`pack`，`sync` 仅作兼容 alias。

## L1 Card metadata

新写或重写 L1 card 使用短 YAML + 尾部 `<!-- meta: ... -->`：

- 开头 YAML 放 Obsidian-friendly fields：`failure_modes`、`design_knobs`、`rl_env`、`rl_interaction`、`rl_reward`、`rl_credit`。
- `failure_modes` 必须来自 `doc/taxonomy/failure-modes.md`。
- `design_knobs` 必须来自 `doc/taxonomy/design-knobs.md`，表示方法改了 RL training loop 的哪个设计位点。
- 不再给新卡写 nested `rl_axes`；旧卡可以暂留，validator 兼容迁移期。
- `authors`、`url`、`arxiv_id`、`pdf`、`brief`、`survey`、`rl_optimizer`、`rl_data_reuse`、`rl_warm_start` 等 source / low-frequency metadata 放尾部 HTML meta。

## 研究约束

- 不把普通 Agent Data 论文放进这里，除非它直接影响 RL warm start、rollout data、reward learning 或 exploration。
- 不因为论文用了 environment-generated data 就自动收录；先判断核心是否是 RL learning loop。
- L1 是 research index，不写全文综述；全面精读写 L2。
- 报告必须标注事实 / 解释 / 猜测 / 开放问题。
