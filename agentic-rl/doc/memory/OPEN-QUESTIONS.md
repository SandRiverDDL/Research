# Agentic RL 未决问题

## Scope

- Tool-use RL 和 reasoning RL 的边界是否按 environment/action space 划分？
- Search-based agent training 是否属于 Agentic RL，还是单独做 search/reasoning background？
- SFT warm start 在哪些论文里是核心变量，哪些只是默认初始化？

## Card Schema

- 是否需要单独字段记录 environment type / action grammar / verifier type？
- `credit_assignment` 应该按 token、step、tool-call、segment、trajectory 哪个粒度记录？
- data/replay 机制是否只 cross-link 到 Agent Data，还是在本项目也保留简短字段？

## Recall

- Seed queue 是否覆盖 2026 主要 Agentic RL overview / ToolRL / Tool-R0 / environment scaling / reinforcement arena？
- 是否需要优先查 OpenReview accepted list，而不是只查 arXiv？
