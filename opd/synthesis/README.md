# OPD 综合分析入口

整理日期：2026-10-06。按文档用途组织，不增加 card taxonomy 或自动维护流程。

## 先读什么

| 目的 | 入口 | 范围与时效 |
|---|---|---|
| 具体会坏在哪里，几篇方法是否处理同一个问题 | [具体 failure modes](failure-modes/concrete-failure-modes.md) | 当前重点综合；原文核查与卡片证据分开标注 |
| teacher/student 是否适合蒸馏 | [Teacher–student mismatch](failure-modes/teacher-pattern-mismatch.md) | 保留的专题；76 张卡时期的覆盖，旧选题建议不视为当前决定 |
| 学习方法大类 | [短版方法地图](reading/opd-method-map.md)、[逐篇方法索引](reading/opd-method-catalog.md) | 2026-09-28 的 77 卡快照，不是当前全库 |
| 本月代表作、直接性能对照与局限 | [arXiv OPD 月度总结](reading/arxiv-opd-2026-09-22-to-10-22.md) | 2026-09-22 至 10-22 首发窗口；30 篇代表作，整理于 10-27，未补查 10-23–27 |
| 选择 EMNLP 2026 阅读对象 | [会议候选总结](reading/emnlp-2026-opd-overview.md) | 2026-10-05 的 38 篇候选，多数仅摘要证据 |
| Agent 场景入口 | [Agentic OPD](reading/agentic-opd.md) | 问题与论文导航，非完整新文献综述 |
| 追溯旧判断、旧检索 | [历史资料](archive/README.md) | 旧内容保留，不能据其判断当前 novelty 或覆盖率 |

## 目录职责

- `failure-modes/`：按具体现象、机制、证据和边界做跨论文综合。
- `reading/`：学习导航、论文清单、会议阅读快照。
- `archive/`：已过时的覆盖口径、检索窗口和选题判断；保留历史证据。
- `queue.md`：现有文献流程的机械队列，保持原路径，不作阅读入口。

新综合优先补充对应主题文档；不要为每轮对话新增一份根目录报告。日期快照不自动升级成最新全集。

## 本次迁移与回滚

| 原位置（相对 synthesis） | 新位置 | 理由 |
|---|---|---|
| `agentic-opd.md`、`emnlp-2026-opd-overview.md`、`opd-method-map.md`、`opd-method-catalog.md` | `reading/` 下同名文件 | 统一阅读导航，保留原覆盖范围 |
| `opd-method-lineage-report.md`、`opd-method-lineage/` | `archive/2026-06-lineage/` 下同名文件／目录 | 71 卡旧谱系及早期 idea 判断 |
| `arxiv-opd-120d-radar.md`、`arxiv-opd-120d-synthesis.md` | `archive/2026-07-radar/` 下同名文件 | 仅覆盖 2026-03-31 至 07-29 |
| `low-hanging-fruit-ideation.md` | `archive/2026-08-ideation/` 下同名文件 | 早期对话判断，非当前选题决定 |

未删除旧文件正文；仅移动、增加状态提示并修复路径。回滚时按此表移回，反向恢复本地链接和 STATE 路径，移除本次整理提示。无需 git reset，避免覆盖工作区已有的其他修改。
