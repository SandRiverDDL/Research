# OPD 文献流程

## 分工

- Zotero：PDF、书目和引用。
- `notes/`：L1/L2 单篇笔记。
- `synthesis/`：comparison、failure modes、bottlenecks、idea generation 和跨论文判断。

## 检索

```text
全部 L1 cards → 10–20 张相关 card → 3–8 篇原文
```

L1 是压缩检索层，不是 mini-survey。Failure mode 是坏现象；单篇解释是 diagnosis；bottleneck 需要跨近邻论文重建。

批量扫描会议时：

- 完整 HTML、搜索结果和 abstracts 只在脚本/工具内过滤，不进入模型上下文。
- 第一遍只保留 `title / venue / source / code / affiliation`，最多输出 20 个候选。
- 第二遍只核验候选的准入理由；通过后每批读取 1–3 篇原文并写卡。
- 换阶段前把 shortlist、include/exclude 理由和 source anchor 写入项目文件，compact 后不重扫会议。

## 只读脚本

```bash
scripts/autoresearch.py lookup <paper-id-url-title-or-slug>
scripts/autoresearch.py status
scripts/autoresearch.py validate
```

Registry 直接扫描 `notes/*.md`。Validator 只检查身份、来源和重复项，不解析正文或判断论文价值。旧卡通过 `arxiv_id` / `url` 兼容。

`_meta/`、旧 queue、maps、triage、manifest 和 brief 仅作历史材料，不自动维护。
