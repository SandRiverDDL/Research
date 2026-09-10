# Triage Audit

> 2026-06-16 修正版：把正式 L1 card、legacy survey-only note、queue row 分开计数。2026-06-16 后续更新：20 个 legacy survey-only notes 已用 original PDF / bounded brief 重新抽卡。2026-06-17 新增 strict-core recall pass。

## Current Counts

- Formal notes in `notes/` root: 48.
- Validator-passing L1/survey notes: 48.
- Legacy survey-only notes in `notes/provisional-survey-derived/`: 0.
- Archived legacy survey-only stubs: 20 under `_meta/legacy-survey-only/upgraded/`.
- Original-paper bounded briefs: 44.
- Survey bounded briefs: 4.
- PDFs downloaded: 48.
- Explicit candidate rows in canonical `comparison/queue.md`: 139 rows by current helper count.
- Latest validator: `scripts/autoresearch.py validate` passes with 0 errors.

## Corrected Interpretation

The current project now has 48 valid formal L1/survey notes.

- The 48 notes in `notes/` root are the current valid formal note set.
- The previous 20 files in `notes/provisional-survey-derived/` were upgraded from original paper PDFs / bounded briefs and archived under `_meta/legacy-survey-only/upgraded/`.
- A candidate becomes a formal L1 card only after original paper PDF/HTML evidence is checked and a bounded paper brief exists.

## What Was Actually Evaluated

Processed into formal notes:

1. Four survey seeds / boundary notes:
   - `The Landscape of Agentic Reinforcement Learning for LLMs`
   - `From Reasoning to Agentic: Credit Assignment in RL for LLMs`
   - `Generate, Filter, Control, Replay`
   - `Environment Scaling for Interactive Agentic Experience Collection`
2. Thirty-eight original-paper notes with local PDFs and bounded paper briefs.
3. Limited forward recall from known anchors:
   - GiGPO / GRPO -> BEACON
   - Search-R1 / R1-Searcher family
   - DeepResearcher / Atom-Searcher
   - WebRL / WebAgent-R1
   - DigiRL / SWE-RL
4. Strict-core recall from keyword search / related work:
   - StepPO
   - AT^2PO
   - ARPO
   - Tree-GRPO
   - APPO
   - Agent-Omit

Upgraded from legacy survey-only notes:

- AgentPRM, AdaptSeg, PRS, ITPO, POAD, LaRe, Turn-PPO, PilotRL, iStar, CCPO, TARL, IGPO, C3, SORL, SWEET-RL, CriticSearch, SCRIBE, VinePPO, HICRA, StepAgent.

## Formal Notes By Type

### Survey

- Landscape Agentic RL Survey
- Credit Assignment Survey
- GFCR Rollout Survey
- Environment Scaling Survey note

### Core RL Method

- ArCHer
- RAGEN / StarPO
- GiGPO
- BEACON
- CARL
- HCAPO
- SPA-RL
- AgentPRM
- AdaptSeg
- PRS
- ITPO
- POAD
- LaRe
- Turn-PPO
- PilotRL
- iStar
- CCPO
- TARL
- IGPO
- C3
- SORL
- SWEET-RL
- CriticSearch
- SCRIBE
- VinePPO
- HICRA
- StepAgent
- StepPO
- AT^2PO
- Tree-GRPO
- ARPO
- APPO
- Agent-Omit

### Environment Recipe

- ToolRL
- WebRL
- WebAgent-R1
- Search-R1
- R1-Searcher
- DeepResearcher
- Atom-Searcher
- DigiRL
- SWE-RL

### Infra / Interface

- Agent Lightning
- VerlTool

## Legacy Survey-Only Queue

No legacy survey-only notes remain in `notes/provisional-survey-derived/`. The upgraded source stubs are retained under `_meta/legacy-survey-only/upgraded/` for audit.

## Rejection / Hold Policy Going Forward

Do not silently ignore methods. Every candidate from survey tables/taxonomies should land in one of:

- `card written`
- `queue`
- `provisional / needs original PDF brief`
- `background`
- `reject`
- `agent-data cross-link`
- `model-system cross-link`

Every `reject` must include one short reason:

- reference-only
- no RL update
- benchmark-only
- prompt-only
- data mechanism only
- model-system / recipe only
- no source found
- duplicate / subsumed by stronger version

## Next Recall Target

To reach a 100-card-level project, the next pass should continue from the broad queue, but upgrade candidates in this order:

1. Remaining strict-core recall rows after code/venue verification: AEPO, DynaWeb, RAPO, EMPO^2, EDGE, RLTR, rStar2-Agent.
2. Remaining core RL method queue rows with original PDFs first.
3. Search / deep research RL methods.
4. Web / GUI / device-control RL methods.
5. Code / software-agent RL methods.
6. Infra / benchmark cards only when they materially affect RL training or evaluation.

Target next milestone:

- Keep roughly 100+ explicit queue rows and update counts via `scripts/autoresearch.py status`.
- Upgrade the next 20-30 queue/core-method candidates into formal L1 cards with original-paper briefs.
- Keep validator passing after each batch.
