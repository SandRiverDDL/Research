# Meta Frontier Family Source Bundle

## Primary

- Meta AI blog: https://ai.meta.com/blog/
- Llama landing: https://www.llama.com/
- Llama 4 announcement: https://ai.meta.com/blog/llama-4-multimodal-intelligence/
- Model cards: https://github.com/meta-llama/llama-models  （含历代 model card）

## Secondary

- 第三方 long-context 复现 / benchmark gaming 报道（进 release-delta 时挑 1-2 篇 cross-check）
- Avocado 相关 leak / 报道（新 release-delta 抓 URL 时再固定）

## Background

- Llama 系开源历史：Llama 1/2/3 paper 在 arxiv 和 ai.meta.com 都有；frontier 比较中作为 lineage 历史。

## Local Files

- 暂无；release-delta 阶段需要保存 model card PDF 时放到 `papers/meta-frontier/<release-id>/`。

## Source Role

Family-level bundle for Meta frontier lineage. 具体 fact 落到 `release-deltas/<id>.md`；family README 不引 fact，只做 lineage 索引。

## Citation Labels

- `[blog-meta-<slug>]`：ai.meta.com blog
- `[model-card-llama-<version>]`：对应 Llama / Avocado model card
- `[third-party]`：独立 eval / 复现 / 报道
- `[leak]`：未官方确认的泄露材料，confidence: very low

## Checked

- last checked: 2026-06-30
- source status: family stub created. release-delta files pending.
