# OpenAI Frontier Family Source Bundle

## Primary

- Index / blog: https://openai.com/index/
- Research: https://openai.com/research/
- System cards: https://openai.com/safety/  （每代 release 有独立 PDF / page）
- Model spec: https://model-spec.openai.com/
- API docs (Responses / Function calling / Agents SDK): https://platform.openai.com/docs

## Agent 产品入口

- Operator: https://openai.com/index/introducing-operator/
- Deep Research: https://openai.com/index/introducing-deep-research/
- Codex (cloud agent): https://openai.com/index/introducing-codex/
- ChatGPT Agent: https://openai.com/index/introducing-chatgpt-agent/

## Secondary

- 第三方 eval（SWE-bench、GAIA、BrowseComp 等）: 进 release-delta 时挑 1-2 篇 cross-check。

## Local Files

- 暂无；按需保存 system card PDF 到 `papers/openai-frontier/<release-id>/`。

## Source Role

Family-level bundle。具体 fact 必须落到 `release-deltas/<id>.md` 对应文件，不要从 family README 引用。

## Citation Labels

- `[blog-oai-<slug>]`：openai.com 上的 blog 文章
- `[sys-card-<release>]`：对应版本 system card / safety report
- `[model-spec]`：Model Spec
- `[api-docs]`：platform.openai.com API 文档
- `[third-party]`：独立 eval / 复现

## Checked

- last checked: 2026-06-30
- source status: family stub created. release-delta files pending.
