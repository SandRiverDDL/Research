# On-Policy Distillation with Best-of-N Teacher Rollout Selection

paper_id: arxiv:2605.09725
tier: U
source_used: html_arxiv
warning: none

## Intro

On-policy distillation (OPD) has rapidly become a standard tool in large language model (LLM) post-training
[
1
,
13
,
29
,
47
,
44
,
51
,
50
,
19
,
21
,
24
]
. The recipe is appealingly simple: have the student generate rollouts from its own policy, and use the teacher’s per-token log-probabilities on those rollouts as a dense supervision signal.
Compared with supervised fine-tuning (SFT) on teacher-generated text or classical sequence-level distillation
[
17
,
23
,
34
,
20
,
42
,
12
]
, OPD is less susceptible to exposure bias because supervision is defined on exactly the states the student visits at inference time
[
3
,
33
,
45
]
. Industry post-training pipelines
[
47
,
44
,
11
]
have adopted OPD as a competitive complement to SFT and outcome-reward reinforcement learning
[
35
,
52
,
15
,
5
,
37
,
4
]
, with reported comparable gains at a fraction of the RL compute cost
[
29
]
.
Despite this appeal, recent work has begun to unpack when OPD works and why
[
26
,
10
,
22
]
.
Two conditions appear to govern success: the student and teacher should share compatible reasoning patterns, and the teacher be able to produce correct, naturally derived solutions beyond the student’s current exploration range, thereby transferring new capabilities on difficult tasks.
This observation is also consistent with recent findings that small models can struggle to imitate strong reasoners when the teacher’s reasoning style is poorly matched to the student
[
9
,
27
,
14
]
.
Standard OPD reduces exposure bias by evaluating teacher feedback on student-generated trajectories, but this also means that supervision is computed on prefixes produced by an imperfect student
[
3
,
33
,
1
,
29
]
. On difficult prompts, these prefixes can drift into noisy reasoning states, where local teacher feedback is less informative, and the student may never observe a complete correct solution path
[
26
,
10
,
27
]
.
Practical OPD-style pipelines therefore often use teacher-side signals, such as reference rollouts, solvability estimates, metadata, or filtering rules, to identify prompts or trajectories that provide useful supervision
[
29
,
44
,
49
,
26
]
.
However, the teacher is also stochastic: for a fixed prompt, its sampled trajectories can differ substantially in correctness, reasoning style, and proximity to the student, especially on hard prompts
[
43
,
53
,
28
,
39
]
.
Thus, a single teacher sample can provide a high-variance estimate of the teacher’s competence and alignment for a given prompt. When this sample is incorrect or poorly matched to the student, it can produce noisy guidance ( Figure
1
(a)).
To address this limitation, we introduce
BRTS
, a
B
est-of-
N
N
R
ollout
T
eacher
S
election framework for on-policy distillation.
As illustrated in Figure
1
(b), BRTS first identifies a reliable teacher trajectory and then distills it as an additional teacher-context supervision signal, rather than learning from an arbitrary teacher rollout.
This complements standard student-context distillation: while OPD corrects the states visited by the student, BRTS exposes the student to complete and reliable teacher reasoning paths.
The teacher-context branch is both correctness-aware and alignment-aware. Correctness prevents erroneous teacher samples from being amplified, while alignment keeps the selected trajectory close to the student’s current reasoning distribution.
For prompts where ordinary teacher sampling fails, BRTS uses a ground-truth-guided recovery step to obtain a teacher derivation, keeping the auxiliary branch active on hard examples where reliable supervision is most needed.
In this way, BRTS turns stochastic teacher rollouts into structured supervision inside the OPD loop.
Experiments on three public datasets show that BRTS improves over standard OPD, with larger gains on harder prompts where reliable teacher trajectories are sparse.
Our contributions are summarized as follows:
•
We identify a high-variance supervision issue in OPD: standard student-context supervision can be limited by noisy student prefixes and stochastic teacher rollouts, making the teacher signal unreliable on hard prompts.
•
We introduce
BRTS
, a Best-of-
N
N
rollout teacher selection framework that provides a lightweight mechanism for selecting and distilling reliable teacher trajectories.
With an answer-hint fallback for failed unconditioned samples, BRTS distills the selected trajectory through a ground truth-guided teacher-context objective.
•
BRTS significantly improves over standard OPD on the hard benchmarks. We also provide diagnostic analyses showing how teacher candidate quality, recovery coverage, and teacher backbone choice affect the resulting OPD performance.

## Method

3.1
Preliminaries
Let
x
x
be an input prompt and
y
⋆
y^{\star}
be its corresponding ground-truth answer. We consider a student policy
π
S
\pi_{S}
and a teacher policy
π
T
\pi_{T}
, each defining an autoregressive next-token distribution over a vocabulary
𝒱
\mathcal{V}
.
For a trajectory
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
, the probability under a policy
π
\pi
factorizes as
π
​
(
y
∣
x
)
=
∏
t
=
1
T
π
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
,
\pi(y\mid x)=\prod_{t=1}^{T}\pi(y_{t}\mid x,y_{<t}),
(1)
where
y
<
t
y_{<t}
denotes the prefix before token
t
t
. Let
y
^
S
∼
π
S
(
⋅
∣
x
)
\hat{y}^{S}\sim\pi_{S}(\cdot\mid x)
and
y
T
∼
π
T
(
⋅
∣
x
)
y^{T}\sim\pi_{T}(\cdot\mid x)
denote student and teacher rollouts, respectively. On-policy distillation trains the student on states induced by its own generation: for rollout
y
^
S
\hat{y}^{S}
, the teacher provides token-level supervision on prefixes
(
x
,
y
^
<
t
S
)
(x,\hat{y}^{S}_{<t})
. A standard formulation minimizes the sequence-level reverse-KL objective
[
1
,
13
,
26
]
:
ℒ
OPD
(
S
)
=
𝔼
x
,
y
^
S
∼
π
S
[
∑
t
=
1
T
D
KL
(
π
S
(
⋅
∣
x
,
y
^
<
t
S
)
∥
π
T
(
⋅
∣
x
,
y
^
<
t
S
)
)
]
.
\mathcal{L}_{\mathrm{OPD}}(S)=\mathbb{E}_{x,\,\hat{y}^{S}\sim\pi_{S}}\left[\sum_{t=1}^{T}D_{\mathrm{KL}}\!\left(\pi_{S}(\cdot\mid x,\hat{y}^{S}_{<t})\,\middle\|\,\pi_{T}(\cdot\mid x,\hat{y}^{S}_{<t})\right)\right].
(2)
In OPD implementations, the per-step KL is often approximated with a sampled or top-
K
K
token set, typically chosen from the student distribution at the current student prefix
[
29
,
44
]
.
This corrects the student on the states it actually visits.
However, the student context can be noisy.
BRTS addresses this by adding a correctness- and alignment-aware teacher-context branch.
We describe BRTS in three parts: teacher trajectory curation (Sec.
3.2
), teacher-context supervision (Sec.
3.3
), and the top-
K
K
candidate direction used in each branch (Sec.
3.4
).
Figure
2
shows our framework and Algorithm
1
summarizes the training step.
3.2
Correctness- and Alignment-aware Trajectory Curation
In the first tier, we draw
N
N
unconditioned teacher samples
{
y
T
,
i
}
i
=
1
N
∼
π
T
(
⋅
∣
x
)
\{y^{T,i}\}_{i=1}^{N}\sim\pi_{T}(\cdot\mid x)
for each prompt.
Each rollout is evaluated against the ground-truth answer
y
⋆
y^{\star}
by extracting its final answer.
If at least one rollout is correct,
i.e.
,
answer
​
(
y
T
,
i
)
=
y
⋆
\mathrm{answer}(y^{T,i})=y^{\star}
, BRTS selects among the correct rollouts the trajectory with the highest token-level overlap with the student’s top-
K
K
candidate set.
This alignment criterion favors correct trajectories that remain close to the student’s high-probability region and are therefore more suitable for distillation.
If none of the unconditioned teacher rollouts is correct, BRTS invokes a ground-truth-guided recovery step.
We construct a modified prompt
x
gt
x^{\mathrm{gt}}
that provides the correct answer
y
⋆
y^{\star}
as a silent validation signal while instructing the teacher to produce a natural derivation.
A guided teacher rollout
y
T
,
gt
∼
π
T
(
⋅
∣
x
gt
)
y^{T,\mathrm{gt}}\sim\pi_{T}(\cdot\mid x^{\mathrm{gt}})
is then sampled and retained only if its extracted answer is correct.
This step targets hard prompts where ordinary teacher sampling fails, allowing the teacher-context branch to remain active on examples where reliable supervision is most needed.
If neither unconditioned sampling nor guided recovery yields a correct trajectory, BRTS falls back to the Tier-1 rollout with the highest student overlap.
Although this fallback trajectory may be incorrect, selecting the closest available rollout avoids introducing an arbitrary teacher trajectory far from the student’s distribution.
Algorithm 1
BRTS training step
0:
Prompt
x
x
, ground-truth answer
y
⋆
y^{\star}
, teacher policy
π
T
\pi_{T}
, student policy
π
S
\pi_{S}
, number of Tier-1 rollouts
N
N
, auxiliary weight
λ
\lambda
1:
Sample a student rollout
y
^
S
∼
π
S
(
⋅
∣
x
)
\hat{y}^{S}\sim\pi_{S}(\cdot\mid x)
2:
Draw
N
N
unconditioned teacher rollouts
{
y
T
,
i
}
i
=
1
N
∼
π
T
(
⋅
∣
x
)
\{y^{T,i}\}_{i=1}^{N}\sim\pi_{T}(\cdot\mid x)
3:
Grade each teacher rollout by checking whether
answer
​
(
y
T
,
i
)
=
y
⋆
\mathrm{answer}(y^{T,i})=y^{\star}
4:
if
at least one Tier-1 rollout is correct
then
5:
Select
y
′
y^{\prime}
as the correct rollout with the highest top-
K
K
overlap with the student trajectory.
6:
else
7:
Construct the ground-truth-guided prompt
x
gt
x^{\mathrm{gt}}
8:
Sample one guided teacher rollout
y
T
,
gt
∼
π
T
(
⋅
∣
x
gt
)
y^{T,\mathrm{gt}}\sim\pi_{T}(\cdot\mid x^{\mathrm{gt}})
9:
if
answer
​
(
y
T
,
gt
)
=
y
⋆
\mathrm{answer}(y^{T,\mathrm{gt}})=y^{\star}
then
10:
Select
y
′
←
y
T
,
gt
y^{\prime}\leftarrow y^{T,\mathrm{gt}}
11:
else
12:
Select
y
′
y^{\prime}
as the Tier-1 rollout with the highest student top-
K
K
overlap
13:
end
if
14:
end
if
15:
Compute the student-context loss
ℒ
stu
​
-
​
ctx
\mathcal{L}_{\mathrm{stu\text{-}ctx}}
on
y
^
S
\hat{y}^{S}
using student top-
K
K
candidates
16:
Compute the teacher-context loss
ℒ
tea
​
-
​
ctx
\mathcal{L}_{\mathrm{tea\text{-}ctx}}
on the selected trajectory
y
′
y^{\prime}
using teacher top-
K
K
candidates
17:
ℒ
total
←
ℒ
stu
​
-
​
ctx
+
λ
​
ℒ
tea
​
-
​
ctx
\mathcal{L}_{\mathrm{total}}\leftarrow\mathcal{L}_{\mathrm{stu\text{-}ctx}}+\lambda\mathcal{L}_{\mathrm{tea\text{-}ctx}}
18:
Update the student parameters by taking a gradient step on
ℒ
total
\mathcal{L}_{\mathrm{total}}
3.3
Teacher-Context Supervision
We retain Eq. (
2
) on student-generated trajectories and augment it with a teacher-context distillation loss defined on the curated teacher trajectory
y
′
y^{\prime}
from Sec.
3.2
.
Both branches compare teacher and student distributions under matched conditioning contexts.
In the student-context branch, both distributions are conditioned on the student prefix
y
^
<
t
S
\hat{y}^{S}_{<t}
.
In the teacher-context branch, both distributions are conditioned on the selected teacher prefix
y
<
t
′
y^{\prime}_{<t}
.
The resulting objectives are
ℒ
stu-ctx
\displaystyle\mathcal{L}_{\text{stu-ctx}}
=
𝔼
[
∑
t
D
KL
(
π
S
(
⋅
∣
x
,
y
^
<
t
S
)
∥
π
T
(
⋅
∣
x
,
y
^
<
t
S
)
)
]
,
\displaystyle\;=\;\mathbb{E}\!\left[\sum_{t}D_{\mathrm{KL}}\!\big(\pi_{S}(\cdot\mid x,\hat{y}^{S}_{<t})\,\|\,\pi_{T}(\cdot\mid x,\hat{y}^{S}_{<t})\big)\right],
(3)
ℒ
tea-ctx
\displaystyle\mathcal{L}_{\text{tea-ctx}}
=
𝔼
[
∑
t
D
KL
(
π
T
(
⋅
∣
x
,
y
<
t
′
)
∥
π
S
(
⋅
∣
x
,
y
<
t
′
)
)
]
,
\displaystyle\;=\;\mathbb{E}\!\left[\sum_{t}D_{\mathrm{KL}}\!\big(\pi_{T}(\cdot\mid x,y^{\prime}_{<t})\,\|\,\pi_{S}(\cdot\mid x,y^{\prime}_{<t})\big)\right],
(4)
ℒ
total
\displaystyle\mathcal{L}_{\text{total}}
=
ℒ
stu-ctx
+
λ
​
ℒ
tea-ctx
.
\displaystyle\;=\;\mathcal{L}_{\text{stu-ctx}}+\lambda\,\mathcal{L}_{\text{tea-ctx}}.
(5)
The two branches play complementary roles.
The student-context loss preserves the on-policy nature of OPD by correcting the states visited by the student.
The teacher-context loss exposes the student to a coherent teacher reasoning path selected for both correctness and compatibility with the student’s current distribution.
Thus, BRTS does not replace OPD; it augments OPD with a structured teacher-context signal that is less sensitive to stochastic teacher failures.
The coefficient
λ
\lambda
controls the strength of the teacher-context branch.
Since this branch is evaluated on selected teacher trajectories that are usually more coherent than noisy student rollouts, its raw contribution can be small with the naive choice
λ
=
1
\lambda=1
.
Empirically, we find that
λ
=
10
\lambda=10
gives the auxiliary branch a meaningful scale while remaining stable, and use this value across all experiments.
3.4
Top-
K
K
Direction: Student- vs. Teacher-Confident
In the sampled-token setting, both objectives are implemented as top-
K
K
aggregation losses, but they differ in how the candidate token set is defined. For the student-context branch, the candidate set consists of the student’s top-
K
K
tokens under the student prefix. This branch therefore supervises the tokens that the student considers plausible, providing targeted correction on student-visited states.
For the teacher-context branch, the candidate set consists of the teacher’s top-
K
K
tokens under the selected teacher prefix. Unlike the student-context branch, this set reflects the teacher’s local distribution along a high-quality trajectory. Thus, the auxiliary branch introduces teacher-preferred tokens that may lie outside the student’s current top choices, while still keeping the supervision concentrated on a compact top-
K
K
candidate set.
Table 1
:
Effect of the teacher-context supervision.
The baseline uses two student rollouts. Our variants replace one student rollout with one auxiliary teacher trajectory selected from
N
N
teacher candidates. We report mean, best, and majority accuracy on AIME24, AIME25, and AMC23.
Rollout Setup
AIME24
AIME25
AMC23
ℒ
tea-ctx
\mathcal{L}_{\text{tea-ctx}}
Student
Teacher / Cand.
Mean
Best
Majority
Mean
Best
Majority
Mean
Best
Majority
×
\times
2
0 / 0
0.3917
0.5915
0.4146
0.2667
0.3503
0.2792
0.6777
0.7959
0.6952
✓
\checkmark
1
1 / 1
0.3750
0.5805
0.4124
0.2583
0.3823
0.2799
0.6747
0.8047
0.6978
✓
\checkmark
1
1 / 2
0.3750
0.5855
0.3953
0.2667
0.4056
0.2748
0.6717
0.8104
0.6917
✓
\checkmark
1
1 / 4
0.4000
0.5991
0.4306
0.2917
0.3700
0.2961
0.6837
0.8004
0.6948
10
10
20
20
30
30
40
40
50
50
0.37
0.37
0.38
0.38
0.39
0.39
0.40
0.40
0.41
0.41
0.42
0.42
0.43
0.43
0.44
0.44
Training step
majority
Baseline
Teacher Cand. 2
(a)
Average over three benchmarks
10
10
20
20
30
30
40
40
50
50
60
60
70
70
80
80
90
90
100
100
110
110
0.20
0.20
0.22
0.22
0.24
0.24
0.26
0.26
0.28
0.28
Training step
majority
Baseline
Teacher Cand. 4
(b)
AIME 24 (teacher peaks higher)
Figure 3
:
Majority-vote accuracy across training steps.
The student-only baseline uses two student rollouts, while BRTS replaces one student rollout with an auxiliary teacher trajectory selected from a small candidate pool. Left: average over AIME24, AIME25, and AMC23. Right: AIME24 results. BRTS achieves a higher early-training peak than the student-only baseline.
