# Agentic OPD L1 Card Template

> L1 is a research index, not a full paper summary. Strong claims need source anchors.

## L1 Compression Contract

- Target length: 700-1000 Chinese characters.
- Keep only information useful for search, comparison, and idea judgment.
- Put full reading notes into L2 or `synthesis/`.

## Citation Anchor Policy

- Usually 3-6 anchors per L1 are enough.
- Anchor key numbers, core mechanisms, limitations, and important ablations.
- Put PDF / brief paths in trailing HTML meta.

```yaml
---
title: <FULL_TITLE>
year: <YYYY>
venue: <venue | arxiv>
paper_type: <from doc/triage-rules.json>
lifecycle_role: <survey-seed | canonical-anchor | strong-baseline | frontier-candidate | background | low-confidence-novelty-risk>
boundary_risk: <none | adjacent | eval | recipe | infra>

failure_modes: [<from doc/taxonomy/failure-modes.md>]
design_knobs: [<from doc/taxonomy/design-knobs.md>]
---
```

## 一句话定位

≤30 字中文，说明它在本项目谱系里的位置。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `<tag>` |  |  |  |

## 方法机制

3-5 句话说明核心机制。证据锚点直接写在句尾，例如 `[PDF §3.1]`、`[Table 2]`。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
|  |  |  |  |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `<tag>` |  |  |

## 方法优缺点 / 适用边界

- 优势：
- 不足 / 风险：

```markdown
<!-- meta:
authors: [<first author>, et al.]
url: <url>
arxiv_id: <id if any>
pdf: papers/<file>.pdf
brief: _meta/briefs/papers/<file>.md
survey: <seed / recall source>
-->
```
