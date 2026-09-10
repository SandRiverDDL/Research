# Anthropic Claude Family Source Bundle

## Primary（系统性公开材料）

- Engineering blog landing: https://www.anthropic.com/engineering
- News / research blog: https://www.anthropic.com/news
- System cards index: https://www.anthropic.com/system-card  （每代 Claude 单独 PDF）
- Claude Code 相关 blog 系列: https://www.anthropic.com/news?topic=claude-code
- Computer Use blog + model card: https://www.anthropic.com/news/3-5-models-and-computer-use 及后续

## Secondary

- Anthropic 论文 / 报告：https://www.anthropic.com/research
- 第三方 eval / 复现报告：进 release-delta 文件时按需挑 1-2 篇 cross-check。

## Local Files

- 没有；按 release-delta 单独存为 PDF/MD 时再放到 `papers/anthropic-claude/<release-id>/`。

## Source Role

Family-level bundle for closed-weights Claude lineage. Stage notes / lens 引用必须落到具体 release 的 `release-deltas/<id>.md`，不要从 family README 直接引 fact。

## Citation Labels

- `[blog-anth-<topic>]`：anthropic.com 上的 engineering / news blog
- `[sys-card-claude-<version>]`：对应版本的 system card
- `[paper-anth-<id>]`：Anthropic 自己发表的论文
- `[third-party]`：独立第三方 eval / 复现

## Checked

- last checked: 2026-06-30
- source status: family stub created. release-delta files pending.

## Next Steps

按优先级补 release-delta：

1. `release-deltas/claude-4.5.md` — Claude Code / Skills / Computer Use 的主要 anchor。
2. `release-deltas/claude-4.md` — agent eval baseline。
3. `release-deltas/claude-3.7-sonnet.md` — extended thinking lineage 起点。
4. 后续 4.6 / 4.7 / 4.8 按 release 节奏补。
