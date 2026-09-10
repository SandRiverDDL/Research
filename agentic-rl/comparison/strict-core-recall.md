# Strict Agentic RL Core Recall

> 2026-06-17 first pass. This list is recall-oriented; it is not the formal card set.

## Screening Rule

High-priority card candidates need a strict RL mechanism for training LLM agent policy plus original source evidence. Method papers should have official code unless they are major-lab / frontier-lab exceptions. New papers can be queued before venue status stabilizes; old papers need venue, code plus impact proxy, or major-lab exception.

## Candidate Table

| decision | title | arxiv / source | first public | open status | venue / impact | strict core reason | recall source |
|---|---|---|---|---|---|---|---|
| card written | StepPO: Step-Aligned Policy Optimization for Agentic Reinforcement Learning | 2604.18401 | 2026-04-20 | official code via AgentR1/StepPO | new arXiv; no stable venue needed yet | reformulates agentic RL as step-level MDP and proposes step-aligned policy optimization / credit assignment | keyword search; Agent-R1 related work |
| card written | AT^2PO: Agentic Turn-based Policy Optimization via Tree Search | 2601.04767 | 2026-01-08 | official code at zzfoutofspace/ATPO | new arXiv; no stable venue needed yet | turn-level tree search, turn-wise credit assignment, and turn-level policy objective | keyword search; StepPO / Tree-GRPO neighborhood |
| card written | ARPO: Agentic Reinforced Policy Optimization | 2507.19849 / OpenReview TX4k7BF6aO | 2025-07 | official code at RUC-NLPIR/ARPO | ICLR 2026 poster + code | adaptive rollout / branching for high-entropy tool-call rounds in multi-turn LLM agents | keyword search; newer papers cite as baseline |
| card written | Tree Search for LLM Agent Reinforcement Learning / Tree-GRPO | 2509.21240 | 2025-09-25 | official code at AMAP-ML/Tree-GRPO | ICLR 2026 + code | tree-structured rollouts and intra/inter-tree grouped relative advantage for agent steps | keyword search; related work in AT^2PO |
| card written | APPO: Agentic Procedural Policy Optimization | 2606.12384 | 2026-06-10 | project page says GitHub | very new arXiv | branch-location selection plus procedure-level advantage scaling for fine-grained agentic credit | keyword search |
| card written | Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL | 2602.04284 | 2026-02-04 | official code/data at usail-hkust/Agent-Omit | GitHub claims ICML 2026 | omit-aware agentic RL with dual sampling and omission reward for efficient multi-turn agents | keyword search |
| card candidate / verify code-impact | AEPO: Agentic Entropy-Balanced Policy Optimization | 2510.14545 | 2025-10-16 | appears in ARPO repo; verify exact release | old by 2026-06-17; impact/venue needs verification | balances entropy in rollout and policy update; entropy-aware advantage estimation for web-agent training | keyword search; ARPO repo follow-up |
| card candidate / major-lab exception | rStar2-Agent: Agentic Reasoning Technical Report | 2508.20722 | 2025-08-28 | Microsoft repo available | Microsoft technical report; community signal via HF paper | GRPO-RoC resample-on-correct rollout strategy for code-environment noise | keyword search; related work |
| card candidate / old + venue | RLTR: Reinforcement Learning for LLM Agent Planning | 2508.19598 / EMNLP Industry 2025 | 2025-08-27 | code unclear | EMNLP Industry 2025; Tencent | decouples planning-module RL with tool-use completeness reward | keyword search |
| card written | DynaWeb: Model-Based Reinforcement Learning of Web Agents | 2601.22149 | 2026-01-29 | project page says code/models/data release at data-for-agents.github.io | new arXiv | web world model supplies imagined on-policy rollouts for model-based web-agent RL | keyword search |
| queue / verify code | RAPO: Retrieval-Augmented Policy Optimization | 2603.03078 | 2026-03 | code unclear | new arXiv | retrieval-augmented exploration / off-policy signal injection for agentic RL | keyword search; Tree-GRPO/ARPO neighborhood |
| card written | EMPO^2: Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization | 2602.23008 / OpenReview UOzxviKVFO | 2026-02-26 | project page `agent-lightning/empo2`; verify exact code path | ICLR 2026 OpenReview page | memory-augmented hybrid on/off-policy optimization for exploration | keyword search |
| queue / very new | EDGE: Experience-Distillation for Guided Exploration in Agentic RL | OpenReview JARVj9rlPP | 2026-05-26 | code unclear | ACL ARR 2026 May submission | distills reusable exploration patterns from interaction trajectories into guided exploration | keyword search |
| queue / old-open-recipe | ReTool: Reinforcement Learning for Strategic Tool Use in LLMs | 2504.11536 | 2025-04-15 | project releases code/data/model | old arXiv; strong community signal needs verification | outcome-driven tool-use RL teaches when/how to invoke code interpreter | keyword search; related work |
| queue / old-open-recipe | ToRL: Scaling Tool-Integrated RL | 2503.23383 | 2025-03-30 | official code at GAIR-NLP/ToRL | old arXiv; impact proxy via citations/community needs verification | tool-integrated RL from base models; likely recipe unless reusable RL mechanism is found | related work |
| card written | PaperScout / PSPO: Process-Aware Sequence-Level Policy Optimization | 2601.10029 | 2026-01-15 | official code at pty12345/PaperScout | new arXiv / OpenReview | sequence-level policy optimization aligns with paper-search agent interaction granularity | related work from StepPO; keyword search |
| card written | SDAR: Self-Distilled Agentic Reinforcement Learning | 2605.15155 | 2026-05-14 | official code at ZJU-REAL/SDAR | new arXiv; HF daily paper signal | gated on-policy self-distillation auxiliary objective while keeping RL as primary backbone | keyword search |
| card written | SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills | 2606.02355 | 2026-06-01 | official code at kirito618/SIRI | new arXiv | self-mines, validates, and internalizes skills using RL / advantage-weighted distillation | keyword search |
| card written | ReSkill: Reconciling Skill Creation with Policy Optimization in Agentic RL | 2606.01619 | 2026-06-01 | code website linked from paper | new arXiv | uses GRPO group structure for skill version comparison and policy-skill co-evolution | keyword search |
| card written | DynaWeb: Model-Based Reinforcement Learning of Web Agents | 2601.22149 | 2026-01-29 | project says code/models/data release at data-for-agents.github.io | new arXiv | world model supplies imagined web rollouts for model-based web-agent RL | keyword search; existing hold upgraded |
| card written | EMPO^2: Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization | 2602.23008 / OpenReview UOzxviKVFO | 2026-02-26 | project page `agent-lightning/empo2`; verify exact code path | ICLR 2026 OpenReview page | memory-augmented hybrid on/off-policy optimization for exploration | existing hold upgraded |
| card written | EAPO: Exploration-Aware Policy Optimization | 2605.08978 | 2026-05-12 | official code at HansenHua/EAPO-ICML26 | ICML 2026 | explicit exploration-and-memory mode plus exploration-aware policy objective | keyword search |
| card candidate / data-overlap review | CLEANER: Self-Purified Trajectories Boost Agentic RL | 2601.15141 | 2026-01-21 | official code at Tianshi-Xu/Open-CLEANER | new arXiv / OpenReview PDF | self-purified trajectories reduce noisy credit from failed tool interactions | keyword search |
| queue / verify code | GEPO: Graph-Enhanced Policy Optimization in LLM Agent Training | 2510.26270 | 2025-10-30 | code promised, not verified | old arXiv; no venue verified | graph centrality supplies intrinsic reward, topology-aware advantage, and dynamic discount | keyword search |
| queue / old-open-recipe | Tool-R1: Sample-Efficient Reinforcement Learning for Agentic Tool Use | 2509.12867 | 2025-09-16 | code promised / verify repo | old arXiv; Huawei Noah's Ark | dynamic sample queue reuses high-quality trajectories for tool-use RL | keyword search |
| queue / old-open-recipe | TAPO: Tool-Augmented Policy Optimization | 2510.07038 | 2025-10-08 | code unclear | old arXiv | DAPO-style policy optimization adapted to adaptive tool invocation | keyword search |
| card written | HGPO: Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks | 2602.22817 / OpenReview T8Dev99qnz | 2026-02-26 | official code at langfengQ/verl-agent recipe/hgpo | ICLR 2026 | hierarchy-of-groups advantage estimation fixes context inconsistency in stepwise relative advantages | Round 2 keyword search; DynaWeb/SIRI neighborhood |
| card written | SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning | 2602.08234 | 2026-02-10 | official code at aiming-lab/SkillRL | new arXiv; HF paper signal | recursively evolves skill library during RL so skills and policy co-evolve | Round 2 related work from SIRI/SDAR |
| card written | D2Skill: Dynamic Dual-Granularity Skill Bank for Agentic RL | 2603.28716 | 2026-03-30 | official code at TU2021/D2Skill-AgenticRL | new arXiv; HF paper signal | paired baseline/skill rollouts produce hindsight utility for task-level and step-level skills plus policy optimization | Round 2 related work from SIRI |
| adjacent hold | ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning | 2603.16060 | 2026-03-18 | official code at Skylanding/ARISE | new arXiv | mostly mathematical reasoning skill evolution without external agent environment; keep as adjacent skill/RL background, not strict agentic-rl card | Round 2 related work from SIRI |
| card written | EAPO: Scaling Agentic Reasoning via Exploration-Aware Policy Optimization | 2605.08978 | 2026-05-12 | official code at HansenHua/EAPO-ICML26 | ICML 2026; code/model release | exploration-and-memory reasoning mode plus exploration-aware policy objective | Round 2 keyword search; existing hold upgraded |
| high-priority card candidate | INSPO: Agentic Policy Optimization via Instruction-Policy Co-Evolution | 2512.01945 | 2025-12-01 | official code at cambridgeltl/inspo | recent arXiv with code | dynamic instruction population sampled in RL loop; reward attributed to instructions and low performers pruned | Round 3 related work from ReSkill |
| high-priority card candidate | SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization | 2604.02268 | 2026-04-02 | official code at ZJU-REAL/SkillZero | new arXiv; HF paper signal | dynamic curriculum withdraws skill context based on on-policy helpfulness until zero-shot skill-free behavior | Round 3 related work from skill branch |
| high-priority card candidate | SAPO / Co-Evolving Skill Generation and Policy Optimization | 2606.08755 | 2026-06-09 | official code at zzwjames/skill_augmented_agent | very new arXiv with code | candidate skills validated by base vs skill-augmented rollout marginal utility, then used to train policy as skill generator | Round 3 related work from ReSkill/D2Skill |

## Immediate Batch

Already upgraded to formal L1 cards:

1. StepPO
2. AT^2PO
3. ARPO
4. Tree-GRPO
5. APPO
6. Agent-Omit

Next hold list for one more verification before card:

- AEPO
- RAPO
- EDGE
- RLTR
- rStar2-Agent

## Round 1 Snowballing Log

- Source cards: StepPO, AT^2PO, Tree-GRPO, ARPO, APPO, Agent-Omit.
- Related-work/direct-competitor additions: PaperScout/PSPO; Agent-R1 and Claw-R1 were observed but treated as framework/data middleware rather than strict-core method candidates.
- Keyword-search additions: SDAR, SIRI, ReSkill, EAPO, CLEANER, GEPO, Tool-R1, TAPO.
- Existing hold upgraded to high-priority after verification signal: DynaWeb, EMPO^2.
- New high-priority strict-core candidates this round: 6+; stop condition not met.

## Round 2 Snowballing Log

- Source cards: PaperScout/PSPO, SDAR, SIRI, DynaWeb, EMPO^2 plus keyword direct search.
- Already-carded hits removed: HCAPO, PRS/VSPO, PilotRL, WebRL, WebAgent-R1 and related 2025 credit-assignment cards.
- Related-work additions: SkillRL, D2Skill, ARISE.
- Keyword-search additions: HGPO; EAPO upgraded after code link verification.
- Carried high-priority candidate from Round 1 for carding: ReSkill.
- New high-priority strict-core candidates this round: 4 after ARISE downgraded to adjacent; stop condition not met.

## Round 3 Snowballing Log

- Source cards: ReSkill, HGPO, EAPO, SkillRL, D2Skill.
- High-priority additions: INSPO, SKILL0, SAPO / Co-Evolving Skill Generation and Policy Optimization.
- Held as adjacent/background: MemRL and EvolveR as non-parametric memory evolution; ACT as action-quality critic; MUA-RL as older 2025 tool-use application without venue/impact exception.
- New high-priority strict-core candidates this round: 3; stop condition not met.
