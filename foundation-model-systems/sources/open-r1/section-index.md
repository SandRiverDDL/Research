# Open-R1 章节索引

```yaml
---
source_id: open-r1
index_status: working
source_files:
  - https://github.com/huggingface/open-r1
coverage:
  toc_index: true
  key_sections_read: true
  appendix_read: false
  tables_extracted: partial
  figures_checked: partial
---
```

## 来源地图

| 来源章节 | 阅读目的 | 关联笔记 | 状态 |
|---|---|---|---|
| `[blog-launch]` 项目计划 | 区分 DeepSeek 缺失 artifact 与 roadmap | `README.md` | 已读 |
| `[repo]` 总览 / news | 区分已完成 release 与规划 | `README.md`, claims | 已读 |
| `[repo]` SFT | 可运行的 distillation recipe 与 config | `notes/sft-distillation.md` | 已读 |
| `[repo]` GRPO | rollout/training architecture 与 reward hook | `notes/rl-training.md` | 已读 |
| `[repo]` 数据集过滤 | 面向可验证任务的 pass-rate filtering | `notes/rl-training.md` | 已读 |
| `[repo]` code interpreter | sandbox provider 与 executable reward | `notes/rl-training.md` | 已读 |
| `[repo]` 数据生成 | Distilabel/vLLM 轨迹生成 | `notes/sft-distillation.md` | 已读 |
| `[hf-org]` 模型 / 数据集 | artifact 清单 | claim audit | 已读 |

## 按问题定位

- 快速本地 recipe：repository 的 `recipes/` 与 `src/open_r1/`。
- 复现 R1-Distill：SFT 章节及 Mixture-of-Thoughts release。
- pure RL 状态：检查 repository news、GRPO recipe 与已发布 checkpoint；不能根据 roadmap 推断已完成。
- code RL：code reward 与 sandbox provider 章节。

## Read Coverage

- 已写入笔记：项目总览、SFT、GRPO、数据生成与 code reward 章节。
- 执行前需重读：固定当前 commit，检查确切 YAML 与依赖版本。
- 没有 PDF 页码锚点；引用全部使用语义标签。
