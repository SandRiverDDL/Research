# MOPD

研究多个 teacher 如何通过 on-policy distillation 把能力整合进一个 student，目标是有实质贡献、可规模化的方法论文。

- [范围与约定](AGENTS.md)
- [当前状态](doc/memory/STATE.md)
- [论文入口](synthesis/seed-sources.md)
- [36篇文献地图](research-wiki/topics/multi-teacher-opd.md)
- [跨论文综述与证据边界](synthesis/mopd-literature-review.md)
- [MOPD领域图景与四个问题主题](synthesis/mopd-gap-analysis.md)
- [ARIS Wiki](research-wiki/index.md)

与 [通用 OPD](../opd/AGENTS.md) 和 [Agentic OPD](../agentic-opd/AGENTS.md) 并列；交叉论文链接已有记录。当前有36篇已填正文的论文页（15篇seed+21篇补搜），含版本化原文与结果边界；更广系统报告和垂直方法仍有待读入口。

`papers/` 放需要保存的原论文，`notes/` 放临时阅读笔记，`synthesis/` 放跨论文分析，`research-wiki/` 保存正式知识页面。

项目参考 Research 新项目模板的范围、memory、seed 和目录结构，按 ARIS wiki 流程裁剪；不创建停用的 card pipeline。

已沿用 Agentic OPD 的 8 个 ARIS skills 及共享依赖。换机后，先恢复 ARIS 源码，再从本目录执行（按实际源码位置调整路径）：

```bash
bash /home/chy/code/external/aris/tools/install_aris_codex.sh "$PWD" \
  --skills experiment-plan,idea-creator,novelty-check,research-refine,research-review,research-wiki,wiki-enrich,research-lit \
  --quiet --no-doc
```

本机链接与安装清单由 installer 管理；初始化不代表 reviewer / MCP 已配置。
