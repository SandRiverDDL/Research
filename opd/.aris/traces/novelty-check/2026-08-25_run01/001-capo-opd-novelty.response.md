Provisional same-family review; acceptance status: provisional.

## Verdict

| Version | Novelty | Top-tier publishability | Verdict |
|---|---:|---|---|
| A: CAPO port | **2/10** | No. At best an ablation or workshop paper. | **ABANDON** |
| B: two-axis OPD router | **5/10 now; perhaps 7/10 if the mechanism is proven** | Weak reject today; plausibly publishable if the two axes are causally dissociated and yield real efficiency. | **PROCEED WITH CAUTION** |

A’s likely review: “This is CAPO applied to another policy-gradient-style objective. The curvature model, masking rule, aggressive optimization regime, and efficiency mechanism are inherited. Worse, the CAPO theory does not directly cover the proposed OPD reward.”

B’s likely review: “This is a hand-engineered composition of TrOPD’s reliability partition and CAPO’s curvature mask. The paper has not shown that the alleged axes are distinct, that a two-dimensional router is necessary, or that gains are more than filtering and hyperparameter tuning.”

## Closest work and exact delta

- [CAPO](https://arxiv.org/html/2510.00819): already owns prospective Hessian/Fisher shifts, sparse last-layer estimation, token/subset masking, and the aggressive-LR/small-batch sample-efficiency mechanism.  
  **A’s delta:** only replacing RLVR advantage with OPD token rewards. Insufficient.  
  **B’s delta:** an OPD-correct curvature derivation plus coupling safety to a separate reliability decision.

- [TrOPD](https://arxiv.org/html/2606.01249): already partitions tokens by teacher/student acceptance probability, masks/clips outliers, redirects them to top-k FKL, and uses teacher-prefix guidance. It explicitly says outliers can remain informative.  
  **B’s reliability branch is substantially TrOPD.** “Preserving high-disagreement useful tokens” is not new by itself. The defensible delta is showing that reliability does not determine update safety.

- [TOP-D](https://arxiv.org/abs/2607.04751): already claims OPD stability, bounded variance, monotonic improvement, sample reuse, and zero added overhead via a proximal teacher. B must beat its quality–teacher-cost–GPU-hour Pareto frontier.

- [Revisiting OPD](https://arxiv.org/abs/2603.25562), [vOPD](https://arxiv.org/abs/2605.07865), and [OPD+](https://arxiv.org/abs/2606.01039): already cover sampled-token bias/support mismatch, variance reduction, and the consequences of student-dependent rewards. These make an unmodified CAPO derivation indefensible.

- [FP-OPD](https://arxiv.org/abs/2608.01263): Fisher geometry is already in OPD, though for projecting corrections into a realizable target space rather than predicting destructive optimizer steps.

- [On the Geometry of OPD](https://arxiv.org/abs/2606.07082) and [Dense Supervision, Sparse Updates](https://arxiv.org/abs/2606.13657): already characterize OPD update/subspace geometry post hoc. B’s delta must be prospective and causal.

- Newly important overlap: [TIDE / Mismatch Matters](https://arxiv.org/abs/2608.09836) separates student-excess from student-deficit mismatch, bounds dangerous corrections, and injects missing teacher top-k mass. This further weakens generic “high-disagreement tokens should be preserved” claims.

Do not claim “existing OPD methods conflate the axes” as a literature fact. That sounds like a straw man. Claim—and demonstrate—that their scalar reliability/magnitude proxies cannot predict prospective update damage.

## CAPO mathematics does not survive unchanged

The Fisher/KL diagnostic mostly survives locally; the Hessian and monotonic-improvement argument do not.

For fixed-prefix negative reverse KL,

\[
J(\theta)=-\mathrm{KL}(\pi_\theta\|\pi_T)
=\mathbb E_{a\sim\pi_\theta}[\log\pi_T(a)-\log\pi_\theta(a)].
\]

The usual sampled score gradient can coincide in expectation because the missing derivative is a constant score-function baseline. But the Hessian does not coincide. If \(r_\theta=\log\pi_T-\log\pi_\theta\) and \(z=\nabla\log\pi_\theta\), then

\[
\nabla^2J
=
\mathbb E\!\left[
r_\theta(\nabla^2\log\pi_\theta+zz^\top)
-zz^\top
\right].
\]

The final \(-F\) term is absent from CAPO’s frozen-advantage Hessian. General \(f\)-divergences add further reward-derivative terms.

Additional failures:

- CAPO assumes a bounded, parameter-independent reward and bounded advantage. OPD log ratios are student-dependent and unbounded under support mismatch.
- Sampled-token OPD is biased relative to sequence-level reverse KL and usually omits future-reward/occupancy coupling. The paper must state exactly which objective its Hessian predicts.
- Hard top-k/top-p sampling changes the behavior policy and is nonsmooth at support boundaries. Either compute Fisher for that truncated policy or acknowledge behavior/target mismatch.
- Token safety is not additive: Hessian cross-terms and Adam’s nonlinear state mean individually “safe” tokens may form an unsafe aggregate update.
- CAPO’s theorem uses true full-parameter \(m_H,m_F\); implementation uses a last-layer approximation and then recomputes an aggregate full-model update. Porting the theorem would be cosmetic, not a guarantee.

## The one mechanism finding required

The paper needs this single falsifiable result:

> **Teacher-correction reliability and prospective update safety are causally dissociable: after conditioning on reliability, curvature predicts destructive realized updates; after conditioning on curvature, reliability predicts whether the correction is useful. One-dimensional filters therefore make opposite, measurable errors.**

The decisive figure is a 2×2 intervention:

- reliable + safe: applying improves;
- reliable + unsafe: applying causes excessive realized KL/objective damage, while softening or deferral preserves benefit;
- unreliable + nominally safe: applying does not help or harms;
- high-disagreement but verifier-reachable + safe: retaining beats masking.

The two-axis router must beat reliability-only, curvature-only, and a tuned scalar combination at identical keep rate and teacher budget. Otherwise it is CAPO + TrOPD plumbing.

Reliability should be grounded in verifier-confirmed reachability on sampled prefixes, at least diagnostically. If it is merely \(\pi_T/\pi_S\), then it is essentially TrOPD and cannot support the “useful high-disagreement” claim.

## Minimum diagnostic and experiment matrix

First run a cheap go/no-go diagnostic on one 1.5–2B student, one 7B teacher, and verifiable math:

1. Collect standard and aggressive OPD batches.
2. Stratify prefixes/tokens by verifier-based reachability and disagreement.
3. Compare CAPO’s original Hessian, the corrected OPD Hessian, Fisher, log-ratio, entropy, and gradient norm against realized post-update objective change and KL.
4. Intervene on the four reliability × safety quadrants with matched token counts.

Only then train.

Minimum full-training comparison:

- vanilla OPD, conservative;
- vanilla OPD, aggressive;
- strongest reliability-only baseline: TrOPD or TIDE;
- OPD-corrected curvature-only method;
- two-axis router;
- matched random mask and tuned scalar-score router;
- one strong stabilization baseline, preferably vOPD or TOP-D.

Screen one seed over three coupled regimes: `(3e-6, 1152)`, an intermediate point, and `(1.5e-5, 96)`. Confirm the selected conservative/aggressive pair with three seeds. Replicate surviving methods on one second domain or teacher–student scale.

Report accuracy versus:

- teacher-scored completions and teacher-scored tokens;
- GPU-hours and wall-clock;
- routing/rejection rate;
- peak memory and step overhead;
- collapse rate, realized KL, length/repetition/truncation.

Any extra teacher continuations used for reliability must count in the efficiency budget.

## Kill criteria

Kill the project if any occurs:

- Aggressive vanilla OPD does not fail reproducibly; there is no bottleneck to solve.
- Corrected curvature adds no predictive value beyond log-ratio, entropy, gradient norm, or TrOPD’s acceptance score.
- The off-diagonal quadrants are negligible, or preserving reliable/high-disagreement/safe tokens gives no causal benefit.
- The router does not beat reliability-only, curvature-only, and scalar filtering at matched keep rate and teacher cost.
- CAPO’s original Hessian performs as well as the OPD-correct version; then the supposed OPD-specific theory contribution evaporates.
- Gains disappear under LR/batch sweeps or are reproduced by matched random masking.
- The method cannot deliver at least roughly **2× fewer teacher-scored completions and lower GPU-hours to matched quality** across two settings. Completion savings without GPU-hour savings support only a narrow sample-efficiency claim.
- Overhead exceeds roughly 10–15% or reliability estimation consumes the saved teacher budget.

Bottom line: keep A only as the safety-only baseline. B is worth a short diagnostic sprint, not a full paper commitment. The paper lives or dies on the crossed-quadrant causal finding, not on deriving another router.
