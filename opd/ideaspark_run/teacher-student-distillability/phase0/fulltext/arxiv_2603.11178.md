# PACED: Distillation and On-Policy Self-Distillation at the Frontier of Student Competence

paper_id: arxiv:2603.11178
tier: U
source_used: html_arxiv
warning: none

## Intro

Knowledge distillation trains a student model to imitate a teacher, yet standard practice spreads the training budget
uniformly
across all problems. This is wasteful: some problems are already mastered and provide redundant signal, while others are far beyond the student’s current reach and produce noisy, incoherent gradients that can erode previously learned knowledge
(French,
1999
; Kirkpatrick
et al.
,
2017
)
.
We begin with an empirical observation that makes this intuition precise. To our knowledge, we are the
first to directly measure the cross-problem gradient signal-to-noise ratio (SNR) in distillation as a function of student competence
. The measurement reveals a striking pattern (Figure
2
): the SNR follows a
bell-shaped curve that collapses at both boundaries
. At
p
≈
0
p\approx 0
, gradients from diverse intractable problems are directionally incoherent. At
p
≈
1
p\approx 1
, per-problem gradients persist (the teacher’s distribution may remain sharper) but point in problem-specific directions that
disperse
in parameter space, canceling when averaged. The maximum SNR—where each gradient step most efficiently advances the student’s capability frontier—lies at intermediate pass rates.
This observation motivates
P
roficiency-
A
daptive
C
ompetence
E
nhanced
D
istillation (
Paced
): weight each problem by
w
​
(
p
)
=
p
​
(
1
−
p
)
w(p)=p(1{-}p)
, concentrating training on the
zone of proximal development
(Vygotsky and Cole,
1978
)
—problems where the student sometimes succeeds and sometimes fails. The weighting requires only student rollouts, no architectural changes, and no hyperparameters.
Why this specific functional form? Taking the boundary-collapse structure as a regularity condition, we show that any SNR profile with power-law decay at both boundaries decomposes as
p
a
′
​
(
1
−
p
)
b
′
⋅
e
r
​
(
p
)
p^{a^{\prime}}(1{-}p)^{b^{\prime}}\cdot e^{r(p)}
with bounded remainder (Proposition
2
), making the Beta kernel
w
​
(
p
)
=
p
α
​
(
1
−
p
)
β
w(p)=p^{\alpha}(1{-}p)^{\beta}
the leading-order, maximum-parsimony weight family. This is not merely a convenient parametrization: the Beta kernel is minimax-optimal under bounded misspecification, with worst-case efficiency loss only
O
​
(
δ
2
)
O(\delta^{2})
(Theorem
6
). Curriculum learning
(Bengio
et al.
,
2009
; Kumar
et al.
,
2010
)
addresses related concerns but relies on fixed difficulty annotations or predetermined schedules; in distillation, difficulty depends on
who
is solving each problem and
when
—a problem intractable at epoch 1 may become productive by epoch 5.
We validate
Paced
across two settings:
Distillation
(Qwen3-8B
GRPO
→
\to
Qwen3-1.7B, forward KL) and
Self-distillation
(Qwen2.5-Math-7B-Instruct, reverse KL), with cross-family generalization to Llama-3.1-8B-Instruct. Our contributions:
1.
A novel empirical finding with theoretical characterization.
We provide the first direct measurement of cross-problem gradient SNR in distillation, revealing its bell-shaped collapse as a function of student pass rate (Figure
2
). We then prove the Beta kernel is the leading-order optimal and minimax-robust weight family arising from this structure (Propositions
1
–
2
, Theorem
6
).
2.
Strong gains with near-zero forgetting.
Paced
improves over unweighted distillation by up to
+
3.9
+3.9
on AIME 2024 (forward KL) and up to
+
8.2
+8.2
on AIME 2025 (reverse KL), while keeping MMLU forgetting
≤
1.4
%
\leq 1.4\%
—matching the best-retention baseline while strictly outperforming it on reasoning. Gains generalize across Qwen3, Qwen2.5, and Llama-3 families.
3.
A two-stage KL schedule.
Forward KL (mode-covering) followed by reverse KL (mode-seeking) pushes gains further to
+
4.6
/
+
4.9
/
+
5.8
+4.6/+4.9/+5.8
over standard forward KL on MATH-500/AIME 2024/AIME 2025, confirming that the two KL directions are complementary.
An overview appears in Figure
1
.
Figure 1:
Overview of
Paced
.
Left:
The pipeline—an expert provides reference solutions, and the student learns via a distillation loss weighted by pass rate.
Right:
The Beta-kernel weighting
w
​
(
p
)
=
p
α
​
(
1
−
p
)
β
w(p)=p^{\alpha}(1-p)^{\beta}
concentrates training on the zone of proximal development, suppressing trivial and intractable problems.

## Method

Paced
rests on a single core idea: a weighting scheme that directs distillation toward the problems where it can do the most good (Section
3.2
).
3.1
Problem Setup
We use two disjoint training splits:
𝒟
dist
\mathcal{D}^{\text{dist}}
for distillation and
𝒟
self
\mathcal{D}^{\text{self}}
for self-distillation. Let
T
T
denote the frozen teacher model and
S
θ
S_{\theta}
the student model. In distillation,
T
T
is a GRPO-finetuned same-family model (Qwen3-8B trained with GRPO
(Shao
et al.
,
2024
)
on DAPO-Math-17k, denoted Qwen3-8B
GRPO
) and
S
θ
S_{\theta}
is Qwen3-1.7B. In self-distillation,
T
T
is a frozen copy of Qwen2.5-Math-7B-Instruct and
S
θ
S_{\theta}
is the trainable copy. In both settings,
T
T
is fixed while
θ
\theta
is updated.
For each prompt
x
x
, distillation uses a teacher-side reference response
y
T
y_{T}
. To construct attainable targets, an external expert
ℰ
\mathcal{E}
(e.g., a frontier API or strong open-weight model) first produces a solution
y
ℰ
y_{\mathcal{E}}
, and the frozen teacher
T
T
then regenerates it in its own distributional voice,
y
T
∼
P
T
​
(
y
∣
x
,
y
ℰ
)
y_{T}\sim P_{T}(y\mid x,y_{\mathcal{E}})
, producing a target naturally within the model family’s expressive range. The student sees only
x
x
; the teacher sees
(
x
,
y
ℰ
)
(x,y_{\mathcal{E}})
. This
prompt asymmetry
converts black-box expert supervision into white-box, same-family distillation signals (full token-level logits rather than hard-label SFT); Appendix
B.1
provides the template.
To measure the student’s current competence on
x
x
, we sample
K
K
rollouts from the student and compute the
pass rate
:
p
(
x
;
θ
)
=
1
K
∑
k
=
1
K
𝟙
[
correct
(
y
S
(
k
)
,
x
)
]
,
y
S
(
k
)
∼
π
θ
(
⋅
∣
x
)
p(x;\theta)=\frac{1}{K}\sum_{k=1}^{K}\mathbbm{1}\left[\texttt{correct}(y_{S}^{(k)},x)\right],\quad y_{S}^{(k)}\sim\pi_{\theta}(\cdot\mid x)
(1)
The pass rate
p
∈
[
0
,
1
]
p\in[0,1]
measures the student’s current competence on problem
x
x
.
3.2
Pass-Rate Weighting
Motivation.
Given a reference target
y
T
y_{T}
for each prompt, the core design question is how to weight problems according to the student’s current competence. Not all training problems contribute equally. At one extreme (
p
≈
0
p\approx 0
), the student cannot solve the problem at all; logit gradients are large but point in near-random directions across prompts, offering high variance and little useful signal. At the other extreme (
p
≈
1
p\approx 1
), individual per-problem gradients need not vanish—for distribution-matching losses, the teacher’s distribution may remain sharper than the student’s—but the remaining corrections are problem-specific calibration refinements (e.g., sharpening predictions on algebraic tokens for one problem, adjusting geometric reasoning for another) that
disperse
in parameter space. When averaged across mastered problems, these dispersed corrections largely cancel, yielding low cross-problem SNR even though each individual gradient carries signal. In practice a substantial fraction of problems falls into these low-SNR extremes—e.g., with Qwen3-1.7B on DAPO, roughly
49
%
49\%
of problems have
p
<
0.2
p<0.2
or
p
>
0.8
p>0.8
(the exact proportion depends on the model and dataset). The richest—highest signal-to-noise ratio—gradient signal concentrates at
intermediate
difficulty, where a coherent skill gap provides a shared gradient direction and each update advances the student’s capability frontier. This raises a natural question:
what is the principled weight function that exploits this structure?
Theoretical answer.
In distillation, the gradient signal-to-noise ratio (SNR) collapses at both boundaries via cross-problem gradient incoherence: at
p
→
0
p\to 0
(diverse intractable problems) and
p
→
1
p\to 1
(dispersed problem-specific refinements; Proposition
1
). Under power-law regularity at the boundaries (Assumption
3
(b)), any such SNR profile decomposes as
p
a
′
​
(
1
−
p
)
b
′
⋅
e
r
​
(
p
)
p^{a^{\prime}}(1-p)^{b^{\prime}}\cdot e^{r(p)}
with bounded remainder (Proposition
2
). The leading-order, maximum-parsimony weight family is therefore the Beta kernel:
w
​
(
p
)
=
p
α
​
(
1
−
p
)
β
\boxed{w(p)=p^{\alpha}(1-p)^{\beta}}
(2)
with peak at
p
∗
=
α
/
(
α
+
β
)
p^{*}=\alpha/(\alpha+\beta)
. The default choice
α
=
β
=
1
\alpha=\beta=1
gives
w
​
(
p
)
=
p
​
(
1
−
p
)
w(p)=p(1-p)
, which is symmetric around
p
∗
=
0.5
p^{*}=0.5
, zero at the boundaries, and equals the inverse Bernoulli Fisher information (Remark
5
). Asymmetric choices (
α
≠
β
\alpha\neq\beta
) shift the peak to prioritize harder or easier problems. This form is minimax-robust: even when the true SNR profile deviates from the Beta model by a multiplicative factor
e
±
δ
e^{\pm\delta}
, the worst-case efficiency loss is only
O
​
(
δ
2
)
O(\delta^{2})
(Theorem
6
). See Appendix
A.5
for the full derivation.
3.3
Overall Algorithm
Putting the pieces together: each problem’s contribution to the loss is scaled by how informative it is for the student right now:
ℒ
​
(
θ
;
x
)
=
w
​
(
p
)
⋅
ℒ
distill
​
(
θ
;
x
)
\mathcal{L}(\theta;x)=w(p)\cdot\mathcal{L}_{\text{distill}}(\theta;x)
(3)
where
p
=
p
​
(
x
;
θ
)
p=p(x;\theta)
,
w
​
(
p
)
=
p
​
(
1
−
p
)
w(p)=p(1-p)
by default, and
ℒ
distill
\mathcal{L}_{\text{distill}}
is chosen by training setting. To keep the instantiation clean, we bind one KL direction to each setting: distillation (Qwen3-8B
GRPO
→
\to
Qwen3-1.7B) uses forward KL, and self-distillation (Qwen2.5-Math-7B-Instruct) uses reverse KL. This pairing reflects their roles: forward KL favors broad teacher-mode coverage when the teacher is stronger, while reverse KL favors compact, high-confidence modes when teacher and student are near-policy. Concretely, we use:
•
Distillation track (Qwen3): Forward KL
along the teacher sequence
y
T
y_{T}
:
∑
t
D
K
​
L
(
p
T
(
⋅
∣
y
T
,
<
t
)
∥
p
S
(
⋅
∣
y
T
,
<
t
)
)
\sum_{t}D_{KL}\!\bigl(p_{T}(\cdot\mid y_{T,<t})\,\|\,p_{S}(\cdot\mid y_{T,<t})\bigr)
.
•
Self-distillation track (Qwen2.5): Reverse KL
along a student sequence
y
S
∼
π
θ
(
⋅
∣
x
)
y_{S}\sim\pi_{\theta}(\cdot\mid x)
:
∑
t
D
K
​
L
(
p
S
(
⋅
∣
y
S
,
<
t
)
∥
p
T
(
⋅
∣
y
S
,
<
t
)
)
\sum_{t}D_{KL}\!\bigl(p_{S}(\cdot\mid y_{S,<t})\,\|\,p_{T}(\cdot\mid y_{S,<t})\bigr)
.
ℒ
​
(
θ
)
=
1
N
​
∑
i
=
1
N
ℒ
​
(
θ
;
x
i
)
\mathcal{L}(\theta)=\frac{1}{N}\sum_{i=1}^{N}\mathcal{L}(\theta;x_{i})
(4)
Algorithm 1
Paced
: Competence-Aware Distillation with Pass-Rate Weighting
0:
Prompt dataset
𝒟
\mathcal{D}
, expert
ℰ
\mathcal{E}
, frozen teacher
T
T
, student
S
θ
S_{\theta}
, distillation loss
ℒ
distill
\mathcal{L}_{\text{distill}}
(forward KL or reverse KL), weight exponents
(
α
,
β
)
(\alpha,\beta)
(default
α
=
β
=
1
\alpha{=}\beta{=}1
), rollouts
K
K
1:
// Stage 1: Teacher-side target preparation (forward KL only)
2:
if
ℒ
distill
\mathcal{L}_{\text{distill}}
is forward KL
then
3:
for
each prompt
x
∈
𝒟
x\in\mathcal{D}
do
4:
y
ℰ
←
ℰ
​
(
x
)
y_{\mathcal{E}}\leftarrow\mathcal{E}(x)
{Expert rollout (e.g., GPT-family API solution)}
5:
y
T
←
T
(
⋅
∣
x
,
y
ℰ
)
y_{T}\leftarrow T(\cdot\mid x,y_{\mathcal{E}})
{Teacher regeneration conditioned on expert solution}
6:
end
for
7:
end
if
8:
// Stage 2: One-shot pass-rate estimation (paper setting)
9:
for
each prompt
x
i
∈
𝒟
x_{i}\in\mathcal{D}
do
10:
Sample
{
y
S
,
i
(
k
)
}
k
=
1
K
∼
π
θ
(
⋅
∣
x
i
)
\{y_{S,i}^{(k)}\}_{k=1}^{K}\sim\pi_{\theta}(\cdot\mid x_{i})
11:
p
i
←
1
K
​
∑
k
𝟙
​
[
correct
​
(
y
S
,
i
(
k
)
,
x
i
)
]
p_{i}\leftarrow\frac{1}{K}\sum_{k}\mathbbm{1}[\texttt{correct}(y_{S,i}^{(k)},x_{i})]
12:
w
i
←
p
i
α
​
(
1
−
p
i
)
β
w_{i}\leftarrow p_{i}^{\alpha}(1-p_{i})^{\beta}
{Default:
w
i
=
p
i
​
(
1
−
p
i
)
w_{i}=p_{i}(1-p_{i})
}
13:
end
for
14:
w
~
i
←
w
i
/
w
¯
\tilde{w}_{i}\leftarrow w_{i}\,/\,\bar{w}
for all
i
i
{Normalize to unit mean and keep fixed during training}
15:
// Stage 3: Weighted Distillation
16:
for
each training iteration
do
17:
for
each prompt
x
i
∈
𝒟
x_{i}\in\mathcal{D}
do
18:
if
ℒ
distill
\mathcal{L}_{\text{distill}}
is forward KL
then
19:
ℒ
​
(
x
i
)
←
w
~
i
⋅
ℒ
distill
​
(
θ
;
y
T
,
i
,
x
i
)
\mathcal{L}(x_{i})\leftarrow\tilde{w}_{i}\cdot\mathcal{L}_{\text{distill}}(\theta;y_{T,i},x_{i})
{Teacher-forced distillation}
20:
else
21:
Sample
y
S
,
i
∼
π
θ
(
⋅
∣
x
i
)
y_{S,i}\sim\pi_{\theta}(\cdot\mid x_{i})
22:
ℒ
​
(
x
i
)
←
w
~
i
⋅
ℒ
distill
​
(
θ
;
y
S
,
i
,
x
i
)
\mathcal{L}(x_{i})\leftarrow\tilde{w}_{i}\cdot\mathcal{L}_{\text{distill}}(\theta;y_{S,i},x_{i})
{Reverse-KL self-distillation on student rollouts}
23:
end
if
24:
end
for
25:
Update
θ
\theta
via gradient descent on
1
N
​
∑
i
ℒ
​
(
x
i
)
\frac{1}{N}\sum_{i}\mathcal{L}(x_{i})
26:
end
for
27:
// Optional extension:
periodically recompute
{
p
i
,
w
~
i
}
\{p_{i},\tilde{w}_{i}\}
every
T
0
T_{0}
steps
Iterative Refinement.
In most experiments we estimate pass rates once before optimization and keep the resulting weights fixed (single-pass weighting); this suffices because the Beta kernel is minimax-robust to stale pass rates (Theorem
6
). When compute allows, pass rates can be recomputed periodically or at stage boundaries to track evolving competence; Appendix
C.1.3
ablates both options.
3.4
Theoretical Guarantees
We provide theoretical justification for Beta-kernel weighting. The core intuition is simple: at both pass-rate extremes,
cross-problem gradient incoherence
drives the SNR to zero, but for structurally distinct reasons. When
p
→
0
p\to 0
, the student is far from solving the problem, so gradients from diverse intractable prompts are poorly aligned, yielding low SNR. When
p
→
1
p\to 1
, per-problem gradients from distribution-matching losses need not vanish (the teacher may remain sharper), but the remaining corrections are problem-specific refinements that disperse in parameter space—unlike intermediate pass rates where a coherent skill gap provides a shared gradient direction. This suggests that useful learning signal should concentrate in the interior of the pass-rate range, and that a principled weight should be near zero at both boundaries while remaining flexible about where to peak. The results below formalize exactly this picture, showing that under mild regularity the Beta family is the leading-order and robust choice. Full proofs, assumptions, and regime distinctions appear in Appendix
A
. The assumptions rest on standard regularity conditions from stochastic optimization
(Ghadimi and Lan,
2013
; Bottou
et al.
,
2018
)
, well-documented properties of gradient statistics in knowledge distillation
(Tang
et al.
,
2020
; Sankararaman
et al.
,
2020
; Agarwal
et al.
,
2022
)
, and our own empirical SNR measurements. In particular, Appendix
A.1
and Figure
2
directly visualize the predicted bell-shaped SNR profile and show that it closely tracks
p
​
(
1
−
p
)
\sqrt{p(1-p)}
.
Key Results at a Glance
•
Structural characterization:
Distillation gradient SNR collapses at both boundaries via cross-problem gradient incoherence (Prop
1
); with power-law regularity, any such profile decomposes as
p
a
′
​
(
1
−
p
)
b
′
⋅
e
r
​
(
p
)
p^{a^{\prime}}(1{-}p)^{b^{\prime}}\cdot e^{r(p)}
with bounded
r
r
(Prop
2
), yielding the Beta kernel as the leading-order weight family
•
Minimax robustness (Main Theorem):
Under bounded misspecification
|
r
​
(
p
)
|
≤
δ
|r(p)|\leq\delta
, the Beta kernel is minimax-optimal for the low-SNR approximation, with worst-case efficiency
sech
2
​
(
δ
)
≥
1
−
δ
2
\text{sech}^{2}(\delta)\geq 1-\delta^{2}
, both pointwise and in aggregate (Thm
6
)
•
Batch-level variance reduction:
R
<
1
R<1
when
−
Cov
​
(
w
~
2
,
s
2
)
>
Var
​
(
w
~
)
​
𝔼
​
[
s
2
]
-\text{Cov}(\tilde{w}^{2},s^{2})>\text{Var}(\tilde{w})\,\mathbb{E}[s^{2}]
(Prop
7
)
•
Exponent selection:
(
α
∗
+
1
)
/
(
α
∗
+
β
∗
+
2
)
=
p
¯
𝒵
(\alpha^{*}{+}1)/(\alpha^{*}{+}\beta^{*}{+}2)=\bar{p}_{\mathcal{Z}}
,
α
∗
+
β
∗
=
p
¯
𝒵
​
(
1
−
p
¯
𝒵
)
/
Var
𝒵
​
(
p
)
−
3
\alpha^{*}{+}\beta^{*}=\bar{p}_{\mathcal{Z}}(1{-}\bar{p}_{\mathcal{Z}})/\text{Var}_{\mathcal{Z}}(p)-3
(Prop
10
)
Full proofs appear in Appendix
A
, which opens with the empirical SNR measurement (Section
A.1
) that motivates the boundary-collapse assumption before developing the formal theory. We briefly unpack the intuition behind Results 3 and 4, which are less immediate than the first two.
Intuition for Result 3.
Non-uniform weighting faces a tug of war: downweighting reduces the effective batch size (increasing variance), but if the downweighted samples are precisely the noisiest ones, the net effect is variance
reduction
. Because gradient noise runs hottest at extreme pass rates
(Agarwal
et al.
,
2022
)
, the Beta kernel’s near-zero boundary weights suppress exactly those high-variance samples, making the coupling term sufficiently negative to win the trade-off (
R
<
1
R<1
). Appendix
A.6
identifies concrete parameter regimes.
Intuition for Result 4.
The moment-matching formula requires only the ZPD pass-rate mean and variance—no gradient computation. When informative problems cluster tightly, it prescribes a peaked kernel; when they spread broadly, a flatter one. See Appendix
A.7
for the derivation.
Forgetting reduction.
By suppressing gradient updates from boundary-pass-rate samples, Beta-kernel weighting substantially reduces catastrophic forgetting; see Tables
4
and
5
.
