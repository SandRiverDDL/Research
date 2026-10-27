# OPD Research Workspace

> 本文件只负责 OPD 项目的任务路由与硬约束，并收窄 `~/Research/AGENTS.md`。

## 目标

形成可投顶会的 OPD 工作：从经典论文学习机制，从近期顶会论文学习 research taste 和 idea pattern。

## 按任务读取

- 启动：`doc/memory/STATE.md`
- 找论文或决定是否抽卡：`doc/card-acceptance.md`
- 写新卡：`doc/templates/l1-card.md`
- 运行文献流程或脚本：`doc/codex-research-process.md`
- 追溯原因或未决问题：`doc/memory/DECISIONS.md` / `OPEN-QUESTIONS.md`

不要为普通任务加载历史 archive。

## 硬约束

- 严格执行用户确认的最小规则；未经要求，不新增字段、层级、评分、taxonomy、例外或自动产物。
- L1 只作检索索引；关键 bottleneck、novelty 和 idea claim 必须回查原文。
- 71 张旧卡不因 schema 或流程变化而迁移。
## ARIS 工具依赖

- ARIS 是可选的本机工具；研究成果和自定义 skills 保存在本仓库。
- 源码独立位于 `~/code/external/aris/`；安装生成的 skill 链接和清单不提交。
- 使用 ARIS workflow 前，确认本项目 `.agents/skills/` 中的相关链接可用；缺失时按 [恢复说明](../doc/aris-setup.md) 安装。
- 不直接修改软链接指向的 skill；上游源码的本地修改须同步保存到 `doc/aris-local-changes.patch`（相对 Research 根目录）。
- 安装或更新时使用 `--no-doc`，避免把本机绝对路径重新写入本文件。


- ARIS 工作目录和输出范围固定为本主题 `opd/`，不要因 Git 根目录是 Research 而切换到 Research 根目录运行研究流程。
- `research-refine` 仅用于用户明确要求细化自己的 idea / proposal 或显式调用该 skill；解释、总结、比较、复现外部论文或代码，以及普通技术追问，不触发该流程。此项目规则替代旧版本的触发范围补丁。
