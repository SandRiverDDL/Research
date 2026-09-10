# Agent Data 决策记录

> 稳定决策放这里；临时状态放 `STATE.md`。

## 2026-06-16 — 一级主题改为 Agent Data，而不是 Agent SFT

决策：当前项目正式命名为 `Agent Data for Training`。SFT 只作为 `training_consumer` / downstream consumer，不作为一级主题。

原因：社区并没有稳定的 “Agent SFT” 综述类目；文献更常按 tool use、web/GUI/coding agent、agentic RL、benchmark/eval 切。用户当前真正关心的是 agent training data 的生成、选择、验证、修复、重加权和课程化。

影响：召回时不搜 “Agent SFT” 作为唯一入口，而是从 tool-use、web/GUI/coding agent、data-centric alignment、synthetic trajectory、agentic RL pipeline 中抽取 data mechanism 论文。

## 2026-06-16 — Agentic RL 拆成独立项目

决策：Agentic RL 单独放在 `/Users/chy/Research/agentic-rl/`。当前项目只在 data mechanism 是核心贡献时收录 RL 相关论文。

原因：Agentic RL 是接近 OPD 体量的独立大类，会自然长出自己的 seed surveys、benchmarks、method lineage 和 failure modes。混在 Agent Data 里会让报告失焦。

影响：遇到 reward design、policy optimization、RL update、online exploration、long-horizon credit assignment 等论文，登记到 `agentic-rl` queue，不在当前项目抽完整卡。

## 2026-06-16 — Data vs RL 的边界按“贡献点”划分

决策：只要核心贡献是 data generation / selection / verification / repair / curriculum，即使它服务 RL，也放 Agent Data。只有核心贡献是 RL objective / policy update / credit assignment / reward optimization，才放 Agentic RL。

原因：现实论文经常同时包含 SFT 和 RL；按训练阶段切会反复纠结。按 “data mechanism vs optimization algorithm” 切更稳定。

影响：混合论文可以双登记。本项目写 data 视角卡，Agentic RL queue 记录 RL 视角，未来再抽。

## 2026-06-23 — 项目初始化为 Agent Post-Training Data

决策：现有 `agent-data/` 不新建目录，直接初始化为 `Agent Post-Training Data`。它是 `llm-post-training-data` 下的 agent 子方向，而不是泛 `llm-data`。

原因：`llm-data` 会把 pretraining corpus、web-scale dedup、版权/污染、token mixture 等吸进来，范围失控；当前真正关心的是 agent 后训练阶段的 trajectory、tool-call、environment feedback、verifier filtering、failure masking、real-world logs 和 search-to-SFT distillation。

影响：本项目可以吸收 data-centric alignment / post-training survey 作为上位 lens，但正式 method card 必须能回答 agent data object、source、selection signal、failure use、adaptivity 和 training consumer。

## 2026-06-23 — 迁移 agentic-rl 的本地 helper 架构

决策：迁移 `/Users/chy/Research/agentic-rl/` 的项目本地 helper 架构：`scripts/autoresearch.py`、`comparison/queue.md`、`doc/acceptance-rules.md`、`doc/retrieval-strategy.md`、L1 template、taxonomy、validator 规则。

原因：skill 只提供通用 research workflow；`agentic-rl` 的成熟流程依赖项目本地文件约定、queue schema、validation/status 生成物和模板字段。只看 skill 无法可靠复用这些机械流程。

影响：后续自然语言任务可以从 `scripts/autoresearch.py status` / `pack` / `validate` 进入，但研究判断仍由 Codex 按本项目 scope 完成；helper 只做 hygiene / lookup / audit / bounded-input pack。

## 2026-06-24 — 项目定位为 goal-driven literature map，不是领域综述

决策：本项目不以“完整总结 Agent Data 领域”为目标，而以“提升 30B A3B MoE agent SFT benchmark 表现”为目标来组织文献。中心链路是 `benchmark bad case -> data action -> ablation / mixture -> stronger model`。

原因：用户当前工作是根据 benchmark 表现反推 SFT 数据生成、筛选、mask、修复、配比和消融策略。很多有用论文不是 agent-data core，例如 data mixture optimization；很多热门 agent 论文也不能改变数据决策，读它们 ROI 低。

影响：收录分为 `core agent SFT data` 和 `supporting methods`。Core 回答“造什么 agent 数据”；supporting 回答“数据怎么选、怎么配、怎么防 regression”。Supporting 可以抽卡，但必须标成 `data-flywheel-method` / `background`，不能污染 core taxonomy。普通领域综述只当背景或 seed，不作为主线阅读目标。
