# Your Teacher Can't Help You Here: Combating Supervision Fidelity Decay in On-Policy Distillation

paper_id: arxiv:2605.30833
tier: U
source_used: html_arxiv
warning: none

## Intro

Large language models (LLMs) with reasoning capabilities have achieved remarkable performance on complex mathematical and coding tasks. Recent advance models
[
27
,
11
,
7
]
demonstrate that extended reasoning chains can unlock capabilities previously thought to require much larger models. On-policy distillation (OPD), where a student model generates its own reasoning trajectories and learns from the teacher’s token-level feedback, has emerged as a primary paradigm for transferring these capabilities to efficient, deployable models
[
1
,
26
,
10
,
patiño2025_unlocking_on_policy_distillation_for_any_model_family
,
32
,
30
,
34
]
.
However, current OPD methods
[
1
,
26
,
10
,
patiño2025_unlocking_on_policy_distillation_for_any_model_family
,
20
]
implicitly treat the teacher as a
static oracle
whose supervision quality is unaffected by what the student generates. We challenge this assumption and reveal a critical failure mode: as the student generates increasingly long sequences, its outputs progressively deviate from the teacher’s training distribution, causing the teacher’s supervision quality to
degrade monotonically
, which we refer to as
Supervision Fidelity Decay (SFD)
.
Does teacher supervision quality remain reliable throughout long reasoning chains — and if not, how can we actively maintain it?
As an initial observation, training OPD with varying maximum generation lengths (Figure
2
) reveals that performance improves from 3k to 9k tokens and plateaus around 16k, followed by a significant decline at 39k. This trend indicates a potential failure mode during extremely long generations. To isolate the cause, we design a controlled prefix-completion experiment (Figure
2
): as the student prefix grows longer, both the teacher’s downstream task accuracy and peak next-token probability decay monotonically, while the teacher on its own prefixes maintains significantly higher confidence, which indicating that SFD stems from student drift. The subplots further show that teacher confidence jumps immediately when the teacher takes over, confirming that different token choices lead to different teacher confidence one step ahead.
Figure 1:
Performance of different generation length in OPD.
AIME24 over training tokens for two model pairs. Performance improves from 3k to 9k, plateaus around 16k, and degrades at 39k.
Figure 2:
Supervision Fidelity Decay.
Main:
Teacher completion accuracy decays with student prefix length.
Insets:
Teacher confidence (max/sampled prob) at the student-to-teacher handoff for
∼
\sim
2k (left) and
∼
\sim
14k (right) prefixes. Confidence jumps at the handoff (dashed line), confirming token choices affect next-step teacher confidence.
Through theoretical analysis, we find that the declining max-prob directly collapses the reverse-KL gradient. As teacher confidence falls, its log-probability varies less across token choices, effectively reducing the learning signal to a student-only signal that reinforces existing modes without correction. Yet observations from the subplot suggest a solution; even at the same out-of-distribution context, teacher confidence at the subsequent position differs across token choices. By the same gradient analysis, higher next position confidence implies a more discriminative future signal: choosing the token that maximizes the next position’s confidence directly preserves future supervision quality. We operationalize this as
Lookahead Group Reward (LGR)
, a group-normalized reward over the student’s top-
K
K
candidates, where this group normalization removes the high-variance absolute confidence level and retains only the relative ranking across candidates. To maintain computational efficiency, we further design a tree-attention mechanism triggered by entropy.
Our key contributions are:
•
We identify SFD as a fundamental failure mode of OPD.
We show that teacher accuracy and peak confidence decay as student prefix length increases, a process that we prove collapses the reverse KL gradient into a signal that reinforces itself based solely on student outputs.
•
We propose a principled remedy that looks one step ahead.
Since higher teacher confidence at the next position provides more discriminative future supervision, LGR selects tokens using group normalized rewards and an efficient tree attention mechanism triggered by entropy.
•
We show LGR’s gains grow with reasoning length.
LGR significantly outperforms OPD and alternative distillation methods, with pronounced gains on long reasoning tasks.

## Method

2.1
On-Policy Reverse-KL as Policy Gradient
Let
π
T
\pi_{T}
denote a teacher model and
π
θ
\pi_{\theta}
a student model parameterized by
θ
\theta
. Given a prompt
𝐜
\mathbf{c}
, the student autoregressively generates a sequence
𝐱
=
(
x
1
,
x
2
,
…
,
x
L
)
\mathbf{x}=(x_{1},x_{2},\ldots,x_{L})
. On-policy reverse-KL distillation minimizes
[
1
,
31
]
:
ℒ
R-KL
​
(
θ
)
=
𝔼
𝐱
∼
π
θ
(
⋅
|
𝐜
)
​
[
∑
t
=
1
L
log
⁡
π
θ
​
(
x
t
|
𝐱
<
t
,
𝐜
)
π
T
​
(
x
t
|
𝐱
<
t
,
𝐜
)
]
.
\mathcal{L}_{\text{R-KL}}(\theta)=\mathbb{E}_{\mathbf{x}\sim\pi_{\theta}(\cdot|\mathbf{c})}\left[\sum_{t=1}^{L}\log\frac{\pi_{\theta}(x_{t}|\mathbf{x}_{<t},\mathbf{c})}{\pi_{T}(x_{t}|\mathbf{x}_{<t},\mathbf{c})}\right].
(1)
Following standard practice in on-policy distillation
[
26
]
, we detach the generated sequence
𝐱
\mathbf{x}
from the computation graph during loss computation. Under this stop-gradient assumption, the per-position KL gradient decomposes independently, yielding the policy gradient form:
∇
θ
ℒ
R-KL
=
𝔼
𝐱
∼
π
θ
​
[
∑
t
=
1
L
∇
θ
log
⁡
π
θ
​
(
x
t
|
𝐱
<
t
)
⋅
A
t
]
,
\nabla_{\theta}\mathcal{L}_{\text{R-KL}}=\mathbb{E}_{\mathbf{x}\sim\pi_{\theta}}\left[\sum_{t=1}^{L}\nabla_{\theta}\log\pi_{\theta}(x_{t}|\mathbf{x}_{<t})\cdot A_{t}\right],
(2)
where the per-token advantage is:
A
t
=
1
+
log
⁡
π
θ
​
(
x
t
|
𝐱
<
t
)
−
log
⁡
π
T
​
(
x
t
|
𝐱
<
t
)
.
A_{t}=1+\log\pi_{\theta}(x_{t}|\mathbf{x}_{<t})-\log\pi_{T}(x_{t}|\mathbf{x}_{<t}).
(3)
This reveals that on-policy reverse-KL is equivalent to a policy gradient in the style of REINFORCE. Equivalently maximizing the per-token reward
r
t
=
log
⁡
π
T
​
(
x
t
|
𝐱
<
t
)
−
log
⁡
π
θ
​
(
x
t
|
𝐱
<
t
)
r_{t}=\log\pi_{T}(x_{t}|\mathbf{x}_{<t})-\log\pi_{\theta}(x_{t}|\mathbf{x}_{<t})
[
29
,
28
]
. We refer to this as
local supervision
, in which the teacher provides a distributional target at each position.
2.2
The Supervision Capability Functional and Supervision Fidelity Decay
Supervision as a functional.
The student policy
π
θ
\pi_{\theta}
generating a sequence of length
L
L
induces a
state visitation distribution
ρ
π
θ
L
​
(
c
)
\rho_{\pi_{\theta}}^{L}(c)
over prefix contexts
c
c
. The teacher’s supervision capability is then a
functional
of the student policy:
𝒞
​
[
π
θ
]
=
𝔼
c
∼
ρ
π
θ
L
​
[
f
T
​
(
c
)
]
,
where
f
T
​
(
c
)
=
max
v
∈
𝒱
⁡
π
T
​
(
v
|
c
)
\mathcal{C}[\pi_{\theta}]=\mathbb{E}_{c\sim\rho_{\pi_{\theta}}^{L}}\!\left[f_{T}(c)\right],\quad\text{where}\quad f_{T}(c)=\max_{v\in\mathcal{V}}\pi_{T}(v|c)
(4)
is the teacher’s local supervision quality at state
c
c
. This functional captures a key asymmetry. While the teacher remains unchanged
[
1
,
26
,
10
,
patiño2025_unlocking_on_policy_distillation_for_any_model_family
,
32
,
30
]
, the student’s state visitation distribution
ρ
π
θ
L
\rho_{\pi_{\theta}}^{L}
that shifts, dragging the integration domain into regions where
f
T
f_{T}
is low.
Position-dependent SFD curve.
We define the position-dependent version:
𝒞
(
t
)
​
[
π
θ
]
=
𝔼
c
∼
ρ
π
θ
t
​
[
max
v
⁡
π
T
​
(
v
|
c
)
]
,
\mathcal{C}^{(t)}[\pi_{\theta}]=\mathbb{E}_{c\sim\rho_{\pi_{\theta}}^{t}}\!\left[\max_{v}\pi_{T}(v|c)\right],
(5)
so that
𝒞
(
t
)
​
[
π
θ
]
\mathcal{C}^{(t)}[\pi_{\theta}]
as a function of
t
t
traces the SFD curve. The aggregate
𝒞
​
[
π
θ
]
=
𝔼
t
​
[
𝒞
(
t
)
​
[
π
θ
]
]
\mathcal{C}[\pi_{\theta}]=\mathbb{E}_{t}[\mathcal{C}^{(t)}[\pi_{\theta}]]
summarizes total supervision quality. When
L
L
is short,
ρ
π
θ
L
\rho_{\pi_{\theta}}^{L}
remains within the teacher’s training manifold and
f
T
​
(
c
)
f_{T}(c)
stays high; when
L
L
is long, autoregressive drift causes
ρ
π
θ
L
\rho_{\pi_{\theta}}^{L}
to shift into the teacher’s OOD region, where
f
T
​
(
c
)
f_{T}(c)
collapses.
Supervision fidelity as a downstream metric.
For a specific student-generated prefix
𝐱
<
t
\mathbf{x}_{<t}
, the teacher’s
supervision fidelity
at position
t
t
is:
ℱ
​
(
t
)
≔
max
v
∈
𝒱
⁡
π
T
​
(
v
|
𝐱
≤
t
,
𝐜
)
,
\mathcal{F}(t)\coloneqq\max_{v\in\mathcal{V}}\pi_{T}(v|\mathbf{x}_{\leq t},\mathbf{c}),
(6)
i.e., the teacher’s peak next-token probability after observing the student’s prefix up to
t
t
. Note that
𝒞
(
t
)
​
[
π
θ
]
=
𝔼
​
[
ℱ
​
(
t
)
]
\mathcal{C}^{(t)}[\pi_{\theta}]=\mathbb{E}[\mathcal{F}(t)]
is the expectation of
ℱ
​
(
t
)
\mathcal{F}(t)
over student trajectories. At the task level, we can also measure supervision fidelity as
P
​
(
teacher completes correctly from position
​
t
∣
𝐱
<
t
θ
)
P(\text{teacher completes correctly from position }t\mid\mathbf{x}_{<t}^{\theta})
, which correlates strongly with
ℱ
​
(
t
)
\mathcal{F}(t)
, thereby validating that max-
p
p
is an effective proxy for downstream supervision quality.
Empirical observation.
Using DeepSeek-R1-Distill-Qwen-1.5B
[
11
]
as the student and 32B
[
11
]
as the teacher on AIME
[
36
]
, we generate student prefixes of varying lengths and hand off to the teacher. Figure
2
shows: (1) teacher completion accuracy drops monotonically with prefix length; (2)
ℱ
¯
\bar{\mathcal{F}}
decreases correspondingly, validating max-
p
p
as a proxy; (3) the teacher on its own prefixes maintains significantly higher fidelity, confirming SFD stems from student drift. The inset subplots further show that at the handoff point, teacher confidence
jumps immediately
, which demonstrates that token choices at position
t
t
do affect teacher confidence at
t
+
1
t{+}1
, even under severe SFD. The jump shrinks at longer prefixes (
∼
14
{\sim}14
k vs.
∼
2
{\sim}2
k) and after OPD optimization, consistent with accumulated drift. This directly motivates Section
3.2
.
2.3
Theoretical Analysis: Signal Collapse and Compounding Drift
We formalize the impact of SFD on gradient quality. As the teacher’s distribution becomes diffuse, its discriminative contribution vanishes; consequently, this single-position failure compounds across positions into a self-reinforcing drift.
Proposition 1
(Teacher signal vanishing under SFD)
.
Define
Δ
T
​
(
t
)
≔
Var
x
t
∼
π
θ
​
[
log
⁡
π
T
​
(
x
t
|
𝐱
<
t
)
]
\Delta_{T}(t)\coloneqq\mathrm{Var}_{x_{t}\sim\pi_{\theta}}[\log\pi_{T}(x_{t}|\mathbf{x}_{<t})]
. Then
Δ
T
(
t
)
≤
log
2
|
𝒱
|
−
Ent
(
π
T
(
⋅
|
𝐱
<
t
)
)
2
\Delta_{T}(t)\leq\log^{2}|\mathcal{V}|-\mathrm{Ent}(\pi_{T}(\cdot|\mathbf{x}_{<t}))^{2}
, so as the teacher’s distribution becomes diffuse under SFD,
Δ
T
​
(
t
)
→
0
\Delta_{T}(t)\to 0
and
SNR
T
​
(
t
)
=
O
​
(
Δ
T
​
(
t
)
)
→
0
\mathrm{SNR}_{T}(t)=O(\Delta_{T}(t))\to 0
: the teacher’s discriminative contribution to the gradient vanishes entirely, leaving a student-only signal that reinforces existing modes without correction.
(Proof: Appendix
F.1
.)
Once the teacher signal vanishes at position
t
t
, the student selects tokens from its own sharpened distribution, pushing the next context further out-of-distribution, thereby further degrading the signal at
t
+
1
t{+}1
.
Proposition 2
(Self-reinforcing drift under reverse-KL)
.
Let
d
t
≔
D
(
π
T
(
⋅
|
𝐱
<
t
θ
)
,
π
T
(
⋅
|
𝐱
<
t
∗
)
)
d_{t}\coloneqq D(\pi_{T}(\cdot|\mathbf{x}_{<t}^{\theta}),\pi_{T}(\cdot|\mathbf{x}_{<t}^{*}))
be the distributional drift at position
t
t
, and assume
Δ
T
​
(
t
)
\Delta_{T}(t)
is non-increasing in
d
t
d_{t}
(greater drift degrades teacher discriminability, as implied by SFD). When
Δ
T
​
(
t
)
<
δ
crit
\Delta_{T}(t)<\delta_{\mathrm{crit}}
, the teacher-free advantage reinforces the student’s existing modes, causing
𝔼
​
[
d
t
+
1
|
d
t
]
≥
d
t
\mathbb{E}[d_{t+1}|d_{t}]\geq d_{t}
: drift compounds across positions, creating a positive feedback loop that degrades supervision irreversibly. Forward-KL avoids this by construction (
d
t
=
0
d_{t}=0
always) but introduces exposure bias.
(Proof sketch: Appendix
F.2
.)
2.4
Training Dynamics: The Vicious Cycle and Supervision Boundary Contraction
The functional perspective reveals a deeper consequence. Define the
effective learning horizon
t
eff
​
(
k
)
=
sup
{
t
:
𝒞
(
t
)
​
[
π
θ
k
]
>
C
min
}
t_{\mathrm{eff}}(k)=\sup\{t:\mathcal{C}^{(t)}[\pi_{\theta_{k}}]>C_{\min}\}
as the furthest position where teacher supervision exceeds a minimum useful threshold at training step
k
k
.
Under the self-reinforcing drift established in Proposition
2
, training induces a
vicious cycle
: positions beyond
t
eff
t_{\mathrm{eff}}
receive no useful supervision (
ℓ
≈
0
\ell\approx 0
) and therefore do not improve; the student’s uncorrected behavior at these positions continues to push the teacher further out-of-distribution, which in turn may cause
t
eff
t_{\mathrm{eff}}
to
shrink
at the next training step. This creates a “learning desert” that expands over training, establishing a
reasoning length ceiling
t
∗
t^{*}
beyond which the student can never improve under standard on-policy distillation.
The
𝒞
(
t
)
\mathcal{C}^{(t)}
curve follows a sigmoidal decay: the early portion maintains high supervision quality, the late portion collapses, and the transition sharpens progressively over training. We verify this empirically: fitting a logistic sigmoid to both curves in Figure
2
yields
R
2
>
0.997
R^{2}>0.997
, and the fitted parameters show that OPD training contracts the supervision boundary (
t
∗
t^{*}
:
7.43
→
7.04
7.43\to 7.04
k) and steepens the transition slope (
ε
\varepsilon
:
0.21
→
0.26
0.21\to 0.26
). Notably, all four parameter shifts align with
the direction predicted by the vicious cycle (see Appendix
C
for full fit results).
This compounding effect is fundamental to on-policy reverse-KL and cannot be resolved by simply adjusting learning rates or adding regularization, as these measures only slow the drift rate
ε
\varepsilon
without changing the structural problem. Instead, it motivates directly optimizing the supervision functional
𝒞
​
[
π
θ
]
\mathcal{C}[\pi_{\theta}]
itself, which provides a structurally different signal that steers the student toward states where the teacher can provide high-quality supervision.
