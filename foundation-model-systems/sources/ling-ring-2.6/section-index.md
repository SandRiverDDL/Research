# Ling / Ring 2.6 章节索引

```yaml
---
source_id: ling-ring-2.6
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/ling-ring-2.6/ling-ring-2.6.pdf
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
| 引言 | 1-3 | family 拆分与贡献地图 | `README.md` | 已读 |
| 架构迁移 / pretraining | 4-10 | base policy 与效率背景 | 待写 architecture note | 略读 |
| Pretraining 评测 | 10-12 | base quality 边界 | claim audit | 略读 |
| Ling post-training | 13-15 | SFT、specialist、token efficiency、preference | `notes/post-training.md` | 深读 |
| Ring tool/agent 数据 | 15-18 | coding/search/tool 混合与筛选 | `notes/tool-agent-training.md` | 深读 |
| KPop | 18-19 | 训练—推理不匹配 objective | `notes/rl-infrastructure.md` | 深读 |
| 评测 | 20-26 | 能力与 scaffold 设置 | `notes/claims-and-gaps.md` | 已读 |
| 长上下文训练 infra | 27-28 | context parallelism 与显存稳定性 | `notes/rl-infrastructure.md` | 已读 |
| ASystem / ARouter / FP8 | 28-30 | rollout 调度与数值对齐 | `notes/rl-infrastructure.md` | 深读 |
| Asynchronous RL | 30-31 | partial rollout 与 bounded staleness | `notes/rl-infrastructure.md` | 深读 |
| 局限 | 33 | token efficiency 与 long-horizon failure | `notes/claims-and-gaps.md` | 已读 |

## 按问题定位

- Ling token-efficiency post-training：第 13-15 页。
- Ring agentic data 与 RL：第 15-19 页。
- KPop：第 18-19 页及 `[kpop-note]`。
- rollout / inference 协同设计：第 28-31 页。
- benchmark 设置与局限：第 20-26 页。

## Read Coverage

- 已写入笔记：第 1-3、13-19、27-31、33 页。
- 略读：architecture/pretraining 与 evaluation tables。
- 做架构比较前需重读：第 4-10 页。

## Lookup Tables / Figures

- Figures 7-8: KPop training dynamics and evaluation.
- Figures 11-12: ARouter and inference optimization.
