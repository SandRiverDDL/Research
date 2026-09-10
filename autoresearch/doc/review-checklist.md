# Autoresearch Paper Review Checklist

> 读 autoresearch 论文时的审查 protocol。
> 不进 card frontmatter tag，属于**汇报/证据层**审查，与 `taxonomy/failure-modes.md`（方法固有缺陷）分离。

## Tier A — 每卡必答（1 项）

写卡 body "可信度 / 限制" 段落时必须显式回答：

- **human-in-the-loop-hidden**：论文是否声称 fully autonomous？如是，是否量化了每 paper / 每 idea 的 human hour / human intervention count？未量化则默认按 `human-in-the-loop-hidden` 处理，body 明写。

Evidence tier（self-report / third-party / audit）标注属于 `DECISIONS.md` 2026-07-15 强制项，见那里，不在本 checklist 重复。

## Tier B — 红旗触发（6 项，看到信号才拉出来审）

**触发条件**（任一命中即启动 Tier B）：

- 声称 "fully autonomous" / "end-to-end" 且未量化 human effort
- 声称 "all-domain SOTA" / "every domain wins" / "全面超越"
- self-eval headline 数字（LLM-Judge / auto-reviewer / self-Elo）大幅高于外部 signal
- 只展示成功案例 / 没有 failure distribution
- Baseline 明显偏弱或缺关键对比
- Metric 定义 non-standard 或看起来"太合身"

**六项审查**：

- **cherry-picked-showcase**：只报成功？有无 hit rate / failure 分布？
- **metric-selection-bias**：换 metric / seed / dataset 数字是否还成立？作者是否报了不利 metric？
- **weak-baseline**：baseline 是否足以证 mechanism？还是刻意挑弱对手？
- **metric-gaming**：metric 能否在不解决真任务的前提下被提升？
- **reproducibility-gap**：code / seed / API dependency / prompts 是否公开？
- **source-gap**：核心 claim 是否有 PDF / code / eval 证据支撑？

Tier B 发现写卡 body 自由文本，**不进 frontmatter tag**（避免污染 method failure mode 池）。

## 与 taxonomy/failure-modes.md 的分工

- **失败模式**（方法自身固有缺陷，与作者诚实度无关）→ `taxonomy/failure-modes.md`，进 frontmatter `failure_modes`
- **汇报 / 证据 pathology**（作者选择性汇报 / 藏 human effort / 混证据档位）→ 本 checklist，进卡 body 自由文本

判断 test：
> "如果换一个诚实的作者用同一个方法，这个问题还在吗？"
> 在 = failure mode。不在 = reporting pathology，走本 checklist。
