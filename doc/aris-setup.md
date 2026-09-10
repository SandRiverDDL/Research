# ARIS 安装与研究仓库的边界

Research 保存研究内容、自定义 skills 和必要的过程记录。ARIS 源码及其安装生成的链接、清单由每台电脑自行恢复。阅读笔记不需要安装 ARIS；运行相应 workflow 才需要。

- `external/aris/`：第三方源码，不提交。
- `aris/`：独立研究工作目录；当前安装 83 个上游 skills。
- `opd/.agents/skills/`：6 个上游 skill 链接不提交；自定义 `generate-method-ideas/` 保留。
- `opd/.aris/traces/`、`opd/idea-stage/`、`opd/refine-logs/`：研究过程和成果保留。
- `.gitignore` 按现有安装项逐项排除链接，不整体排除 skills 或 traces。以后新增上游 skills 时需补相应规则。

## 在新电脑恢复

以下命令从克隆后的 Research 根目录执行，适用于尚未安装 ARIS 的新副本。已有 `external/aris/` 时不要重复 clone 或重复应用补丁；先检查其版本和本地修改。

```bash
research_root="$PWD"
git clone https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep.git external/aris
git -C external/aris checkout f4f20f90ead9cb8d68e830ee5b006121adc41f80
git -C external/aris apply --check "$research_root/doc/aris-local-changes.patch"
git -C external/aris apply "$research_root/doc/aris-local-changes.patch"

bash external/aris/tools/install_aris_codex.sh "$research_root/opd" --skills experiment-plan,idea-creator,novelty-check,research-refine,research-review --quiet --no-doc
bash external/aris/tools/install_aris_codex.sh "$research_root/aris" --all --quiet --no-doc
```

安装脚本会按新电脑路径重新生成链接和清单。只有使用 OPD 时可省略最后一条独立 ARIS 工作目录安装命令。

## 更新本地 ARIS 修改

当前补丁保存两份 `research-refine/SKILL.md` 的修改，基准版本记录在 `aris-local-changes-base.txt`。今后修改上游已追踪文件后，在 Research 根目录更新补丁：

```bash
git -C external/aris diff --binary HEAD > doc/aris-local-changes.patch
```

此命令不包含上游仓库的未追踪新文件；若新增文件，需要另外纳入可恢复的备份。升级上游版本时，同时更新基准记录、本说明中的 checkout 版本和补丁。

## 原子仓库历史

整合前 `opd/`、`aris/` 的 Git 元数据保存在 `.local-git-backup/20260910-234231/`，仅在本机保留且被忽略。总仓库将从当前文件快照开始；这些旧提交不会随总仓库上传。
