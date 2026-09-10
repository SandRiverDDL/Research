# Round 3 Review

<details>
<summary>Raw reviewer response</summary>

## Round 3 Review: ForkProgress-OPD

**CALIBRATION: none**

### Summary

The proposal is now conceptually coherent and method-first ready for a pilot. Branch value has one exact interpretation, stochastic/censoring optimism is controlled, cost accounting is well-defined, and the paper remains centered on one contribution: **teacher-continuation-relative action-fork progress for repeated prompt acquisition**.

No redesign of the thesis is needed. Two small protocol specifications should be corrected before implementation; everything decisive after that is empirical.

### GAP

The gap is now sharply stated. Prior work schedules prompts using outcome or continuation reliability, or modifies weighting, rollout depth, truncation, and rollout source after a trajectory has been selected. ForkProgress instead intervenes at the acquisition level using an action-local counterfactual quantity and revisits prompts when their confirmed first-fork frontier advances. The novelty is defensible because the method claims neither policy-independent causal correctness nor truncation novelty. Whether this gap is scientifically consequential remains an empirical question: the statistic must add predictive value beyond ReOrder-style reliability and overcome its probing cost.

## Scores

| Dimension | Score |
|---|---:|
| Problem Fidelity | 8.5 |
| Method Specificity | 8.5 |
| Contribution Quality | 8.5 |
| Frontier Leverage | 9.0 |
| Feasibility | 7.5 |
| Validation Focus | 8.0 |
| Venue Readiness | 6.5 |

**WEIGHTED OVERALL SCORE: 8.4/10**

### Assessment

- **Problem Fidelity:** The exact teacher-continuation advantage directly separates consequential action forks from raw disagreement within the scoped simulator setting. Keeping earliness conditional preserves the operational anchor without making it an unsupported mechanism.
- **Method Specificity:** Greedy teacher continuation, remaining horizon, exact terminal outcome, censoring, cost, support, and update rules are mostly frozen.
- **Contribution Quality:** The dominant contribution is singular and distinguishable from ReOrder-OPD and within-trajectory controllers.
- **Frontier Leverage:** Schema-constrained actions, deterministic replay, terminal verification, decision-complete support, and zero inference overhead are used naturally.
- **Feasibility:** The method is implementable in tool-DAG environments. ALFWorld replay feasibility and branch-probe latency remain genuine engineering risks, but the proposal handles failure by narrowing scope rather than inventing a surrogate.
- **Validation Focus:** The two claims and stop gates are sufficient. No larger benchmark package is currently needed.
- **Venue Readiness:** The method is polished, but top-venue readiness cannot be established before incremental prediction and matched-wall-clock benefit are demonstrated.

## Remaining Conceptual/Protocol Actions

1. **Complete the two-hit state transition.** The case `D < d < Q` is currently unspecified. Two consecutive observations both exceeding old `D` confirm movement to `min(Q,d)`, even if the second does not reach the first pending depth. Use:

   - first `d>D`: set `Q=d`;
   - next consecutive `d>D`: commit `D←min(Q,d)`;
   - `d≤D`: apply the stated stagnation/regression rule.

   This preserves conservative confirmation without discarding valid partial progress.

2. **Disambiguate baseline probe costs.** A “uniform” sampler using the same critical-action mask must perform the same branch tests, whereas vanilla uniform OPD would not. State two distinct comparisons:

   - sampler attribution: identical probe-and-mask pipeline, different acquisition policies;
   - end-to-end utility: ForkProgress versus vanilla no-probe uniform OPD, with all overhead included.

   Otherwise shared probe cost could make acquisition look free while changing the reference pipeline.

These are local specification fixes, not conceptual revisions to the research mechanism.

## Venue-Readiness Issue Below 7

- **Weakness:** There is no evidence yet that `A^T,d,L` add information beyond continuation reliability, that standard reverse-KL responds to teacher-improvable forks, or that probing pays for itself.
- **Fix:** Run the frozen tool-DAG pilot and apply the existing stop gates literally. Do not add modules after a negative result.
- **Priority:** P0.

## Drift Warning

**No drift.** The verbatim anchor is operationally reconciled, and the method remains within prompt acquisition. Adding a learned estimator, process reward, teacher takeover, or action-imitation objective after a weak pilot would constitute drift.

## Verdict

**REVISE**

No blocking conceptual redesign remains. Fix the two protocol ambiguities, freeze the implementation, and move to the empirical pilot. READY is inappropriate before evidence and because the weighted score remains below 9.

`review_independence: same-family`  
`acceptance_status: provisional`

</details>
