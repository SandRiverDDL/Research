# ARIS：research pipeline

> 返回 [overview.md](overview.md)。主证据：[research-pipeline skill](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/research-pipeline/SKILL.md)、[experiment-bridge skill](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/experiment-bridge/SKILL.md)、技术报告 [§4, pp. 10–12](../../papers/aris-2605.03042.pdf)。

## 1. Idea discovery：不是直接从一句 prompt 跳到论文

**事实**：Stage 1 调 `/idea-discovery`，内部串 `/research-lit → /idea-creator → /novelty-check → /research-review`，输出 `idea-stage/IDEA_REPORT.md`。当前 README 将更完整的 discovery 描述为：survey/landscape 后 brainstorm 8–12 ideas、novelty check、对 top 2–3 做 pilot，再按 empirical signal 排序，并生成 `refine-logs/EXPERIMENT_PLAN.md`。[idea-discovery skill](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/idea-discovery/SKILL.md)；[README workflow 1](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/README.md)

**判断**：ARIS 的 idea 层比 ResearchStudio-Idea 更偏“并行生成→pilot 选择”，不是同样的 corpus-induced operator compiler。它的优势在于能让 early empirical signal 进入选择；弱点是 literature/novelty/reviewer 仍可能同源，taste 没有由统一 pattern evidence contract 约束。

## 2. Gate 1：human checkpoint 是可配置的，不是必然存在

**事实**：`AUTO_PROCEED=false` 时，系统展示 top ideas 后等待用户确认；`true`（skill 当前默认）则展示后等待 10 秒，无输入便选 pilot signal + novelty 最强的 #1。Stages 2–3 涉及 GPU 与多轮 review，skill 明确建议在需要控制成本时关闭 auto proceed。[research-pipeline constants / Stage 1](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/research-pipeline/SKILL.md)

**判断**：个人使用应把 `AUTO_PROCEED=false` 设为默认。让同一系统用自己的 novelty/review/pilot signals 自动决定昂贵实验，会把 evaluator bias 直接转成 compute allocation。

## 3. Experiment Bridge：plan → code → sanity → full run

**事实**：`/experiment-bridge` 的 phase contract：

1. parse experiment plan，提取 milestones、依赖、compute budget；
2. 在新 repo 或 `BASE_REPO` 上实现代码；
3. `CODE_REVIEW=true` 时由 cross-model reviewer 检查 logic、metrics、ground-truth misuse；
4. 先跑最小 sanity experiment，失败自动 debug，最多 3 次并可调用 rescue；
5. 部署完整 experiments；
6. 收集结果到 `EXPERIMENT_RESULTS.md` 与 `EXPERIMENT_TRACKER.md`；主结果正向时再规划 ablation。

[experiment-bridge source](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/experiment-bridge/SKILL.md)

**边界**：这是 runbook 驱动的 agent coding/execution，不是一个统一实验引擎。真正能否执行取决于宿主权限、repo、环境、SSH、metric parser、W&B 和模型能力。

## 4. GPU queue 与远程执行

**事实**：Stage 2 自动按任务形态路由：较少 jobs（文档示例 ≤5）走 `/run-experiment`；较多 jobs（示例 ≥10）或存在 teacher→student phase dependency 时走 `/experiment-queue`。queue 提供 OOM retry、wave gating、crash-safe state；`monitor-experiment` 负责远端进程与结果状态。[research-pipeline Stage 2](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/research-pipeline/SKILL.md)；[experiment-queue](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/experiment-queue/SKILL.md)；[run-experiment](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/run-experiment/SKILL.md)

**解释**：它解决的是 unattended execution 的常见工程问题：OOM、依赖未完成、screen/tmux 进程遗留、结果没落盘、session 中断。它不自动证明实验设计公平，也不保证 cluster scheduler 级别的资源隔离。

## 5. Auto Review Loop：review 触发真实修改与新增实验

**事实**：Stage 3 最多 4 轮：cross-family reviewer 评分并列 weaknesses/minimum fixes；executor 修改代码/论文、运行新 experiments、收结果，再送回 reviewer。默认正向停止条件是 `score ≥ 6/10` 且 verdict 属于 `ready/almost`；context compact 后从 `REVIEW_STATE.json` 恢复。预计超过 4 GPU-hours 的单个建议默认跳过并标 manual follow-up。[auto-review-loop](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/auto-review-loop/SKILL.md)；[research-pipeline Stage 3](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/research-pipeline/SKILL.md)

**风险**：停止条件仍以 reviewer score/verdict 为核心，可能优化成“更像 reviewer 喜欢的论文”。即使新实验是真实的，实验选择、叙事和终止仍可能 reward hack reviewer。raw-evidence audits 能约束夸大，但不能提供领域价值真值。

## 6. Summary → paper

**事实**：Stage 4 从 idea、implementation、configs/results、review history 生成 `NARRATIVE_REPORT.md`，列 core claim、quantitative evidence、figure/table inventory、limitations。默认 `AUTO_WRITE=false`，到这里停止；开启后进入 `/paper-writing`，串 plan、figure、write、可选 proof-checker、paper-claim-audit、compile、improvement loop。submission assurance 下还需要 mandatory audits 通过 deterministic verifier。[research-pipeline Stage 4–5](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/research-pipeline/SKILL.md)；[paper-writing](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/paper-writing/SKILL.md)

## 7. 恢复机制：`done` 不等于 `accepted`

**事实**：长流程状态写入 `.aris/runs/<run_id>.json`。stage 可处于 running/done/accepted；executor 写完 artifact 只能标 done，必须等 cross-model gate 或 deterministic verifier 后才能 accepted。resume 会重跑 running/failed，并重新审计 done-but-unaccepted stage。[resumable runs](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/shared-references/resumable-runs.md)；[pipeline acceptance table](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/research-pipeline/SKILL.md)

**判断**：这是值得直接吸收的工程原则。科研 agent 最危险的不是 crash，而是把“文件生成完了”误当成“科学上成立”。ARIS 至少在状态机里显式拆开两者。

## 8. Human checkpoints 与 unattended heartbeat

**事实**：`HUMAN_CHECKPOINT=true` 可在每轮 review 后暂停；`AUTO_PROCEED` 控制 idea gate；paper writing 在 venue/手工 figure 缺失时也会停。overnight heartbeat 只允许检测 stalled phase、重启/结构性 pivot，不允许自己判定“已经足够好”。[external cadence contract](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/shared-references/external-cadence.md)

**判断**：最佳用法不是完全无人值守，而是：低风险 execution unattended；idea commit、metric contract、claim promotion、submission 四处 human gate。

## 9. Research Wiki：跨 session 的项目记忆

**事实**：`/research-wiki init` 创建 paper、idea、experiment、claim 四类 Markdown entities 与 typed edges。`query_pack.md` 硬限制 8,000 chars，优先保留 gaps 和 failed ideas；idea-creator 读它但仍查最近 3–6 个月文献。`result-to-claim` 新建 experiment node、更新 idea outcome，并把 empirical support 写为 edges；claim 的 proof status 由 proof-checker 独占，两个轴不混写。[research-wiki skill](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/research-wiki/SKILL.md)；[技术报告 pp. 10–11, §4.2](../../papers/aris-2605.03042.pdf)

**判断**：保留 failed ideas 是 ARIS 最适合长期个人系统的设计之一。但不建议让 ARIS wiki 替换本项目 cards：前者是单项目 execution memory，后者是跨系统 evidence map。可以用 stable IDs/links 连接，而不要复制两份全文。

