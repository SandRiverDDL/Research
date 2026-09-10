# X-OPD: Cross-Modal On-Policy Distillation for Capability Alignment in Speech LLMs

paper_id: arxiv:2603.24596
tier: U
source_used: html_arxiv
warning: none

## Intro

As multimodal LLMs become increasingly popular, speech interaction is transitioning from traditional cascaded architectures — typically comprising Automatic Speech Recognition (ASR), an LLM, and Text-to-Speech (TTS) — toward End-to-End (E2E) paradigms. By modeling directly within the continuous speech signal space, E2E models significantly reduce interaction latency and capture rich paralinguistic information, such as intonation, emotion, and environmental context, thereby offering a user experience that is far more expressive and akin to human-to-human interaction. This potential is exemplified by recent flagship systems — including GPT-4o
[
hurst2024gpt
]
, Gemini 2.5
[
comanici2025gemini
]
, Qwen3-Omni
[
xu2025qwen3
]
and Voxtral
[
liu2025voxtral
]
— which have collectively redefined unified audio-text understanding.
However, despite the superior interaction fluency of E2E architectures, the significant performance gap remains a barrier to their widespread deployment. Empirical studies
[
lu25c_interspeech
,
chen2025aha
,
fang2025s2sbench
,
zhang2025echox
]
indicate that these models frequently exhibit significant degradation in complex instruction following, logical reasoning, or knowledge-intensive queries compared to their text-based counterparts. Consequently, while cascaded systems may be slower, they remain the industrial selection due to the robust capabilities inherited from the underlying text LLM. This misalignment between modalities prevents speech models from fully leveraging the cognitive power of their textual foundations.
We attribute this degradation primarily to two factors: the scarcity of high-quality, paired speech-reasoning data, and the inherent misalignment between continuous acoustic representations and the discrete logical space of text LLMs. As a result, the high-quality Supervised
Fine-Tuning (SFT) and Reinforcement Learning (RL) data in text LLM training cannot be fully transferred into the training of a Speech LLM, resulting in a gap in the standard SFT+RL training pipeline. Consequently, there is an urgent need for training paradigms that can align cross-modal capabilities without heavy reliance on static datasets.
Some methods try to bridge this gap by performing offline distillation from a cascaded system. However, these methods often struggle with distribution shifts — known as the exposure bias problem — where the model's generation trajectory during inference diverges from the training distribution. Furthermore, the accumulated errors in cascaded pipelines will also harm the performance.
Addressing these challenges, we propose X-OPD, a novel Cross-Modal On-Policy Distillation framework designed to systematically bridge the intelligence gap between Speech LLMs and their text-based counterparts. We introduce a training strategy that utilizes transcribed text as an alignment bridge. In our framework, the student model performs autonomous rollouts across both speech and text modalities. Simultaneously, a more capable text-based teacher model generates a reference distribution based on the synchronized text input. By leveraging Kullback-Leibler (KL) divergence, denoted as
D
KL
​
(
P
∥
Q
)
D_{\text{KL}}(P\parallel Q)
, for dynamic credit assignment, we precisely distill the teacher's logical knowledge into the student's multimodal representations. This approach offers three distinct advantages: it significantly enhances training efficiency; it eliminates the dependency on ground truth data, allowing for the utilization of open-source models where training data is undisclosed; and it minimizes the catastrophic forgetting of other acoustic capabilities. Through this framework, we aim to achieve a low-cost, high-efficiency alignment of cross-modal intelligence, paving the way for the next generation of smart, expressive spoken language agents.
In this work, we introduce X-OPD, a novel optimization strategy that achieves robust modality alignment while effectively preserving the pre-trained model's general proficiency. We demonstrate that X-OPD consistently outperforms various training paradigms and distillation benchmarks, significantly narrowing the performance gap.

## Method

The overall framework of our proposed Cross-Modal On-Policy Distillation (X-OPD) is shown in Figure
1
. X-OPD leverages on-policy sampling from the student model across both modalities, guided by token-level scoring from the text-based teacher. Optimized by policy gradients, X-OPD ensures Speech LLMs efficiently inherit the teacher's capabilities through direct cross-modal alignment.
3.1
Cross-Modal Alignment Data
To enable effective distillation, we define a parallel dataset
𝒟
=
{
(
S
i
,
T
i
)
}
\mathcal{D}=\{(S_{i},T_{i})\}
, consisting of paired speech and text prompts. The fundamental requirement for
𝒟
\mathcal{D}
is Semantic Invariance: the acoustic signal
S
i
S_{i}
and the textual instruction
T
i
T_{i}
must be strictly aligned in their logical intent. In practice, such alignment can be established by either synthesizing speech from textual instructions or transcribing existing audio prompts via speech recognition.
3.2
Robust Multi-sampling Rollout
Single-sample rollouts often suffer from inherent stochasticity, yielding excessive variance in gradient estimation that can destabilize the training process. To enhance optimization robustness, the policy independently samples
n
n
candidate trajectories for each prompt. By marginalizing the gradients across these multiple paths, we achieve broader coverage of the policy space and significantly attenuate the high volatility characteristic of on-policy reinforcement learning updates.
3.3
In-modal and Cross-modal Advantage Function
To ensure the student model
π
θ
\pi_{\theta}
faithfully inherits the teacher's capabilities, we introduce a dual-advantage mechanism. This framework first employs an in-modal advantage to stabilize the student's foundational proficiency within the textual domain, providing a consistent reference for cross-modal alignment.
For a given trajectory
y
y
sampled from the student policy
π
θ
\pi_{\theta}
, let
y
t
y_{t}
be the
t
t
-th token. The in-modal advantage
A
i
​
m
​
(
y
t
)
A_{im}(y_{t})
measures the log-probability discrepancy between the teacher
π
ϕ
\pi_{\phi}
and the student
π
θ
\pi_{\theta}
when both are conditioned on the text prompt
T
T
:
A
i
​
m
​
(
y
t
)
=
log
⁡
π
ϕ
​
(
y
t
|
T
,
y
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
y
t
|
T
,
y
<
t
)
A_{im}(y_{t})=\log\pi_{\phi}(y_{t}|T,y_{<t})-\log\pi_{\theta}(y_{t}|T,y_{<t})
(1)
Building on this, the cross-modal advantage
A
c
​
m
​
(
y
t
)
A_{cm}(y_{t})
is defined to bridge the gap between the teacher's textual logic and the student's speech-conditioned output:
A
c
​
m
​
(
y
t
)
=
log
⁡
π
ϕ
​
(
y
t
|
T
,
y
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
y
t
|
S
,
y
<
t
)
A_{cm}(y_{t})=\log\pi_{\phi}(y_{t}|T,y_{<t})-\log\pi_{\theta}(y_{t}|S,y_{<t})
(2)
Together, these terms provide a cross-modal reward signal, anchoring the student's alignment to the teacher's established proficiency.
3.4
X-OPD Optimization Objective
Integrating the aforementioned mechanisms, the optimization objective is formulated as a policy gradient loss comprising two components: the in-modal loss
ℒ
i
​
m
\mathcal{L}_{im}
and the cross-modal loss
ℒ
c
​
m
\mathcal{L}_{cm}
. To estimate the gradient with reduced variance, the policy samples
m
m
independent rollouts
y
j
y_{j}
for each input through multi-sample rollout. The individual loss terms are defined as:
ℒ
i
​
m
​
(
θ
)
=
𝔼
​
[
1
m
​
∑
j
=
1
m
1
|
y
j
|
​
∑
t
=
1
|
y
j
|
r
j
,
t
​
(
θ
)
​
A
i
​
m
​
(
y
j
,
t
)
]
\mathcal{L}_{im}(\theta)=\mathbb{E}\left[\frac{1}{m}\sum_{j=1}^{m}\frac{1}{|y_{j}|}\sum_{t=1}^{|y_{j}|}r_{j,t}(\theta)A_{im}(y_{j,t})\right]
(3)
ℒ
c
​
m
​
(
θ
)
=
𝔼
​
[
1
m
​
∑
j
=
1
m
1
|
y
j
|
​
∑
t
=
1
|
y
j
|
r
j
,
t
​
(
θ
)
​
A
c
​
m
​
(
y
j
,
t
)
]
\mathcal{L}_{cm}(\theta)=\mathbb{E}\left[\frac{1}{m}\sum_{j=1}^{m}\frac{1}{|y_{j}|}\sum_{t=1}^{|y_{j}|}r_{j,t}(\theta)A_{cm}(y_{j,t})\right]
(4)
In these formulations,
y
j
=
{
y
j
,
1
,
…
,
y
j
,
|
y
j
|
}
y_{j}=\{y_{j,1},\dots,y_{j,|y_{j}|}\}
denotes the
j
j
-th trajectory sampled from the behavior policy. The term
r
j
,
t
​
(
θ
)
=
π
θ
​
(
y
j
,
t
|
⋅
)
π
old
​
(
y
j
,
t
|
⋅
)
r_{j,t}(\theta)=\frac{\pi_{\theta}(y_{j,t}|\cdot)}{\pi_{\text{old}}(y_{j,t}|\cdot)}
represents the probability ratio between the current policy
π
θ
\pi_{\theta}
and the sampling policy
π
old
\pi_{\text{old}}
.
The final optimization objective for X-OPD is defined as the weighted sum of these two components:
ℒ
​
(
θ
)
=
λ
​
ℒ
i
​
m
​
(
θ
)
+
(
1
−
λ
)
​
ℒ
c
​
m
​
(
θ
)
\mathcal{L}(\theta)=\lambda\mathcal{L}_{im}(\theta)+(1-\lambda)\mathcal{L}_{cm}(\theta)
(5)
where
λ
∈
[
0
,
1
]
\lambda\in[0,1]
is a balancing hyperparameter.
Table 2:
Ablation Study of X-OPD.
The results are presented in the same format as Table
1
. The default X-OPD configuration is based on the Qwen3-Omni-A3B-Instruct, utilizing Qwen3-A3B-Instruct as the teacher with
λ
=
0.5
\lambda=0.5
.
Method
BIG Bench Audio
Audio Multi-Chall.
Voice Bench
Avg. Drop (%)
S
S
T
T
S
S
T
T
S
S
T
T
Δ
​
S
\Delta S
Δ
​
T
\Delta T
Reference (Text-only Models)
Qwen3-A22B-Instruct
–
99.10
–
35.73
–
94.09
–
–
Qwen3-A3B-Instruct
–
97.72
–
29.31
–
91.00
–
–
Qwen3-Omni-A3B-Instruct
85.67
92.10
23.57
26.14
89.22
91.04
11.29
5.51
X-OPD
93.41
96.85
28.14
28.66
89.29
91.18
3.43
0.97
w/ Qwen3-A22B-Instruct
91.91
95.29
26.62
27.86
89.60
91.67
5.55
2.23
λ
=
1.0
\lambda=1.0
(Text-only OPD)
91.76
96.01
25.44
27.62
89.70
91.21
6.91
2.43
λ
=
0.0
\lambda=0.0
(Speech-only OPD)
92.74
95.22
27.02
27.74
88.89
91.31
5.08
2.52
