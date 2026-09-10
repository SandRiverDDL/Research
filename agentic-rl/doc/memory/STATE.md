# Agentic RL 当前状态

> Hot memory for Codex. 当前项目正在补 strict Agentic RL core method。

## 当前目标

调研 Agentic RL：environment interaction + reward + policy update 如何训练 agent。

它和 `/Users/chy/Research/agent-data/` 分开维护。Agent Data 研究数据机制；Agentic RL 研究优化和交互式学习机制。

## 当前边界

收录：

- environment interaction + reward 更新 policy。
- tool-use RL / web RL / GUI RL / coding-agent RL。
- long-horizon agent reward / credit assignment。
- online exploration / self-play / environment curriculum。
- replay / off-policy data 如果核心服务 RL update。
- SFT warm start 如何影响 RL 上限或探索。

迁到 Agent Data：

- training data generation / filtering / verification / repair / curriculum 是核心贡献。
- RL 只是 consumer 或 evaluation。

## 当前流程修正

- 已同步模板 helper 架构：`scripts/autoresearch.py` 支持 status / validate / lookup / audit / pack。
- 正式 L1 card 必须有 original paper PDF/HTML brief；legacy survey-only note 不算 card。
- `notes/provisional-survey-derived/` 是 legacy cleanup 隔离区，不计入 valid L1；当前已清空。
- 20 个此前 survey-only notes 已用 original PDF / bounded paper brief 重新抽正式 L1 card；旧 stubs 已归档到 `_meta/legacy-survey-only/upgraded/`。
- `comparison/queue.md` 是脚本主队列；`seed-queue.md` / `survey-derived-full-queue.md` 保留为来源说明。
- 2026-06-17 新增 strict-core recall：不再只依赖 survey，使用 keyword search、related work、source-verified Codex hypothesis。
- 2026-06-17 最新验证：35 formal notes、0 active legacy survey-only notes、174 queue rows、61 original-paper briefs、4 survey briefs、65 PDFs、0 validation errors。

## 下一步

当用户在本目录会话发出 `找新的论文抽卡` 时：

1. 先读 `comparison/queue.md` 和 `scripts/autoresearch.py status`。
2. 先读 `doc/retrieval-strategy.md`、`doc/acceptance-rules.md` 和 `comparison/strict-core-recall.md`，区分 strict core / recipe / framework / data overlap。
3. Strict core 扩充默认从 high-confidence core seed 做 related recall；keyword direct search 只在阶段开始或发现新术语族时补一轮。
4. 如果发现 data mechanism paper，登记到 `/Users/chy/Research/agent-data/`，不要在本项目写完整卡。
5. 下一批 strict-core 优先核查 AEPO、DynaWeb、RAPO、EMPO^2、EDGE、RLTR、rStar2-Agent 的 code/venue/exception，再决定是否抽卡。

## 当前 seed 状态

- 已有 seed note：`notes/non-grpo-like/2511_environment-scaling-agentic-experience-survey.md`。
- Seed queue：`comparison/seed-queue.md`。
- 脚本主队列：`comparison/queue.md`。
- Strict core recall：`comparison/strict-core-recall.md`。
- 本地检索策略：`doc/retrieval-strategy.md`。
- 本地准入规则：`doc/acceptance-rules.md`。
- 已建立模板式 helper；脚本只做 hygiene / lookup / audit / pack，不做研究判断。

## 关键文件

- `AGENTS.md`: 主题规则。
- `comparison/seed-queue.md`: Agentic RL seed / queue。
- `comparison/queue.md`: 脚本主队列。
- `comparison/strict-core-recall.md`: strict core method recall 候选与筛选状态。
- `doc/retrieval-strategy.md`: 本项目检索循环 / seed 扩展规则。
- `doc/acceptance-rules.md`: 本项目准入 / 抽卡规则。
- `doc/templates/l1-card.md`: L1 card 模板。
- `doc/taxonomy/failure-modes.md`: failure / decision 词表。
- `scripts/autoresearch.py`: 项目本地 hygiene helper。
- `/Users/chy/Research/agent-data/`: Agent Data 独立项目。
