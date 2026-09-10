# Expanded Candidate Queue

> 2026-06-16 修复：此前只处理了手工 first queue，recall 太窄。这里从三篇 seed survey 正文 / taxonomy / tables 以及 post-survey forward recall 扩展候选。

## Recall Rules

- Survey 正文 / taxonomy / table 中出现：进入 queue。
- Reference-only：不进，除非另有正文讨论或用户点名。
- Post-survey forward recall：从已抽卡 anchor 的直接后续或强对比论文补入，例如 BEACON 是 GiGPO/GRPO 的后续对比。
- Card 仍按 `doc/triage-rules.json`：强 venue + code，或 arXiv + official code + clear RL mechanism。

## Carded

| Paper | Track | Basis |
|---|---|---|
| Landscape Agentic RL Survey | survey | TMLR 2026 seed |
| Credit Assignment Survey | survey | seed |
| GFCR Rollout Survey | survey | seed |
| ArCHer | credit-assignment / off-policy | ICML 2024 + code; Credit survey core method |
| RAGEN / StarPO | rollout / stability | arXiv + code; Landscape/GFCR/Credit survey |
| GiGPO | credit-assignment | NeurIPS 2025 + code; Landscape/GFCR/Credit survey |
| Agent Lightning | system-interface / credit | arXiv + code; Landscape/Credit survey |
| ToolRL | reward-verifier / tool-use | arXiv + code; Landscape |
| WebRL | web / curriculum | ICLR 2025 + code; GFCR |
| Search-R1 | search / rollout | COLM 2025 + code; Landscape/GFCR |
| VerlTool | tool-use / environment-interface | arXiv + code; Landscape/GFCR |
| WebAgent-R1 | web / multi-turn RL | EMNLP 2025 + code; Landscape |
| BEACON | credit-assignment / milestone | post-survey; arXiv + code; compares against GRPO/GiGPO |

## Credit-Assignment Queue

| Priority | Paper / method | Track | Why queued | Status |
|---|---|---|---|---|
| S | CARL: Critical Action Reinforcement Learning | credit-assignment | entropy-based critical actions; Credit survey section + table. | card written |
| S | HCAPO: Hindsight Credit Assignment for Policy Optimization | credit-assignment | 2026; hindsight / retrospective turn credit; Credit survey section + table. | card written |
| S | SPA-RL: Stepwise Progress Attribution | credit-assignment | agentic stepwise progress estimator; Landscape/Credit survey. | card written |
| A | IGPO: Information Gain Policy Optimization | credit-assignment | information-gain turn credit; Credit survey section + table. | queue |
| A | VinePPO | reasoning-to-agentic background | ICML 2025 token-level MC value; foundational CA method; useful baseline even if reasoning-centric. | queue / maybe card |
| A | SWEET-RL | credit-assignment / collaborative agents | privileged critic / collaborative reasoning; Credit survey + Landscape references. | queue |
| A | AgentPRM | credit-assignment | TD+GAE / turn-level value for agents; Credit survey taxonomy. | queue |
| A | C3 / CCPO | multi-agent credit | counterfactual / causal credit; Credit survey taxonomy. | queue |
| B | POAD | credit-assignment | action decomposition; Credit survey taxonomy. | queue |
| B | iStar | credit-assignment | implicit DPO-style credit; Credit survey taxonomy. | queue |
| B | HICRA | credit-assignment | hierarchy; Credit survey taxonomy. | queue |
| B | PURE / SPRO / RED / T-REG / SCAR | reasoning CA background | may inform token/segment credit but likely not core agentic. | background queue |
| B | CriticSearch / CAPO / LaRe | LLM-as-critic credit | retrospective / critic-based credit; need scope check. | queue |

## Search / Deep-Research / Retrieval Queue

| Priority | Paper / method | Track | Why queued | Status |
|---|---|---|---|---|
| S | R1-Searcher | search RL | Landscape table marks GitHub; two-stage PPO for search invocation/exploitation. | card written |
| A | R1-Searcher++ | search RL | Dynamic knowledge / search follow-up; Landscape table marks GitHub. | queue |
| A | DeepResearcher | deep-research RL | Scaling deep research via RL in real-world environments; Landscape table marks GitHub. | card written |
| A | Atom-Searcher | deep-research reward | fine-grained atomic thought reward; Landscape table marks GitHub. | card written |
| A | ASearcher | adaptive search RL | search lane; Landscape table marks GitHub. | queue |
| B | SimpleDeepResearcher / SimpleDeepSearcher | search/deep-research | Landscape table marks GitHub; check mechanism vs data synthesis. | queue |
| B | Kimi-Researcher | deep-research system | website only; likely model-system / product report, not card unless technical report appears. | background |

## Web / GUI / Device Queue

| Priority | Paper / method | Track | Why queued | Status |
|---|---|---|---|---|
| A | DiGiRL | device-control RL | offline-to-online autonomous RL; Landscape web/GUI section marks GitHub. | card written |
| A | MobileGUI-RL | GUI RL | scales Android virtual-device RL; Landscape section. | queue |
| A | UI-R1 | GUI action prediction RL | GUI action prediction via RL; Landscape references. | queue |
| B | ARLAS | web robustness / adversarial RL | GFCR mentions adversarial training for browser tasks. | queue |
| B | Agent Q | web agent RL/search | web-agent family; need source check. | queue |
| B | BrowserGym / AgentDojo | environment | useful env background, not method card unless RL update. | background |

## Code / Software Queue

| Priority | Paper / method | Track | Why queued | Status |
|---|---|---|---|---|
| A | SWE-RL | code / software RL | Landscape and GFCR mention; outcome signals from GitHub commits / SWE tasks. | card written |
| A | SWE-Gym | code environment / verifier | GFCR mentions agents + verifiers; may be environment/data overlap. | queue / cross-link |
| B | rStar2-Agent | code/math agent RL | Landscape references; scope check needed. | queue |

## Tool / Environment Queue

| Priority | Paper / method | Track | Why queued | Status |
|---|---|---|---|---|
| S | Tool-R0 | tool-use / self-play | zero-data self-play tool learning; already in seed queue; code/env needs confirmation. | arXiv exception pending |
| A | ToolGym | tool environment | environment + curation; likely background unless RL loop method. | queue |
| A | ASTRA | reinforcement arenas | may be model-system/data overlap; check reinforcement arena side. | queue |

## Immediate Next Cards

1. IGPO
2. SWEET-RL
3. AgentPRM
4. R1-Searcher++
5. ASearcher
6. MobileGUI-RL / UI-R1
7. Tool-R0
