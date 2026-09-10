# Survey-Derived Full Queue

> Source-of-truth queue from the three seed surveys. This file is recall-oriented. It intentionally includes methods that may later be downgraded to background, agent-data cross-link, or model-system cross-link.

## Counts

- Credit Assignment survey inventory: 45 visible method rows extracted from Table 10 (survey text says 47 total; PDF text extraction dropped or merged two rows).
- Landscape search/research table: 18 rows.
- Landscape code/software table: 33 rows.
- Landscape GUI table: 16 RL-based rows plus RL-free background rows.
- Landscape framework table: 13 agentic RL frameworks.
- GFCR adds rollout-interface/background rows: SWE-Gym, BrowserGym, AgentDojo, ARLAS, DeepSearch, Tree-OPO.

Expected queue size after dedup: about 110-120 rows.

## Status Labels

- `card written`: L1 exists.
- `queue / needs original PDF brief`: L1 exists but original paper PDF has not been individually checked.
- `queue`: should be checked.
- `background`: useful but not first-pass card target.
- `cross-link`: likely belongs partly in Agent Data or model-system.

## Core RL Method Queue

| Method | Source | Paper type | Status |
|---|---|---|---|
| ArCHer | Credit Table 10 | core-rl-method | card written |
| StepAgent | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| POAD | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| GiGPO | Credit Table 10 / Landscape / GFCR | core-rl-method | card written |
| SWEET-RL | Credit Table 10 / Landscape | core-rl-method | queue / needs original PDF brief |
| AgentPRM | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| Turn-Level | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| Turn-PPO | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| SORL | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| TARL | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| ITPO | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| IGPO | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| CARL | Credit Table 10 | core-rl-method | card written |
| iStar | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| PilotRL | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| LaRe | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| HCAPO | Credit Table 10 | core-rl-method | card written |
| C3 | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| CCPO | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| CriticSearch | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| SPA-RL | Credit Table 10 / Landscape | core-rl-method | card written |
| Lightning | Credit Table 10 / Landscape | infra-interface | card written |
| RAGEN / StarPO | Credit Table 10 / Landscape / GFCR | core-rl-method | card written |
| SCRIBE | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| PRS | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| AdaptSeg | Credit Table 10 | core-rl-method | queue / needs original PDF brief |
| BEACON | Forward recall | core-rl-method | card written |

## Reasoning Credit-Assignment Background

| Method | Source | Paper type | Status |
|---|---|---|---|
| VinePPO | Credit Table 10 / Landscape | core-rl-method | queue / background |
| RED | Credit Table 10 | core-rl-method | queue / background |
| T-REG | Credit Table 10 | core-rl-method | queue / background |
| From r to Q | Credit Table 10 | core-rl-method | queue / background |
| SPO | Credit Table 10 | core-rl-method | queue / background |
| SCAR | Credit Table 10 | core-rl-method | queue / background |
| TEMPO | Credit Table 10 | core-rl-method | queue / background |
| PURE | Credit Table 10 | core-rl-method | queue / background |
| SPRO | Credit Table 10 | core-rl-method | queue / background |
| CAPO | Credit Table 10 | core-rl-method | queue / background |
| ACPO | Credit Table 10 | core-rl-method | queue / background |
| HICRA | Credit Table 10 | core-rl-method | queue / background |
| PRL | Credit Table 10 | core-rl-method | queue / background |
| InT | Credit Table 10 | core-rl-method | queue / background |
| FinePO | Credit Table 10 | core-rl-method | queue / background |

## Multi-Agent Credit Queue

| Method | Source | Paper type | Status |
|---|---|---|---|
| M-GRPO | Credit Table 10 | core-rl-method | queue |
| LLM-MCA | Credit Table 10 | core-rl-method | queue |
| QLLM | Credit Table 10 | core-rl-method | queue |
| SHARP | Credit Table 10 | core-rl-method | queue |

## Search / Deep Research Queue

| Method | Source | Paper type | Status |
|---|---|---|---|
| DeepRetrieval | Landscape Table 4 | environment-recipe | queue |
| Search-R1 | Landscape Table 4 / GFCR | environment-recipe | card written |
| R1-Searcher | Landscape Table 4 | environment-recipe | card written |
| R1-Searcher++ | Landscape Table 4 | environment-recipe | queue |
| ReSearch | Landscape Table 4 | environment-recipe | queue |
| StepSearch | Landscape Table 4 | environment-recipe | queue |
| DeepResearcher | Landscape Table 4 | environment-recipe | card written |
| WebDancer | Landscape Table 4 | environment-recipe | queue |
| WebThinker | Landscape Table 4 | environment-recipe | queue |
| WebSailor | Landscape Table 4 | environment-recipe | queue |
| WebWatcher | Landscape Table 4 | environment-recipe | queue |
| WebShaper | Landscape Table 4 | environment-recipe | queue |
| ASearcher | Landscape Table 4 | environment-recipe | queue |
| Atom-Searcher | Landscape Table 4 | environment-recipe | card written |
| MiroMind Open Deep Research | Landscape Table 4 | environment-recipe | background |
| SimpleDeepResearcher | Landscape Table 4 | environment-recipe | queue |
| AWorld | Landscape Table 4 / Framework Table 11 | infra-interface | queue |
| SFR-DeepResearch | Landscape Table 4 | environment-recipe | queue |

## Code / Software Queue

| Method | Source | Paper type | Status |
|---|---|---|---|
| AceCoder | Landscape Table 5 | environment-recipe | queue |
| DeepCoder-14B | Landscape Table 5 | environment-recipe | queue |
| RLTF | Landscape Table 5 / GFCR | core-rl-method | queue |
| CURE | Landscape Table 5 | environment-recipe | queue |
| Absolute Zero | Landscape Table 5 | environment-recipe | queue |
| StepCoder | Landscape Table 5 | core-rl-method | queue |
| PSGPO | Landscape Table 5 | core-rl-method | queue |
| CodeBoost | Landscape Table 5 | environment-recipe | queue |
| PRLCoder | Landscape Table 5 | core-rl-method | queue |
| o1-Coder | Landscape Table 5 | environment-recipe | queue |
| Posterior-GRPO | Landscape Table 5 | core-rl-method | queue |
| Policy Filtration for RLHF | Landscape Table 5 | data-overlap | cross-link |
| CodeFavor | Landscape Table 5 | environment-recipe | queue |
| Focused-DPO | Landscape Table 5 | core-rl-method | queue |
| Re:Form | Landscape Table 5 | environment-recipe | queue |
| Qwen Team coder RL | Landscape Table 5 | environment-recipe | background |
| RLEF | Landscape Table 5 | environment-recipe | queue |
| µCode | Landscape Table 5 | environment-recipe | queue |
| R1-Code-Interpreter | Landscape Table 5 | environment-recipe | queue |
| IterPref | Landscape Table 5 | core-rl-method | queue |
| LeDex | Landscape Table 5 | core-rl-method | queue |
| CTRL | Landscape Table 5 | environment-recipe | queue |
| ReVeal | Landscape Table 5 | environment-recipe | queue |
| DeepSWE | Landscape Table 5 | environment-recipe | queue |
| SWE-RL | Landscape Table 5 / GFCR | environment-recipe | card written |
| Satori-SWE | Landscape Table 5 | environment-recipe | queue |
| RLCoder | Landscape Table 5 | environment-recipe | queue |
| Qwen3-Coder | Landscape Table 5 | environment-recipe | background |
| ML-Agent | Landscape Table 5 | environment-recipe | queue |
| OS-R1 | Landscape Table 5 | environment-recipe | queue |
| Golubev et al. | Landscape Table 5 | environment-recipe | queue |
| SWE-Gym | GFCR | benchmark-env | queue / cross-link |

## Web / GUI Queue

| Method | Source | Paper type | Status |
|---|---|---|---|
| GUI-R1 | Landscape Table 7 | environment-recipe | queue |
| UI-R1 | Landscape Table 7 | environment-recipe | queue |
| InFiGUI-R1 | Landscape Table 7 | environment-recipe | queue |
| AgentCPM | Landscape Table 7 | environment-recipe | queue |
| UI-Venus | Landscape Table 7 | environment-recipe | queue |
| WebAgent-R1 | Landscape Table 7 | environment-recipe | card written |
| UI-TARS | Landscape Table 7 | environment-recipe | queue |
| UI-TARS-2 | Landscape Table 7 | environment-recipe | queue |
| DiGiRL | Landscape Table 7 | environment-recipe | card written |
| ZeroGUI | Landscape Table 7 | environment-recipe | queue |
| MobileGUI-RL | Landscape Table 7 | environment-recipe | queue |
| ComputerRL | Landscape Table 7 | environment-recipe | queue |
| ARLAS | GFCR | environment-recipe | queue |
| BrowserGym | GFCR | benchmark-env | background |
| AgentDojo | GFCR | benchmark-env | background |

## Framework / Infra Queue

| Method | Source | Paper type | Status |
|---|---|---|---|
| Verifiers | Landscape Table 11 | infra-interface | queue |
| SkyRL-v0 | Landscape Table 11 | infra-interface | queue |
| AREAL | Landscape Table 11 | infra-interface | queue |
| MARTI | Landscape Table 11 | infra-interface | queue |
| EasyR1 | Landscape Table 11 | infra-interface | queue |
| AgentFly | Landscape Table 11 | infra-interface | queue |
| Agent Lightning | Landscape Table 11 / Credit Table 10 | infra-interface | card written |
| AWorld | Landscape Table 11 | infra-interface | queue |
| RL-Factory | Landscape Table 11 | infra-interface | queue |
| ROLL | Landscape Table 11 | infra-interface | queue |
| AgentRL | Landscape Table 11 | infra-interface | queue |
| VerlTool | Landscape Table 11 / GFCR | infra-interface | card written |
| OpenRLHF | Landscape Table 11 | infra-interface | background |
