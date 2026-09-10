---
name: generate-method-ideas
description: Generate and review research ideas constrained to focused new-method papers with non-incremental contributions. Use when the user asks for method-only research ideas, non-incremental ideas, top-venue method directions, or wants idea-creator run through fixed lenses for supervision-object mismatch, broken shared assumptions, or cross-paper contradictions.
---

# Generate Method Ideas

Read and follow `../idea-creator/SKILL.md` completely as the base workflow. Apply the stricter rules below throughout generation, review, and reporting. User instructions override both skills.

## Required outcome

Generate only ideas whose dominant contribution is a new method. Exclude diagnostic-only studies, benchmarks, taxonomies, surveys, theory-only questions, and empirical findings without a new intervention.

A candidate must:

- target a concrete, consequential failure mode;
- state in 2–4 plain-language steps what is built or trained;
- change a substantive learning object, such as the supervision or optimization object, information set, state/action abstraction, or policy decision space;
- need the proposed method for its central claim;
- admit a cheap failure-existence test and a decisive method kill test;
- remain explicitly provisional until claim-level novelty checking is complete.

## Fixed generation lenses

Use one fresh, read-only generator shard for each lens. Give every shard the same literature, project state, compute limits, and banlist. Shards generate only; they never rank, reject, write shared files, or communicate with one another.

### Lens 1: Wrong supervision abstraction

Find cases where the object optimized by current methods differs from the object that determines task success. Look for distinctions such as token versus action, trajectory versus environment effect, surface form versus semantic state, or individual solution versus equivalence class.

Require the method to redefine the supervised object or probability space. Do not accept an auxiliary diversity term or another weight on the old object.

### Lens 2: Broken shared assumption requiring a method

Find an assumption shared by a method family that fails in a realistic training or deployment setting, such as equal information, equal tools, a unique correct route, reliable teacher continuation, or stable action semantics.

Require a new training interface, information projection, or decision abstraction. If measuring the assumption violation already completes the paper, classify the candidate as diagnostic and reject it.

### Lens 3: Cross-paper contradiction requiring a method

Find two or more primary papers with genuinely incompatible claims after accounting for model, data, decoder, budget, and evaluation differences. Identify the smallest hidden regime variable that could reconcile them.

Require that the hidden variable changes what the algorithm should optimize or how supervision must be represented. If a factorial experiment alone resolves the contradiction, classify the candidate as diagnostic and reject it.

## Generator output contract

Each lens returns 6–8 candidates using the base skill's structured shard envelope. Each candidate must include:

- title;
- failure mode;
- method in 2–4 concrete steps;
- why the method is necessary;
- non-incremental delta;
- cheapest failure-existence test;
- decisive method kill test;
- `dedup_key` and lens provenance.

Return fewer candidates instead of filling the quota with weak variations. Merge all shards and perform only mechanical deduplication before the jury.

## Non-incremental jury gate

Reject a candidate when its dominant contribution is any of the following:

- a new token, step, segment, or trajectory weight;
- prompt sampling, curriculum, replay, filtering, pruning, truncation, rollout-depth, or teacher-intervention scheduling;
- ordinary regularization, augmentation, canonicalization, or entropy preservation;
- applying a known method to a new domain without changing the underlying research question;
- combining known components whose roles remain unchanged;
- a predictor, controller, router, or proxy whose only novelty is deciding when to use an existing method;
- new terminology for an existing supervision or evaluation object;
- a central claim that can be established without training and testing the proposed method.

A candidate survives only if the jury can name the new decision or learning object, explain why strong simple baselines cannot express it, and identify a result that would falsify the claimed method advantage. Record any same-family jury verdict as provisional.

## Human checkpoints

Default to staged execution unless the user explicitly requests a one-shot run.

1. **Landscape checkpoint:** Present the evidence-backed gap seeds under the three fixed lenses. Stop for the user to approve, remove, or narrow seeds before generating candidates.
2. **Candidate checkpoint:** Present the mechanically deduplicated candidates without ranking. Stop for the user to select at most five candidates for expensive novelty checking. Do not write them to `research-wiki/`.
3. **Verdict checkpoint:** Run claim-level novelty checks and one fresh jury only on the approved shortlist. Present the provisional ranking and strongest objection. Do not launch pilots or write wiki entries without explicit approval.

After the user selects one idea, recommend `research-refine`; after the method is frozen, recommend `experiment-plan`. Do not invoke either automatically.

## Reporting

Use the base skill's report structure, but report only method candidates as recommended. Put diagnostic or incremental candidates in the eliminated table with the exact failed gate. Lead each surviving idea with the method, then give the hypothesis, closest work, non-incremental argument, failure-existence test, kill threshold, compute estimate, and strongest reviewer objection.

Never describe an unpiloted idea as accepted, novel, or top-venue ready.
