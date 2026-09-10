# OPD L1 Card

L1 是单篇论文的压缩检索层，不是完整综述。新卡只保存稳定身份字段；研究判断写在正文，脚本不解析正文结构。

```yaml
---
title: "Paper Title"
authors: [First Author, et al.]
year: 2026
venue: icml-2026
paper_id: arxiv:2601.12345
source: https://arxiv.org/abs/2601.12345
---
```

身份规则：

- `paper_id` 优先使用无版本号的 arXiv ID；没有 arXiv 时使用 `openreview:<forum-id>` 或 `doi:<doi>`。
- `source` 是本卡实际阅读的原论文版本。Venue 由官方录用名单或 proceedings 核验。
- `authors` 默认只写首作者和 `et al.`。
- 预印本尚未录用时写 `venue: arxiv`。

正文不使用 `#` / `##` 标题。推荐用以下软标签和子列表：

```markdown
- **一句话**：本文解决什么问题，靠什么关键机制。

- **Failure mode**

  - 已观察到的坏现象；优先复用现有 failure-mode 名称。
  - 作者如何解释该现象。不要把 diagnosis 写成领域共识。

- **瓶颈（可选）**：仅当论文有明确因果诊断证据时填写，并标明是作者诊断；若只是换句话重复 failure mode，则删除。

- **核心做法**

  1. 按实际 dataflow 写关键步骤。
  2. 每步只保留理解机制所必需的信息。

- **方法增量**

  - 相对最强近邻或主要 baseline，具体改变了什么。

- **关键证据与边界**

  - 决定性实验、消融和 source anchor。
  - 仍然失败的条件、依赖和复现边界。
```

`Failure mode`、`核心做法`、`方法增量`、`关键证据与边界`是常规项；`瓶颈`是可选项。Validator 不检查正文标签、taxonomy、方法类别、创新性或 idea 质量。

Failure mode 是坏现象；bottleneck 是阻止性能或可信度继续前进的因果约束。单篇论文通常只能支持 failure mode 和作者 diagnosis，跨论文 bottleneck 主要由 synthesis 重建。每个事实尽量在句末标出原文位置，例如 `（§3.2；Table 2）`。

旧卡保持原样，不要求迁移到本模板。
