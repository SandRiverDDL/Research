# Skywork Open Reasoner 1 章节索引

```yaml
---
source_id: skywork-or1
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/skywork-or1/skywork-or1.pdf
coverage:
  toc_index: true
  key_sections_read: true
  appendix_read: false
  tables_extracted: partial
  figures_checked: partial
---
```

## 阅读地图

| 章节 | 页码 | 阅读目的 | 关联笔记 | 状态 |
|---|---:|---|---|---|
| 引言 | 3-5 | 主要发现与范围 | `README.md` | 已读 |
| 预备知识 | 6 | policy objective baseline | `notes/rl-training.md` | 已读 |
| MAGIC 总览 | 7-9 | 完整训练控制栈 | `notes/rl-training.md` | 深读 |
| 数据混合 / curriculum | 9-16 | 组件消融 | `notes/rl-training.md` | 深读 |
| Entropy control / no KL | 16-18 | 关键稳定性机制 | `notes/entropy-control.md` | 深读 |
| Entropy collapse 研究 | 18-26 | on/off-policy 与 SGD reuse | `notes/entropy-control.md` | 深读 |
| 资源分配 | 27-30 | rollout budget 与 update reuse | `notes/entropy-control.md` | 已读 |
| 数据集准备 | 31-33 | 来源、去重、难度与 judge | `notes/data-verifier.md` | 深读 |
| 数学 / 代码 verifier | 34-35 | reward 可靠性与 sandbox | `notes/data-verifier.md` | 深读 |
| 训练 / 评测 | 35-37 | config、设置与 claim | claim audit | 已读 |

## 按问题定位

- 完整 MAGIC 流程：第 7-18 页。
- entropy collapse：第 18-30 页。
- data recipe：第 31-33 页。
- verifier / sandbox：第 34-35 页。
- 精确 context / batch / group schedule：第 35-36 页。

## Read Coverage

- 已写入笔记：第 3-37 页，少量 figure-level 细节除外。
- 未穷尽阅读：references 与全部曲线数值。
- 复跑前需重读：repository commit/config 与已发布数据版本。

## Lookup Tables / Figures

- MAGIC component ablations: pages 9-18.
- Entropy-collapse experiments: pages 18-26.
- Training stage tables: page 36.
