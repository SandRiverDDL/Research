# 2026 会议索引

下载/复核日期：2026-10-16。用于当前MOPD项目的会议录用检索；原始官方metadata、来源和规范化索引保存在本目录，共约125 MB。

| 会议 | 去重记录数 | 收录类别 |
|---|---:|---|
| ICLR | 5,575 | Conference；排除BlogPosts |
| ICML | 6,563 | Conference 6,341；Position 222 |
| NeurIPS | 6,070 | Conference 5,406；Evaluations/Datasets 616；Position 48 |
| ACL | 4,459 | 主会long 2,222、short 74；Findings 2,163 |
| EMNLP | 5,611 | MAIN 2,710；FIND 2,487；Industry 265；Demo 86；TACL 50；CL 13 |
| 合计 | 28,278 | 各类别分别保留，不把Findings或特殊track混算为主会 |

这是五场会议的官方可用来源快照，不是所有学科顶会全集；未下载workshop合集。NeurIPS/ICLR/ICML按accepted记录过滤并合并同一论文的重复展示；EMNLP使用官方日程表，其展示类型不是评审decision字段。ACL来自官方MODS XML。

## 文件

- `raw/`：10份官方JSON/XML/CSV，成功下载后缓存复用。
- `sources.json`：每份文件的原始URL、本地路径、大小和SHA256。
- `papers.jsonl`：28,278条规范化记录，保留会议、track、展示/decision、题目、可用作者/摘要、标识符和来源。
- `summary.json`：各会议及track计数。
- `mopd-matches.json`：36篇本地论文的完整标题命中、可用arXiv标识符命中及每篇最多3个近似/作者候选。
- `shortlist-verification.json`：定向API核查的失败记录与候选的索引证据；失败不当作否定结果。
- `validation.json`：数据结构、去重、来源哈希和36篇匹配覆盖检查。

## 检索

在MOPD项目目录执行（已安装PyYAML）：

```bash
python3 scripts/check-conference-acceptance.py --search 'multi teacher distillation' --limit 20
python3 scripts/check-conference-acceptance.py --search 'H-OPD' --venue EMNLP
```

检索标题、可用摘要和作者，要求所有查询词命中；默认只显示20条简要记录和总数。不要将整个索引读入对话上下文。

无参数执行脚本会复用已下载raw并重建索引和MOPD匹配；下载失败最多重试2次。更新源时需明确刷新对应raw文件，现有文件不会被静默重新下载。共享`../literature-index/`中的脚本和旧缓存没有修改。

## 改标题的边界

先做大小写/标点/Unicode规范化的完整标题匹配；有官方arXiv链接时检查arXiv ID；再用标题相似度和作者交集生成少量待核查候选。作者交集只能召回，不能确认同一论文。EMNLP这份日程没有作者和摘要，因此无法仅靠此表排除彻底改标题的漏检；近似候选须核对原文或作者正式发表列表。

官方索引会更新，本次数据是2026-10-16快照。旧NeurIPS缓存缺AVSD，新下载官方JSON包含其Accept (poster)记录，故最后结果使用新源。
