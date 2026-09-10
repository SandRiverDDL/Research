# Agent Data 未决问题

## Scope

- data pipeline 和 RL algorithm 都有实质贡献时，什么情况下需要在本项目写完整卡，什么情况下只登记到 Agentic RL queue？
- benchmark/eval paper 如果主要改变 data collection protocol，是否进入 Agent Data 主线？
- web/GUI/coding agent 的场景差异是否需要形成子报告，还是统一放在 data mechanism map 中？
- `agent-post-training-data` 是否应长期保持为 `llm-post-training-data` 的子方向，还是未来和 `llm-post-training-data/` 合并成上位项目？
- metacognitive failure-switching 是本项目主线，还是只作为 idea frontier / scaffold background？

## Card Schema

- L1 card 是否需要 `data_quality_signal` 独立字段，还是继续放在 `selection_signal`？
- `rl_overlap: true` 是否足够标记混合论文，还是需要 `agentic_rl_queue_path`？
- data axes 是否足够覆盖 environment-generated data、student-feedback data generation、trajectory completion、trajectory judgment？
- `data_knobs` 是否足够覆盖 real-world log mining、search-to-SFT distillation 和 negative transfer control？

## Recall

- current priority seed references 是否足够覆盖 FireAct、STeP、InSTA、MAG-V、DataEnvGym、Exploring Expert Failures？
- 是否需要单独建立 benchmark/eval paper 队列，例如 AgentBench、ToolBench、WebShop、Mind2Web、WebLINX、GAIA？
- 是否需要从 agentic RL surveys 中反向抽取 data mechanism papers？
- 2026 第一批 known-items 是否需要按 code / GUI / tool / metacognition 分批抽卡，还是先做统一 comparison？
