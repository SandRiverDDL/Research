# Brief: Rethinking the Capacity Gap in On-Policy Distillation for Large Language Models

> Generated: 2026-06-15T07:32:51+00:00
> Source: `~/.arxiv-mcp-storage/openreview-TteFp6TLUA.md`
> Use this bounded brief instead of reading the full cached paper.

## [method] offset 9300 pattern `\n3\.1\b`

while Busbridge et al. (2025) derive general 161
distillation scaling laws for predicting student per- 162
formance. Another line of research aims to bridge 163
the teacher-student gap by constructing more suit- 164
2
# Page 3
able teacher. For example, Ding et al. (2025) em-165
ploy intermediate-sized model as teacher assistants,166
and Zhang et al. (2025b) achieve personalized dis-167
tillation through a query-level teacher router. How-168
ever, existing studies mainly focus on off-policy169
knowledge distillation, leaving the capacity-gap170
issue in OPD underexplored.171
3 Preliminaries172
3.1 Notation173
Let x ∈ D x denote a query and y = (y1, . . . , yT )174
be a response of length T . We write y<t =175
(y1, . . . , yt−1) for the prefix up to step t. A lan-176
guage model π defines a next-token distribution177
π(· | x, y<t) over a vocabulary V. We refer to178
the model being trained as the student πθ, with179
learnable parameters θ, and to a frozen reference180
model as the teacher πT . Both models share the181
same vocabulary V. Knowledge distillation trans-182
fers knowledge from πT to πθ by minimizing the183
KL divergence between the distributions P and Q:184
DKL(P ∥ Q) =
v∈V
P(v) log P(v)
Q(v) . (1)185
3.2 On-Policy Distillation186
Given a query x ∼ D x, On-policy Distillation first187
samples a response y ∼ πθ(· | x), and then the188
student-generated trajectory is forwarded through189
both πθ and πT , yielding two next-token distribu-190
tions for each prefix y<t: pt = πθ(· | x, y<t) and191
qt = πT (· | x, y<t). The standard OPD objective is192
the sequence-level reverse KL divergence between193
the student and teacher under trajectories sampled194
from the student policy, which, by autoregressive195
factorization, can be formalized as a token-level196
KL objective:197
LOPD(θ) = Ex∼Dx, y ∼πθ (·|x)
" TX
t=1
DKL(pt ∥ qt)
. (2)198
Following Agarwal et al. (2024), we do not back-199
propagate through the student’s sampling distri-200
bution πθ(· | x) that produces y. Gradients are201
computed only through πθ in the per-token KL202
terms, thereby avoiding policy-gradient optimiza-203
tion (Williams, 1992), which leads to more stable204
training.205
In practice, there are three common implemen-206
tations that differ in how the per-token reverse207
KL is computed. Sampled-token OPD is the most208
lightweight variant, evaluating only the token sam-209
pled by the student at each step and yielding an un-210
biased Monte Carlo estimator of each token-level211
KL term. Full-vocabulary OPD, at the other ex- 212
treme, computes the KL divergence over the entire 213
vocabulary at each prefix. Top-k OPD provides an 214
intermediate design by restricting the divergence 215
computation to a subset of full vocabulary. 216
Here we focus on the student top-k variant, as it 217
achieves a good trade-off between supervision fi- 218
delity and computational cost. Specifically, at each 219
prefix y<t, we select the subset St = TopK(pt, k), 220
consisting of the k tokens with the highest proba- 221
bilities under the student distribution pt. We then 222
restrict both the student and teacher distributions 223
to St and renormalize them as follows: 224
¯p(St)
t = pt ⊙ 1StP
u∈St pt(u) , ¯q(St)
t = qt ⊙ 1StP
u∈St qt(u) , (3) 225
Distillation is then performed by minimizing the 226
subset KL divergence DKL
¯p(St)
t ∥ ¯q(St)
. This yields 227
an approximation to the full-vocabulary reverse KL, 228
where probability mass outside St is discarded. 229
4 Capacity Gap in On-Policy Distillation 230
A recurring observation in traditional off-policy 231
distillation is that stronger teachers do not always 232
yield better students, a phenomenon known as the 233
capability gap. Since on-policy distillation has 234
been shown to effectively mitigate exposure bias 235
and catastrophic forgetting, a natural question is 236
whether it can also overcome the capability gap. 237
Datasets and Evaluation. We conduct our OPD 238
experiments on 10,000 prompts randomly sampled 239
from the OpenR1-Math-220k dataset1. Unless oth- 240
erwise specified, we use the default implementa- 241
tion and hyperparameter settings described in Ap- 242
pendix A. The distilled student models are eval- 243
uated on GSM8K (Cobbe et al., 2021), MATH- 244
500 (Lightman et al., 2024), and AMC (Li et al., 245
2024). Results on AIME24/25 (Balunovic et al., 246
2026) are provided as complementary evaluations 247
for strong student models. We use the EvalScope 248
framework for standardized evaluation across all 249
benchmarks and report Pass@1 accuracy averaged 250
over three independent runs. 251
Models. We study three student models span- 252
ning two model families: Qwen2.5-0.5B-Instruct, 253
Qwen2.5-3B-Instruct (Qwen et al., 2025), and 254
Qwen3-1.7B (Non-thinking) (Yang et al., 2025). 255
1https://huggingface.co/datasets/open-r1/
OpenR1-Math-220k
3
# Page 4
Setup GSM8K MA TH-500 AMC
Qwen2.5-0.5B (baseline) 44.9 29.0 9.0
+ 3B 46.9 30.0 8.9
+ 7B 45.7 32.8 9.0
+ 14B 48.5 32.8 8.2
Qwen2.5-3B (baseline) 85.8 63.8 33.6
+ 7B 84.4 60.2 27.6
+ 14B 84.0 62.0 29.1
Qwen3-1.7B (baseline) 82.9 73.6 40.3
+ Qwen3-4B 79.8 71.0 35.8
+ Qwen3-8B 80.4 70.0 41.0
+ Qwen3-14B 81.4 72.8 40.3
Table 1: Accuracy of OPD-trained students across dif-
ferent student-teacher setups. Each block begins with
the pre-distillation baseline, followed by OPD results
with same-family teachers of different sizes. We bold
numbers that show improvements from distillation. Re-
sults on AIME24/25 are reported in Appendix B.
For each student, we sweep teachers of increas-256
ing size from the same family: 3B/7B/14B for257
Qwen2.5 students, and 4B/8B/14B for the Qwen3258
student2.259
Results. Table 1 presents that stronger teach-260
ers may fail to improve the student and can even261
degrade its performance. For both Qwen2.5-3B-262
Instruct and Qwen3-1.7B, performance degradation263
is consistently observed across all teacher choices.264
These results empirically demonstrate that the ca-265
pability gap persists in OPD, consistent with obser-266
vations from concurrent work (Li et al., 2026).267
Unlike the conventional off-policy setting, where268
larger teacher-student capacity gaps usually lead to269
worse distillation outcomes, OPD shows a differ-270
ent pattern. For example, Qwen2.5-0.5B-Instruct271
achieves modest improvements on GSM8K and272
MATH-500 even with larger teachers. Moreover,273
for Qwen2.5-3B-Instruct and Qwen3-1.7B-Instruct,274
the degree of performance degradation tends to de-275
crease as teacher size increases. These findings276
motivate us to identify and understand the distinc-277
tive mechanisms underlying the capability gap in278
OPD.279
5 Mechanistic Analysis280
Having established in §4 that stronger teachers fre-281
quently fail or even degrade the student under OPD,282
we now ask why. We dissect OPD’s training signal283
through three complementary analyses, each an-284
swering one diagnostic question about a different285
2All Qwen3 models emplo

## [evaluation] offset 12666 pattern `\bexperiment`

t)
. This yields 227
an approximation to the full-vocabulary reverse KL, 228
where probability mass outside St is discarded. 229
4 Capacity Gap in On-Policy Distillation 230
A recurring observation in traditional off-policy 231
distillation is that stronger teachers do not always 232
yield better students, a phenomenon known as the 233
capability gap. Since on-policy distillation has 234
been shown to effectively mitigate exposure bias 235
and catastrophic forgetting, a natural question is 236
whether it can also overcome the capability gap. 237
Datasets and Evaluation. We conduct our OPD 238
experiments on 10,000 prompts randomly sampled 239
from the OpenR1-Math-220k dataset1. Unless oth- 240
erwise specified, we use the default implementa- 241
tion and hyperparameter settings described in Ap- 242
pendix A. The distilled student models are eval- 243
uated on GSM8K (Cobbe et al., 2021), MATH- 244
500 (Lightman et al., 2024), and AMC (Li et al., 245
2024). Results on AIME24/25 (Balunovic et al., 246
2026) are provided as complementary evaluations 247
for strong student models. We use the EvalScope 248
framework for standardized evaluation across all 249
benchmarks and report Pass@1 accuracy averaged 250
over three independent runs. 251
Models. We study three student models span- 252
ning two model families: Qwen2.5-0.5B-Instruct, 253
Qwen2.5-3B-Instruct (Qwen et al., 2025), and 254
Qwen3-1.7B (Non-thinking) (Yang et al., 2025). 255
1https://huggingface.co/datasets/open-r1/
OpenR1-Math-220k
3
# Page 4
Setup GSM8K MA TH-500 AMC
Qwen2.5-0.5B (baseline) 44.9 29.0 9.0
+ 3B 46.9 30.0 8.9
+ 7B 45.7 32.8 9.0
+ 14B 48.5 32.8 8.2
Qwen2.5-3B (baseline) 85.8 63.8 33.6
+ 7B 84.4 60.2 27.6
+ 14B 84.0 62.0 29.1
Qwen3-1.7B (baseline) 82.9 73.6 40.3
+ Qwen3-4B 79.8 71.0 35.8
+ Qwen3-8B 80.4 70.0 41.0
+ Qwen3-14B 81.4 72.8 40.3
Table 1: Accuracy of OPD-trained students across dif-
ferent student-teacher setups. Each block begins with
the pre-distillation baseline, followed by OPD results
with same-family teachers of different sizes. We bold
numbers that show improvements from distillation. Re-
sults on AIME24/25 are reported in Appendix B.
For each student, we sweep teachers of increas-256
ing size from the same family: 3B/7B/14B for257
Qwen2.5 students, and 4B/8B/14B for the Qwen3258
student2.259
Results. Table 1 presents that stronger teach-260
ers may fail to improve the student and can even261
degrade its performance. For both Qwen2.5-3B-262
Instruct and Qwen3-1.7B, performance degradation263
is consistently observed across all teacher choices.264
These results empirically demonstrate that the ca-265
pability gap persists in OPD, consistent with obser-266
vations from concurrent work (Li et al., 2026).267
Unlike the conventional off-policy setting, where268
larger teacher-student capacity gaps usually lead to269
worse distillation outcomes, OPD shows a differ-270
ent pattern. For example, Qwen2.5-0.5B-Instruct271
achieves modest improvements on GSM8K and272
MATH-500 even with larger teachers. Moreover,273
for Qwen2.5-3B-Instruct and Qwen3-1.7B-Instruct,274
the degree of performance degradation tends to de-275
crease as teacher size increases. These findings276
motivate us to identify and understand the distinc-277
tive mechanisms underlying the capability gap in278
OPD.279
5 Mechanistic Analysis280
Having established in §4 that stronger teachers fre-281
quently fail or even degrade the student under OPD,282
we now ask why. We dissect OPD’s training signal283
through three complementary analyses, each an-284
swering one diagnostic question about a different285
2All Qwen3 models employed in our experiments default
to non-thinking mode unless we specify otherwise.
aspect of the signal: (i) a correctness-controlled 286
ablation (§5.1) asks what OPD actually learns; (ii) 287
a per-token entropy analysis (§5.2) asks where its 288
gains come from; and (iii) a per-token reward anal- 289
ysis (§5.3) asks why it sometimes degrades the stu- 290
dent. Figure 2 summarizes the question and main 291
finding of each subsection. 292
5.1 Data: Supervision Quality Analysis 293
In off-policy distillation, such as SFT, an implicit 294
assumption is that the pre-collected data have been 295
filtered for correctness, so the student learns pri- 296
marily from correct reasoning paths. However, 297
OPD provides no such guarantee. On the same 298
dataset, stronger teachers may provide more correct 299
supervision, whereas smaller teachers may them- 300
selves fail on many problems. This raises a natu- 301
ral question: what does OPD actually learn? If 302
OPD mainly learns from correctness, this could ex- 303
plain the benefits sometimes observed with larger 304
teacher-student capacity gaps, given the substan- 305
tial knowledge gap between stronger and smaller 306
teachers. 307
Setup. We investigate this question by design- 308
ing rigorous controlled experiments. Using the 309
same math reasoning dataset as in §4, we con- 310
struct two correct

## [related-work] offset 6835 pattern `\brelated work\b`

111
model families, including cases where dis-112
tillation drives the student below its pre-113
distillation performance (§4).114
• Through a systematic mechanistic analysis 115
(§5) we show that (i) OPD transfers the 116
teacher’sreasoning behavior rather than its 117
problem-level knowledge; (ii) OPD’s gains 118
come from aligning the student’s per-position 119
entropy shape with the teacher’s, so pairings 120
that are already shape-aligned have no head- 121
room; and (iii) the regression is caused by 122
destructive Q3 tokens, teacher disagreements 123
at confidently-correct tokens. 124
2 Related Work 125
On-Policy Distillation. Exposure bias in off- 126
policy distillation motivates the shift to on-policy 127
distillation. MiniLLM (Gu et al., 2024) introduces 128
OPD for LLMs, optimizing the reverse KL objec- 129
tive on student-generated rollouts via policy gradi- 130
ents, while GKD (Agarwal et al., 2024) generalizes 131
this approach by directly minimizing token-level 132
divergences on mixtures of on- and off-policy data. 133
Thinking Machines Lab (Lu and Lab, 2025) demon- 134
strate that on-policy dense supervision is more effi- 135
cient than outcome-reward RL and shows promise 136
for continual learning. More recently, OPD has 137
been extended to the self-distillation setting, where 138
the student serves as its own teacher by condition- 139
ing on privileged information (Hübotter et al., 2026; 140
Shenfeld et al., 2026; Zhao et al., 2026). Concur- 141
rent studies have begun to investigate the failure 142
modes and underlying mechanisms of OPD (Li 143
et al., 2026; Fu et al., 2026). Our work further 144
contributes to this direction through an in-depth 145
analysis of the root causes underlying OPD success 146
and failure. 147
Curse of Capacity Gap. A widely observed phe- 148
nomenon in knowledge distillation is that large 149
teacher–student capacity gaps can diminish or 150
even reverse the benefits of distillation (Cho and 151
Hariharan, 2019; Mirzadeh et al., 2020). Zhang 152
et al. (2023) document the curse of capacity gap 153
in language model distillation, and subsequent 154
work extends this observation to instruction tun- 155
ing (Xu et al., 2025) and chain-of-thought distil- 156
lation (Li et al., 2025). A body of work seeks 157
to address this issue through better teacher selec- 158
tion. Zhang et al. (2025a) characterize the rela- 159
tionship between student scale and optimal teacher 160
scale, while Busbridge et al. (2025) derive general 161
distillation scaling laws for predicting student per- 162
formance. Another line of research aims to bridge 163
the teacher-student gap by constructing more suit- 164
2
# Page 3
able teacher. For example, Ding et al. (2025) em-165
ploy intermediate-sized model as teacher assistants,166
and Zhang et al. (2025b) achieve personalized dis-167
tillation through a query-level teacher router. How-168
ever, existing studies mainly focus on off-policy169
knowledge distillation, leaving the 

## [limitations] offset 34717 pattern `\blimitation`

r rather than its problem-level knowledge554
Method GSM8K MA TH-500 AMC
Qwen2.5-3B (vanilla) 85.8 63.8 33.6
+ 14B, standard OPD 84.0 62.0 29.1
+ 14B, top-20% mask 83.8 64.4 32.8
Table 6: Masking low-entropy tokens suppresses the
degradation.
(§5.1). Second, gains come from aligning the stu- 555
dent’sentropy shape with the teacher’s, so already 556
shape-aligned pairings have no headroom to gain 557
(§5.2). Third, the regression observed in such pair- 558
ings is caused by destructive Q3 tokens and can 559
be causally suppressed by masking low-entropy 560
positions during training (§5.3). 561
Limitations 562
We highlight two limitations of this work. First, all 563
experiments are conducted on math-reasoning task, 564
and it remains unclear whether the capacity gap 565
phenomenon and the identified mechanisms gener- 566
alize to other domains such as code and open-ended 567
settings. Second, due to limited computational re- 568
sources, our study is restricted to relatively small 569
student and teacher models; whether the same find- 570
ings hold at at the larger scales remains an open 571
question. 572
References 573
Rishabh Agarwal, Nino Vieillard, Yongchao Zhou, Pi- 574
otr Stanczyk, Sabela Ramos Garea, Matthieu Geist, 575
and Olivier Bachem. 2024. On-policy distillation 576
of language models: Learning from self-generated 577
mistakes. In International Conference on Learning 578
Representations, volume 2024, pages 21246–21263. 579
Mislav Balunovic, Jasper Dekoninck, Ivo Petrov, Nikola 580
Jovanovi´c, and Martin Vechev. 2026. Matharena: 581
8
# Page 9
Evaluating llms on uncontaminated math competi-582
tions. Advances in Neural Information Processing583
Systems, 38.584
Samy Bengio, Oriol Vinyals, Navdeep Jaitly, and Noam585
Shazeer. 2015. Scheduled sampling for sequence586
prediction with recurrent neural networks. Advances587
in neural information processing systems, 28.588
Dan Busbridge, Amitis Shidani, Floris Weers, Jason589
Ramapuram, Etai Littwin, and Russell Webb. 2025.590
Distillation scaling laws. In International Con-591
ference on Machine Learning , pages 5977–6045.592
PMLR.593
Howard Chen, Noam Razin, Karthik Narasimhan, and594
Danqi Chen. 2025. Retaining by doing: The role595
of on-policy data in mitigating forgetting. arXiv596
preprint arXiv:2510.18874.597
Jang Hyun Cho and Bharath Hariharan. 2019. On the598
efficacy of knowledge distillation. In Proceedings of599
the IEEE/CVF international conference on computer600
vision, pages 4794–4802.601
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,602
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias603
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro604
Nakano, Christopher Hesse, and John Schulman.605
2021. Training verifiers to solve math word prob-606
lems. arXiv preprint arXiv:2110.14168.607
Muxi Diao, Lele Yang, Wuxuan Gong, Yutong Zhang,608
Zhonghao Yan, Yufei Han, Kongming Liang, Weiran609
Xu, and Zhanyu Ma. 2026. Entropy-adaptive fine-610
tuning: Resolving confident conflicts to mitig
