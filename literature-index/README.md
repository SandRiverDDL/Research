# Conference Literature Index

共享的顶会 metadata 缓存。它只负责机械检索，不保存研究 taxonomy，也不替代 Zotero、L1 cards 或原文。

```bash
cd /Users/chy/Research

# 同步官方 metadata
uv run python literature-index/index.py sync --venue all --year 2026

# 检索；默认所有词都命中，--any 表示任一词命中
uv run python literature-index/index.py search "on-policy distillation" --year 2026
uv run python literature-index/index.py search "agent data selection" --any --limit 20 --json

# 查看覆盖范围
uv run python literature-index/index.py status
```

当前来源：

- ICLR / ICML：会议官网一次性 JSON；仅保留官方 Conference track 的 accepted papers。
- ACL：ACL Anthology 的 long / short 主会 MODS XML。

ICLR / ICML 的批量源包含摘要和作者机构；ACL 的批量 XML 当前只包含题目、作者和正式链接，摘要等信息只对 shortlist 再补查。

`papers.sqlite` 是可重新生成的本地缓存，不应进入版本控制。代码、数据和机构补充核验只对检索后的 shortlist 进行。
