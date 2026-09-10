# Method Candidates: Pre-Jury Mechanical Merge

- Direction: non-incremental new methods for agentic / long-horizon online policy distillation
- Generation: three isolated, read-only lens shards
- Merge rule: exact `dedup_key` equality only
- Generated: 13
- Exact duplicates removed: 0
- Status: provisional; not novelty-checked

## Lens 1 — Wrong supervision abstraction

### C01 — Joint Distribution Over Complete Attempt Sets

- `dedup_key`: `joint-distribution-complete-attempt-sets`
- Provenance: `lens1:L1-A capability-set supervision`
- Failure mode: Token-level OPD can improve the average attempt while making multiple attempts increasingly correlated, so the student loses solution-family coverage and leaves some tasks unsolvable at large K.
- Method:
  1. Collect fixed-size groups of K complete teacher attempts for each prompt while preserving group membership; define the target probability space over unordered K-attempt sets rather than individual trajectories.
  2. Train the student to assign likelihood to the entire set with an exact permutation-summed set objective for small K, then generate all K deployment attempts jointly from that distribution.
- Why necessary: Independent trajectory likelihood identifies only single-attempt marginals. Matching whether a set contains complementary successful solutions requires a joint set-valued learning object.
- Non-incremental delta: Replaces per-rollout imitation with direct learning of the joint law of a deployment-sized collection of complete solutions.
- Cheapest failure-existence test: At similar single-attempt success, test whether an OPD model has lower probability that four attempts collectively contain a success or cover teacher-observed solution families.
- Kill test: At matched training and inference compute, kill if learned joint statistics are no closer to the teacher and there is no improvement in pass@K, recovered unsolvable tasks, or solution-family coverage over independent OPD attempts.
- Compute: Moderate; K=3 or K=4 permits exact permutation summation.
- Obvious risk: Set likelihood may remain dominated by surface-form variation and be difficult to estimate for long trajectories without reverting to marginal token imitation.

### C02 — Joint Capability-Vector Distribution Matching

- `dedup_key`: `joint-capability-vector-distribution-matching`
- Provenance: `lens1:L1-A capability-set supervision`
- Failure mode: Matching behavior task by task can preserve marginal success rates while destroying the probability that one student policy simultaneously possesses all required capabilities.
- Method:
  1. Evaluate teacher and student policy instances on the same small bundle of existing tasks and represent each result as one binary or verifier-valued capability vector.
  2. Optimize the student end to end with a proper distribution-matching objective over complete capability vectors, using full-episode likelihood-ratio gradients rather than token-loss weights.
- Why necessary: Per-task objectives cannot distinguish a policy that jointly retains several capabilities from a population whose runs retain disjoint subsets.
- Non-incremental delta: Moves supervision from actions or rollouts to the policy-induced distribution over simultaneously held capabilities.
- Cheapest failure-existence test: Find checkpoints with similar average and per-task success but different probability of solving every task in a three-task bundle with the same policy checkpoint.
- Kill test: Kill if matching joint capability vectors does not improve held-out all-capabilities success or retained-plus-acquired capability probability after controlling for marginal task success.
- Compute: Moderate; bundles of three to five tasks and a small number of environment seeds.
- Obvious risk: The probe bundle may not identify underlying capabilities, allowing bundle-level outcome overfitting.

### C03 — Distillation of Capability Changes Across Online Updates

- `dedup_key`: `capability-changes-across-online-updates`
- Provenance: `lens1:L1-A capability-set supervision`
- Failure mode: A student can imitate the current teacher batch while its update changes unrelated capabilities in the opposite direction, causing gradual forgetting or missed acquisition.
- Method:
  1. For each online update, measure teacher and student success vectors on a fixed probe bundle immediately before and after the current data block; make the joint before-to-after capability transition the supervised object.
  2. Meta-optimize the student's update rule so its distribution over complete capability transitions matches the teacher's, without adding a token-loss term or changing data order.
- Why necessary: Snapshot imitation does not identify how new evidence should transform the policy. Acquisition and retention are properties of the update operator.
- Non-incremental delta: Replaces supervision of a policy snapshot with supervision of the functional change produced by an online learning update.
- Cheapest failure-existence test: Locate batches where two updates reach similar immediate imitation loss but differ in which probe capabilities are gained, retained, or lost.
- Kill test: Kill if transition matching does not reduce capability losses or improve acquisition on later unseen batches, or if benefits disappear after matching post-update probe success.
- Compute: Moderate; truncated meta-gradients through one or two updates and a three-to-five-task probe bundle.
- Obvious risk: Second-order optimization may be unstable, and short transitions may not predict long-run behavior.

### C04 — Distribution Over Terminal Achievement Sets

- `dedup_key`: `distribution-over-terminal-achievement-sets`
- Provenance: `lens1:L1-A capability-set supervision`
- Failure mode: Long-horizon rollouts with similar locally correct actions can differ in which combinations of objectives they ultimately satisfy, recover, or leave reachable; token supervision conflates them.
- Method:
  1. Map each completed episode through the task verifier into the subset of required terminal objectives it achieves, defining teacher and student distributions over achievement sets.
  2. Train the student with a proper scoring rule on the full achievement-set distribution using episode-level gradients; deploy the unchanged policy normally.
- Why necessary: Scalar success and token likelihood cannot represent whether objectives are achieved jointly or traded off.
- Non-incremental delta: Changes the supervised random variable from a rollout sequence to the verifier-defined subset of achieved terminal objectives.
- Cheapest failure-existence test: On tasks exposing two or three objectives, test whether OPD improves average objective completion while reducing full-set completion or rare combinations.
- Kill test: Kill if achievement-set matching fails to improve full-set completion on held-out tasks, especially after controlling for expected number of achieved objectives.
- Compute: Moderate; complete episodes and structured verifier outputs with three to six objectives.
- Obvious risk: Episode-level gradients may be sparse and verifier objectives may omit important solution-family distinctions.

## Lens 2 — Broken information-set assumption

### C05 — Observable-History Policy Projection

- `dedup_key`: `observable-history-policy-projection`
- Provenance: `lens2:L2-A+L3-B information-set mismatch`
- Failure mode: For the same deployment-observable history, privileged teacher states prescribe incompatible next actions, so direct distillation fits distinctions the student cannot represent.
- Method:
  1. Group teacher states sharing the complete student-observable history but differing in instance-specific privileged information; estimate their deployment-conditional frequencies.
  2. Replace each privileged target with the action distribution obtained by marginalizing teacher decisions over compatible privileged states, then train only against this observable-history conditional.
- Why necessary: Removing privileged inputs cannot repair contradictory labels; the target must be projected onto the student's observable information.
- Non-incremental delta: Changes the learning object from `p(a|o,z)` to the realizable projected policy `p(a|o)`.
- Cheapest failure-existence test: Use paired short tasks with identical observable prefixes and different hidden facts forcing different teacher actions; compare gradient agreement and held-out action accuracy.
- Kill test: With an oracle marginal from the true hidden-state distribution, kill if the projected target does not improve long-horizon return or fork recovery over direct privileged distillation.
- Compute: Moderate; several teacher evaluations per paired observable history, then ordinary student training.
- Obvious risk: The marginal can be multimodal and yield an action mixture that is statistically realizable but poor for an individual episode.

### C06 — Observable Action-Value Projection

- `dedup_key`: `observable-action-value-projection`
- Provenance: `lens2:L2-A+L3-B information-set mismatch`
- Failure mode: A privileged teacher chooses different actions in observationally identical situations, while action imitation gives the student no basis for choosing among conflicting labels.
- Method:
  1. For every student-observable history, evaluate each feasible action under teacher continuations across compatible privileged states and integrate returns under the deployment hidden-state distribution.
  2. Train the student to predict the resulting observable-history action values and act by their ordering instead of imitating the realized privileged action.
- Why necessary: When the teacher label is not a function of student information, supervision must move to decision values defined on the student's information set.
- Non-incremental delta: Changes the object from privileged next-action labels to an observable-history action-value function.
- Cheapest failure-existence test: Use a hidden-bit branching environment with analytically known expected action values and test whether projected values recover the Bayes-optimal visible policy.
- Kill test: With exact oracle observable action values, kill if the policy does not outperform direct distillation on hidden-information long traces.
- Compute: Moderate; batched continuation evaluation for a small candidate-action set.
- Obvious risk: Integrating long-horizon returns may be expensive and noisy when candidate actions are numerous.

### C07 — Compatible-State Minimax Decisions

- `dedup_key`: `compatible-state-minimax-decisions`
- Provenance: `lens2:L2-A+L3-B information-set mismatch`
- Failure mode: Averaging privileged policies can produce a mixed decision that performs badly in every hidden state compatible with the student's observation, especially at irreversible forks.
- Method:
  1. Enumerate privileged states compatible with each observable history and compute each feasible action's regret relative to the teacher decision in every state.
  2. Supervise the set of actions minimizing worst-case regret using set-valued likelihood rather than a single privileged label.
- Why necessary: The student needs a decision rule defined before the hidden instance is known; a compatible-state minimax object represents that constraint directly.
- Non-incremental delta: Changes the object from one privileged action to an observation-feasible action set chosen by worst-case decision loss.
- Cheapest failure-existence test: Build paired irreversible-choice tasks with the same visible prefix and opposing hidden optimal actions; compare direct, mean-policy, and minimax targets.
- Kill test: With oracle compatible states and exact returns, kill if minimax supervision fails to improve worst-case task completion without collapsing average completion.
- Compute: Moderate for consequential points and bounded feasible-action sets.
- Obvious risk: Rare compatible states may make the method excessively conservative.

### C08 — Observation-Contingent Plan Distillation

- `dedup_key`: `observation-contingent-plan-distillation`
- Provenance: `lens2:L2-A+L3-B information-set mismatch`
- Failure mode: A privileged teacher emits one linear plan tailored to hidden facts, but the student must defer commitments and revise behavior when future observations identify the branch.
- Method:
  1. Constrain the teacher interface to return a plan tree whose branch predicates reference only observations available to the deployed student; privileged information may evaluate branches but cannot appear in predicates.
  2. Train the student to predict and execute the contingent plan, advancing or revising only when observable predicates resolve.
- Why necessary: A linear privileged trajectory cannot teach behavior for unresolved alternatives or later self-correction.
- Non-incremental delta: Changes the object from a privileged action sequence to an observation-indexed contingent plan with alternative continuations.
- Cheapest failure-existence test: Use a two-fork tool task where the correct second action depends on a later observation; compare linear traces with shallow contingent trees at the same teacher-query budget.
- Kill test: With oracle plan trees and correct predicates, kill if execution does not improve fork handling and recovery over linear distillation.
- Compute: Moderate; a small branching plan per instance, one branch at execution.
- Obvious risk: Plan trees may grow quickly and predicates may omit distinctions required for success.

## Lens 3 — State-coverage versus bad-prefix contradiction

### C09 — Closed-Loop Reachable-State Continuation Graphs

- `dedup_key`: `closed-loop-reachable-state-continuation-graphs`
- Provenance: `lens3:L3-C state-coverage versus bad-prefix contradiction`
- Failure mode: A linear teacher continuation assumes the student stays on one imagined suffix; after another deviation, later actions can be invalid even when the new state remains recoverable.
- Method:
  1. From each student state, expand bounded legal environment transitions and backward transitions from successful terminals, recording bidirectional-reachability witnesses and dead ends.
  2. Replace the linear target with a closed-loop graph whose nodes are actual states and whose edges specify actions after each reachable observation; supervise the graph as one coupled continuation object.
- Why necessary: Robustness after additional deviations requires a state-conditioned continuation object; more independent suffixes do not represent the closed-loop mapping.
- Non-incremental delta: Changes the object from a sequence to an executable state-action graph tied to reachability and terminal outcomes.
- Cheapest failure-existence test: Inject one legal off-suffix action and measure how often the teacher suffix becomes invalid while a successful path still exists.
- Kill test: At equal labeled states and teacher calls, kill if graph supervision does not improve success after forced deviations over independent linear continuation targets.
- Compute: About 2–4x ordinary OPD labeling cost with bounded branching and transition caching.
- Obvious risk: Branching may grow too quickly and small graphs may omit important deviations.

### C10 — Backward Success-Preimage Transition Targets

- `dedup_key`: `backward-success-preimage-transition-targets`
- Provenance: `lens3:L3-C state-coverage versus bad-prefix contradiction`
- Failure mode: A teacher continuing from a bad prefix may invent plausible actions without establishing that any proposed successor still permits completion.
- Method:
  1. Construct backward preimage layers from exact successful terminal states, storing legal predecessor state-action pairs whose successor is in the preceding layer.
  2. At a student state, supervise the set-valued successor-state relation and executable action witnesses; states outside the success preimage receive an explicit legal failure-termination target.
- Why necessary: Recoverability must be established before defining the target; backward preimages encode whether an action stays inside the success-reachable region.
- Non-incremental delta: Changes the object to a state-transition relation grounded in the success preimage, representing both successful and impossible continuations.
- Cheapest failure-existence test: On short deterministic tasks, enumerate exact preimages and count teacher first actions outside them when an inside-preimage action exists.
- Kill test: With identical states and labeling budgets, kill if exact preimage targets do not beat ordinary action targets on first-action validity and end-to-end success.
- Compute: About 1.5–3x labeling cost on bounded-horizon tasks with memoized predecessor expansion.
- Obvious risk: Many agentic environments lack an exact predecessor operator or compact success-state specification.

### C11 — Dual-Ended Executable Trajectory Infilling

- `dedup_key`: `dual-ended-executable-trajectory-infilling`
- Provenance: `lens3:L3-C state-coverage versus bad-prefix contradiction`
- Failure mode: Open-ended teacher continuation from a malformed state can rationalize the prefix without reconnecting it to any state on a valid completion.
- Method:
  1. Search forward from the actual student state and backward from exact states on successful executions; identify a reachable meeting state with legal transition checks.
  2. Distill the verified bridge plus remaining successful trajectory as one endpoint-constrained infilling object; if no connection exists, target an explicit legal failure closeout.
- Why necessary: Reconnecting the actual state to a success-bearing state must be part of the supervised object rather than an assumption made by the teacher.
- Non-incremental delta: Changes the target from autoregressive continuation to executable trajectory infilling constrained by current state and reachable successful endpoint.
- Cheapest failure-existence test: Compare unconstrained suffixes with exact bidirectional search and count failures where a bridge to a successful execution exists.
- Kill test: At matched environment-search cost, kill if verified infill targets do not improve held-out bad-prefix states with known bridges.
- Compute: About 2–5x teacher-side cost with shallow bidirectional search and caching.
- Obvious risk: Exact meeting states may be rare in large continuous or text-valued state spaces.

### C12 — Compensating-Transaction Continuation Targets

- `dedup_key`: `compensating-transaction-continuation-targets`
- Provenance: `lens3:L3-C state-coverage versus bad-prefix contradiction`
- Failure mode: Student actions may create external commitments that invalidate nominal next steps, although a legal compensation sequence could restore a success-reachable state.
- Method:
  1. Use the environment transition log to construct executable compensation actions for completed commitments and verify the resulting postcondition.
  2. Replace the nominal suffix with a transaction target containing compensation actions, intermediate observations, verified postcondition, and a successful continuation; when compensation is impossible, supervise legal containment or failure closeout.
- Why necessary: Recoverability requires changing external state before ordinary behavior can resume; compensation is part of the learned policy rather than a scheduling decision.
- Non-incremental delta: Changes the object to an atomic repair-and-resume transaction with verified postconditions.
- Cheapest failure-existence test: Induce one incorrect reversible reservation, file edit, or queued action and test whether compensation restores success while direct continuation fails.
- Kill test: Kill if students trained on verified compensation transactions do not exceed direct-continuation students on recovery after the same commitments.
- Compute: About 1.5–3x labeling cost when environments expose logs and compensation APIs.
- Obvious risk: Many consequential actions have no legal inverse, limiting applicability.

### C13 — Residual State-Goal Program Supervision

- `dedup_key`: `residual-state-goal-program-supervision`
- Provenance: `lens3:L3-C state-coverage versus bad-prefix contradiction`
- Failure mode: A teacher suffix conditioned on text history can inherit a mistaken narrative even though the actual environment has a different set of achievable remaining goals.
- Method:
  1. Derive unsatisfied task predicates and irreversible commitments from the current environment state, then determine joint reachability using legal transition witnesses.
  2. Replace textual continuation with an executable partial-order program whose guarded action blocks establish those predicates; if joint achievement is unreachable, terminate through an explicit legal failure path.
- Why necessary: Reconstructing the remaining task as state-changing guarded blocks makes actual reachability, rather than malformed narrative, define supervision.
- Non-incremental delta: Changes the object from a sequential suffix to a state-grounded partial-order program with intermediate postconditions and executable blocks.
- Cheapest failure-existence test: For machine-checkable tasks, corrupt textual prefix and compare the teacher's remaining plan with predicates actually reachable from the resulting state.
- Kill test: At the same states and teacher budget, kill if program-target training does not improve intermediate postconditions or final success over sequence targets.
- Compute: About 2–4x labeling cost for predicate extraction, bounded reachability checks, and execution.
- Obvious risk: Open-ended tasks may not expose precise success predicates, making the program incomplete or environment-specific.
