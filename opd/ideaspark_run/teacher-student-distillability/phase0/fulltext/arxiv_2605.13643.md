# Prefix Teach, Suffix Fade: Local Teachability Collapse in Strong-to-Weak On-Policy Distillation

paper_id: arxiv:2605.13643
tier: U
source_used: html_arxiv
warning: none

## Intro

On-policy distillation (OPD) trains a student model on its own generated trajectories using feedback from a stronger teacher
Agarwal
et al.
(
2024
)
. This on-policy setting is advantageous because the teacher evaluates states the student actually visits, thereby mitigating the exposure bias associated with fixed offline teacher demonstrations. Recent work has improved OPD through reward extrapolation, entropy-aware objectives, support matching, and computationally efficient prefix-style supervision
(Yang
et al.
,
2026
; Jin
et al.
,
2026
; Fu
et al.
,
2026
; Zhang
et al.
,
2026
)
. However, a common assumption underlying dense OPD is that once teacher feedback is available for a rollout, applying supervision across the entire generated sequence is uniformly beneficial.
However, we contend that this assumption is overly coarse. While foundation model research typically emphasizes OPD between models of comparable scale, this paper focuses on
strong-to-weak OPD
. This paradigm is increasingly prevalent in on-device modeling and local deployments, where a highly capable teacher supervises a significantly smaller student. In this regime, the critical challenge is not merely whether a preference gap persists between the teacher and the student; rather, the teacher’s feedback must remain discriminative over the local region of the rollout being trained. This mirrors a fundamental principle in outcome-driven reinforcement learning (RL): updates are most effective when feedback clearly distinguishes between alternatives, such as the common heuristic of training on queries with a 50% rollout-accuracy
(Qu
et al.
,
2026
)
. Conversely, samples that are uniformly correct, uniformly incorrect, or otherwise low-contrast provide negligible learning signals
(Qu
et al.
,
2026
; Bae
et al.
,
2026
; Shu
et al.
,
2026
; Yu
et al.
,
2025
)
. Consequently, if strong-to-weak OPD applies dense supervision to segments where the teacher’s feedback has become nearly flat, it risks optimizing over low-informative noise without providing meaningful local prioritization for the student.
We term this failure mode
local teachability collapse
: a sustained decrease in the teacher’s local contrast over the course of a student rollout. In this paper, we first diagnose this phenomenon within a standard strong-to-weak distillation framework from prior work
(Yang
et al.
,
2026
)
, where the capability gap is sufficiently large to expose the effect clearly. Although the mean teacher-student advantage remains nonzero toward the end of a response, the discriminative power of the sampled token advantages decays. This demonstrates that the teacher’s global guidance can persist even as dense feedback becomes less informative for identifying which specific actions are relatively better or worse.
To mitigate this issue, we evaluate a simple trajectory-specific release rule. At each prefix, we construct the student’s top-
K
K
candidate set to represent its reachable space and compute the teacher’s margin between the top-1 and top-2 candidates within that set. This nearest-competitor margin serves as a proxy for whether the teacher still provides a sharp local preference signal. We then aggregate this margin over NLTK-tokenized sentence segments
(Bird
et al.
,
2009
)
and apply a Bayesian Information Criterion (BIC)-style downward change-point rule. Before the detected change point, training relies on the standard OPD advantage objective. After this point, dense OPD supervision is masked out. This experiment isolates the effect of modifying the supervision region while keeping the underlying OPD objective intact.
Across our strong-to-weak distillation experiments, this release rule improves the average score across five in-domain benchmarks from 36.8% with full OPD to 40.1% for a 1.7B student. A random-release control yields weaker performance, supporting the need to couple each trajectory with its own local-teachability signal. Furthermore, the same release rule improves aggregate performance over full OPD and other alternative baselines for 4B and 8B students. Finally, the out-of-domain benchmark check suggests that this method better preserves out-of-domain capabilities compared to alternative baselines.
The contribution of this paper is threefold:
1.
Identify local teachability collapse in strong-to-weak OPD
: Motivated by the observation that outcome-RL updates are most useful when feedback distinguishes between alternatives, we analyze whether dense strong-to-weak OPD advantages remain locally discriminative along a student rollout. This perspective reveals
local teachability collapse
, where teacher-student disagreement remains nonzero even as sampled-token advantage dispersion and teacher local contrast decay.
2.
A trajectory-specific release rule
: We introduce a mechanism to determine if teacher feedback remains locally actionable for student trajectory. This rule measures the teacher’s top-1 and top-2 margin over the student’s reachable candidates, aggregates the signal over sentence segments, and terminates dense supervision after a statistical change point.
3.
Empirical validation of the teachability signal
: Across various Qwen3 strong-to-weak distillation settings, our release rule consistently outperforms full OPD on in-domain benchmarks for multiple student sizes and better preserves performance on the out-of-domain benchmark. These results support the central claim of this paper: dense strong-to-weak OPD should consider not only whether a teacher-student advantage exists, but also whether that advantage remains locally teachable.

## Method

Preliminaries.
In on-policy distillation (OPD), the student samples its own response
y
=
(
y
1
,
…
,
y
T
)
y=(y_{1},\ldots,y_{T})
for an input
x
x
, and the teacher is evaluated on the same visited prefixes
(
x
,
y
<
t
)
(x,y_{<t})
(Agarwal
et al.
,
2024
; Yang
et al.
,
2026
; Xiaomi,
2026
; Lu and Thinking Machines Lab,
2025
)
. This makes the supervision on-policy: the teacher does not provide a separate offline trajectory, but instead scores the states actually induced by the student.
There are two primary approaches to formulating the loss in On-Policy Distillation: minimizing the Kullback-Leibler (KL) divergence over a full or partial vocabulary, or optimizing a reinforcement learning (RL) objective via advantage estimation. In this work, we adopt the latter formulation, as it is more memory-efficient and widely utilized in large-scale industrial deployments, such as Alibaba Qwen3
(Yang
et al.
,
2025
)
, Tencent HunYuan
(Yang
et al.
,
2026
)
, XiaoMi MiMo-v2
(Xiaomi,
2026
)
, ZhiPu GLM-5
(Zeng
et al.
,
2026
)
, NVIDIA
(Wu
et al.
,
2026
)
and ThinkMachineLab
(Lu and Thinking Machines Lab,
2025
)
. Under this framework, the standard OPD signal is defined as the log-probability difference between the teacher and the student for a sampled token. For each sampled response token
y
t
y_{t}
, the teacher-student advantage is
A
t
=
log
⁡
p
T
​
(
y
t
∣
x
,
y
<
t
)
−
log
⁡
p
S
​
(
y
t
∣
x
,
y
<
t
)
.
A_{t}=\log p_{T}(y_{t}\mid x,y_{<t})-\log p_{S}(y_{t}\mid x,y_{<t}).
The signed mean of
A
t
A_{t}
measures teacher-student disagreement on the sampled trajectory. A positive
A
t
A_{t}
indicates that the teacher assigns a higher probability to the action than the student, suggesting the student should increase its likelihood, while a negative value implies the opposite. The training loss incorporates
A
t
A_{t}
as dense feedback along the sampled trajectory, typically by weighting the student’s log-probabilities within a policy-gradient objective.
Diagnosing local teachability collapse.
(a)
Mean advantage.
(b)
Advantage dispersion.
Figure 1
:
The presence of a guidance signal does not guarantee high-value local teachability.
(a) The mean teacher-student advantage remains nonzero across late response regions, indicating that the teacher has not simply ceased guiding the student. (b) The within-bin standard deviation of
A
t
A_{t}
, normalized by its early-region value, steadily decays throughout the rollout. This decrease in sampled-path dispersion is a diagnostic indicator that the feedback becomes less token-specific, yielding relatively lower instructional value compared to the earlier dense feedback.
OPD assumes that teacher disagreement remains uniformly informative throughout the sampled response. In strong-to-weak OPD, this assumption can break down because a preference gap may persist even as the teacher provides diminishing contrast across later segments. This issue is significant for the same reason that outcome-driven RL benefits most from non-degenerate feedback groups: when feedback fails to distinguish between alternative or partial trajectories, it yields a weaker learning signal
(Qu
et al.
,
2026
; Bae
et al.
,
2026
; Shu
et al.
,
2026
; Yu
et al.
,
2025
)
. We term the OPD variant of this failure mode
local teachability collapse
: a sustained decline in the teacher’s local discriminability along a rollout.
We initially examine this phenomenon using the strong-to-weak distillation framework established in previous OPD study
(Yang
et al.
,
2026
)
. The purpose of this setting is not to demonstrate uniform scaling curves across all student sizes; rather, the pronounced performance gap between the teacher (Qwen3-30B-A3B-Instruct-2507) and student (Qwen3-1.7B) serves to expose the local-support mismatch. Section
4.5
then investigates whether our release rule formulated from this analysis generalizes to more capable students.
Our analysis compares the base student model (denoted as
Student
in Figure
1
) with its OPD-optimized counterpart (denoted as
OPD
in Figure
1
). While the base student provides a baseline for the initial on-policy distribution, the OPD model serves as our primary subject for evaluating policy convergence. This comparison allows us to isolate the generic characteristics of weak-model rollouts from the patterns that emerge or persist specifically following OPD optimization.
To quantify the value of local teachability, we sample responses from both models across 500 training instances. For each trajectory, we compute the teacher and student log-probabilities at every decoding step to derive the pointwise advantage,
A
t
A_{t}
. We partition these sequences into 20 discrete segments based on their normalized temporal position within the trajectory. For each segment, we compute two primary bin-wise statistics:
1.
Mean Advantage:
This represents the aggregate teacher preference relative to the student’s current policy, capturing whether the teacher continues to actively guide the student toward optimization.
2.
Standard Deviation of Advantage:
This measures the local token-level variance, reflecting the discriminative power of the teacher’s guidance signal across adjacent actions.
Figure
1
disentangles two questions that are frequently conflated. Panel (a) examines whether the teacher and student still disagree on sampled tokens. The results indicate that they do: for the OPD-optimized model, the late mean advantage remains at approximately
A
t
≈
−
0.3
A_{t}\approx-0.3
. Panel (b) investigates whether the dense feedback retains token-specific variation. This effect is noticeably weaker, as the normalized standard deviation of
A
t
A_{t}
decreases substantially in later regions. Consequently, the teacher’s global guidance can persist even when the token-level signal becomes less informative for distinguishing the relative quality of local actions. A representative log-probability trace in Figure
4
exhibits the same qualitative pattern. This initial diagnostic serves as the primary motivation for the rest of our work. By examining the sampled advantage sequence, we illustrate that dense supervision applied to the entire response often yields diminishing local information.
Figure 2
:
Teacher margin over student top-
K
K
candidates.
The normalized margin declines along the response, providing the local signal that is later aggregated over sentence segments for release.
Trajectory-specific release rule.
The preceding diagnostic, combined with the established insight from outcome-driven RL that high-contrast advantages are more useful for policy updates while low-contrast advantages can often be discarded
(Qu
et al.
,
2026
; Bae
et al.
,
2026
; Shu
et al.
,
2026
)
, suggests a natural strategy: dropping supervision when the chunk-level
std
​
(
A
t
)
\mathrm{std}(A_{t})
becomes low. In practice, however, we observe that the chunk-level
std
​
(
A
t
)
\mathrm{std}(A_{t})
is unstable because it measures variance solely across the specific tokens sampled by the student. This narrow evaluation places undue emphasis on individual sampled trajectories and ignores the underlying capacity of the teacher to guide the student at each prefix state, thereby yielding an inconsistent measure of local teachability. This limitation is particularly pronounced during the early stages of student training. As illustrated in Figure
1(b)
, when a trajectory reaches the final answer summary stage (the last bin), the teacher might abruptly provide discriminative action-level feedback for an obviously incorrect answer, even if local teachability has already collapsed during earlier segments of the solution. Consequently, before determining where to apply supervision, a more robust measure must answer a fundamental question: given the current prefix state, can the teacher still discriminate among the actions the student is likely to take? Answering this requires analyzing the local support of the student policy rather than relying exclusively on the sampled token sequence. We revisit this distinction in Section
4.4
.
We therefore estimate chunk-level teachability using a state-local teacher margin and subsequently aggregate it over NLTK-tokenized sentence segments
(Bird
et al.
,
2009
)
. At prefix
(
x
,
y
<
t
)
(x,y_{<t})
, let
𝒞
t
=
TopK
a
⁡
p
S
​
(
a
∣
x
,
y
<
t
)
\mathcal{C}_{t}=\operatorname{TopK}_{a}\;p_{S}(a\mid x,y_{<t})
be the student’s top-
K
K
candidate set, which represents the student’s reachable action space at that prefix. We rank candidates in
𝒞
t
\mathcal{C}_{t}
using teacher log-probabilities and define
a
t
(
1
)
=
arg
⁡
max
a
∈
𝒞
t
⁡
log
⁡
p
T
​
(
a
∣
x
,
y
<
t
)
,
a
t
(
2
)
=
arg
⁡
max
a
∈
𝒞
t
∖
{
a
t
(
1
)
}
⁡
log
⁡
p
T
​
(
a
∣
x
,
y
<
t
)
.
a_{t}^{(1)}=\arg\max_{a\in\mathcal{C}_{t}}\log p_{T}(a\mid x,y_{<t}),\qquad a_{t}^{(2)}=\arg\max_{a\in\mathcal{C}_{t}\setminus\{a_{t}^{(1)}\}}\log p_{T}(a\mid x,y_{<t}).
The token-level local contrast proxy is the teacher’s nearest-competitor margin
M
t
=
log
⁡
p
T
​
(
a
t
(
1
)
∣
x
,
y
<
t
)
−
log
⁡
p
T
​
(
a
t
(
2
)
∣
x
,
y
<
t
)
.
M_{t}=\log p_{T}(a_{t}^{(1)}\mid x,y_{<t})-\log p_{T}(a_{t}^{(2)}\mid x,y_{<t}).
Unlike
A
t
A_{t}
, this margin does not score the sampled token itself. Instead, it evaluates whether the teacher can still express a sharp pedagogical preference within the student’s reachable support. Following sentence-level aggregation, a sustained margin drop indicates that the corresponding segment has diminished point-level teaching value.
The margin curve in Figure
2
reflects the broader decline implied by advantage dispersion, but it evaluates a distinct quantity: the teacher’s ranking over candidates reachable by the student under the same prefix. This distinction is central to our release rule. While the realized-path statistic
std
​
(
A
t
)
\mathrm{std}(A_{t})
identifies the underlying symptom,
M
t
M_{t}
translates this intuition into a state-local control signal by assessing whether the teacher maintains a clear preference among the student’s viable candidates.
Although we fixed the number of bins at 20 during our analysis, the significant variance in trajectory lengths makes it difficult to define an appropriate bin parameter for actual training. To address this, we adopt a more natural approach using NLTK sentence segmentation
(Bird
et al.
,
2009
)
. Let
ℬ
i
\mathcal{B}_{i}
denote the set of tokens within sentence segment
i
i
. The segment-level teachability signal is defined as follows:
S
i
=
log
⁡
(
1
+
1
|
ℬ
i
|
​
∑
t
∈
ℬ
i
M
t
)
.
S_{i}=\log\!\left(1+\frac{1}{|\mathcal{B}_{i}|}\sum_{t\in\mathcal{B}_{i}}M_{t}\right).
The logarithmic function is applied primarily to stabilize the numerical scale. Furthermore, sentence-level aggregation mitigates transient token-level artifacts while aligning the release decision with natural linguistic boundaries.
We then use the sequence
{
S
i
}
i
=
1
n
\{S_{i}\}_{i=1}^{n}
to decide whether the rollout should keep full OPD supervision or be released after a local-teachability drop. This can be cast as a simple two-model comparison. The null hypothesis is that the trajectory has one stable teachability level, while the alternative is that there is a single downward shift after some segment
τ
\tau
. The no-change model is
H
0
:
S
i
=
μ
+
ϵ
i
,
H_{0}:\quad S_{i}=\mu+\epsilon_{i},
and the one-drop model is
H
1
(
τ
)
:
S
i
=
{
μ
pre
+
ϵ
i
,
i
≤
τ
,
μ
post
+
ϵ
i
,
i
>
τ
,
μ
pre
>
μ
post
.
H_{1}(\tau):\quad S_{i}=\begin{cases}\mu_{\mathrm{pre}}+\epsilon_{i},&i\leq\tau,\\
\mu_{\mathrm{post}}+\epsilon_{i},&i>\tau,\end{cases}\qquad\mu_{\mathrm{pre}}>\mu_{\mathrm{post}}.
For each candidate
τ
\tau
, we compute the residual sum of squares:
RSS
0
=
∑
i
(
S
i
−
S
¯
)
2
,
\mathrm{RSS}_{0}=\sum_{i}(S_{i}-\bar{S})^{2},
RSS
1
​
(
τ
)
=
∑
i
≤
τ
(
S
i
−
S
¯
≤
τ
)
2
+
∑
i
>
τ
(
S
i
−
S
¯
>
τ
)
2
.
\mathrm{RSS}_{1}(\tau)=\sum_{i\leq\tau}(S_{i}-\bar{S}_{\leq\tau})^{2}+\sum_{i>\tau}(S_{i}-\bar{S}_{>\tau})^{2}.
We use a profiled RSS-BIC criterion, where the noise variance is absorbed into the residual term rather than counted as an additional explicit parameter:
BIC
0
=
n
​
log
⁡
(
RSS
0
+
ϵ
n
)
+
k
0
​
log
⁡
n
,
\operatorname{BIC}_{0}=n\log\left(\frac{\mathrm{RSS}_{0}+\epsilon}{n}\right)+k_{0}\log n,
BIC
1
⁡
(
τ
)
=
n
​
log
⁡
(
RSS
1
​
(
τ
)
+
ϵ
n
)
+
k
1
​
log
⁡
n
.
\operatorname{BIC}_{1}(\tau)=n\log\left(\frac{\mathrm{RSS}_{1}(\tau)+\epsilon}{n}\right)+k_{1}\log n.
Under this convention, the no-change model has one free mean parameter, so
k
0
=
1
k_{0}=1
. The one-drop model has two segment means and one discrete change-point parameter, so
k
1
=
3
k_{1}=3
.
We select the best downward change point by minimizing the BIC among candidates satisfying
μ
pre
>
μ
post
\mu_{\mathrm{pre}}>\mu_{\mathrm{post}}
:
τ
⋆
=
arg
⁡
min
τ
:
S
¯
>
τ
<
S
¯
≤
τ
⁡
BIC
1
⁡
(
τ
)
.
\tau^{\star}=\arg\min_{\tau:\,\bar{S}_{>\tau}<\bar{S}_{\leq\tau}}\operatorname{BIC}_{1}(\tau).
A release is accepted when the best one-drop model improves over the no-change model:
BIC
1
⁡
(
τ
⋆
)
<
BIC
0
.
\operatorname{BIC}_{1}(\tau^{\star})<\operatorname{BIC}_{0}.
If no downward candidate improves the no-change model, the trajectory defaults to full OPD supervision.
Given the accepted change point
τ
⋆
\tau^{\star}
, we retain only the tokens preceding the corresponding segment boundary. Let
q
t
∈
{
0
,
1
}
q_{t}\in\{0,1\}
denote this prefix mask, and let
l
t
l_{t}
denote the original loss mask covering the entire trajectory. To preserve the per-sample loss mass after truncation, we rescale the retained prefix to ensure the overall consistency of the gradient magnitude:
A
t
′
=
A
t
⋅
q
t
⋅
∑
t
l
t
∑
t
l
t
​
q
t
.
A^{\prime}_{t}=A_{t}\cdot q_{t}\cdot\frac{\sum_{t}l_{t}}{\sum_{t}l_{t}q_{t}}.
Consequently, the release rule modifies where teacher-guided OPD supervision is applied, rather than altering the total supervision weight assigned to a trajectory. This approach focuses learning on the prefix region where the teacher still provides a clear state-local preference within the student’s reachable action space, while attenuating the influence of low-teachability suffixes.
(a)
BIC gain.
(b)
Pre/post margin.
(c)
Release distribution.
Figure 3
:
The release rule detects trajectory-specific drops in local contrast.
Statistics are computed on the exported OPD rollouts using the teacher’s top-1 and top-2 margin over the student’s top-
K
K
candidates. (a) The profiled RSS-BIC gain,
BIC
0
−
min
τ
⁡
BIC
1
⁡
(
τ
)
\operatorname{BIC}_{0}-\min_{\tau}\operatorname{BIC}_{1}(\tau)
, is positive for most samples. The mean gain is 24.0, and 79% of the samples accept a significant downward BIC-improving release with a gain greater than 6. (b) For accepted samples, the average chunk-level margin decreases from the pre-release region to the post-release region. (c) Relative release positions vary across trajectories, with a mean of 0.25 and a median of 0.13, demonstrating that the rule is not merely a fixed prefix in disguise.
Figure
3
characterizes the release rule itself. The BIC gain demonstrates when a one-drop summary is preferred; the pre/post comparison confirms that accepted changes are downward; and the release distribution illustrates substantial sample-level variation. Appendix
A.1
provides the implementation details, and Appendix
A.2
gives a signal-to-noise interpretation of why locally low-contrast suffix supervision can reduce the usefulness of dense OPD updates. Figure
6
and Appendix
A.4
present some representative release cases.
The proposed rule operates as a practical heuristic rather than a theoretical guarantee that all post-release tokens are detrimental. Designed to validate the central claim of this paper, its objective is to maintain standard OPD as long as sentence segments retain sufficient teacher contrast to be informative, and to halt dense supervision once the sentence-level margin curve exhibits a substantial downward shift. The following section evaluates whether this trajectory-specific release mechanism effectively improves training performance.
