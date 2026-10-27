# ARIS 安装与研究仓库的边界

## 当前安装（2026-09-28）

- ARIS 源码：`~/code/external/aris/`，独立 Git 仓库，不进入 Research 的提交范围。
- 本次从上游默认分支 clone，版本：`341f914024d270dc5c8fa51337d1ad38829273aa`。
- OPD 安装五个 Codex skills：`experiment-plan`、`idea-creator`、`novelty-check`、`research-refine`、`research-review`，以及依赖的 `shared-references`。
- 项目入口：`opd/.agents/skills/`；安装清单：`opd/.aris/installed-skills-codex.txt`。这些机器相关项已被 Git 忽略。
- 自定义 `generate-method-ideas`、现有笔记和 `.aris/traces/` 保留。未新建或修改 wiki，未迁移论文笔记，未配置外部 reviewer 服务。OPD 已有旧 `research-wiki/`（含 ideas、query_pack 等），后续流程可能自动读取，使用前应核对其时效性。
- OPD 的 Git 根目录是 Research；运行研究流程时仍以 OPD 为工作目录和输出边界。

## 在新电脑恢复

以下命令在 Research 根目录执行。若源码目录已存在，先检查版本和本地修改，不要重复 clone。

```bash
research_root="$PWD"
aris_source="$HOME/code/external/aris"
mkdir -p "$HOME/code/external"
git clone https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep.git "$aris_source"
# 复现本次安装；若有意升级，先检查目标版本变更。
git -C "$aris_source" checkout 341f914024d270dc5c8fa51337d1ad38829273aa
bash "$aris_source/tools/install_aris_codex.sh" "$research_root/opd" --skills experiment-plan,idea-creator,novelty-check,research-refine,research-review --quiet --no-doc
```

安装器生成项目链接、安装清单和 `~/.aris/repo` 工具定位文件。使用 `--no-doc` 保留手写的 AGENTS.md；安装后重新打开 OPD 任务，使技能目录重新发现。

## 旧目录与补丁

- 2026-09-28 检查时，旧 `Research/aris/` 仅有 `AGENTS.md`，没有论文、wiki 或研究结果。截至 2026-10-27，该目录已从工作副本移除；研究内容保存在各主题目录，恢复时不再创建旧独立入口。
- 此检查仅覆盖本机当前工作副本，不代表旧电脑上被 Git 忽略的内容也为空。
- 旧源码位置 `Research/external/aris/` 在本机不存在。
- `doc/aris-local-changes.patch` 和 `doc/aris-local-changes-base.txt` 保留作为历史记录。旧补丁不能直接应用于本次新版，未强行应用。
- 旧补丁只限制 `research-refine` 的触发范围；该限制现在写入 `opd/AGENTS.md`，新版源码保持无本地修改。

## 原子仓库历史

整合前 `opd/`、`aris/` 的 Git 元数据原先保存在 `.local-git-backup/20260910-234231/`，属于被忽略的本机备份，不保证已随换机恢复。
