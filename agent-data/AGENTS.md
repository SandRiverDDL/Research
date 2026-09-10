# Agent Post-Training Data Research Workspace

> 本文件收窄 `~/Research/AGENTS.md`。当前目录仍叫 `agent-data/`，但研究对象已经初始化为 **Agent Post-Training Data**：LLM agent 后训练阶段的数据机制，尤其是轨迹、工具调用、环境反馈、失败样本和 verifier 信号如何进入 SFT / pre-RL / RL pipeline。

## 项目定位

本项目是 **goal-driven literature map**，不是普通领域综述项目。

中心目标：

```text
benchmark bad case -> agent SFT data action -> ablation / mixture -> stronger model
```

因此，论文是否收录不由“是否属于 Agent Data 领域”单独决定，而由它是否能改变当前 30B A3B MoE agent SFT 的数据决策决定。

### Frontier closed 阵营 disclosure 元结论

本项目方法论**故意聚焦 TR-anchored 工业共识 + 论文方法对照**，而不是把 frontier closed 阵营放进同一份证据库。原因：Anthropic / OpenAI / Gemini 3 / Meta frontier 都已收敛到 blog + system card 的 disclosure floor，没有 training-recipe 级公开材料可以加入第一档共识。closed 阵营信号有研究价值，但只能作为方向 signal（见 `comparison/industry-tr-data-practices.md` §8），不进 reject-pipeline 主线证据。看到 closed 阵营 disclosure 不够时**不要**误判为项目缺口；这是有意识的方法论选择。

核心问题：

- 看到 benchmark failure 后，应该合成、挖掘、过滤、mask、修复或重加权哪类数据？
- 哪些 agent trajectory / tool-call / observation / artifact / verifier data 能直接改善 agent 能力？
- 多个候选数据包之间如何做 ablation、mixture search 和 regression guardrail？

## 当前目标

建立 Agent 后训练数据机制的文献地图，优先理解：

- agent trajectory / tool-call / observation-action data 如何生成、记录和切分。
- synthetic agent traces、teacher traces、self-generated traces、real-world logs 如何验证。
- success / failure trajectories 如何筛选、局部 mask、修复、对比、挖掘或蒸馏。
- verifier / judge / executable environment / format validity 如何作为 data selection signal。
- curriculum / difficulty sampling / student-feedback / environment-feedback 如何形成 data flywheel。
- 这些 data mechanisms 如何服务 SFT、pre-RL、RLVR / agentic RL warm start 或 eval-only。

本项目不是成熟社区综述类目。它是 `llm-post-training-data` 下的 agent 子方向：横切 tool-use、web/GUI/coding agent、data-centric alignment、synthetic data、verifier filtering 和部分 agentic RL 的 **data mechanism lens**。

## 和 LLM Post-Training Data 的关系

本项目只覆盖 LLM post-training data 的 agent 子集。

收录：

- Agent SFT / trajectory imitation / tool-call supervision。
- 可验证 synthetic trajectory / executable environment。
- real-world long-horizon logs，例如 PR sequence、IDE / browser / GUI interaction history。
- search / rollout / critic 结果蒸馏成 supervised data。
- verifier / judge / reward / environment success 做 data filtering 或 reweighting。
- metacognitive scaffold / failure-switching data recipe，只要核心是训练数据或 scaffold 设计。

不作为主线：

- pretraining corpus / web-scale dedup / tokenizer / data mixture。
- 普通 instruction tuning 数据，除非直接影响 agent trajectory / tool / environment interaction。
- 纯 RL optimizer / reward objective / online exploration algorithm。

## Core vs Supporting

本项目区分两类文献：

- **core agent SFT data**：agent-specific 数据论文，回答“造什么 agent 数据”。例如 trajectory、tool-call、observation、artifact、environment feedback、verifier-selected traces。
- **supporting methods**：不一定 agent-specific，但能服务 agent SFT 数据决策的方法，回答“这些数据怎么选、怎么配、怎么消融”。例如 data mixture optimization、target/general data regularization、benchmark-driven data flywheel。

Supporting methods 可以抽卡，但必须标成 `paper_type: data-flywheel-method` 或 `background`，不要污染 core agent data taxonomy。

不收录不能改变数据决策的热门论文；venue / citation / SOTA claim 只是弱证据。

## 和 Agentic RL 的边界

收录到本项目：

- 核心贡献是 training data 的生成、选择、验证、修复、重加权、课程化。
- 即使论文服务 RL，只要新意在 data pipeline，而不是 RL objective / policy update，也先放这里。
- SFT warm-start data、offline trajectory data、rollout filtering、failure mining、verifier-based data curation。
- RL 只是 data consumer，或论文重点是 rollout / replay / trajectory 的选择、清洗、局部监督。

迁到 `/Users/chy/Research/agentic-rl/`：

- 核心贡献是 reward design、policy optimization objective、RL update mechanics。
- online exploration、long-horizon credit assignment、on/off-policy RL algorithm。
- environment interaction protocol 主要服务 RL learning loop，而不是数据生成/筛选。

两边都有实质贡献时：本项目只写 data 视角卡，并在卡里标 `rl_overlap: true`；RL 视角登记到 `/Users/chy/Research/agentic-rl/comparison/seed-queue.md`。

## 当前入口

进入项目时先读：

1. `doc/memory/STATE.md` — 当前状态和下一步。
2. `comparison/queue.md` — 当前脚本主队列。
3. `doc/acceptance-rules.md` — 什么论文可以进入 queue / 抽正式 L1。
4. `doc/retrieval-strategy.md` — 本项目怎么找论文。
5. `doc/templates/l1-card.md` — L1 card 模板。
6. `doc/taxonomy/failure-modes.md` 和 `doc/taxonomy/design-knobs.md` — 稳定 tag 词表。
7. `doc/agent-data-scope.md`、`comparison/seed-sources.md`、`comparison/data-mechanisms.md` — 旧 Agent Data scope 和 seed 背景。

需要解释稳定选择时再读：

- `doc/memory/DECISIONS.md`
- `doc/memory/OPEN-QUESTIONS.md`

## Literature Pipeline 硬门槛

- Queue row 不是 card；survey mention 只是 recall signal，不是论文证据。
- 没有 original paper PDF / HTML / bounded brief，不写正式 L1 card。
- `notes/` 根目录只放正式 L1/L2 note；临时候选、survey-only stub、未验证卡不要放入正式 notes。
- 大批量抽卡前后运行 `scripts/autoresearch.py validate`；最终汇报说明 queue / brief / PDF / valid card / warning 计数。
- `scripts/autoresearch.py` 只做 hygiene / lookup / audit / pack，不替代研究判断。

## 目录约定

- `doc/`: 主题规则、模板、taxonomy、memory。
- `notes/`: Agent Post-Training Data L1/L2 paper notes；不要放纯 Agentic RL notes。
- `comparison/`: queue、seed、结构化对比、crosscut、总结报告。
- `papers/`: PDF 镜像或临时下载。
- `_meta/`: 后续脚本生成物；不手动维护 generated files。
- `scripts/autoresearch.py`: 项目本地 hygiene helper；支持 `status`、`validate`、`lookup`、`audit`、`pack`、`sync`。

## L1 Card metadata

新写或重写 L1 card 使用短 YAML + 尾部 `<!-- meta: ... -->`：

- 开头 YAML 放 Obsidian-friendly fields：`paper_type`、`lifecycle_role`、`boundary_risk`、`failure_modes`、`data_knobs`、`agent_domain`、`data_object`、`data_source`、`selection_signal`、`adaptivity`、`failure_use`、`training_consumer`。
- `failure_modes` 必须来自 `doc/taxonomy/failure-modes.md`。
- `data_knobs` 必须来自 `doc/taxonomy/design-knobs.md`，表示方法改了 agent data pipeline 的哪个设计位点。
- `authors`、`url`、`arxiv_id`、`pdf`、`brief`、`survey`、`agentic_rl_overlap` 等 source / low-frequency metadata 放尾部 HTML meta。
- 旧 nested `data_axes` 不再给新卡使用；旧卡可逐步迁移。

## 研究约束

- 不按社区综述目录直接建类；本项目按 benchmark failure -> data action -> ablation/mixture 的实用链路组织。
- 不做完整领域综述；优先读 recipe、data section、ablation、mixture 和 benchmark slice，而不是读 claim。
- 不因为论文使用 RL 就自动迁出；先判断新意是否在 data。
- 不因为论文有 SFT warm start 就自动收录；SFT 只是普通初始化时，迁到 Agentic RL。
- 2023/2024 agent 总综述默认只当 historical background；当前 seed 优先 2026，最早放宽到 2025Q4。
- L1 是 research index，不写全文综述；全面精读写 L2。
- 报告必须标注事实 / 解释 / 猜测 / 开放问题。
