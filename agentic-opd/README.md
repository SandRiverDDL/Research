# Agentic OPD

研究多轮 Agent / tool-use 场景的 on-policy distillation：student 访问哪些状态，teacher 如何监督，训练更新如何改善长程任务表现。

- [项目范围与操作约定](AGENTS.md)
- [当前状态](doc/memory/STATE.md)
- [本地资料入口](synthesis/seed-sources.md)
- [ARIS 研究 Wiki](research-wiki/index.md) · [首篇样例：TCOD](research-wiki/papers/wang2026_tcod_exploring_temporal.md)
- [Awesome-Agentic-OPD 完整筛选与综合](research-wiki/awesome-agentic-opd-review.md)：70篇去重论文，24篇保留、46篇排除。

当前使用 **ARIS wiki**。Research workflow / autoresearch 已于 2026-10-14 在本项目停用：不默认维护旧 queue、L1/L2 cards、brief 或运行 card validator。旧文件保留，其他 Research 项目不受影响。

研究目录：`papers/` 放论文，`research-wiki/` 放 ARIS 知识页面，`synthesis/` 放按任务需要的跨论文分析，`doc/` 放规则和 memory。

## ARIS

已安装 8 个 Codex skills：`idea-creator`、`novelty-check`、`research-review`、`research-refine`、`experiment-plan`、`research-wiki`、`wiki-enrich`、`research-lit`，以及依赖 `shared-references`。

本地源码：`/home/chy/code/external/aris`；核验版本：`26b95cfa0d8747078e9e43b42e20952709e561b8`（2026-10-14）。安装链接位于本项目 `.agents/skills/`，机器相关链接与清单不提交。

从本目录恢复安装：

```bash
bash /home/chy/code/external/aris/tools/install_aris_codex.sh "$PWD" \
  --skills experiment-plan,idea-creator,novelty-check,research-refine,research-review,research-wiki,wiki-enrich,research-lit \
  --quiet --no-doc
```

通用恢复说明见 [Research ARIS 文档](../doc/aris-setup.md)；其中历史版本与本项目当前版本可能不同，以本页和本地 manifest 为准。换机需先恢复 ARIS 源码并调整路径。

在 Codex 中以本目录打开任务以发现项目 skills。外部 reviewer / MCP 服务的可用性需要另行核验。

## 验证范围

ARIS helper 负责入库、去重、索引与 query pack。结构和链接用脚本检查；方法、实验数字与结论依据由原文阅读核查。TCOD 首次样例使用了临时 Python 检查，尚无项目级持久化 wiki validator，详见 [样例检查记录](research-wiki/LINT_REPORT.md)。
