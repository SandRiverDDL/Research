# Google Gemini Family Source Bundle

## Primary

- Google DeepMind blog: https://deepmind.google/discover/blog/
- Google blog (Gemini): https://blog.google/technology/google-deepmind/
- Gemini paper landing: https://deepmind.google/technologies/gemini/
- Gemini 1.5 paper: https://arxiv.org/abs/2403.05530
- Gemini 2.5 paper: https://arxiv.org/abs/2507.06261  （以实际 arXiv ID 为准，需在 release-delta 里 verify）
- Model cards / system cards: 各 release 单独发布
- API docs: https://ai.google.dev/gemini-api/docs

## Agent 产品入口

- Project Mariner: https://deepmind.google/technologies/project-mariner/
- Project Astra: https://deepmind.google/technologies/project-astra/
- Jules (coding agent): https://blog.google/technology/google-labs/jules/
- Gemini CLI / Gemini Code: 视 release-delta 时补 URL。

## Secondary

- 第三方 eval（GAIA、BrowseComp、SWE-bench）和复现：进 release-delta 时挑 1-2 篇。

## Local Files

- 暂无；TR 出来后保存到 `papers/google-gemini/<release-id>/`。

## Source Role

Family-level bundle. 具体 fact 落到 `release-deltas/<id>.md`。Gemini 2.5/3 TR 如果信息密度够，可单独升级为 `sources/gemini-2.5/`，届时 family README 改为 lineage index。

## Citation Labels

- `[blog-dm-<slug>]`：deepmind.google blog
- `[blog-google-<slug>]`：blog.google
- `[paper-gemini-<version>]`：对应 release 的 TR / paper
- `[model-card-<version>]`：对应 model / system card
- `[api-docs]`：ai.google.dev API 文档
- `[third-party]`：独立 eval / 复现

## Checked

- last checked: 2026-06-30
- source status: family stub created. release-delta files pending.
