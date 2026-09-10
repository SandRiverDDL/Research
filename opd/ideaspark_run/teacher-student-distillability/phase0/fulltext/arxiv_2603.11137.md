# Scaling Reasoning Efficiently via Relaxed On-Policy Distillation

paper_id: arxiv:2603.11137
tier: U
source_used: html_arxiv
warning: none

## Intro

Figure 2
:
Illustration of
Reopold
.
While standard on-policy distillation (a) often introduces instability and inefficiency by forcing the student to mimic the teacher excessively, our proposed
Reopold
(b) fosters a more stable and effective learning environment. By establishing a formal connection between distillation and RL via a stop-gradient operation (Section
3.1
),
Reopold
utilizes teacher signals temperately (Section
4.1
) and selectively (Section
4.2
). As depicted, this approach filters out potentially harmful signals, preventing the student from deviating excessively from its original distribution.
Large language models (LLMs) have achieved remarkable reasoning capabilities through reinforcement learning (RL) post-training and test-time scaling, exemplified by OpenAI’s o1/o3
(Jaech
et al.
,
2024
)
and DeepSeek-R1
(Guo
et al.
,
2025
)
. However, replicating this success in small language models (SLMs) proves difficult. Due to limited representational capacity, SLMs struggle with direct reward optimization, rendering standard RL approaches ineffective
(Guo
et al.
,
2025
; Dang and Ngo,
2025
; Yan
et al.
,
2025
)
. This disparity necessitates alternative mechanisms specifically tailored for transferring reasoning abilities to capacity-constrained models.
To address this, recent work
(Yang
et al.
,
2025
;
patiño2025unlocking
)
adopts on-policy distillation, where the student learns from its own trajectories under the guidance of a high-capacity teacher, with superior reasoning capabilities. Unlike direct RL on sparse or high-variance rewards, this approach reduces optimization difficulty by constraining learning to regions aligned with the teacher’s behavior. Empirically, on-policy distillation has proven superior to RL algorithms and supervised fine-tuning (SFT) for reasoning tasks
(Lu and others,
2025
; Xiao
et al.
,
2026
)
, offering a robust pathway for capability transfer.
Despite its recent popularity, on-policy distillation lacks the methodological depth seen in modern RL. While RL for reasoning has rapidly evolved through specialized optimizers like GRPO
(Shao
et al.
,
2024
)
and mechanistic studies
(Shao
et al.
,
2025
; Wang
et al.
,
2025a
)
, distillation lacks comparable reasoning-centric advancements, despite efforts in standard instruction tuning
(Gu
et al.
,
2024
; Ko
et al.
,
2025a
)
. This imbalance suggests that on-policy distillation has yet to benefit from the advanced optimization techniques that have propelled RL forward, presenting a significant opportunity for refinement.
Empirically, vanilla on-policy distillation suffers from instability
(Gudibande
et al.
,
2023
; Gu
et al.
,
2024
)
. We observe that it frequently leads to negative transfer, where the student degrade compared to its initialization base model (Section
5.1
and
Figure 7
), and suffers from rapid entropy collapse which leads to premature convergence (Section
3.2
and
Figure 5
). Notably, similar limitations are echoed in recent literature
(Lu and others,
2025
)
, which restricts teachers to matching sizes to ensure stability (
e.g.,
using an 8B teacher for an 8B student instead of 32B). Such constraints fundamentally limit the practical utility of current distillation.
Contributions.
We analyze on-policy distillation through the lens of RL to diagnose optimization instabilities. By interpreting the teacher–student log-likelihood ratio as a fixed reward, we cast distillation as policy optimization, leveraging modern RL insights to stabilize training. Our contributions are summarized as follows:
•
Diagnosing on-policy distillation:
We demonstrate that stop-gradient renders the objective equivalent to standard policy gradient, acting as a control variate to mitigate variance and establish a robust baseline. Crucially, this allows us to diagnose bottlenecks, identifying heavy-tailed negative rewards and signal inefficiencies as the primary causes of instability.
•
Distillation-aware policy optimization:
Addressing the optimization bottlenecks identified in our analysis, we propose
Reopold
, which filters out harmful distillation signals and softens aggressive updates by temperately and selectively applying learning signals from the teacher (
Figure 2
). This method formulates a unified framework integrating reward clipping, token-level dynamic sampling, and multi-stage training. By explicitly regulating the learning signal,
Reopold
stabilizes the optimization where vanilla methods fail.
•
State-of-the-art efficiency and scalability:
Empirically,
Reopold
achieves superior training sample efficiency and unlocks test-time scaling for SLMs (
Figure 1
). It establishes state-of-the-art performance across mathematical, visual, and tool-use reasoning tasks, significantly outperforming standard baselines.
Figure 3
:
Comparison of training dynamics between vanilla RKL and RKL with stop-gradient.
(a) Training loss dynamics exhibit similar trends, aligning with the theoretical equivalence in Remark
3.1
. (b) The gradient norm is markedly lower and more stable when stop-gradient is applied, which (c) leads to superior validation performance. This confirms that treating the log-likelihood ratio as a fixed reward signal is beneficial for optimization stability.

## Method

3.1
Theoretical Equivalence to RL and Strong Baseline
Here, we provide the theoretical foundation of our approach by establishing the relationship between on-policy distillation and RL. Following the recent success of
(Lu and others,
2025
;
patiño2025unlocking
)
, we formulate the on-policy distillation objective by combining Eq. (
1
) and Eq. (
2
):
𝒥
RKL
​
(
θ
)
=
𝔼
q
∼
𝒬
,
{
o
i
}
i
=
1
G
∼
π
θ
old
(
⋅
∣
q
)
[
1
∑
i
=
1
G
|
o
i
|
​
∑
i
=
1
G
∑
t
=
1
|
o
i
|
ρ
i
,
t
​
(
θ
)
​
R
i
,
t
​
(
θ
)
]
,
\begin{split}\mathcal{J}_{\text{RKL}}(\theta)=&\mathbb{E}_{q\sim\mathcal{Q},\,\{o_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid q)}\\
&\left[\frac{1}{\sum_{i=1}^{G}|o_{i}|}\sum_{i=1}^{G}\sum_{t=1}^{|o_{i}|}\rho_{i,t}(\theta)R_{i,t}(\theta)\right],\end{split}
(3)
where
R
i
,
t
​
(
θ
)
=
log
⁡
π
T
​
(
o
i
,
t
|
q
,
o
i
,
<
t
)
π
θ
​
(
o
i
,
t
|
q
,
o
i
,
<
t
)
R_{i,t}(\theta)=\log\frac{\pi_{T}(o_{i,t}|q,o_{i,<t})}{\pi_{\theta}(o_{i,t}|q,o_{i,<t})}
represents the token-level log-likelihood ratio. Unlike conventional distillation, which computes discrepancies over the full vocabulary
(Agarwal
et al.
,
2024
; Ko
et al.
,
2024
)
, this approach operates on sampled tokens, avoiding the prohibitive memory cost of storing full distributions as shown in Appendix
D
.
Unlike standard RL where rewards are fixed, the term
R
i
,
t
​
(
θ
)
R_{i,t}(\theta)
itself depends on
θ
\theta
. While prior works such as MiniLLM
(Gu
et al.
,
2024
)
have explored this connection, we explicitly adopt a
fixed reward
perspective to stabilize optimization. Specifically, we employ a stop-gradient operator to teat
R
i
,
t
​
(
θ
)
R_{i,t}(\theta)
as a constant extrinsic signal. Let
𝒥
RKL
(sg)
\mathcal{J}_{\text{RKL}}^{\text{(sg)}}
denote this stop-gradient objective. Then, the following property holds:
Remark 3.1
.
Under standard regularity conditions, the expected gradients of
𝒥
RKL
​
(
θ
)
\mathcal{J}_{\text{RKL}}(\theta)
and
𝒥
RKL
(sg)
\mathcal{J}_{\text{RKL}}^{\text{(sg)}}
coincide:
∇
θ
𝒥
RKL
​
(
θ
)
=
∇
θ
𝒥
RKL
(sg)
​
(
θ
)
=
𝔼
q
∼
𝒬
,
{
o
i
}
i
=
1
G
∼
π
θ
old
(
⋅
|
q
)
[
1
∑
i
=
1
G
|
o
i
|
​
∑
i
=
1
G
∑
t
=
1
|
o
i
|
ρ
i
,
t
​
(
θ
)
​
R
i
,
t
​
(
θ
)
​
∇
log
⁡
π
θ
​
(
o
t
|
q
,
o
<
t
)
]
,
\begin{split}\nabla_{\theta}&\mathcal{J}_{\text{RKL}}(\theta)=\nabla_{\theta}\mathcal{J}_{\text{RKL}}^{\text{(sg)}}(\theta)=\mathbb{E}_{q\sim\mathcal{Q},\{o_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot|q)}\\
&\left[\frac{1}{\sum_{i=1}^{G}|o_{i}|}\sum_{i=1}^{G}\sum_{t=1}^{|o_{i}|}\rho_{i,t}(\theta)R_{i,t}(\theta)\nabla\log\pi_{\theta}(o_{t}|q,o_{<t})\right],\end{split}
A full proof is provided in Appendix
A.1
, showing that the gradient contribution from the reward term vanishes in expectation. This establishes that on-policy distillation is formally equivalent to an on-policy policy-gradient method where the reward is defined by
R
i
,
t
​
(
θ
)
R_{i,t}(\theta)
.
While Remark
3.1
ensures theoretical consistency in expectation, the dynamics differ in the finite-sample regime of stochastic optimization. Crucially, the omitted term
∇
θ
R
i
,
t
​
(
θ
)
\nabla_{\theta}R_{i,t}(\theta)
has zero expectation but non-zero variance. By removing this term, the stop-gradient operator effectively acts as a control variate, suppressing high-variance noise in the gradient estimates. Empirically, we observe that this leads to reduced gradient norms implying variance reduction
(Greensmith
et al.
,
2004
; Tucker
et al.
,
2018
)
and results in stable training dynamics, leading to better validation performance as shown in
Figure 3
(and
subsection 5.2
).
Figure 4
:
Log-scale histogram of token-level log-likelihood ratio rewards.
The
red dashed ellipse
indicates degenerate near-zero rewards, while the
purple dashed region
highlights the heavy tail of negative rewards. These distributions pose challenges for RL-based on-policy distillation by causing gradient vanishing and training instability, respectively.
3.2
Optimization Challenges in On-policy Distillation
While the stop-gradient formulation establishes a strong baseline by stabilizing training dynamics, we identify that on-policy distillation still inherits fundamental challenges characteristic of RL. By viewing distillation through the lens of policy gradients, we isolate three critical issues impeding performance:
Instability from heavy-tailed negative rewards.
We observe a severe misalignment issue when the student policy samples tokens to which the teacher assigns negligible probability (i.e.,
π
T
​
(
o
t
|
q
,
o
<
t
)
→
0
\pi_{T}(o_{t}|q,o_{<t})\rightarrow 0
). As shown in
Figure 4
, this causes log-likelihood ratios to approach
−
∞
-\infty
, creating a heavy-tailed distribution of negative rewards. These extreme values dominate the gradient estimation, resulting in optimization instability. Consequently, destructive parameter updates suppress specific tokens, causing the model to deviate significantly from its original distribution (
subsection 4.3
,
subsection 5.1
).
Inefficiency from near-zero rewards.
For the majority of tokens, the student and teacher distributions are well-aligned, yielding log-likelihood ratios near zero (see
Figure 4
). From an RL perspective, these vanishing advantages provide negligible learning signals while consuming batch memory and computation. This signal dilution reduces the effective sample size and degrades sample efficiency. Unlike standard RL, which allows for prompt-level filtering
(Yu
et al.
,
2025
)
, on-policy distillation operates at the token level, rendering such coarse-grained strategies ineffective.
Entropy-collapse and exploration-alignment trade-off.
Effective reasoning requires exploration of diverse solution paths. We observe that the policy’s entropy decreases rapidly during training (see
Figure 6
), leading to premature convergence on a narrow set of outputs. While increasing sampling temperature is a standard RL remedy for exploration, we find it detrimental here: higher temperatures introduce tokens that diverge further from the teacher’s distribution, exacerbating the reward variance described above. This results in a challenging trade-off between maintaining exploration and ensuring student-teacher alignment.
