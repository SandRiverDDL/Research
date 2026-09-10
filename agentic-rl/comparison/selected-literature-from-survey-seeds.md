# Selected Literature From Survey Seeds

> 目标：从前三个 survey seed 里挑第一批后续候选。2026-06-16 更新：queue 宽，card 用简单外部证据准入。

## Seed Surveys

| Priority | Paper | Track | Local PDF | Status |
|---|---|---|---|---|
| S | The Landscape of Agentic Reinforcement Learning for LLMs | boundary / overview | `papers/2509.02547-landscape-agentic-rl-survey.pdf` | card written |
| S | From Reasoning to Agentic: Credit Assignment in RL for LLMs | credit-assignment | `papers/2604.09459-credit-assignment-rl-llms.pdf` | card written |
| A | Generate, Filter, Control, Replay | rollout-replay | `papers/2605.02913-gfcr-rollout-strategies-llm-rl.pdf` | card written |

## First Follow-up Queue

当前准入：survey 正文提到 + 开源代码/环境 + 强 venue，直接抽卡；arXiv + 开源 + 明确 RL mechanism 走 exception。纯 reference-only、benchmark-only、prompt-only 不进第一批。

| Priority | Paper | Track | Why selected | Status |
|---|---|---|---|---|
| S | RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning | rollout-replay / exploration | 多轮 agent RL；StarPO / StarPO-S；直接研究 environment feedback、trajectory filtering、reward variance cliffs。 | card written |
| S | GiGPO: Group-in-Group Policy Optimization for LLM Agent Training | credit-assignment / optimizer-objective | 用 anchor-state grouping 做 step-level relative advantage，是 agentic credit assignment 的强机制候选。 | card written |
| S | Agent Lightning: Train ANY AI Agents with Reinforcement Learning | credit-assignment / system-interface | 把 agent execution 形式化为 MDP，提出 hierarchical RL 和 credit assignment module；但也有 model-system overlap。 | card written / cross-link |
| A | ToolRL: Reward is All Tool Learning Needs | reward-verifier / tool-use | 工具调用中的 reward design；适合判断 coarse answer reward vs fine-grained tool reward。 | card written / arXiv exception |
| A | WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum RL | exploration-curriculum / web | ICLR 2025 + code；web agent online curriculum、sparse feedback、policy distribution drift。 | card written |
| A | Search-R1: Training LLMs to Reason and Leverage Search Engines with RL | search-deep-research / rollout | COLM 2025 + code；multi-turn search interaction + outcome reward + retrieved token masking。 | card written |
| A | VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use | environment-interface / tool-use | 统一 ARLT multi-turn tool-use interface；有 model-system overlap。 | card written / arXiv exception / cross-link |
| B | ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL | credit-assignment / off-policy | ICML/PMLR + code；较早 hierarchical multi-turn RL anchor。 | card written |
| B | WebAgent-R1 | web-gui / optimizer-objective | EMNLP 2025 + code；web multi-turn RL lane 候选。 | card written |
| A | Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data | exploration-curriculum / tool-use | arXiv 2026；self-play RL + zero-data tool learning，需确认官方代码/环境。 | queue / arXiv exception pending |
| B | ToolGym | environment-interface / tool-use | arXiv 2026；open-world tool environment，更偏 testing/data curation，暂不主抽。 | queue |
| B | ASTRA | environment-interface / mixed | synthetic trajectories + reinforcement arenas；可能更偏 data/model-system，待核。 | queue |

## Exclusions For Now

| Paper / family | Reason |
|---|---|
| Generic autonomous agent surveys | scope 太宽，不改变 RL loop。 |
| Benchmark-only web / GUI / tool papers | 只作为 environment background，除非提出 reward/update/exploration 机制。 |
| Training Recipes for Agentic RL in LLMs | 更适合未来 `model-system` 项目；这里只保留 cross-link。 |
| RL Foundations for Deep Research Systems | 偏 deep research system；作为 search/deep-research background，不主抽卡。 |

## Open Questions

- `Agent Lightning` 和 `VerlTool` 到底是 agentic-rl 机制卡，还是未来 `model-system` 主卡？
- `GFCR` 里 data/replay 相关论文是否需要同步登记到 `/Users/chy/Research/agent-data/`？
- 第一批正式抽卡是否优先走 `credit-assignment`：RAGEN、GiGPO、Agent Lightning、ArCHer？

## Expanded Recall

更宽的候选队列已移到 `comparison/expanded-candidate-queue.md`。此前 first queue 太窄，漏掉了 CARL、HCAPO、SPA-RL、IGPO、R1-Searcher、DeepResearcher、DiGiRL、SWE-RL，以及 post-survey 的 BEACON。
