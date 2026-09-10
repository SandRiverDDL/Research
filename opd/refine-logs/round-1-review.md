# Round 1 Review

<details>
<summary>Raw reviewer response</summary>

## Review: BranchFront-OPD

**CALIBRATION: none**

**Summary.** The proposal identifies an important unresolved problem: prompt-level value in long-horizon agent OPD should depend on where an actionable state fork occurs, not only on pass rate or token divergence. The potentially novel contribution is a causally checked action-fork statistic used for repeated prompt acquisition. However, the current method does not yet make “first critical repairable divergence” observable without oracle-like supervision. Its priority formula also assumes “earlier is better” before establishing that relationship, while action-boundary truncation is already subsumed at the contribution level by Prune-OPD, SOD, TCOD/TurnOPD, Guided-OPD, and Relay-OPD. As written, this risks becoming ReOrder-OPD plus a semantic Prune-OPD variant.

### GAP

There is a plausible gap: none of the listed closest works directly turns a causally verified agent action fork into a per-prompt, repeatedly refreshed acquisition signal. ReOrder-OPD orders prompts by continuation reliability; Prune-OPD/SOD control unreliable within-trajectory supervision; TCOD/TurnOPD allocate trajectory depth; Guided-OPD/Relay-OPD intervene in rollout generation. But the proposal has not yet operationalized its claimed statistic. A short branch showing higher “progress” does not establish that the student action is critical, unrecoverable, or that OPD can learn the teacher alternative. Without a well-defined branch-value test, the method falls back to semantic disagreement plus existing scheduling/truncation components.

## Scores

| Dimension | Score | Assessment |
|---|---:|---|
| Problem Fidelity | 6.0 | Strong anchor, but the proposed observable does not yet identify the anchored causal event. |
| Method Specificity | 5.0 | Several quantities required to implement the algorithm remain undefined. |
| Contribution Quality | 5.5 | A potentially strong central signal is mixed with already-occupied truncation and curriculum ideas. |
| Frontier Leverage | 7.0 | Frozen teachers, structured actions, environment snapshots, and counterfactual execution are natural primitives. |
| Feasibility | 5.0 | Practicality depends on cloneable states and process-like progress signals absent from many target environments. |
| Validation Focus | 6.5 | Good go/no-go logic, but Claim 3 unnecessarily turns an implementation condition into a separate contribution. |
| Venue Readiness | 4.5 | Central variable and novelty boundary remain conditional on an unrun pilot. |

**WEIGHTED OVERALL SCORE: 5.6/10**

## Dimension-specific weaknesses and fixes

### 1. Problem Fidelity — 6.0

- **Weakness:** “Teacher branch has higher short-term progress” is not equivalent to “student made the first critical error.” The student branch may be a slower valid route, may recover later, or may require a different short horizon. The proposed `r` measures teacher-branch recoverability, not whether one OPD update can repair the student.
- **Concrete fix:** Restrict the first method to deterministic, snapshot-capable environments with an exact terminal verifier. At each candidate fork, run paired continuations under the same fixed continuation policy and seeds. Define criticality by a lower-confidence-bound advantage in terminal success, not an unspecified progress score. Rename `repairability` to `teacher-recoverability`; only claim OPD learnability if one-update gain supports it.
- **Priority:** P0.

### 2. Method Specificity — 5.0

- **Weakness:** The proposal does not specify teacher action decoding, branch horizon, continuation policy, number of paired branches, criticality threshold, treatment of right-censored trajectories, stochastic depth estimation, or initialization/sign of `ell`. “Known execution-equivalent class” is unrealistic and context-dependent.
- **Concrete fix:** Provide one exact algorithm. Use syntax canonicalization only; treat actions as equivalent when their paired branch values are statistically indistinguishable. Normalize depth by a fixed environment horizon, not the currently truncated horizon. Define `ell = EMA(max(0, d_k-d_{k-1}))`, with explicit rules for unseen and censored prompts. State exactly which tokens receive reverse-KL loss.
- **Priority:** P0.

### 3. Contribution Quality — 5.5

- **Weakness:** The paper currently supports three stories: causal fork detection, dynamic prompt sampling, and semantic truncation. Claim 3 makes truncation look like an independent contribution, despite prior work already establishing drift-triggered truncation, step/turn boundaries, and state-aware termination.
- **Concrete fix:** Make the sole contribution **causally grounded prompt acquisition**. Use action-boundary stopping as a fixed measurement/training interface across sampler comparisons and reduce Claim 3 to one sanity ablation. Explicitly disclaim novelty for truncation.
- **Priority:** P0.

### 5. Feasibility — 5.0

- **Weakness:** ALFWorld/WebShop do not automatically provide the exact dense progress oracle assumed by the definition. Teacher action generation plus two branch continuations at every candidate boundary may dominate training cost. Current matched-compute accounting omits branch-verification and environment costs.
- **Concrete fix:** Scope the initial method to replayable simulators with exact state snapshots and terminal verification. Count teacher action decoding, both branch continuations, verifier calls, and environment steps in the sampler cost `c(x)` and all matched-compute comparisons.
- **Priority:** P0.

### 6. Validation Focus — 6.5

- **Weakness:** The validation is mostly disciplined, but the boundary-truncation experiment expands the paper and obscures attribution.
- **Concrete fix:** Retain the causal pilot and one matched-compute dynamic-sampling test. Collapse truncation into an implementation sanity check rather than a third claim.
- **Priority:** P1.

### 7. Venue Readiness — 4.5

- **Weakness:** The dominant claim is conditional on the fork statistic predicting update gain, and the proposed statistic is not yet well-defined on the intended benchmarks.
- **Concrete fix:** Run the stated go/no-go pilot only after freezing the exact branch-value definition. Stop if it does not beat teacher continuation reliability after conditioning on cost and baseline success.
- **Priority:** P0.

## Critical questions

**Is the first critical repairable divergence identifiable without an oracle?**  
No, not as currently specified. Environment “progress” is effectively process supervision, while terminal paired continuation is an expensive counterfactual oracle. A single improved next state cannot certify criticality. The proposal must either acknowledge an oracle-assisted, cloneable-simulator setting or replace the claim with a weaker “teacher-preferred consequential fork.”

**Is “earlier is better” justified?**  
No. Relay-OPD’s front-loaded intervention evidence is specific to reflection-triggered mathematical reasoning and does not establish prompt-level OPD value in tool agents. TurnOPD also shows that deeper decisions may be systematically undertrained. The main sampler should initially omit `(1-d)`:

\[
u(x)=\frac{r(x)(\epsilon+\max(0,\ell(x)))}{c(x)}
\]

Earliness should enter only if it predicts one-update gain after controlling for recoverability, cost, prompt length, and baseline success. Otherwise the method should remain a frontier-movement curriculum.

**Is boundary truncation already subsumed?**  
At the novelty level, yes. Stopping after a complete structured action and before the changed observation is a sound semantic implementation, but not an independent top-venue contribution. Guided-OPD already treats complete thought-plus-action turns as state-transition units; Prune-OPD, SOD, TCOD/TurnOPD, and Relay-OPD occupy the broader reliability/depth/termination space.

A further concern from Tool-Call Drift is that top-k teacher support may omit the decision-critical tool-entry token. If the base OPD uses truncated logits, the sampler may correctly detect a behavioral fork while the training loss cannot directly repair the branch-switch coordinate. The method must specify full-vocabulary or otherwise decision-complete teacher scoring at tool boundaries without presenting this as another contribution.

## Simplification Opportunities

1. Remove the earliness factor from the primary method until the pilot establishes conditional monotonicity.
2. Remove Claim 3 as an independent claim; use one common action-boundary mask.
3. Eliminate hand-built execution-equivalence classes; use paired branch-value equivalence.

## Modernization Opportunities

1. Use JSON-schema-constrained action decoding and environment-native snapshots so the compared objects are executable actions rather than free-form token strings.
2. Use paired, seed-matched simulator branches and exact terminal verification instead of an LLM judge or vague progress heuristic.

## Drift Warning

No current problem drift, but adding a learned recoverability model, teacher takeover, action-level imitation objective, or a new semantic encoder would change the anchored problem and create contribution sprawl. Conversely, retaining truncation as a standalone contribution drifts toward Prune-OPD/TurnOPD rather than strengthening the prompt-acquisition thesis.

## Verdict

**RETHINK**

The problem is worth pursuing, but the core variable must be redefined before implementation. A focused paper can emerge if it becomes: **a causally verified action-fork statistic for online prompt acquisition, with existing OPD and truncation held fixed**.

`review_independence: same-family`  
`acceptance_status: provisional`

</details>
