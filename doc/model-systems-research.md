# Model Systems Research Workflow

> Workspace-level rules for studying frontier model technical reports, open training projects, and reusable training / system insights.

## Scope

Use this workflow when the research question is about large model systems:

- frontier model technical reports from companies or labs;
- open training projects and recipes;
- model architecture, data pipeline, training recipe, post-training / RL, evaluation, safety, and infra;
- reusable method / technique / tuning insight extracted from those sources.

This workflow is not limited to "training recipes". A model TR is usually a system source: it may contain recipe evidence, architecture decisions, data processing, evaluation practice, safety claims, and infra ideas.

## Core Split

Do not split the project by `TR vs recipe` as the primary research boundary. Split by responsibility:

- `sources/`: preserve source understanding by model, release, or open project.
- `lenses/`: extract cross-source insights by research question.
- `comparison/`: make cross-model judgments, transferability claims, and evidence audits.

The rule:

```text
sources/ answers: what did this model/project do?
lenses/ answers: where does this idea appear and can it transfer?
comparison/ answers: what do we believe across sources?
```

## Recommended Project Layout

For a dedicated topic, use a project such as `~/Research/foundation-model-systems/`:

```text
foundation-model-systems/
  AGENTS.md
  doc/memory/STATE.md

  sources/
    deepseek-vx/
      README.md
      source-bundle.md
      section-index.md
      notes/
        architecture.md
        pretraining-data-mixture.md
        pretraining-engineering.md
        rl-training.md
        eval.md
        infra.md
        claims-and-gaps.md
    open-r1/
      README.md
      source-bundle.md
      section-index.md
      notes/
        data-pipeline.md
        distillation.md
        eval.md

  lenses/
    architecture/
    data-pipeline/
    training-recipes/
    rl-training/
    eval-and-benchmarking/
    infra-and-efficiency/

  comparison/
    model-system-matrix.md
    frontier-vs-open-transfer.md
    recipe-fragment-index.md
    claims-vs-reproducibility.md
```

Do not create all section files by default. Create only the files needed by the source. A small source may only need `README.md`, `training.md`, `eval.md`, and `claims-and-gaps.md`.

## Source Dossier Rules

A major model TR or open project should be treated as a source dossier, not as one enlarged paper card.

The dossier `README.md` is the default context entry. Keep it short enough to read first:

```markdown
# <Model / Project> Source Dossier

```yaml
---
source_id:
source_type:
org:
release_date:
priority:
status:
openness:
confidence:
---
```

## 一句话

## 为什么重要

## 核心机制 / Takeaways

## Source Bundle

## Citation Labels

## 最大证据缺口

## Lens Hooks

## 阅读入口
```

`section-index.md` is the navigation layer for returning to the source; it is not a summary. Long section notes live under `notes/` and hold evidence and local understanding. They should preserve source anchors such as page numbers, tables, figures, config paths, commits, logs, or repository links.

Stage notes use a human-first structure:

- `Core Design / Innovation`: the core design, innovation, tradeoff, or training-system idea.
- `Why It Matters`: what is worth learning vs what is lookup-only.
- `Mechanism Sketch`: the short process for how it works.
- `Details / Evidence`: necessary detail, ablations, controls, and anchors.
- `Gaps / Open Questions`: missing disclosures and claims that need checking.
- `Lookup-only`: exact percentages, hyperparameters, benchmark entries, kernel names, cluster details.
- `Evidence Anchors`: page or source labels.

Do not use `fact / interpretation / speculation / open question` as default top-level headings. Use those labels only inside bullets or local caveats.

## Lens Note Rules

Lens notes are not second copies of source dossiers. They are cross-source indexes and synthesis notes.

A lens entry should link back to the source dossier and preserve the exact anchor:

```markdown
## DeepSeek-Vx

source: ../../sources/deepseek-vx/README.md
anchor: TR Section X / Table Y / repo config path

### Reusable Decision

### Why It Might Work

### Scale Dependence

### Transferability

### Evidence / Caveats
```

Use lenses for questions such as:

- how frontier TRs and open projects handle SFT data mixing;
- which RL / verifier loops are claimed vs actually reproducible;
- which architecture choices appear tied to scale;
- which infra ideas matter for training or inference economics.

## Recipe Fragment Taxonomy

A recipe can be full, partial, or fragmentary. Do not discard useful fragments just because they are not end-to-end.

Use these categories:

- `full-recipe`: end-to-end training pipeline, preferably with code/config/logs.
- `stage-recipe`: one training stage with enough detail to execute or compare.
- `method`: reusable decision procedure with input, operation, and output.
- `technique`: local implementation or tuning choice.
- `tuning-insight`: empirical lesson that guides decisions but is not itself a procedure.
- `claim`: low-evidence or anecdotal statement to track but not trust yet.

Useful metadata:

```yaml
primary_type: full-recipe | stage-recipe | method | technique | tuning-insight | claim
training_stage: pretraining | sft | preference | rl | opd | distillation | eval | infra
scope: local | stage | pipeline | system
scale_regime: frontier-industrial | open-midscale | open-smallscale | toy
evidence_mode: tr-claim | paper-ablation | config-code | logs | reproduction | anecdote
confidence: low | medium | high
```

Do not overfit on whether something "sounds like a method". Prefer this rule:

```text
method = a reusable decision procedure
technique = a local implementation or tuning choice
insight = a lesson that changes decisions
claim = a statement not yet backed by enough evidence
```

## Model TR vs Open Recipe

Model TRs and open recipes overlap. Keep the distinction in evidence mode, not in source ownership.

- Frontier TRs often provide industrial practice signals but lack reproducible details.
- Open projects often provide code/config/logs but may be smaller-scale or less frontier-relevant.

For comparison, ask:

- Which training stage does this insight affect?
- At what scale regime did it appear?
- Is there public code/config/log evidence?
- Is it frontier practice, reproducible practice, or both?
- What could transfer to our feasible experiment scale?

## Boundary With Existing Agent Topics

Keep general model-system notes out of `agent-data/` and `agentic-rl/` unless the core contribution matches those topics.

Route by primary contribution:

- data generation / filtering / verification / curriculum for agent training -> `agent-data/`;
- reward design, rollout, policy update, exploration, credit assignment -> `agentic-rl/`;
- model release claim audit or broad system understanding -> `foundation-model-systems`;
- reusable LLM training / post-training / infra / eval insight -> `foundation-model-systems` lens note.

When one source is relevant to multiple topics, write the full source understanding once in `foundation-model-systems/sources/`, then create narrow cross-links or viewpoint notes elsewhere.

## Evidence Discipline

Every strong statement should make its epistemic status clear when it matters:

- fact;
- interpretation;
- speculation;
- open question.

Use these as local claim labels or caveats, not as mandatory top-level note sections. Human-first stage notes should still be organized by core design, mechanism, evidence, gaps, and lookup-only details.

For hard-to-understand infra or systems details, do not block the dossier. Mark:

```yaml
depth: surface | working | deep
confidence: low | medium | high
need_expert_review: true | false
```

At `surface` depth, capture only:

- what bottleneck the source claims to address;
- how it may affect training or inference;
- which terms or mechanisms are not yet understood;
- what comparison or transfer decision it might change.

## Autoresearch Fit

Borrow the evidence discipline from autoresearch, but do not copy the card pipeline:

- A source listing or manifest row is not a note.
- Survey, blog, and announcement text are recall / positioning signals, not enough for a formal source dossier.
- Important model TRs and open projects become source dossiers, not oversized L1 cards.
- Lenses and comparison files carry cross-source reasoning.
- Do not feed full TRs into synthesis prompts by default; read dossier README files first, then section files only as needed.
- Use scripts for manifest / status / validation only. Do not recreate heavy queue / card validators unless the source volume justifies it.

## Skill Boundary

The global `research-codex-workflow` skill should keep cross-project behavior: evidence before conclusion, bounded context, validator-as-hygiene, and project-local rules. Do not put model-system-specific vocab, stage-note file names, citation labels, or TR checklist details into the global skill.

If the same source-dossier workflow is reused across multiple independent model-system projects, consider a separate local skill later. Until then, keep these rules in project docs.
