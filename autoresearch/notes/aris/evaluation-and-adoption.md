# ARIS：evaluation 与个人采用判断

> 返回 [overview.md](overview.md)。本页严格区分 operational adoption、作者自报 trajectory、community self-report 与 independent scientific evaluation。

## 1. Operational snapshot（带日期，不外推质量）

**事实，2026-07-22**：GitHub 主分支 `53562a7…` 当天有提交；页面约 13.7k stars、1.2k forks、1,056 commits、44 issues、12 PRs；最新 release `v0.4.22` 于 2026-07-12 发布；审计 commit 有 81 个 top-level skills。[GitHub repo](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)；[releases](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/releases)

**解释**：这些信号支持“维护频繁、社区有采用、不是一次性论文代码”。它们不支持“论文产出更正确”“成功率高”或“SOTA”。

## 2. 官方 overnight run 能说明什么

**自报事实**：README 与技术报告描述一个约 8 小时、4 轮的真实 ML project trajectory：20+ GPU experiments，AI reviewer score 从 5.0 提到 7.5；过程中关键 improvement claim 未复现、大 seed study 杀掉主提升 claim，最终改成 diagnostic evidence。[README: Score Progression](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/README.md)；[技术报告 p. 13, §5.1](../../papers/aris-2605.03042.pdf)

**可支持的结论**：harness 在至少一条 trajectory 中能运行 experiments、响应 reviewer、删掉失败 claim、恢复并产出新叙事。

**不能支持的结论**：7.5 不是官方 peer-review 分数；single trajectory 不能证明 ARIS 比同算力人工/其他 agent 更好，也不能把分数提升解释为 scientific quality 因果提升。技术报告自己明确称其为 observational evidence，不能归因于 ARIS alone。

## 3. Community runs

**自报事实，2026-07-22 页面状态**：README 展示 3 个 papers/signals：

- CS conference submission：AI simulated review 8/10，等待官方反馈；
- AAAI 2026 submission：Stanford Agentic Reviewer 7/10，等待官方决定；
- UAV-CC：投稿 IEEE TGRS，under review。

README 明确说前两项是 AI-review signals，不是官方 acceptance。[README: Community Showcase](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/README.md)

**判断**：这是 adoption/sample-output 证据，不是 independent benchmark。没有随机样本、失败 run 分母、compute budget、一致实验 protocol 或盲人类评审，不能估计成功率。

## 4. 当前科学证据缺口

技术报告在 §5 与结论中承认缺 controlled evaluation。至少缺：

- compute-matched ARIS vs no-ARIS / same-model self-review / human baseline；
- audit cascade 对预植 integrity bugs 的 precision/recall；
- reviewer-family、executor-family 与 domain 的 factorial ablation；
- 完整 run denominator、失败率、GPU/token/wall-time 分布；
- 独立团队从 clean checkout 复现；
- 真实 conference outcomes 或 expert blind assessment；
- 长期 wiki 是否减少重复失败、是否也造成 stale belief/self-poisoning。

[技术报告 pp. 13–15, §5–§7](../../papers/aris-2605.03042.pdf)

## 5. SOTA 判断

**判断**：在“能实际执行 ML 实验、跨模型 review、文件化恢复、claim assurance、活跃维护”的开源 harness 中，ARIS 属于 **operational frontier / top cohort candidate**，而且满足大仓库、持续维护、完整系统这些实用筛选条件。

它不是 established scientific SOTA：没有独立 benchmark 证明其端到端科研质量、integrity error recall 或真实投稿成功率优于其他系统。更准确的说法是“少数成熟、活跃、可直接部署的全流程 autoresearch harness 之一”。

## 6. 它应该接在现有系统哪里

**判断**：ARIS 最适合做下游，不替代本项目的 literature/cards：

```text
本项目 L1/cards/comparison
  → ResearchStudio-Idea 式 bottleneck + operator + collision
  → 人类选择/冻结 metric contract
  → ARIS experiment plan / bridge / GPU queue
  → ARIS assurance + raw evidence
  → 结果回写 cards / failure modes / insights
```

- cards 提供跨项目、跨系统的持久证据索引；
- ResearchStudio-Idea 提供 idea compiler；
- ARIS 提供 execution、recovery 与 result-to-claim assurance；
- 人负责方向、metric、昂贵 compute、关键 claim 与 submission。

若让 ARIS 自己包办 literature、idea scoring、实验选择和 reviewer termination，整个闭环仍可能被同一个 LLM taste 支配。

## 7. 推荐采用与拒绝采用

### 值得接入

- `done` / `accepted` 分离与 resumable run state；
- experiment plan → sanity → pilot → full run 的 milestone discipline；
- GPU queue 的 OOM retry、dependency/wave gate、crash recovery；
- executor/reviewer fresh-context separation；
- experiment audit、claim ledger、paper claim/citation audits；
- failed ideas/negative results 进入 wiki，而不是被最终 paper 覆盖。

### 不应直接照搬

- 81 skills 全量安装后立即跑 `/research-pipeline`；先选择性安装最小闭环。
- 用 reviewer score 作为循环主 optimization target；改成 hard evidence gates + 人类 stop decision。
- `AUTO_PROCEED=true` 自动从 idea 进入昂贵 GPU；个人默认应关闭。
- 把 “submission-ready” 标签当科学质量证明；它最多说明规定 audits 已完成。
- 把 wiki 变成另一套跨论文 L1 数据库；只保留项目执行状态与 links。

## 8. 最小个人试点

**判断**：不要先移植全系统。选一个已有 codebase、1–2 GPU、24 小时内能出 signal 的方向：

1. 只启用 research wiki、experiment-bridge、experiment-audit、result-to-claim；
2. 人工提供已审核的 idea、baseline、metric 与 budget；
3. `AUTO_PROCEED=false`，禁止自动 submission；
4. 记录 token/API/GPU cost、失败恢复次数、审计发现数及 human false-positive review；
5. 与同一计划的人工执行或普通 Codex/Claude baseline 比较。

只有当它降低了无效 GPU 支出或发现了人工容易漏的 claim/evidence mismatch，再逐步加入 auto-review 与 paper layer。

**开放问题**：最重要的第三方验证不是“它能否再生成一篇 PDF”，而是“在预先冻结的 metric 和预算下，它是否提高有效实验吞吐，同时不增加 false claims”。

