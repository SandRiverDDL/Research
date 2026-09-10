# Teacher-Guided Policy Optimization for On-Policy Reasoning Distillation under Large Policy Divergence

paper_id: arxiv:2605.13230
tier: U
source_used: html_arxiv
warning: none

## Intro

Reinforcement Learning with Verifiable Rewards (RLVR)
Team
et al.
(
2025
); Guo
et al.
(
2025
)
and knowledge distillation
Team (
2025
); Xiao
et al.
(
2026
)
are two widely used approaches for improving the reasoning abilities of LLMs.
RLVR enables scalable optimization from verifiable outcomes, but its reward signals are sparse and uniformly applied across all generated tokens, providing limited fine-grained feedback.
In contrast, knowledge distillation offers dense token-level supervision from a teacher model but relies on off-policy data.
Recently,
on-policy distillation (OPD)
Agarwal
et al.
(
2024
); Lu and Lab (
2025
); Xu
et al.
(
2025
)
has emerged as a promising paradigm that combines the advantages of both approaches.
Unlike conventional teacher-forced distillation, OPD trains the student on trajectories sampled from its own policy while leveraging teacher supervision signals.
By aligning training with the student-induced distribution, OPD alleviates the mismatch between training and inference and naturally complements RLVR-based reasoning optimization.
Figure 1:
RKL vs. TGPO. (a)
RKL relies on scalar rewards to penalize deviation. When the policy gap is significant, these penalties fail to provide directional information.
(b)
TGPO utilizes the teacher’s predicted distribution as
guidance
, explicitly informing the student
what
to generate next rather than
what not
to generate.
Most existing OPD methods formulate teacher supervision through reverse KL (RKL)-based objectives.
As detailed in Section
2
, such objectives mainly provide
evaluative
supervision, rewarding trajectories preferred by the teacher while penalizing unlikely ones.
In practice, existing OPD methods often reduce teacher–student policy divergence before applying on-policy distillation.
For example, prior work constructs teacher–student pairs within the same model family
Agarwal
et al.
(
2024
)
, employs self-teaching strategies
Hübotter
et al.
(
2026
); Zhao
et al.
(
2026
)
, or introduces additional intermediate training stages to increase distribution overlap
Lu and Lab (
2025
); Xu
et al.
(
2025
)
.
These design choices suggest that RKL-based OPD methods implicitly rely on sufficient overlap between teacher and student trajectory distributions for effective supervision.
However, we argue that this dependence on distribution overlap reflects a fundamental limitation of RKL-based supervision:
the teacher primarily evaluates sampled trajectories and does not provide explicit guidance toward better continuations
.
As a result, the student must rely on exploration to discover teacher-preferred trajectories.
This limitation becomes more severe when the student policy drifts far from the teacher distribution, as we analyze in Section
2
.
In such cases, the teacher assigns near-zero probability to many student-generated tokens, causing optimization to be dominated by uninformative negative feedback rather than useful directional guidance.
Such token-level penalties can further degrade the quality of sampled trajectories.
When combined with RLVR optimization (e.g., GRPO) in reasoning-oriented post-training, this issue can destabilize optimization, as sampled groups become increasingly dominated by poor trajectories
Le
et al.
(
2025
)
.
To address these limitations, we propose Teacher-Guided Policy Optimization (TGPO), an on-policy reasoning distillation framework designed to provide informative supervision even under large teacher–student divergence.
As illustrated in Figure
1
, unlike RKL-based objectives, which evaluate the teacher’s likelihood of the student’s actions, TGPO queries the teacher for the optimal action conditioned on the student’s generated context.
By maximizing the likelihood of teacher-predicted tokens during RLVR, TGPO leverages the exploration benefits of on-policy sampling while retaining the constructive supervision of supervised learning.
This mechanism enriches traditional on-policy RL with fine-grained token-level supervision, bridging the gap between sparse outcome rewards and dense teacher guidance.
Based on this perspective, we make the following contributions:
•
We analyze the limitations of RKL-based OPD and empirically show that its effectiveness depends on sufficient teacher–student distribution overlap.
•
We propose TGPO, an on-policy reasoning distillation framework that provides token-level teacher guidance on student-generated trajectories, enabling effective supervision under large teacher–student divergence.
•
Experiments on reasoning benchmarks show that TGPO improves the robustness of OPD under large teacher–student divergence, even outperforming the mixed-policy approach.

## Method

In this section, we analyze the limitations of prior RKL-based on-policy distillation methods. We first formulate the RKL objective in Section
2.1
, then show why RKL-based supervision becomes unstable under large teacher–student distribution divergence in Section
2.2
. Finally, Section
2.3
provides empirical evidence supporting the analysis.
2.1
RKL-Based On-Policy Distillation
Given a prompt dataset
𝒟
=
{
x
}
\mathcal{D}=\{x\}
, we aim to train a student policy
π
θ
(
⋅
|
x
)
\pi_{\theta}(\cdot|x)
to approximate a fixed, superior teacher policy
π
T
(
⋅
|
x
)
\pi_{T}(\cdot|x)
. On-policy distillation (OPD)
Gu
et al.
(
2023
); Team
et al.
(
2024
); Agarwal
et al.
(
2024
)
achieve this by minimizing the RKL divergence over student-generated responses
y
y
:
𝒥
RKL
​
(
θ
)
=
𝔼
x
∼
𝒟
D
KL
(
π
θ
|
|
π
T
)
=
𝔼
x
∼
𝒟
,
y
∼
π
θ
(
⋅
|
x
)
​
[
log
⁡
π
θ
​
(
y
|
x
)
π
T
​
(
y
|
x
)
]
.
\begin{split}\mathcal{J}_{\text{RKL}}(\theta)&=\mathbb{E}_{x\sim\mathcal{D}}D_{\text{KL}}(\pi_{\theta}||\pi_{T})\\
&=\mathbb{E}_{x\sim\mathcal{D},y\sim\pi_{\theta}(\cdot|x)}\left[\log\frac{\pi_{\theta}(y|x)}{\pi_{T}(y|x)}\right].\end{split}
(1)
Unlike Forward KL or supervised fine-tuning, which rely on teacher-generated samples, the RKL objective takes expectations over responses sampled from the student policy itself. This on-policy formulation shares the same expectation structure as RL objectives, where optimization is also performed over trajectories sampled from the current policy. As a result, RKL-based distillation can be naturally interpreted within an RL framework.
Let
r
​
(
y
)
r(y)
denote the reward assigned to a sampled sequence
y
y
. Standard RL objectives can then be written as:
𝒥
RL
​
(
θ
)
=
𝔼
x
∼
𝒟
,
y
∼
π
θ
(
⋅
|
x
)
​
[
r
​
(
y
)
]
.
\mathcal{J}_{\text{RL}}(\theta)=\mathbb{E}_{x\sim\mathcal{D},y\sim\pi_{\theta}(\cdot|x)}\left[r(y)\right].
(2)
Comparing Eq.
1
and Eq.
2
, minimizing
𝒥
RKL
\mathcal{J}_{\text{RKL}}
is equivalent to maximizing
𝒥
RL
\mathcal{J}_{\text{RL}}
with intrinsic reward
r
​
(
y
)
=
−
log
⁡
π
θ
​
(
y
|
x
)
π
T
​
(
y
|
x
)
r(y)=-\log\frac{\pi_{\theta}(y|x)}{\pi_{T}(y|x)}
, enabling OPD to be naturally optimized within standard RL frameworks.
Figure 2:
Comparison of RKL distillation dynamics. We distill a
Qwen2.5-Math-1.5B
student using either an In-Family teacher (
Qwen2.5-Math-7B
) or a Cross-Family teacher (
Qwen3-30B-A3B
). While the In-Family setting converges stably, the Cross-Family setting exhibits catastrophic instability, characterized by sharp training score degradation
(Left)
, gradient norm spikes
(Middle)
, and unbounded response length growth
(Right)
.
2.2
The Limitations of RKL-based Methods
Despite its simple formulation, the RKL objective introduces optimization challenges under large teacher–student distribution gaps. In this section, we analyze this issue by viewing RKL as an intrinsic reward within an RL framework, following recent studies on RKL-based OPD
Xu
et al.
(
2025
); Lu and Lab (
2025
)
.
Let
ρ
​
(
y
)
=
π
θ
​
(
y
|
x
)
π
T
​
(
y
|
x
)
\rho(y)=\frac{\pi_{\theta}(y|x)}{\pi_{T}(y|x)}
denote the density ratio. The intrinsic reward
−
log
⁡
ρ
​
(
y
)
-\log\rho(y)
decreases monotonically with
ρ
​
(
y
)
\rho(y)
. Since trajectories
y
y
are sampled from the student policy
π
θ
(
⋅
|
x
)
\pi_{\theta}(\cdot|x)
, they are concentrated in regions where the student already assigns high probability. Consequently, the optimization dynamics mainly fall into two regimes:
1
1
1
Because sampling is performed from
π
θ
\pi_{\theta}
, trajectories with
π
θ
​
(
y
|
x
)
≪
π
T
​
(
y
|
x
)
\pi_{\theta}(y|x)\ll\pi_{T}(y|x)
(i.e.,
ρ
​
(
y
)
≪
1
\rho(y)\ll 1
) are rarely observed in practice. As a result, the student seldom receives strong positive rewards for trajectories favored by the teacher but not yet covered by the student policy.
:
•
ρ
​
(
y
)
≈
1
\rho(y)\approx 1
(
Consensus
): The generated trajectories lie within the teacher’s high-probability support. In this case, the density ratio is close to one, leading to a near-neutral intrinsic reward (
−
log
⁡
ρ
​
(
y
)
≈
0
-\log\rho(y)\approx 0
).
•
ρ
​
(
y
)
≫
1
\rho(y)\gg 1
(
Rejection
): The student assigns high probability to trajectories that receive low probability under the teacher policy. This produces a large density ratio and a strong negative reward (
−
log
⁡
ρ
​
(
y
)
≪
0
-\log\rho(y)\ll 0
).
In the Consensus regime, successful rollouts are naturally reinforced by the RL algorithm. However, in the Rejection regime, the teacher functions merely as a punitive critic, providing only negative scalar feedback without guidance toward better actions. As a result, the student must explore the large action space through inefficient trial-and-error, which often leads to optimization stagnation. As illustrated in Figure
1
(a), the lack of directional correction makes escaping the low-reward region computationally intractable.
Beyond the lack of directional guidance, RKL-based objectives also exhibit asymmetry in reward scaling. While the density ratio
ρ
​
(
y
)
\rho(y)
becomes unbounded from above when
π
T
​
(
y
|
x
)
→
0
\pi_{T}(y|x)\to 0
, it is lower-bounded by the student’s own probability
π
θ
​
(
y
|
x
)
\pi_{\theta}(y|x)
.
Because trajectories are sampled from the student policy, the ratio rarely falls far below 1.
As a result, negative penalties can dominate positive rewards by a large margin.
This imbalance allows a single “bad" sample to produce gradients that overwhelm the accumulated positive signals from “good" samples, leading to unstable optimization. We provide a detailed analysis in Appendix
A
.
2.3
Empirical Validation
Based on our analysis, we conjecture that training stability and performance degrade when the student frequently generates trajectories with high density ratios (
ρ
​
(
y
)
≫
1
\rho(y)\gg 1
). To validate this hypothesis, we train a
Qwen2.5-Math-1.5B
student under two configurations that induce different levels of teacher–student distributional shift
2
2
2
Detailed experimental settings and hyperparameters are provided in Appendix
B.1
.
:
•
In-Family Distillation:
We use
Qwen2.5-Math-7B
as the teacher. Since the teacher and student belong to the same model family and share similar training distributions, the resulting distribution mismatch is relatively small.
•
Cross-Family Distillation:
We use
Qwen3-30B-A3B
as the teacher.
3
3
3
We use the reasoning-oriented “thinking” MoE model as a proxy for a strong general-purpose model that differs substantially from the specialized math student.
Compared to the student, this teacher exhibits different reasoning behaviors and output distributions, leading to a larger distribution mismatch.
Result.
Figure
2
shows the training dynamics under the two settings. Although training uses only the intrinsic RKL reward, we report the average task reward on the training set to evaluate outcome correctness. The two settings exhibit markedly different behaviors. In the In-Family setting, the student converges steadily and achieves consistent improvements in task accuracy, indicating that RKL provides stable supervision when
π
θ
\pi_{\theta}
and
π
T
\pi_{T}
are initially well aligned.
In contrast, training in the Cross-Family setting becomes highly unstable. Consistent with our analysis of the “Rejection” regime, we observe three failure modes: (1)
Performance Collapse
, where task rewards fail to improve consistently; (2)
Exploding Gradients
, where persistently large gradient norms suggest that unbounded penalties destabilize optimization; and (3)
Distributional Divergence
, where the student rapidly deviates from its initial distribution (e.g., pathological response length drift) after only
∼
\sim
100 training steps. When combined with GRPO, these instabilities can further increase the likelihood of groups dominated by low-reward samples.
Figure 3:
Overview of the TGPO. The Policy Model generates a group of rollouts
{
y
i
}
i
=
1
g
\{y_{i}\}_{i=1}^{g}
conditioned on input
x
x
. At each step, the Teacher Model provides dynamic token-level guidance by predicting the optimal target token
y
T
y^{T}
based on the student’s current prefix. This dense guidance signal (
J
J
) complements the outcome-based advantage (
A
A
) derived from the Rule-based Verifier to update the policy.
