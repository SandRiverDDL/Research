# ARIS source dossier

> 唯一入口。对象：[ARIS / Auto-Research-In-Sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/53562a7c64cc1d55946cba1fb8a8416137143d14)，源码快照固定于 `53562a7c64cc1d55946cba1fb8a8416137143d14`（2026-07-22）。技术报告镜像：[aris-2605.03042.pdf](../../papers/aris-2605.03042.pdf)。

## 一句话定位

**事实**：ARIS 是一个 research harness / methodology，而不是训练出来的独立科研模型。审计 commit 下有 81 个主要由 `SKILL.md` 定义的 skills，并用 plain-text artifacts、Python helpers、MCP bridges 和宿主 agent 的 shell/file/tool capability 串成 idea → experiment → review → paper 工作流。[repo README](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/README.md)；[技术报告 §4, pp. 10–12](../../papers/aris-2605.03042.pdf)

**判断**：ARIS 的核心价值不是“自动写论文的 prompt 数量”，而是把长科研轨迹拆成可恢复、可检查、可由不同模型扮演 executor/reviewer 的工序，并加入从 raw experiment 到 manuscript claim 的 assurance chain。

## 怎么运行：Claude Code、Codex、GPU、API 分别做什么

### 默认形态

**事实**：官方 setup 推荐 macOS 上 Claude Code 做 executor，Codex 以 MCP server 做 cross-family reviewer；skills 通过项目本地 symlink 安装到 `.claude/skills/`，`.aris/tools` 指向 helper scripts。Codex-as-executor、Cursor、Trae、Antigravity、Copilot CLI、OpenClaw 等也有适配；另有独立 ARIS-Code CLI。[SETUP_GUIDE](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/SETUP_GUIDE.md)；[README: host support](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/README.md)

推荐安装大意：

```bash
git clone https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep.git ~/aris_repo
cd <your-research-project>
bash ~/aris_repo/tools/install_aris.sh
```

Codex 作为 executor 有单独 installer/适配说明；不用把整个研究流程写成一次 API request。技能是宿主内的 slash command，例如：

```text
/research-wiki init
/idea-discovery "research direction"
/experiment-bridge "refine-logs/EXPERIMENT_PLAN.md"
/auto-review-loop
/research-pipeline "research direction"
```

### GPU

**事实**：GPU 不是 ARIS 本体的一部分，而是实验后端。`experiment-bridge` 可把实验交给 local GPU、remote SSH、Vast.ai 或 Modal；job 多或有 teacher→student 依赖时可走 queue。没有 GPU 仍能用 literature/review/writing skills，但新增实验会被标为 manual follow-up。[GPU setup](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/docs/GPU_SETUP.md)；[research-pipeline skill](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/research-pipeline/SKILL.md)

### 成本

**事实**：仓库 MIT 开源；成本来自宿主模型/订阅或 API、cross-model reviewer calls、可选 OpenRouter/Oracle 等路由、文献服务，以及实际 GPU compute。官方提供多模型组合与部分 free-tier route，但 assurance 级判断要求 reviewer 与 executor 不同 family，并推荐固定 reviewer backend。[model combinations](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/docs/MODEL_COMBINATIONS.md)；[reviewer routing](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/53562a7c64cc1d55946cba1fb8a8416137143d14/skills/shared-references/reviewer-routing.md)

**判断**：如果已有 Codex/Claude Code 订阅和自己的 GPU，ARIS 可主要消费订阅额度与本地算力；若所有 reviewer、长上下文和 GPU 都按量付费，完整 overnight pipeline 仍然昂贵。真正成本通常是错误实验与无人检查的远程执行风险，而不只是 token 单价。

## 系统分层

**事实**：技术报告将系统概括为三层：

1. **Execution**：可单独调用的 Markdown skills、工具、research wiki；
2. **Orchestration**：workflow chaining、artifact contracts、resume/checkpoints、reviewer routing；
3. **Assurance**：cross-family reviewer、实验/claim/citation/paper audits。

[技术报告 §2–§4, pp. 4–12](../../papers/aris-2605.03042.pdf)

## 真实主流程

```text
literature / idea discovery
  → novelty + pilot + experiment plan
  → implement / code review / sanity / GPU runs
  → result collection + audit + claim mapping
  → adversarial review / fixes / more experiments
  → narrative handoff / paper / audits / compile
```

`/research-pipeline` 默认串 Idea Discovery、Experiment Bridge、Auto Review、Summary；paper writing 默认不自动开启，需 `AUTO_WRITE=true`。每 stage 的 `done` 与 `accepted` 分开，中断可从 `.aris/runs/<run_id>.json` 恢复。[详见 research-pipeline.md](research-pipeline.md)

## 维护与社区成熟度快照（2026-07-22）

**事实**：审计日主分支 `53562a7…` 当天仍提交；GitHub 页面约 13.7k stars、1.2k forks、1,056 commits、44 open issues、12 PRs。最新 release 为 `v0.4.22`，GitHub 显示 2026-07-12 发布。skills 数在审计 commit 为 81。[GitHub snapshot](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)；[releases](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/releases)

**解释**：这足以说明它是活跃、有明显社区采用的 operational system；81 skills 与千次提交也意味着接口/行为变化快、复杂度高。stars/releases 不能证明其研究产出质量。

## 适用边界与风险

- **适合**：已有明确方向/代码库/GPU，希望把实验执行、失败恢复、review 与 paper evidence 对齐做成 harness。
- **不适合直接全自动**：敏感代码、昂贵或危险的远程任务、缺少可信 metric 的项目、需要湿实验/伦理审批的任务。
- **核心残余风险**：reviewer 仍是 LLM；cross-family 降低相关错误但不等于独立真值。循环还可能过拟合 reviewer taste。
- **安全事实**：技术报告明确提醒 repo-level review 可能把代码发给外部 API，local-only reviewer routing 当时尚未实现。[技术报告 pp. 13–14, §5.2](../../papers/aris-2605.03042.pdf)

## 本 dossier 导航

- [research-pipeline.md](research-pipeline.md)：literature/idea 到 GPU、review、paper 的真实工作流、queue、recovery、human checkpoints、wiki。
- [experiment-assurance.md](experiment-assurance.md)：`experiment-audit → result-to-claim → paper-claim-audit → citation-audit` 的职责与盲区。
- [evaluation-and-adoption.md](evaluation-and-adoption.md)：社区 run、自报分数、scientific evidence 缺口，以及如何接在本项目下游。

