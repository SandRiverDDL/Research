# DeepSeek-R1 章节索引

```yaml
---
source_id: deepseek-r1
index_status: working
source_files:
  - /Users/chy/Research/foundation-model-systems/papers/deepseek-r1/deepseek-r1.pdf
coverage:
  toc_index: true
  key_sections_read: true
  appendix_read: partial
  tables_extracted: partial
  figures_checked: partial
---
```

## 阅读地图

| 章节 | PDF 页码 | 阅读目的 | 关联笔记 | 状态 |
|---|---:|---|---|---|
| 引言 / 定位 | 1-2 | R1-Zero 与 R1 的研究问题 | `README.md` | 已读 |
| GRPO 与 R1-Zero | 2-5 | objective、rollout、reward、长度变化 | `notes/rl-training.md` | 深读 |
| R1 pipeline 总览 | 6 | 四阶段流程 | `notes/rl-training.md`, `notes/sft-distillation.md` | 深读 |
| Model-based reward | 6-7 | helpfulness 与 safety RM | `notes/reward-verifier.md` | 已读 |
| 第一、第二 RL 阶段 | 7-8 | 语言一致性与通用 RL | `notes/rl-training.md` | 深读 |
| 主要评测 | 8-10 | 能力与可比性 | `notes/claims-and-gaps.md` | 已读 |
| 补充训练 / 数据信息 | 13-20, 35-40 | 超参数、数据与消融 | stage notes | 部分 |
| 蒸馏附录 | 60-62 | 80 万条轨迹与小模型对比 | `notes/sft-distillation.md` | 已读 |
| RL/RM 局限与相关分析 | 63-65 | PRM/RM 局限 | `notes/reward-verifier.md` | 部分 |
| 评测 prompt 与 safety 细节 | 40-78 | 设置与 judge prompt | claim audit | 略读 |

## 按问题定位

- pure RL / GRPO：第 2-5 页。
- 完整 R1 阶段顺序：第 6-8 页。
- reward 拆分：第 3-4、6-7 页。
- distillation：第 60-62 页。
- Headline results：第 8-10 页；比较前必须核对 metric 与 sampling setting。

## Read Coverage

- 已写入 notes：第 1-10、60-63 页。
- 仅 skim：training/data 与 evaluation appendices。
- 未完整阅读：safety prompt appendix 与 references。
- 复现前需重读：exact data construction、verifier code 与 infra appendix。

## Lookup Tables / Figures

- Figure 1：R1-Zero accuracy 与 response-length 的变化。
- Figure 2：R1 multi-stage pipeline。
- 蒸馏表格：附录中的小模型对比。
