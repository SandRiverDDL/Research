# Conference Literature Index

共享的顶会 metadata 缓存。它只负责机械检索，不保存研究 taxonomy，也不替代 Zotero、L1 cards 或原文。

```bash
# 在克隆后的 Research 根目录执行；脚本只依赖 Python 标准库。

# 同步官方 metadata
python3 literature-index/index.py sync --venue all --year 2026

# 检索；默认所有词都命中，--any 表示任一词命中
python3 literature-index/index.py search "on-policy distillation" --year 2026
python3 literature-index/index.py search "agent data selection" --any --limit 20 --json

# 查看覆盖范围
python3 literature-index/index.py status
```

当前来源：

- ICLR / ICML：会议官网一次性 JSON；仅保留官方 Conference track 的 accepted papers。
- ACL：ACL Anthology 的 long / short 主会 MODS XML。

ICLR / ICML 的批量源包含摘要和作者机构；ACL 的批量 XML 当前只包含题目、作者和正式链接，摘要等信息只对 shortlist 再补查。

`papers.sqlite` 是可重新生成的本地缓存，不应进入版本控制。代码、数据和机构补充核验只对检索后的 shortlist 进行。

## 本地索引盘点与来源（2026-10-27）

以下来自本地文件、数据库同步记录和已有来源清单；本轮没有重新下载，也没有核实网址当前是否仍可访问。路径均相对 Research 根目录，大小为当前工作副本的近似值。会议记录随日期、track 范围和去重方式变化，不把不同快照的条数差异直接当作数据丢失。

| 位置 | 当前内容与覆盖范围 | 来源记录与恢复能力 |
| --- | --- | --- |
| `literature-index/papers.sqlite`（约 42 MiB） | 2026 ICLR 5,575、ICML 6,341、ACL 主会 long/short 2,296；合计 14,212。ICLR/ICML 均有摘要，ACL 无摘要 | `index.py` 可从下表网址重建；原数据库 `sync_runs` 保存网址与同步时间。本次各场最后同步均为 2026-10-23，详见下表 |
| `literature-index/tmp/neurips-2026-index/`（约 45 MiB） | 2026-10-14 旧快照；规范化文件 6,514 条，另有 oral/spotlight 子集、摘要补查和后训练 shortlist | 原始 JSON 的网址、下载时间和哈希原已记在该目录 `sources.json`；下文保留关键来源。不是 `index.py sync --venue all` 的一部分 |
| `literature-index/tmp/emnlp-2026-availability-20261014/`（约 1.5 MiB） | 2026-10-14 的来源可用性核查、官方日程 CSV 与页面缓存；不是完整摘要索引 | `availability.json`、`followup.json` 保存当时网址与响应状态；日程来源见下文。历史 404/403 不能代表当前状态 |
| `literature-index/tmp/emnlp-2026-post-training/`（约 3.7 MiB） | 文本 LLM 后训练专项筛选，标题审阅 1,179 条：include 403、uncertain 464、exclude 312；另含部分摘要结果 | 依赖 EMNLP 日程及后续查询，非完整会议索引；筛选判断和人工/模型审阅不能靠重新下载日程恢复 |
| `mopd/notes/conference-index-2026/`（约 125 MiB） | 2026-10-16 五会议快照：ICLR 5,575、ICML 6,563、NeurIPS 6,070、ACL 4,459、EMNLP 5,611；共 28,278，包含分别标记的非主会 track | [说明](../mopd/notes/conference-index-2026/README.md)、[10 个原始下载地址及哈希](../mopd/notes/conference-index-2026/sources.json)、[下载/重建脚本](../mopd/scripts/check-conference-acceptance.py)。本轮 10 份 raw 文件 SHA256 均与清单一致 |
| `opd/tmp/icml-2026-index/`（约 24 MiB） | ICML 原始展示/摘要 JSON，OPD 候选 34 条、shortlist 16 条 | 未发现该目录独立的下载来源或时间清单。原始文件名与下表 ICML 官方批量源一致，作为恢复入口推定；不声称已恢复原始下载时间或完全相同的历史版本 |
| `opd/tmp/emnlp-2026-index/`（约 2 MiB） | 2026-10-05 官方日程 CSV/XLSX，5,611 条；另有 OPD shortlist 与摘要证据 | 原目录 `README.md` 已记录官网下载入口、两个导出地址、时间和 SHA256；关键地址在下文重复保存，避免说明随 `tmp/` 被遗漏 |

### 共享数据库的确切下载地址

下面的时间来自当前数据库 `sync_runs`，以 UTC 记录；这是本地快照信息，不是今天重新同步的结果。

| 会议 | 来源 | 最后同步时间（UTC） |
| --- | --- | --- |
| ICLR 2026 | [论文展示及 decision JSON](https://iclr.cc/static/virtual/data/iclr-2026-orals-posters.json)；[摘要 JSON](https://iclr.cc/static/virtual/data/iclr-2026-abstracts.json) | 2026-10-23 13:22:51 |
| ICML 2026 | [论文展示及 decision JSON](https://icml.cc/static/virtual/data/icml-2026-orals-posters.json)；[摘要 JSON](https://icml.cc/static/virtual/data/icml-2026-abstracts.json) | 2026-10-23 13:23:07 |
| ACL 2026 | [主会 long MODS XML](https://aclanthology.org/volumes/2026.acl-long.xml)；[主会 short MODS XML](https://aclanthology.org/volumes/2026.acl-short.xml) | 2026-10-23 13:23:08 |

共享数据库不含 ICML Position、ACL Findings、NeurIPS 或 EMNLP；`--venue all` 当前仅代表 ICLR、ICML、ACL 三种来源，不代表上述全部本地索引。

### 其他快照的下载入口

- NeurIPS：[展示/decision JSON](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json)、[摘要 JSON](https://neurips.cc/static/virtual/data/neurips-2026-abstracts.json)。2026-10-14 旧清单的缓存时间为 14:24:20 / 14:24:19 UTC，SHA256 分别为 `45e583e2d9173ad2d421e238ce1f382de25c7f5d63f84798b8e77d96a808a12a` / `74e780f15c3ea22617c7a82d1ef10b93f7852f65d1067bb6febf839a51a95f12`。10-16 的 MOPD 快照来自相同网址但内容不同，不能互相冒充。
- ACL Findings：[2026 Findings-ACL MODS XML](https://aclanthology.org/volumes/2026.findings-acl.xml)，由 MOPD 脚本下载，未导入共享数据库。
- EMNLP：原下载记录的入口是[会议官网 program](https://2026.emnlp.org/program/)，指向 [Author Presentations 日程表](https://docs.google.com/spreadsheets/d/1aXGTy_7Xeh-OXIs3iJSbDpUsZ6YhbfA76b17kBZH0Yk/edit?gid=943432490)。直接下载：[CSV](https://docs.google.com/spreadsheets/d/1aXGTy_7Xeh-OXIs3iJSbDpUsZ6YhbfA76b17kBZH0Yk/export?format=csv&gid=943432490)、[XLSX](https://docs.google.com/spreadsheets/d/1aXGTy_7Xeh-OXIs3iJSbDpUsZ6YhbfA76b17kBZH0Yk/export?format=xlsx)。这是报告日程，没有完整作者列表和摘要，报告形式不能当作评审 decision。
- EMNLP 2026-10-05 旧清单记录的 SHA256：CSV `dda3c88a684f0562f926df4b664c673f7768848b3ead421b54a006ff77dd63d7`；XLSX `7eb253e37303e876b4a7a8eb894fb356a07bd2bcce7ba2a3da7d43cd4cd171b5`。10-14、10-16 日程可能更新，需分别保留快照日期和哈希。

### 换机恢复与提交边界

1. 提交索引脚本、本说明、MOPD 的 `sources.json` 与目录说明，以及研究采用的匹配结果、shortlist、纳入/排除理由和综合结论。`sources.json` 的旧绝对路径只是原机器上的位置；定位下载文件应结合条目的 `name` 与所在快照目录，不要求新机器保留 `/home/chy/`。
2. 共享数据库可用上面的 `sync` 命令重新获取；这会得到下载时的官方版本，不保证与历史快照逐字相同。
3. MOPD 五会议索引的恢复：先在 Research 根目录 `uv sync`，再运行 `uv run python mopd/scripts/check-conference-acceptance.py`。脚本需要 PyYAML 和系统 `curl`，会复用已有 raw；缺失时下载，再重建索引和当前本地论文的匹配结果。原始源变化、本地论文变化都会使结果与旧快照不同；不要用重建操作覆盖唯一的历史证据。
4. 大型原始 JSON/XML/CSV、SQLite 和规范化全量索引可以不放普通 Git，但换机时应另做快照备份，尤其是需要复核当时结论的版本。下载地址加哈希只能识别版本，不能保证未来还能下载到同一内容；本仓库目前没有记录独立快照备份的存放地址，不假设已有备份。
5. **`tmp/` 不是“可全部丢弃”的保证。** 根忽略规则会忽略上述 `tmp/`，其中的标题审阅、摘要补查、纳入/排除判断和 shortlist 不一定可重建；应在提交准备时把要长期保存的证据纳入持久目录或明确跟踪，再决定缓存是否排除。本次来源盘点只补说明，不迁移或删除这些文件，也不改变忽略规则；提交范围单独选择。
