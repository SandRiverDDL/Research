# Wiki Lint Report

日期：2026-10-14；范围：TCOD 单篇试入库，ARIS commit `26b95cfa0d8747078e9e43b42e20952709e561b8`。

检查方式：本报告由 Codex 整理。Schema、相对路径、graph / query pack 和重复导入正文 hash 使用本次临时 Python 检查，未保存为可复用的项目 validator；入库与索引使用 ARIS 自带 helper；方法、数字和局限的证据由 Codex 阅读原论文核对。无独立 reviewer 复核。

## 验证结果

- 1 篇 paper、1 条 addresses_gap 关系、1 个 G1 gap；idea / experiment / claim 均为 0。
- ARIS paper schema 的 12 个章节齐全，9 个原有 TODO 已补全；已有 thesis 保留。frontmatter、Connections、Abstract (original) 未在 enrich 阶段修改。
- 本地 PDF 与页面中全部相对路径存在；主要方法 / 结果 / 局限含原论文 HTML anchors 与 PDF 页码。
- 同一 arXiv ID 重复调用 canonical ingest_paper 后被跳过，正文 SHA-256 不变；不会覆盖已补全内容。
- index 与 query pack 均包含该 paper；query pack 含 G1 和关系，低于 8000 字符，strict threat scan clean。
- 7 个已安装 skills 入口可读；项目 helper validate 为 0 errors / 0 warnings。该 helper 只验证 card pipeline，不能代替本报告的 wiki 检查；本次没有新建正式 L1 cards。
- Orphan paper：0；stale claims / contradictory claims / dead ideas：0（尚无这些实体）；共享多个 tag 的无关联 paper pairs：0（仅一篇）。

## 已知限制

- 上游规则称 Connections 自动生成，但当前 add_edge / rebuild_index 实现没有回填此章节。本次遵守 protected section 约定保留其模板，真实关系见 graph/edges.jsonl；页面 Relevance 段已链接该文件与 G1。未修改上游源码。
- 当前 query-pack helper 从 RESEARCH_BRIEF.md 取 project direction，尚未实现规则中宣称的 AGENTS.md fallback；本项目没有该 brief，所以 pack 暂无独立 Project Direction 段。当前样例包含 gap 与 paper thesis，后续 ideation 时仍需读取项目 AGENTS.md。
- 已阅读原论文重点章节，并目视核对 PDF pp. 5、6、8、9、10；未审计代码、复现实验、验证外部 reviewer 或 Zotero 导入，也未完成其余候选的逐篇筛选 / 入库。
