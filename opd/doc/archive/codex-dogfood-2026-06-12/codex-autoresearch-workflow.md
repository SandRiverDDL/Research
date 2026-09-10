# OPD Codex Autoresearch Workflow

> 2026-06-12 handoff. This file records the current Codex workflow after the v2 pointer-only plan was rejected. Treat this as newer than the archived cc-intern notes in `doc/archive/cc-intern-2026-06-11/` and the schema notes embedded in `doc/memory/STATE.md`.

## Status

`current L1 schema dogfood` is in progress.

- GKD pilot has been rerun with the current schema.
- MiniLLM and DistiLLM in `notes/_v3-pilot/` are still older outputs and need current-schema reruns.

## One-line Decision Chain

OPD cards are no longer pure pointers. v2 is rejected. The current design is dual-source cross-checking from PDF + song-2026 survey, with Python extraction in the parent session and tightly bounded subagent inputs to reduce token use.

## Current Schema

The schema is implemented in `~/Research/opd/doc/templates/l1-card.md`.

Structure:

- frontmatter, about 17 lines
- 5 body sections: `一句话` / `核心做法` / `谱系位置` / `优缺点` / `headline number`
- 2 footer lines: `<!-- pdf: ... -->` and `<!-- song-2026: ... -->`

New fields:

- `surveys: {song-2026: "§x; §y"}`: survey anchor, multi-survey friendly.
- `addresses: [<tag>]`: failure mode targeted by the method. Tags are controlled by `doc/taxonomy/failure-modes.md`; each card uses at most 3.

Kept fields:

- `title`
- `authors`
- `org`
- `year`
- `venue`
- `arxiv_id`
- `confidence`
- `open_source`
- `verified`
- `decisions`, the OPD 6-field dict

Deleted from v1:

- `## What's Actually New`
- `## Method` experiment setup prose
- `## Verdict`
- `## Evidence` prose block

## Discipline

| ID | Rule | Problem Solved |
|---|---|---|
| S1 | Every paragraph must point back to a specific PDF or survey brief location. Footer is split into `<!-- pdf: ... -->` and `<!-- song-2026: ... -->`. | Hallucination defense and auditability. |
| S2 | Pros/cons source labels must be one of `[作者 ack §x]`, `[song-2026 §x]`, or `[<下游 paper> 年 §x]`. If the survey repeats a downstream critique, the source is the downstream paper, not the survey. | Prevents mistakes like marking DistiLLM's critique of GKD as `[song-2026]`. |
| S3 | Every `addresses:` tag must first be registered in `doc/taxonomy/failure-modes.md`. | Controlled vocabulary. |
| S4 | The `一句话` identity sentence has a banned-word list: `reverse-KL`, `SKL`, `REINFORCE`, `token-level`, `sequence-level`, etc. It should only describe position + time anchor. | Prevents duplication between identity and mechanism. |
| S5 | Formula block is at most 2 lines of LaTeX; use one main formula. | Prevents overstuffed formula blocks, as seen in DistiLLM. |
| S6 | `headline number` has at most 2 items and each must point to `§Table k` or `§Fig k`; prose-only numbers are cut. | Prevents unanchored numbers like "up to 4.3x" from becoming headline evidence. |
| S7 | If a frontmatter field is unknown, delete it; do not write `unknown`. | Improves information density. |
| S8 | Remove verdict language from L1. L2 decisions and subjective judgments move to `doc/memory/STATE.md`. | Keeps L1 as a query entry, not a decision log. |

## Workflow

Parent session preprocessing has produced these controlled inputs:

```text
~/Research/opd/_meta/briefs/papers/<arxiv_id>_<name>.md
  PDF Abstract + Method main formula region + Related Work + Limitations + Conclusion
  About 17-27 kB per paper in the current pilot.

~/Research/opd/_meta/briefs/surveys/<arxiv_id>_<name>.json
  All song-2026 survey mention windows for the method, ±400 chars with true section labels.
  Current pilot has 6 windows per paper.

~/Research/opd/_meta/briefs/surveys/_survey-clean.txt
  Unescaped survey plain text, used for section extraction.

~/Research/opd/doc/taxonomy/failure-modes.md
  Controlled vocabulary, currently 10 tags plus aliases.
```

Subagent hard constraints:

- Must not call `mcp__arxiv__*`, `WebFetch`, or read `~/.arxiv-mcp-storage/`.
- May only read the controlled files above, `doc/templates/l1-card.md`, `doc/taxonomy/failure-modes.md`, and the v1 old card as reference.
- If the brief is insufficient, write that in an ack note; do not fetch more context.

## Open Questions

1. **Subagent vs main-session cost tradeoff**  
   Current measurement: the bounded-input subagent single card used about 104k tokens / 9.6 min, compared with the previous pass at 162k tokens / 5.3 min. Token use is down about 36%, but duration is up about 80%. Switch remaining ordinary card writing back to main-session direct execution.

2. **MiniLLM / DistiLLM current-schema rerun**  
   `notes/_v3-pilot/24_minillm.md` and `notes/_v3-pilot/24_distillm.md` are still older outputs. They contain known findings such as DistiLLM identity sentence overclaim and old source-label issues. Rerun both with the current schema.

3. **13 vs 18 split**  
   Survey-covered cards should be rewritten with the current schema. Survey-uncovered cards should keep v1 for now. The generated `_meta/generated/target-cards.md` is the formal queue.

4. **Failure-mode coverage**  
   `doc/taxonomy/failure-modes.md` exists, but the controlled vocab is still incomplete. DistiLLM motivated `kld-gradient-explosion`; other likely tags include `policy-gradient-variance` and `sgo-generation-cost`. Need map failure modes to the 13 target cards.

5. **Generic `paper-summary` skill backport**  
   The current schema is OPD-specific. After dogfood, backport generic discipline to Codex `autoresearch`: footer anchors, source-labeled pros/cons, no verdict in L1, and parent-extracted PDF controlled regions.

## Dogfood Findings

| ID | Severity | Finding |
|---|---|---|
| F1 | P0 | GKD card incorrectly labeled DistiLLM's critique as `[song-2026]`; it should be `[DistiLLM 2024 §2.2]`. |
| F2 | P0 | MiniLLM `org` is `tsinghua`, but should be `msr-tsinghua`; v1 was already wrong and v3 carried it forward. |
| F3 | P0 | DistiLLM identity sentence says "三篇开山之一"; subagent acknowledged uncertainty, so this is chy inference and violates S2. |
| F4 | P1 | Controlled vocab was missing during the first dogfood pass; subagent wanted to register `kld-gradient-explosion` but could not. |
| M1 | P1 | Identity sentence duplicated the first mechanism sentence in MiniLLM / DistiLLM; fixed by S4 banned-word rule. |
| M2 | P2 | GKD lineage put SeqKD and ImitKD in one bullet; readability is poor. Use one paper per bullet. |
| M3 | P2 | Footer had 7 anchors on one long line; fixed by splitting into PDF and survey footer lines. |
| M4 | P1 | DistiLLM headline used `§Abstract / §Contributions` without a table or figure anchor; fixed by S6. |
| M5 | P2 | DistiLLM formula block contained both SKL and SRKL; fixed by one-main-formula rule. |

Already fixed in current template:

- F1
- F4
- M1
- M3
- M4
- M5

Still needs rerun verification:

- F2
- F3
- M2

## Landed Files

```text
~/Research/opd/doc/templates/l1-card.md
  current schema + discipline.

~/Research/opd/doc/taxonomy/failure-modes.md
  Controlled vocab, 10 tags plus aliases.

~/Research/opd/_meta/briefs/papers/
  bounded paper briefs.

~/Research/opd/_meta/briefs/surveys/
  survey-window JSON files plus clean survey text.

~/Research/opd/notes/_v3-pilot/24_gkd.md
  current-schema rerun output.

~/Research/opd/notes/_v3-pilot/24_minillm.md
  v3 old output; rerun pending.

~/Research/opd/notes/_v3-pilot/24_distillm.md
  v3 old output; rerun pending.
```
