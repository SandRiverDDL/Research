# Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes

paper_id: arxiv:2603.25562
tier: U
source_used: html_arxiv
warning: none

## Intro

On-policy distillation (OPD) is becoming an increasingly common component of LLM post-training, especially for reasoning and agentic models. Recent public reports from Thinking Machines Lab
(Lu and Lab,
2025
)
, Qwen3
(Yang
et al.
,
2025
)
, MiMo-V2-Flash
(Xiao
et al.
,
2026
)
, and GLM-5
(Zeng
et al.
,
2026
)
suggest a broader shift toward supervision on model-generated trajectories, or closely related on-policy variants, alongside off-policy distillation and reinforcement learning. By training on student rollouts while evaluating them with a stronger teacher, OPD combines on-policy data collection with dense token-level feedback at relatively low cost
(Agarwal
et al.
,
2024
; Gu
et al.
,
2024
)
. This profile is attractive in practical post-training pipelines, where training efficiency matters and models often need to combine or recover capabilities across domains and training stages
(Xiao
et al.
,
2026
; Zeng
et al.
,
2026
; Wang
et al.
,
2026a
; DeepSeek-AI,
2026
)
.
Most OPD implementations in current LLM pipelines use a token-level estimator, even though it is biased relative to sequence-level reverse-KL
(Lu and Lab,
2025
)
. A basic reason is that sequence-level objectives couple each token update to many future rewards, which can make optimization substantially noisier in long-horizon settings. We make this trade-off explicit: token-level OPD removes future-reward coupling and is therefore biased, yet it admits more favorable worst-case variance scaling. Our toy experiment shows the same pattern empirically, with stronger future coupling leading to higher gradient variance and less stable optimization. This suggests a practical design principle for long-horizon training:
keep supervision token-level to control variance.
In current LLM pipelines, this token-level objective is usually instantiated by sampled-token comparison: at each training step, the update is driven by the teacher–student log-probability difference on the sampled token
(Lu and Lab,
2025
; Xiao
et al.
,
2026
)
. This implementation is simple and efficient, but its learning signal can become brittle once rollouts grow long.
Gu
et al.
(
2024
)
report degraded outputs such as repetition, which is consistent with our observations. Recent work also reports entropy collapse under sampled-token OPD in certain cases
(Ko
et al.
,
2026
; Jin
et al.
,
2026b
)
. More recently, full-vocabulary distillation has been reported to outperform sampled-token variants in some settings
(Zhao
et al.
,
2026
; DeepSeek-AI,
2026
)
, suggesting that the one-token formulation can leave useful teacher information unused.
Our empirical analysis shows that this brittleness stems from several recurring failure modes. In particular, we identify two
objective-level
issues: the one-token signal is often highly imbalanced, and teacher guidance can become unreliable on student-generated prefixes. We also observe an additional
implementation-level
issue from tokenizer or special-token mismatch, which can further distort one-token comparisons. Taken together, these results point to a practical question:
how can we retain the variance advantage of token-level OPD while making its supervision signal less brittle in practice?
The analysis above suggests a targeted modification of the standard sampled-token objective. We replace one-token supervision with teacher top-
K
K
local support matching, where teacher and student are compared over a teacher-supported token subset at each prefix rather than only on the sampled token. We implement this objective as truncated reverse-KL, together with top-
p
p
rollout sampling and special-token masking. The resulting update remains local and inexpensive, while providing a less brittle training signal.
Overall,
our main contributions
are as follows:
•
We clarify the theoretical trade-off in OPD: token-level OPD is biased relative to sequence-level OPD, but has substantially better worst-case variance scaling with sequence length, making it attractive for long-horizon LLM post-training.
•
We present an empirical analysis of why sampled-token OPD can be unstable in practice, highlighting two recurring objective-level issues—imbalanced one-token supervision and unreliable teacher guidance on student-generated prefixes—along with an additional implementation issue from tokenizer or special-token mismatch.
•
We propose teacher top-
K
K
local support matching as an analysis-driven revision of sampled-token OPD, implemented with truncated reverse-KL, top-
p
p
rollouts, and special-token masking, and show that it yields more stable optimization and stronger empirical performance than sampled-token OPD in single-task math reasoning and multi-task agentic-plus-reasoning training.

## Method

Our method is designed as a direct response to the failure modes above: it retains token-level OPD, but replaces one-token supervision with a distribution-level comparison over a teacher-selected support set at each prefix.
This yields a truncated reverse-KL objective that preserves the efficiency of local updates while reducing dependence on any single sampled token.
Section
3.1
introduces the objective, and Section
3.2
describes the practical choices that ensure stable training.
3.1
Teacher top-
K
K
local support matching
Instead of comparing teacher and student on a single sampled token, we compare their next-token distributions over a teacher-defined local support set. A natural starting point is the full-vocabulary reverse-KL at prefix
c
t
c_{t}
:
ℒ
full
​
(
c
t
)
=
∑
v
∈
𝒱
π
θ
​
(
v
∣
c
t
)
​
log
⁡
π
θ
​
(
v
∣
c
t
)
q
​
(
v
∣
c
t
)
.
\mathcal{L}_{\mathrm{full}}(c_{t})=\sum_{v\in\mathcal{V}}\pi_{\theta}(v\mid c_{t})\log\frac{\pi_{\theta}(v\mid c_{t})}{q(v\mid c_{t})}.
(4)
Sampled-token OPD can be viewed as a Monte Carlo approximation to this quantity:
ℒ
sample
(
c
t
,
y
t
)
=
log
π
θ
​
(
y
t
∣
c
t
)
q
​
(
y
t
∣
c
t
)
,
y
t
∼
π
θ
(
⋅
∣
c
t
)
.
\mathcal{L}_{\mathrm{sample}}(c_{t},y_{t})=\log\frac{\pi_{\theta}(y_{t}\mid c_{t})}{q(y_{t}\mid c_{t})},\qquad y_{t}\sim\pi_{\theta}(\cdot\mid c_{t}).
(5)
This approximation is computationally attractive, but it concentrates the entire update on a single sampled token. We instead compare teacher and student over a teacher-supported candidate set at each prefix.
For each prompt
x
x
, we sample a group of outputs
{
o
i
}
i
=
1
G
\{o_{i}\}_{i=1}^{G}
using the student inference policy. Let
c
i
,
t
=
(
x
,
y
i
,
<
t
)
c_{i,t}=(x,y_{i,<t})
be the prefix at position
t
t
of output
o
i
o_{i}
, and define the teacher support set
S
​
(
c
i
,
t
)
=
TopK
q
​
(
c
i
,
t
)
,
S(c_{i,t})=\mathrm{TopK}_{q}(c_{i,t}),
(6)
which contains the
K
K
highest-probability tokens under the teacher at that prefix.
Within this support, we renormalize both teacher and student distributions:
π
^
θ
​
(
v
∣
c
i
,
t
)
=
π
θ
​
(
v
∣
c
i
,
t
)
∑
u
∈
S
​
(
c
i
,
t
)
π
θ
​
(
u
∣
c
i
,
t
)
,
q
^
​
(
v
∣
c
i
,
t
)
=
q
​
(
v
∣
c
i
,
t
)
∑
u
∈
S
​
(
c
i
,
t
)
q
​
(
u
∣
c
i
,
t
)
.
\hat{\pi}_{\theta}(v\mid c_{i,t})=\frac{\pi_{\theta}(v\mid c_{i,t})}{\sum_{u\in S(c_{i,t})}\pi_{\theta}(u\mid c_{i,t})},\qquad\hat{q}(v\mid c_{i,t})=\frac{q(v\mid c_{i,t})}{\sum_{u\in S(c_{i,t})}q(u\mid c_{i,t})}.
(7)
Our local support matching (LSM) objective averages the truncated reverse-KL over all rollout positions:
ℒ
LSM
=
𝔼
x
,
{
o
i
}
∼
π
θ
,
infer
​
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
∑
v
∈
S
​
(
c
i
,
t
)
π
^
θ
​
(
v
∣
c
i
,
t
)
​
log
⁡
π
^
θ
​
(
v
∣
c
i
,
t
)
q
^
​
(
v
∣
c
i
,
t
)
]
.
\mathcal{L}_{\mathrm{LSM}}=\mathbb{E}_{x,\,\{o_{i}\}\sim\pi_{\theta,\mathrm{infer}}}\left[\frac{1}{\sum_{i=1}^{G}|o_{i}|}\sum_{i=1}^{G}\sum_{t=1}^{|o_{i}|}\sum_{v\in S(c_{i,t})}\hat{\pi}_{\theta}(v\mid c_{i,t})\log\frac{\hat{\pi}_{\theta}(v\mid c_{i,t})}{\hat{q}(v\mid c_{i,t})}\right].
(8)
Relative to sampled-token OPD, this replaces a one-token point estimate with a distribution-level comparison over teacher-supported candidates at the same prefix. The update is therefore no longer determined by the sign and magnitude of a single sampled-token log-ratio, while remaining much cheaper than full-vocabulary KL.
3.2
Practical stabilization choices
Support-set renormalization.
Renormalization is necessary because the objective is evaluated on a truncated support rather than the full vocabulary. Specifically, we apply a separate softmax over the logits inside the support set, so gradients do not directly propagate to tokens outside this set. Without this step, optimization can become unstable because the teacher and student probability masses inside the support are not directly comparable.
Top-
p
p
rollout sampling.
We generate rollouts with top-
p
p
sampling.
Unconstrained sampling occasionally produces very low-probability tokens, creating prefixes on which the teacher signal becomes less informative and optimization less stable.
Top-
p
p
sampling keeps trajectories closer to typical continuations and makes the teacher signal more reliable.
Special-token masking.
We mask problematic special tokens to reduce false negatives caused by incompatible tokenization conventions. This is an orthogonal practical fix: it materially helps sampled-token OPD in our experiments, while our local support objective is much less sensitive to it.
In principle, one could also merge multi-token marker variants or average over equivalent tokenizations, but we do not pursue those tokenizer-specific remedies here because masking is the simplest model-agnostic correction.
