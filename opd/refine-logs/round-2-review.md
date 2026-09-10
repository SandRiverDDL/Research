# Round 2 Review

<details>
<summary>Raw reviewer response</summary>

## Round 2 Review: ForkProgress-OPD

**CALIBRATION: none**

### Summary

The revision resolves the three main round-1 objections. Criticality is now an explicit paired terminal branch-value test; unverified earliness has been removed from the default sampler; and action-boundary truncation is correctly treated as a shared interface rather than novelty. The proposal now has one coherent contribution: **using the movement of a causally grounded action-fork frontier as an online prompt-acquisition signal for agent OPD**.

This is substantially sharper, simpler, and more implementable. It is not READY because the contribution remains empirically conditional and three definitions should be frozen more precisely before the pilot.

### Anchor Preservation / Drift

**No substantive drift.** The revision still addresses the original bottleneck: outcome accuracy loses error location, while raw disagreement confounds alternative valid actions with consequential mistakes. Restricting the first paper to snapshot/replay environments is a justified scope correction, not problem drift.

There is one textual inconsistency: the retained Problem Anchor still says prompts with an “earlier” and “reliably repairable” fork should be prioritized, whereas the default method does not use earliness and only establishes teacher-improvability. Rewrite the anchor using the revised terminology; otherwise reviewers may perceive an unresolved mismatch between motivation and method.

### GAP

The gap is now precise and defensible: existing methods either schedule prompts using outcome/continuation reliability or control supervision within an already selected trajectory. ForkProgress instead estimates the consequence of a particular agent action by paired terminal branches and repeatedly acquires prompts whose first teacher-improvable fork is moving backward in the trajectory. This is not merely ReOrder-OPD plus Prune-OPD because the acquisition statistic is action-localized, counterfactual, and revisitable. The remaining uncertainty is empirical: fixed-policy branch advantage may still add little beyond teacher continuation reliability or may be too expensive to improve the total-cost frontier.

## Scores

| Dimension | Score | Assessment |
|---|---:|---|
| Problem Fidelity | 8.0 | The causal test now addresses the anchored localization problem directly within a clearly scoped setting. |
| Method Specificity | 7.5 | Almost implementable as written; confidence estimation, continuation semantics, and scalar cost need final freezing. |
| Contribution Quality | 8.0 | One dominant mechanism-level contribution with clear stop conditions and no parallel novelty claims. |
| Frontier Leverage | 8.5 | Natural use of constrained tool actions, exact verifiers, snapshot/replay, paired seeds, and decision-complete logits. |
| Feasibility | 6.5 | Technically feasible in the scoped environments, but branch probing may dominate cost and ALFWorld replay needs validation. |
| Validation Focus | 8.5 | Claim-driven, minimal, matched to the novelty, and equipped with a credible go/no-go gate. |
| Venue Readiness | 6.0 | Strong proposal, but no evidence yet that the new statistic has incremental predictive value or positive net efficiency. |

**WEIGHTED OVERALL SCORE: 7.7/10**

## Dimension-Specific Issues Below 7

### Feasibility — 6.5

- **Weakness:** `c(x)` currently appears to combine teacher tokens, student tokens, environment steps, and wall-clock into one denominator without specifying conversion weights. These resources cannot simply be added, and matching all four simultaneously may be impossible. Repeated teacher continuations at every candidate fork could dominate runtime.
- **Concrete fix:** Choose one primary scalar cost—preferably measured wall-clock or normalized monetary/GPU cost—and treat the other resources as reported constraints and Pareto axes. Freeze the branch-probe budget and include every teacher decode, replay step, verifier call, and failed candidate test.
- **Priority:** P0.

### Venue Readiness — 6.0

- **Weakness:** Novelty and usefulness still depend on two unobserved results: incremental prediction beyond ReOrder-style reliability and improvement after accounting for probe cost. Standard reverse-KL may also fail to learn some teacher-improvable action forks despite decision-complete support.
- **Concrete fix:** Execute the already proposed causal pilot before expanding the method or benchmark suite. Apply the stated stop rule literally if either incremental prediction or one-update responsiveness fails.
- **Priority:** P0.

## Remaining Method Actions

1. **Freeze what branch value means.** With teacher continuation on both branches, `A_j` estimates action advantage under the teacher continuation policy, not policy-independent criticality. State this explicitly. Freeze one primary `π_C`, one paired confidence-bound procedure, and whether the horizon is the remaining global budget `H-j`.  
   **Priority: P0.**

2. **Make frontier movement robust to detection noise.** A fork can disappear because an LCB becomes inconclusive rather than because the student improved. Do not treat every transition to `H+1` as capability progress. Require censoring-aware EMA logic or confirmation before recording positive movement.  
   **Priority: P0.**

3. **Align the anchor language.** Replace “earlier and repairable” with “teacher-improvable and showing positive first-fork movement.” Keep earliness explicitly conditional.  
   **Priority: P1.**

4. **Freeze the proposal after these definitions.** Do not add a critic, takeover, learned equivalence model, new KL, or extra contribution if the pilot is weak.  
   **Priority: P1.**

## Simplicity Assessment

The revision is appropriately minimal:

- One scientific object: paired action-fork value.
- One use of that object: repeated prompt acquisition from frontier movement.
- Zero new trainable components.
- Existing OPD and boundary masking remain fixed.
- Truncation, support handling, and simulator machinery are implementation prerequisites rather than competing claims.

The `r × positive movement / cost` sampler is substantially cleaner than the original multiplicative earliness formulation.

## Frontier Leverage

The modern primitives are used naturally rather than decoratively. JSON-schema-constrained action generation makes the causal object executable; snapshot/replay permits paired interventions; the terminal verifier supplies outcome grounding; paired seeds reduce variance; and decision-complete support addresses tool-boundary failures that ordinary top-k OPD can miss. Importantly, none remains at inference.

## Drift Warning

No current methodological drift. The main risk is future reaction to a negative pilot: adding a learned recoverability model, process judge, teacher relay, or action-imitation objective would change the paper from prompt acquisition into a multi-module supervision method. A failed incremental-prediction gate should terminate this direction.

## Verdict

**REVISE**

This has moved from a composite idea to a credible top-venue research hypothesis. Freeze the remaining definitions and run the causal pilot; further conceptual expansion is not needed.

`review_independence: same-family`  
`acceptance_status: provisional`

</details>
