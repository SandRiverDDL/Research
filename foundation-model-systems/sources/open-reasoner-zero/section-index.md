# Open-Reasoner-Zero 章节索引

```yaml
---
source_id: open-reasoner-zero
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/open-reasoner-zero/open-reasoner-zero.pdf
coverage:
  toc_index: true
  key_sections_read: true
  appendix_read: partial
  tables_extracted: partial
  figures_checked: partial
---
```

## 阅读地图

| 章节 | 页码 | 阅读目的 | 关联笔记 | 状态 |
|---|---:|---|---|---|
| 引言 | 3 | 开放度与核心 claim | `README.md` | 已读 |
| PPO/GAE 算法 | 4-5 | 基于 critic 的 objective | `notes/rl-training.md` | 深读 |
| 设计原则 | 5-7 | critic、γ/λ、no KL、minimal reward | 全部机制笔记 | 深读 |
| 数据 / reward 设置 | 7 | 数据筛选与 binary verifier | `notes/data-reward.md` | 深读 |
| 训练与消融 | 8-10 | λ、KL 与 data-scale 证据 | stage notes | 深读 |
| Critic 分析 | 10-11 | token credit assignment | `notes/critic-and-advantage.md` | 深读 |
| 评测 / 结论 | 11-12 | 适用范围与核心 claim | `notes/claims-and-gaps.md` | 已读 |
| 超参数附录 | 17-19 | 精确设置与曲线 | lookup-only | 部分 |
| PPO 伪代码 | 20-21 | 实现路径 | `notes/rl-training.md` | 已读 |

## 按问题定位

- 最小 recipe：第 4-7 页。
- 关键消融：第 8-10 页。
- critic 机制：第 10-11 页。
- 复现设置：第 17-21 页及 `[repo]`。

## Read Coverage

- 已写入笔记：第 3-12、20-21 页。
- 略读：第 17-19 页。
- 复跑前需重读：repository config 与确切 data release 版本。

## Lookup Tables / Figures

- Figure 2: reward/length scale-up across sizes.
- Figure 3: λ, KL and data-scale ablations.
- Critic/advantage figures: pages 10-11.
