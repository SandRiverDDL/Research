---
name: literature-zotero
description: Use when the user asks for literature search, arXiv or conference paper lookup, related work, bibliography building, paper PDF download, Zotero import, or research-paper triage.
metadata:
  origin: local-custom
  language: zh-CN
  depends-on:
    - Zotero plugin
    - huggingface-papers plugin
    - pdf skill
---

# Literature Zotero

## 目标

这个 skill 是文献调研总控流程。默认保持简单：先帮助用户找到重要论文，生成可读的 `reading_matrix.md`；只有用户明确要求入库时，才下载 PDF 并导入 Zotero。

实际执行能力来自其他工具：

- `huggingface-papers`：查 Hugging Face paper page、arXiv URL/ID、论文摘要。
- `Zotero` 插件：操作本地 Zotero，导入 RIS/BibTeX，导出 BibTeX，验证附件。
- `pdf` skill：读取和检查 PDF 内容。
- Web/OpenReview/arXiv/会议官网：作为一手来源。

## 默认规则

当用户要求文献调研、related work、找论文、找最新 arXiv/顶会工作时，不要只给论文列表。默认完成最小有用闭环：

1. 搜索可靠来源。
2. 筛选相关论文。
3. 输出每篇论文的核心 idea、创新点、弱点、与用户研究的关系。
4. 需要保存时，只生成 `reading_matrix.md`。

只有用户明确说“导入 Zotero”“下载 PDF”“生成 BibTeX”“做系统综述”“需要可复现记录”时，才升级到更重的流程。

## 推荐来源优先级

优先使用一手或准一手来源：

- arXiv。
- OpenReview。
- NeurIPS、ICML、ICLR、ACL、EMNLP、AAAI、CVPR、ICCV、ECCV 等官方 proceedings。
- DOI 页面、出版社开放页面、作者项目页。
- Hugging Face paper page。

避免只依赖博客、排行榜、社交媒体或二手总结。它们可以作为线索，但不能作为最终出处。

## 输出层级

默认不要制造一堆文件。按任务严肃程度分三档：

### Quick：快速调研

适合探索方向、判断相关 work、先看有没有必要深入。

默认产物：

```text
reading_matrix.md
```

如果用户没有要求保存文件，也可以直接在最终回复里给简短矩阵。

### Import：正式入库

适合用户明确要求“补充进 Zotero”。

默认产物：

```text
topic_literature_YYYYMMDD/
  reading_matrix.md
```

临时产物：

```text
tmp/
  import.ris
  downloads/
```

`tmp/` 只用于导入 Zotero。PDF 长期应归 Zotero 管。只有确认 Zotero 中的附件可打开、且不是依赖 `tmp/downloads/` 的脆弱链接后，才清理临时 PDF；如果 Zotero 只是创建 linked attachment，则不要删除临时文件，先报告给用户。

只有用户要写 LaTeX、references、related work 草稿，或明确要求 BibTeX 时，才导出：

```text
references.bib
```

### Archive：可复现系统综述

适合系统综述、长期项目、需要解释搜索覆盖率和筛选标准的任务。

额外产物：

```text
search_log.md
papers_manifest.jsonl
references.bib
```

文件职责：

- `reading_matrix.md`：给人看的核心文献总结，默认最重要。
- `references.bib`：写 LaTeX/论文引用时使用；平时可从 Zotero 重新导出。
- `import.ris`：导入 Zotero 的临时中间文件，默认不需要长期保留。
- `search_log.md`：记录 query、来源、时间范围、筛选标准、排除理由；仅系统综述或可复现调研需要。
- `papers_manifest.jsonl`：机器可读索引，用于自动去重、增量更新、重新导入；日常不用。

## 环境分支：codex plugin vs cc MCP

这个 skill 同时被 codex 和 Claude Code 两个 harness 使用。两边访问 Zotero 的通道不同，**先判断你在哪个 harness 里**，再选对应路径：

- 如果可见的工具集里包含 `mcp__zotero__zotero_search_items`（或任何 `mcp__zotero__*`）—— **你是 cc**，走 §"cc 路径（Zotero MCP）"。
- 如果工具集里没有 zotero MCP，但 shell 里能跑 `python3 <zotero-plugin-root>/skills/zotero/scripts/zotero.py` —— **你是 codex**，走 §"codex 路径（Zotero plugin 脚本）"。
- 两条都走不通 —— 直接报告 Zotero 通道不可用，降级为只生成 RIS 让用户手动拖入 Zotero。

下面的导入/验证流程在两条路径上**逻辑相同**（确认 Zotero 状态 → RIS 导入 → 验证 collection 与 PDF 附件），只是工具调用形态不同。

### codex 路径（Zotero plugin 脚本）

导入前确认状态：

```bash
python3 <zotero-plugin-root>/skills/zotero/scripts/zotero.py status --json
python3 <zotero-plugin-root>/skills/zotero/scripts/zotero.py selected-target --json
```

导入：

```bash
python3 <zotero-plugin-root>/skills/zotero/scripts/zotero.py import-ris --file tmp/import.ris --yes
```

### cc 路径（Zotero MCP）

cc 这边没有 plugin 脚本，所有操作通过 `mcp__zotero__*` 工具：

- 检索已有条目去重：`mcp__zotero__zotero_search_items(query, qmode)`
- 读条目元数据：`mcp__zotero__zotero_item_metadata(item_key)`
- 读条目全文/附件：`mcp__zotero__zotero_item_fulltext(item_key)`

zotero MCP 当前不直接暴露"导入 RIS"工具。在 cc 这边遇到入库需求时：

1. 仍然按 §"Reading Matrix 模板" 生成 `reading_matrix.md`
2. 把待入库论文写入 `tmp/import.ris`
3. **不要假装自己导入了**——告诉用户："RIS 已生成在 `tmp/import.ris`，请在 Zotero 里 File → Import 一次"，并在用户确认后用 `zotero_search_items` 抽样验证条目数与附件
4. 如果用户要求 BibTeX，从 Zotero 端导出后让用户提供路径，cc 不主动生成

如果未来 cc 这边接入了能直接写入 Zotero 的 MCP 工具，把上面这条写入路径替换为对应的 MCP 调用即可，本节其它内容无需改。

## 状态确认与阻塞点

无论走哪条路径，如果 Zotero 没运行、本地 API 没开、connector 不可用、或 MCP 工具调用失败，先报告阻塞点。用户已经明确要求导入 Zotero 时，可以继续执行启用或导入动作；否则写入 Zotero 前先确认。

导入后必须验证：

- Zotero collection 顶层 item 数。
- PDF attachment 数。
- 随机或逐项确认 PDF attachment 可打开，且没有依赖即将删除的临时路径。
- 缺失 PDF 的论文列表。
- 如果用户要求 BibTeX，确认 BibTeX 是否成功导出。

## 去重规则

导入前必须去重。优先级：

1. DOI。
2. arXiv ID。
3. OpenReview URL 或 forum ID。
4. 标题规范化后匹配。
5. PDF URL 或 PDF 文件 hash。

同一论文同时有 arXiv 版和会议版时，优先保留会议正式版元数据，同时保留 arXiv URL。

## 论文筛选标准

不要把所有搜索结果都塞进 Zotero。按覆盖面筛选：

- 直接竞争工作。
- 经典或 survey/benchmark 工作。
- 最近 2-3 年顶会或 arXiv 直接相关工作。
- 强 baseline。
- 代表不同方法家族的论文。
- 可能影响 novelty 判断的危险相关工作。

## Reading Matrix 模板

`reading_matrix.md` 使用这个结构：

```markdown
# Reading Matrix

| Paper | Venue | Core idea | Novelty | Weakness | Relevance | Zotero |
|---|---|---|---|---|---|---|
```

每篇论文写 3-5 句话，必须覆盖：

- Core idea：这篇论文到底在做什么。
- Novelty：真正新在哪里，不要复述作者自称。
- Method：核心技术机制。
- Weakness：实验或假设上的弱点。
- Relevance：对用户当前研究有什么用，属于 direct competitor、baseline、method inspiration、must cite，还是 low priority。

## 快速模式

如果用户说“先快速扫一下”或“不要导入 Zotero”，只输出候选列表和分类，不下载 PDF、不导入 Zotero。

推荐分类：

- direct competitors
- must-cite baselines
- surveys / benchmarks
- method inspiration
- low priority

## 完成标准

快速调研完成时，最终回复必须包含：

- `reading_matrix.md` 路径，或直接给出简短矩阵。
- 每篇论文的核心 idea、创新点、弱点、与用户研究的关系。

Zotero 入库完成时，最终回复必须包含：

- Zotero collection 名称或当前选中目标。
- 导入论文数。
- PDF 附件数。
- 缺失 PDF 或元数据不确定的论文。
- `reading_matrix.md` 路径。
- 如果生成了 `references.bib`、`search_log.md`、`papers_manifest.jsonl`，再列出这些路径。

如果失败，必须指出具体阻塞点：网络失败、PDF 不可用、Zotero 未安装、Zotero local API 未开启、connector 不可用、导入失败、collection 验证失败、BibTeX 导出失败。
