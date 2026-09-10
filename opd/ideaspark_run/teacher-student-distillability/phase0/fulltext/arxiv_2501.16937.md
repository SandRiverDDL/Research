# TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models

paper_id: arxiv:2501.16937
tier: U
source_used: html_arxiv
warning: none

## Intro

Large language models are too large.
Causal language models (
LMs
) are increasingly becoming essential tools across various sectors
(Malinka et al.,
2023
; Wu et al.,
2023
; Zhang et al.,
2023a
; He et al.,
2024
)
. Scaling data size, model size, and training steps has been the primary approach to improve LM performance
(Kaplan et al.,
2020
; Hoffmann et al.,
2022
; OpenAI et al.,
2024
)
, leading to rapid advancements in both proprietary and open-source LMs
(Touvron et al.,
2023
; Abdin et al.,
2024
; Yang et al.,
2024
)
.
However, the success of large LMs creates challenges: they are too large for edge devices
(Qu et al.,
2024
; Thawakar et al.,
2024
; Liu et al.,
2024
)
, have decoding times too long for real-time applications
(Wan et al.,
2023
; Leviathan et al.,
2023
; Miao et al.,
2024
)
, and consume significant energy resources
(Luccioni et al.,
2023
; Faiz et al.,
2024
)
. This paradox of scale hinders the widespread deployment and use of LMs despite their potential and high demand.
Knowledge distillation offers a promising prescription.
One promising approach to developing compact yet high-performing models is knowledge distillation (
KD
)
(Hinton et al.,
2015
)
.
KD aims to transfer the knowledge, specifically the predicted distributions, from a well-trained, high-capacity teacher model to a more compact student model, often achieving better performance than small models trained solely
(Buciluundefined et al.,
2006
; Ba & Caruana,
2014
; Hinton et al.,
2015
)
.
In the context of compressing large LMs, KD is becoming a mainstream approach, with many specialized KD methods actively being developed
(Xu et al.,
2024
; Team et al.,
2024
; Muralidharan et al.,
2024
)
.
The formidable, unresolved challenge of teacher-student differences.
Nevertheless, KD is not a flawless method, and two significant issues remain, both stemming from the differences between teacher models and the student models.
(i)
Capacity gap
—
the substantial capacity gap between a large teacher model and compact student model makes effective knowledge transfer more difficult
(Mirzadeh et al.,
2020
; Cho & Hariharan,
2019
; Zhang et al.,
2023b
)
. As LMs continue to grow in size and complexity, this capacity gap becomes increasingly pronounced, making it even more challenging to distill knowledge effectively.
(ii)
Mode averaging and mode collapse
—
due to the disparity in model capacity,
KD methods often struggle with mode-averaging and mode-collapse issues, where student models either fail to oversmooth rich output distributions of a teacher model or
become overly focused on specific modes
(Wen et al.,
2023
; Gu et al.,
2024
; Agarwal et al.,
2024
)
.
Figure 1:
Comparison of standard KD and TAID.
(Left)
Standard KD methods typically employ direct optimization towards a fixed teacher distribution.
(Right)
TAID creates a dynamic bridge through adaptive, time-dependent
intermediate teacher
distributions (green dashed lines), enabling gradual optimization of the student. This approach facilitates a flexible transition from the student’s initial distribution towards the teacher’s distribution over time, effectively addressing the capacity gap and balancing knowledge transfer across varying model sizes.
A new method to overcome the teacher-student difference.
To overcome the fundamental issue of differences between teacher and student models,
we introduce Temporally Adaptive Interpolated Distillation (
TAID
), a new approach to KD for LMs.
TAID reduces the gap between teacher and student model throughout the training process by dynamically introducing an
intermediate teacher
that interpolates teacher and student models to provide a target distribution with a modest capability (see Figure
1
).
This simple technique allows for learning a higher-quality student model than with existing KD methods (Section
6
),
scales student’s performance with teacher’s size even under large capacity gaps (Section
6.3.2
),
and suppresses mode-averaging and mode-collapse issues theoretically and empirically (Section
4
and
6.3.3
).
Our main contributions to this paper are as follows:
•
We introduce TAID (Section
3
), a new knowledge distillation method that reimagines the distillation process as a dynamic, adaptive knowledge transfer from student to teacher distributions. This approach addresses common challenges in distilling large language models.
•
We provide a theoretical analysis of TAID (Section
4
) with a regression model as a proxy to the language modeling objective, demonstrating its ability to prevent mode collapse in the distillation process.
This theoretical guarantee sets TAID apart from traditional self-distillation methods, which can suffer from mode collapse.
•
We conduct extensive experiments (Section
6
) across various model sizes and architectures, demonstrating TAID’s superiority in both instruction tuning and pre-training scenarios. Moreover, we experimentally reveal TAID’s robustness to capacity gaps (Section
6.3.2
), and its ability to balance between mode averaging and mode collapse, unlike existing KD methods (Section
6.3.3
).
•
We demonstrate TAID’s practical impact by developing two state-of-the-art compact models (Section
7
):
TAID-LLM-1.5B
achieves the best performance for language models under 2B parameters, while
TAID-VLM-2B
outperforms vision-language models up to 4B parameters, showcasing TAID’s effectiveness across different domains.

## Method

TAID distills from the intermediate distribution
p
t
subscript
𝑝
𝑡
p_{t}
italic_p start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT
, partially containing the student model
q
θ
subscript
𝑞
𝜃
q_{\theta}
italic_q start_POSTSUBSCRIPT italic_θ end_POSTSUBSCRIPT
as the mixture component.
This may apparently cause the collapse because student’s modes are amplified repeatedly during the fitting recursion.
Such a collapse phenomenon has been theoretically observed for self-distillation, where the teacher and student models are identical
(Mobahi et al.,
2020
)
.
We aim to demonstrate that TAID avoids mode collapse, unlike self-distillation.
We borrow the analysis framework of
Mobahi et al. (
2020
)
to study least-square regression as a proxy to language modeling.
In each training step, the student model is updated by fitting to the interpolated label
(
1
−
t
)
⁢
y
t
+
t
⁢
y
teacher
1
𝑡
subscript
𝑦
𝑡
𝑡
subscript
𝑦
teacher
(1-t)y_{t}+ty_{\text{teacher}}
( 1 - italic_t ) italic_y start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT + italic_t italic_y start_POSTSUBSCRIPT teacher end_POSTSUBSCRIPT
, where
y
t
subscript
𝑦
𝑡
y_{t}
italic_y start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT
and
y
teacher
subscript
𝑦
teacher
y_{\text{teacher}}
italic_y start_POSTSUBSCRIPT teacher end_POSTSUBSCRIPT
are the labels of the current student and teacher models, respectively, and
t
𝑡
t
italic_t
is the interpolation parameter (being linearly increased) at the current step.
Here, we suppose the student model achieves
ϵ
italic-ϵ
\epsilon
italic_ϵ
-interpolation
of the training signals so that the regression loss is minimized near-perfectly in each time step.
Theorem 4.1
(Non-collapse Nature (Informally))
.
Suppose we run distillation for
T
𝑇
T
italic_T
steps in total.
If the teacher model has sufficiently large signals so that the label is at least as large as
Ω
⁢
(
T
⁢
ϵ
)
Ω
𝑇
italic-ϵ
\Omega(\sqrt{T\epsilon})
roman_Ω ( square-root start_ARG italic_T italic_ϵ end_ARG )
, then the student model does not collapse for any time
t
𝑡
t
italic_t
.
Notably, self-distillation inevitably collapses for sufficiently large steps
(Mobahi et al.,
2020
, Proposition 4)
, corroborating the benefit of the intermediate distribution and its adaptive update.
The formal statement and more discussions can be found in Appendix
B
.
