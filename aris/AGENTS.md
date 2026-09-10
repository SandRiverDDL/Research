# ARIS 独立项目

这个目录是 ARIS 的隔离运行项目。这里专门放 ARIS 生成的文献、idea、review、实验计划和论文草稿。

- 优先使用本项目 `.agents/skills/` 下由 ARIS 管理的 Codex skills。
- 不要把 ARIS 的 skills 或输出扩散到 `~/Research` 的其他研究主题。
- 论文、idea 和实验产物都保存在本目录内；真正的训练任务按需要转移到 `~/Code/` 或远程 GPU 环境。
## ARIS 工具依赖

- ARIS 是可选的本机工具；研究成果和自定义 skills 保存在本仓库。
- 源码位于 Research 根目录的 `external/aris/`；安装生成的 skill 链接和清单不提交。
- 使用 ARIS workflow 前，确认本项目 `.agents/skills/` 中的相关链接可用；缺失时按 [恢复说明](../doc/aris-setup.md) 安装。
- 不直接修改软链接指向的 skill；上游源码的本地修改须同步保存到 `doc/aris-local-changes.patch`（相对 Research 根目录）。
- 安装或更新时使用 `--no-doc`，避免把本机绝对路径重新写入本文件。

