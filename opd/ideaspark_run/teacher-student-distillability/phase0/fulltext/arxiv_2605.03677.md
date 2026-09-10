# Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe

paper_id: arxiv:2605.03677
tier: U
source_used: html_arxiv
warning: none

## Intro

Injecting complex reasoning abilities, domain knowledge, and human preferences into LLMs and MLLMs remains a core challenge in the post-training stage.
Conventional approaches typically follow a two-stage paradigm: supervised fine-tuning (SFT) first, followed by reinforcement learning (RL)
(Guo
et al.
,
2025a
; Xu
et al.
,
2025a
; Zeng
et al.
,
2026
; Zhao
et al.
,
2026a
)
.
While SFT leverages expert data for training, its inherently off-policy nature introduces substantial exposure bias
(Qin
et al.
,
2025
; Song and Zheng,
2026
)
.
Entering rarely covered erroneous states during inference may lead to compounding errors.
Alternatively, on-policy RL (
e.g.,
GRPO
(Shao
et al.
,
2024b
)
) alleviates distribution shift through online sampling.
However, it mainly relies on sequence-level or terminal rewards, making fine-grained credit assignment difficult and limiting the stability of long-term training
(Team
et al.
,
2026
)
.
Recently, on-policy distillation (OPD) has emerged as a promising post-training paradigm for efficiently transferring the knowledge and capabilities of domain experts into a single, unified model.
It combines the strengths of RL and SFT, namely on-policy sampling and token-level supervision. Concretely, OPD trains the student on its own sampled trajectories with teacher feedback under a reverse KL objective
(Lu and Lab,
2025
; Xu
et al.
,
2026a
)
.
Despite its empirical success, current OPD research remains largely confined to LLM distillation
(Zhou
et al.
,
2025
; Yang
et al.
,
2026b
; Xiao
et al.
,
2026
; Yang
et al.
,
2026c
; Wu
et al.
,
2026
)
.
Although a few recent works extend OPD to MLLMs, they are restricted to limited subsets of tasks within a single modality, such as video
(Li
et al.
,
2026a
)
or speech
(Cao
et al.
,
2026
)
.
To this end, we first aim to develop a unified OPD framework for both LLMs and MLLMs, enabling effective knowledge distillation across tasks and modalities.
Key observations.
Beyond unifying the framework, we raise a more fundamental question:
what makes OPD a reliable optimization paradigm?
We posit that effective OPD depends on two factors.
First
, the student must sufficiently explore informative states,
i.e.,
diverse and appropriately difficult self-generated trajectories.
Second
, the teacher’s token-level supervision must remain reliable when applied to student rollouts.
In particular, the reliability of token-level guidance is significantly enhanced when its trajectory-level aggregation remains order-consistent with outcome reward (
i.e.,
correct trajectories receive higher aggregated scores than incorrect ones).
The outcome reward thus provides a global anchor for calibrating unreliable teacher supervision.
These observations motivate a dual-perspective optimization strategy that jointly improves student exploration and the reliability of teacher signals.
Our recipe.
Building on these insights, we introduce
Uni-OPD
, a dual-perspective strategy for optimizing OPD from the fundamental roles of the student and the teacher.
In this unified framework, we adopt two complementary data-balancing strategies, namely offline difficulty-aware and online correctness-aware balancing, to promote exploration of informative student-generated states. We further present a novel outcome-guided margin calibration mechanism to obtain reliable teacher supervision. Extensive experiments on LLMs and MLLMs verify our recipe.
To summarize, our contributions are threefold:
∙
\bullet
Key bottlenecks of OPD.
We identify two core bottlenecks in OPD: insufficient exploration of informative states and unreliable teacher supervision for student rollouts. Our analysis reveals that reliable teacher supervision largely depends on whether token-level guidance remains order-consistent with the outcome reward.
∙
\bullet
Dual-perspective optimization recipe.
We present a dual-perspective optimization recipe for unified OPD that jointly improves student exploration and teacher supervision. Concretely, we combine offline and online data balancing with an outcome-guided margin calibration mechanism, leading to more effective optimization.
∙
\bullet
Comprehensive experimental validation.
We conduct extensive experiments on 5 domains and 16 benchmarks covering diverse settings, including single-teacher and multi-teacher distillation across LLMs and MLLMs, strong-to-weak distillation, and cross-modal distillation (
i.e.,
combining text-only and multimodal tasks). Our results verify the effectiveness and versatility of
Uni-OPD
and provide practical insights into reliable OPD.

## Method

Figure 2:
Overview of the
Uni-OPD
framework.
(
Left
) Offline difficulty-aware and online correctness-aware data balancing promote student exploration.
(
Right
) Outcome-guided margin calibration mechanism improves the reliability of teacher supervision.
(
Middle
) The resulting student policy merges complementary capabilities from multiple domain-specific teachers more effectively than standard OPD, leading to stronger overall performance.
We propose
Uni-OPD
, a unified framework that advances OPD across LLMs and MLLMs, as shown in
Fig.
2
.
Our design is driven by two fundamental bottlenecks in OPD:
insufficient exploration of informative student-generated states
and
unreliable teacher supervision for student rollouts
.
Uni-OPD
addresses them with a dual-perspective recipe that enhances student exploration and calibrates teacher supervision to align with the outcome reward.
We first introduce the preliminaries in
section
3.1
, followed by an overview of
Uni-OPD
in
section
3.2
.
We then detail the exploration strategy in
section
3.3
and the supervision calibration mechanism in
section
3.4
.
3.1
Preliminaries
On-policy distillation.
OPD retains the
on-policy
nature of optimization while providing
token-level credit assignment
, enabling effective post-training.
During training, the student policy
π
𝜽
\pi_{{\bm{\theta}}}
samples its trajectories and is optimized by minimizing the reverse Kullback-Leibler (KL) divergence to the teacher policy
π
T
\pi_{\mathrm{T}}
over these samples:
𝒥
OPD
(
𝜽
)
=
min
𝜽
𝔼
𝒒
∼
D
,
𝝉
∼
π
𝜽
(
⋅
∣
𝒒
)
[
𝒟
KL
(
π
𝜽
(
𝝉
∣
𝒒
)
∥
π
T
(
𝝉
∣
𝒒
)
)
]
,
\mathcal{J}_{\text{OPD}}(\bm{\theta})=\min_{\bm{\theta}}\mathbb{E}_{\bm{q}\sim D,\,\bm{\tau}\sim{\pi}_{\bm{\theta}}(\cdot\mid\bm{q})}\!\Big[\mathcal{D}_{\mathrm{KL}}\!\Big({\pi}_{\bm{\theta}}(\bm{\tau}\!\mid\!\bm{q})\,\big\|\,\pi_{\text{T}}(\bm{\tau}\!\mid\!\bm{q})\Big)\Big],
(1)
where
𝒒
{\bm{q}}
is the input question,
𝝉
=
(
o
1
,
…
,
o
|
𝝉
|
)
\bm{\tau}=(o_{1},\dots,o_{|\bm{\tau}|})
is a trajectory sampled by the student,
o
t
o_{t}
is the token at decoding step
t
t
, and
|
𝝉
|
|\bm{\tau}|
is the length of the trajectory. The gradient of OPD can be derived as:
∇
𝜽
𝒥
OPD
​
(
𝜽
)
=
𝔼
𝒒
∼
D
,
𝝉
∼
π
𝜽
(
⋅
∣
𝒒
)
​
[
∑
t
=
1
|
𝝉
|
(
log
⁡
π
𝜽
​
(
o
t
∣
𝒒
,
𝒐
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
o
t
∣
𝒒
,
𝒐
<
t
)
)
​
∇
𝜽
log
⁡
π
𝜽
​
(
o
t
∣
𝒒
,
𝒐
<
t
)
]
,
\nabla_{\bm{\theta}}\mathcal{J}_{\text{OPD}}(\bm{\theta})=\mathbb{E}_{\bm{q}\sim D,\,\bm{\tau}\sim{\pi}_{\bm{\theta}}(\cdot\mid\bm{q})}\!\Big[\sum_{t=1}^{|\bm{\tau}|}\!\big(\log{\pi}_{\bm{\theta}}(o_{t}\mid\bm{q},\bm{o}_{<t})-\log\pi_{\text{T}}(o_{t}\mid\bm{q},\bm{o}_{<t})\big)\,\nabla_{\bm{\theta}}\log{\pi}_{\bm{\theta}}(o_{t}\mid\bm{q},\bm{o}_{<t})\Big],
(2)
where
𝒐
<
t
{\bm{o}}_{<t}
denotes the prefix before step
t
t
. The gradient naturally induces a token-level reward at step
t
t
, analogous to standard RL:
r
t
OPD
=
log
⁡
π
T
​
(
o
t
∣
𝒒
,
𝒐
<
t
)
−
log
⁡
π
𝜽
​
(
o
t
∣
𝒒
,
𝒐
<
t
)
=
log
⁡
π
T
​
(
o
t
∣
𝒒
,
𝒐
<
t
)
π
𝜽
​
(
o
t
∣
𝒒
,
𝒐
<
t
)
.
r^{\mathrm{OPD}}_{t}=\log\pi_{\text{T}}(o_{t}\mid\bm{q},\bm{o}_{<t})-\log{\pi}_{\bm{\theta}}(o_{t}\mid\bm{q},\bm{o}_{<t})=\log\frac{\pi_{\text{T}}(o_{t}\mid\bm{q},\bm{o}_{<t})}{{\pi}_{\bm{\theta}}(o_{t}\mid\bm{q},\bm{o}_{<t})}.
(3)
This formulation provides fine-grained credit assignment signals at the token level.
Analyzing teacher supervision in OPD.
As shown in
Eq.
3
, OPD relies on the teacher to provide fine-grained supervision for student-generated trajectories.
For effective optimization, this signal should align with overall trajectory correctness.
In practice, this alignment is not guaranteed and can fail in several typical ways:
(a) OOD degradation
: when student rollouts enter sparse or out-of-distribution regions relative to the teacher,
log
⁡
π
T
​
(
o
t
∣
⋅
)
\log\pi_{\mathrm{T}}(o_{t}\mid\cdot)
may become noisy, disrupting the ranking between correct and incorrect trajectories.
(b) Overestimation of incorrect trajectories
: incorrect trajectories may receive abnormally high scores when their local token patterns align with the teacher’s high-confidence regions.
(c) Underestimation of correct trajectories
: correct trajectories may receive abnormally low scores when their generation paths deviate from the teacher’s dominant regions, thereby suppressing useful reasoning paths.
These phenomena suggest that teacher supervision is not always reliable, motivating us to introduce an outcome reward as a global anchor for calibrating trajectory-level supervision.
3.2
The Overview of Uni-OPD
In this work, we propose
Uni-OPD
, a unified OPD framework that generalizes across both LLMs and MLLMs, as illustrated in
Fig.
2
.
Formally, given
M
M
expert teachers
{
π
T
1
,
π
T
2
,
…
,
π
T
M
}
\{\pi_{\mathrm{T}_{1}},\pi_{\mathrm{T}_{2}},\dots,\pi_{\mathrm{T}_{M}}\}
who specialize in different domains, and letting
w
i
w_{i}
denote the weight assigned to teacher
π
T
i
\pi_{\mathrm{T}_{i}}
, we define the objective as:
𝒥
Uni-OPD
​
(
𝜽
)
=
∑
i
=
1
M
w
i
​
𝒟
KL
​
(
π
𝜽
∥
π
T
i
)
,
\mathcal{J}_{\text{Uni-OPD}}(\bm{\theta})=\sum_{i=1}^{M}w_{i}\,\mathcal{D}_{\mathrm{KL}}\!\left({\pi}_{\bm{\theta}}\,\|\,\pi_{\mathrm{T}_{i}}\right),
(4)
This formulation provides a unified objective for both single-teacher and multi-teacher distillation by aggregating supervision from multiple experts.
Building on this objective, we optimize OPD from the two fundamental roles.
From the student’s perspective, we introduce a data-balancing strategy that promotes exploration via offline difficulty-aware and online correctness-aware selection.
From the teacher’s perspective, we develop an outcome-guided margin calibration mechanism to correct unreliable token-level supervision by enforcing consistency with outcome rewards.
These designs stabilize optimization and improve the reliability of OPD.
3.3
Joint Offline and Online Data Balancing Strategy for Student Exploration
From the student’s perspective, sufficient diversity and an appropriate level of difficulty in the generated trajectories are essential for effective OPD.
To this end, based on our empirical study, we propose complementary data-balancing strategies for both offline data construction and online sampling.
Figure 3:
Data difficulty distribution and its impact on OPD performance.
(
Left
) Training data often exhibits mirrored J-shaped or U-shaped difficulty distributions.
(
Right
) A naive strategy is to filter out overly easy or overly hard samples (
i.e.,
all-correct or all-wrong cases), but this reduces diversity.
In contrast, our difficulty-balancing strategy upsamples mid-difficulty samples to preserve a balanced spectrum and empirically outperforms filtering.
Offline difficulty-aware data balancing.
A prevalent practice in RL is to estimate prompt difficulty via multiple rollouts and then filter out samples that are either overly easy (
i.e.,
always correct) or overly hard (
i.e.,
always incorrect)
(An
et al.
,
2025
; Zhou
et al.
,
2023a
)
.
However, for small-scale models, training data often exhibits a mirrored J-shaped or U-shaped distribution (see
Fig.
3
).
Strictly removing these easy or hard samples can substantially reduce data diversity and limit exploration of informative student-generated states.
Our empirical findings show that such filtering leads to substantial performance degradation in OPD.
Based on this observation, we adopt a difficulty-aware balancing strategy that selectively upsamples mid-difficulty samples (
i.e.,
correct in only some of multiple rollouts).
As shown in
Fig.
3
, this strategy reshapes the data distribution into a more uniform form while preserving both diversity and difficulty.
In addition, it consistently improves performance on math reasoning and code generation.
Overall, these results show that maintaining data diversity and a balanced difficulty spectrum enables the student to generate more informative trajectories, thereby exploring a broader solution space.
Figure 4:
Impact of online correct and incorrect ratio on student final performance.
Online correctness-aware data balancing.
After applying offline difficulty-aware balancing, we further observe that insufficient exploration can cause the model to collapse to local optima during training, especially when rollout groups lack sufficient outcome diversity (
e.g.,
only incorrect trajectories).
To mitigate this issue, we explicitly enforce a balanced composition of correct and incorrect trajectories within each rollout group during training.
This prevents degenerate cases in which all samples share the same outcome and thus yield uninformative gradients.
By maintaining such a balance, we ensure that the student consistently receives meaningful contrastive signals for stable on-policy learning.
As shown in
Fig.
4
, an appropriate outcome balance achieves better performance than using only correct samples or an excessively high correct/incorrect ratio.
3.4
Outcome-guided Margin Calibration for Teacher Supervision
A basic premise of OPD is that the teacher exhibits a directional likelihood preference over positive and negative trajectories. In particular, relative to the student, the teacher should assign higher likelihood to correct trajectories and lower likelihood to incorrect ones. Under this premise, the resulting distillation signal should remain consistent with outcome-level correctness at the trajectory level. We next formalize this principle through a trajectory-level distillation return and develop an outcome-guided calibration strategy based on it.
Figure 5:
Demonstration of unreliable teacher supervision and outcome-guided margin calibration mechanism.
(
Left
) Standard teacher supervision in OPD suffers from misalignment between trajectory-level return and outcome rewards, yielding unreliable supervision signals.
(
Right
) Our method uses outcome rewards as a global anchor to calibrate returns through margin-based adjustment, restoring order consistency and improving optimization stability.
Trajectory-level distillation return.
To characterize the overall supervision signal along a rollout trajectory, we define the
trajectory-level distillation return
as the average log-probability gap between the teacher and the student:
G
OPD
​
(
𝒒
,
𝝉
)
≜
1
|
𝝉
|
​
∑
t
=
1
|
𝝉
|
log
⁡
π
T
​
(
o
t
∣
𝒒
,
𝒐
<
t
)
π
𝜽
​
(
o
t
∣
𝒒
,
𝒐
<
t
)
=
1
|
𝝉
|
​
∑
t
=
1
|
𝝉
|
r
t
OPD
,
G_{\mathrm{OPD}}(\bm{q},\bm{\tau})\triangleq\frac{1}{|\bm{\tau}|}\sum_{t=1}^{|\bm{\tau}|}\log\frac{\pi_{\mathrm{T}}(o_{t}\mid\bm{q},\bm{o}_{<t})}{\pi_{\bm{\theta}}(o_{t}\mid\bm{q},\bm{o}_{<t})}=\frac{1}{|\bm{\tau}|}\sum_{t=1}^{|\bm{\tau}|}r^{\mathrm{OPD}}_{t}\,,
(5)
This quantity measures the teacher’s
average log-likelihood preference
over the student along trajectory
𝝉
\bm{\tau}
. When
G
OPD
​
(
𝒒
,
𝝉
)
>
0
G_{\mathrm{OPD}}({\bm{q}},\bm{\tau})>0
, the teacher assigns higher confidence than the student on average, encouraging the student to move toward this trajectory. Conversely, when
G
OPD
​
(
𝒒
,
𝝉
)
<
0
G_{\mathrm{OPD}}({\bm{q}},\bm{\tau})<0
, the student is discouraged from moving toward this trajectory. The normalization by trajectory length ensures comparability across trajectories of different lengths.
Order consistency as a trajectory-level criterion.
For a given question
𝒒
{\bm{q}}
, let
R
​
(
𝒒
,
𝝉
)
∈
{
0
,
1
}
R({\bm{q}},\bm{\tau})\in\{0,1\}
denote the outcome reward of a sampled trajectory
𝝉
\bm{\tau}
, where
R
​
(
𝒒
,
𝝉
)
=
1
R({\bm{q}},\bm{\tau})=1
indicates that the final answer in
𝝉
\bm{\tau}
is correct for question
𝒒
{\bm{q}}
, and
R
​
(
𝒒
,
𝝉
)
=
0
R({\bm{q}},\bm{\tau})=0
otherwise. We then define the positive and negative trajectory sets as:
S
+
​
(
𝒒
)
≜
{
𝝉
∣
R
​
(
𝒒
,
𝝉
)
=
1
}
,
\displaystyle S_{+}({\bm{q}})\triangleq\{\bm{\tau}\mid R({\bm{q}},\bm{\tau})=1\},\qquad
S
−
​
(
𝒒
)
≜
{
𝝉
∣
R
​
(
𝒒
,
𝝉
)
=
0
}
.
\displaystyle S_{-}({\bm{q}})\triangleq\{\bm{\tau}\mid R({\bm{q}},\bm{\tau})=0\}.
(6)
Following the trajectory-level bandit formulation in
(Ouyang
et al.
,
2022
)
, we treat the prompt as the context and the entire generated trajectory as a macro-action. Under this view, the associated outcome reward naturally serves as a one-step trajectory-level return, denoted as
G
RL
​
(
𝒒
,
𝝉
)
=
R
​
(
𝒒
,
𝝉
)
G_{\mathrm{RL}}({\bm{q}},\bm{\tau})=R({\bm{q}},\bm{\tau})
. Therefore, the outcome-level RL return induces the following oracle ordering:
G
RL
​
(
𝒒
,
𝝉
+
)
≥
G
RL
​
(
𝒒
,
𝝉
−
)
,
\displaystyle G_{\mathrm{RL}}({\bm{q}},\bm{\tau}_{+})\geq G_{\mathrm{RL}}({\bm{q}},\bm{\tau}_{-})\,,\qquad
∀
𝝉
+
∈
S
+
​
(
𝒒
)
,
∀
𝝉
−
∈
S
−
​
(
𝒒
)
.
\displaystyle\forall\bm{\tau}_{+}\in S_{+}({\bm{q}}),\;\forall\bm{\tau}_{-}\in S_{-}({\bm{q}})\,.
(7)
The derivation process is provided in
section
B.1
. This motivates a trajectory-level reliability criterion for OPD. Under the distillation premise, the trajectory-level distillation return
G
OPD
​
(
𝒒
,
𝝉
)
G_{\mathrm{OPD}}({\bm{q}},\bm{\tau})
should preserve the same outcome-induced ordering as
G
RL
​
(
𝒒
,
𝝉
)
G_{\mathrm{RL}}({\bm{q}},\bm{\tau})
. Specifically, for any prompt
𝒒
{\bm{q}}
, we expect:
G
OPD
​
(
𝒒
,
𝝉
+
)
≥
G
OPD
​
(
𝒒
,
𝝉
−
)
,
\displaystyle G_{\mathrm{OPD}}({\bm{q}},\bm{\tau}_{+})\geq G_{\mathrm{OPD}}({\bm{q}},\bm{\tau}_{-})\,,\qquad
∀
𝝉
+
∈
S
+
​
(
𝒒
)
,
∀
𝝉
−
∈
S
−
​
(
𝒒
)
.
\displaystyle\forall\bm{\tau}_{+}\in S_{+}({\bm{q}}),\;\forall\bm{\tau}_{-}\in S_{-}({\bm{q}})\,.
(8)
Teacher supervision may violate ordering.
In practice, however, the teacher’s supervision is not always reliable. As discussed in
section
3.1
, teacher scoring may degrade in sparse out-of-distribution regions, overestimate incorrect trajectories, or underestimate correct ones due to spurious local patterns. Such failures may persist even after token-level supervision is aggregated to the trajectory level. A mean-based criterion is therefore insufficient, since the mismatch is often concentrated in a few extreme samples: a single overly confident negative trajectory or a severely underestimated positive trajectory can already distort the supervision signal for the entire prompt group.
Outcome-guided margin calibration.
Based on the above analysis, during OPD training, the constraint in
Eq.
8
should hold between positive and negative trajectories within each prompt. To this end, we consider the margin between the lowest-scoring correct trajectory and the highest-scoring incorrect trajectory, which directly characterizes whether the ordering is violated in the most adversarial case. We define the prompt-level margin as
m
​
(
𝒒
)
≜
min
𝝉
∈
S
+
​
(
𝒒
)
⁡
G
OPD
​
(
𝒒
,
𝝉
)
−
max
𝝉
∈
S
−
​
(
𝒒
)
⁡
G
OPD
​
(
𝒒
,
𝝉
)
.
m(\bm{q})\triangleq\min_{\bm{\tau}\in S_{+}(\bm{q})}\!G_{\mathrm{OPD}}(\bm{q},\bm{\tau})-\max_{\bm{\tau}\in S_{-}(\bm{q})}\!G_{\mathrm{OPD}}(\bm{q},\bm{\tau})\,.
(9)
By construction,
m
​
(
𝒒
)
≥
0
m({\bm{q}})\geq 0
indicates strict order consistency on prompt
𝒒
{\bm{q}}
, since even the worst positive trajectory still outperforms the best negative one (see Fig.
5
). Thus,
m
​
(
𝒒
)
≥
0
m({\bm{q}})\geq 0
means that all positive trajectories are ranked above all negative ones for prompt
𝒒
{\bm{q}}
. To improve robustness, we further require:
m
​
(
𝒒
)
≥
δ
,
m(\bm{q})\geq\delta\,,
(10)
where
δ
>
0
\delta>0
defines a safety margin against estimation noise and finite-sample fluctuations. Since
S
+
​
(
𝒒
)
S_{+}({\bm{q}})
and
S
−
​
(
𝒒
)
S_{-}({\bm{q}})
are determined by outcome rewards, this criterion uses the outcome signal as a global anchor to calibrate the teacher’s trajectory-level scores. This formulation enables direct interventions on the margin, allowing us to suppress ordering violations or enlarge the separation between positive and negative trajectories.
Margin calibration strategy.
Based on
Eq.
10
, we present two calibration strategies:
margin mask
and
margin shift
.
Specifically, the margin mask keeps only the prompt groups satisfying
m
​
(
𝒒
)
≥
δ
m({\bm{q}})\geq\delta
and discards the rest, so that training is performed only with reliable supervision.
Margin shift instead repairs an unreliable group with the smallest additive correction. For groups with
m
​
(
𝒒
)
<
δ
m({\bm{q}})<\delta
, we define:
λ
​
(
𝒒
)
=
δ
−
m
​
(
𝒒
)
,
G
~
OPD
​
(
𝒒
,
𝝉
)
=
G
OPD
​
(
𝒒
,
𝝉
)
+
λ
​
(
𝒒
)
​
1
​
{
R
​
(
𝒒
,
𝝉
)
=
1
}
.
\lambda({\bm{q}})=\delta-m({\bm{q}}),\qquad\widetilde{G}_{\mathrm{OPD}}({\bm{q}},\bm{\tau})=G_{\mathrm{OPD}}({\bm{q}},\bm{\tau})+\lambda({\bm{q}})\,\mathbf{1}\{R({\bm{q}},\bm{\tau})=1\}.
(11)
This shift preserves the relative ordering within
S
+
​
(
𝒒
)
S_{+}({\bm{q}})
and guarantees
min
𝝉
∈
S
+
​
(
𝒒
)
⁡
G
~
OPD
​
(
𝒒
,
𝝉
)
−
max
𝝉
∈
S
−
​
(
𝒒
)
⁡
G
~
OPD
​
(
𝒒
,
𝝉
)
=
δ
.
\min_{\bm{\tau}\in S_{+}({\bm{q}})}\widetilde{G}_{\mathrm{OPD}}({\bm{q}},\bm{\tau})-\max_{\bm{\tau}\in S_{-}({\bm{q}})}\widetilde{G}_{\mathrm{OPD}}({\bm{q}},\bm{\tau})=\delta\,.
(12)
In this way, margin shift restores outcome-consistent ordering with a minimal group-level correction, while margin mask provides a more conservative alternative when the supervision signal is too unreliable to calibrate.
Table 1:
Performance of
Qwen3-4B Student
under math reasoning and code generation benchmarks.
Teacher models (
i.e.,
Qwen3-4B-Math-RL
and
Qwen3-4B-Code-RL
) are developed through domain-specific RL. The performance of teacher models is denoted by the “RL” type.
Bold
values indicate the best score within each group.
Avg.
denotes the average score within each domain.
Method
Math Reasoning
Code Generation
AIME
2024
AIME
2025
HMMT
25 Feb.
HMMT
25 Nov.
Avg.
Human
Eval+
MBPP+
LCB
Avg.
Student (4B)
23.0
19.3
12.3
9.2
15.9
77.4
65.3
17.7
53.5
Teacher (RL)
60.1
55.1
32.5
38.5
46.6
85.2
69.8
26.6
60.5
Single–Teacher Distillation
ExPO
58.7
55.2
32.4
37.0
45.8
84.8
70.2
28.0
61.0
OPD
57.9
52.4
30.2
37.8
44.6
82.6
68.8
25.7
59.0
ExOPD
62.7
56.1
33.9
39.3
48.0
86.9
70.7
28.6
62.1
Uni-OPD
63.3
57.0
34.8
39.8
48.7
88.3
71.6
29.7
63.2
Multi–Teacher Distillation
SFT
58.5
53.3
30.7
34.8
44.3
86.4
69.6
26.4
60.8
ExPO
57.5
54.5
31.7
36.3
45.0
86.7
72.0
29.0
62.6
OPD
60.9
55.2
33.4
38.3
47.0
86.3
70.9
23.4
60.2
ExOPD
61.0
56.0
34.4
39.2
47.7
86.3
70.6
29.0
62.0
Uni-OPD
62.3
57.2
34.9
39.6
48.5
88.0
72.6
30.1
63.6
