# Brief: ReNIO: Reweighting Negative Trajectory Importance for LLM On-Policy Distillation

> Generated: 2026-06-15T07:32:51+00:00
> Source: `~/.arxiv-mcp-storage/openreview-kv6QSpUJbc.md`
> Use this bounded brief instead of reading the full cached paper.

## [method] offset 11815 pattern `\n3\.1\b`

ger student–teacher de-202
viations deserve more emphasis, directly motivat-203
ing ReNIO’s sample-level weighting strategy.204
3 Methodology205
Figure 2 summarizes ReNIO. We ﬁrst formal-206
ize the on-policy distillation setup (Section 3.1),207
then describe three design components: a preﬁx-208
computable student–teacher log-ratio signal for209
SGO quality (Section 3.2), ﬁxed-threshold key-210
token selection (Section 3.3), and geometric-mean211
aggregation into a normalized sample weight (Sec-212
tion 3.4). Finally, we integrate the weight into the213
distillation objective (Section 3.5).214
3.1 Problem Setup215
Consider a student policy πS and a teacher policy216
πT . Given a prompt x sampled from the training217
prompt distribution D, on-policy distillation ﬁrst218
samples a student-generated output (SGO) y =219
(y1, . . . , yn) ∼ πS(·|x), and then asks the teacher 220
to provide token-level supervision on the same 221
student-visited preﬁxes. For a model M ∈ {S, T }, 222
we write 223
M (v) = πM (v|x, y<t) (1) 224
for the next-token distribution at position t. We 225
also use πM (y|x) as shorthand for the collection 226
of preﬁx-conditioned distributions {pt
M }n
t=1 along 227
the sampled SGO, rather than only the probability 228
of the completed sequence. 229
Standard OPD trains the student by matching 230
its preﬁx-conditioned distributions to the teacher’s 231
distributions on every sampled SGO. We deﬁne 232
the sequence-level distillation divergence along y 233
as the sum of token-level divergences over all vis- 234
ited preﬁxes: 235
D(πS(y|x)∥πT (y|x)) =
t=1
d(pt
S, pt
T ), (2) 236
where d(·, ·) is the distribution divergence, like 237
FKLD, RKLD. Thus, D does not denote a sin- 238
gle divergence between two completed-sequence 239
probabilities; it denotes the accumulated teacher– 240
student discrepancy along the sampled SGO pre- 241
ﬁxes. The unweighted on-policy objective is there- 242
fore 243
LOPD = Ex∼D, y∼πS (·|x)
D(πS(y|x)∥πT (y|x))
(3) 244
In this objective, every SGO contributes equally 245
even though Section 2 shows that different SGOs 246
can affect learning in substantially different ways. 247
3.2 Finding an Information Signal for SGO 248
Quality 249
The central challenge is to identify high-value 250
SGOs without using their ﬁnal answers. Sec- 251
3
# Page 4
1 Student-Teacher Log Ratio
Student-Generated Trajectory(SGO)
5 + 3 12 ^2 =...
Student conditional probability
Teacher conditional probability
...
...
0.90 0.90 0.90 0.70 0.80 0.90
...
0.10 0.90 0.90 0.01 0.70 0.90
Student-Teacher Log Ratio
2.1 0.0 0.0 4.2 0.1 0.0... ...
Output: Token log ratio
2 Key Token Information Selection
2.1 4.2... ...
Threshold-based Selection
Select tokens with
Outlier Clipping
Clip the selected log-ratio to ( ,c] (c=3,for example)
2.1 4.22.1 3.0
Output: Clipped key token log ratio set
),|( <ttS yxyP
),|(
),|(log=
ttT
ttS
t yxyP
yxyPd
τdt >
3 Information Aggregation
Mean of log ratio, with batch normalization
Output: Final sample weight (example)
exp{ ( + ) / 2 }2.1 3.0
Batch-Level Normalization
1.5
),|( <ttT yxyP
...
...
0.0 0.0 0.0 0.0
}{ td
(a) Overall pipeline of ReNIO.
... She has 9 * 2 = <<<< 9 * 2 = 18 >>ANS
... She has 13 * 2 = << 13 * 2 26= >>
...
...SGO
0.67 0.76 0.21 0.00 1.00 0.99 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00
0.74 0.36 0.78 0.13 0.98 0.96 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00
Teacher
Student
(b) An example about how the pivotal tokens leading to a wrong trajectory, and teacher/student probilities on these tokens.
Figure 2: Overview of the proposed ReNIO.Phase I computes the student–teacher log ratio along the SGO; Phase II
selects pivotal tokens with a ﬁxed threshold; Phase III aggregates selected log ratios into a normalized sample-level
weight.
tion 2 suggests that incorrect SGOs can play a dis-252
tinct and useful role in OPD, but directly weight-253
ing trajectories by correctness would require com-254
plete answer-containing rollouts. ReNIO therefore255
looks for a preﬁx-computable signal that indicates256
when a student trajectory is likely to contain an in-257
formative failure.258
The signal should focus on branching decisions259
rather than all tokens. A reasoning trajectory usu-260
ally becomes wrong after a small number of lo-261
cal choices redirect an otherwise plausible solu-262
tion path. In Figure 2b, for example, the stu-263
dent chooses “13” at a critical step. Because264
this token is sampled from the student policy, it265
has relatively high probability under πS(·|x, y<t);266
because it moves the solution away from the267
teacher-preferred path, it has low probability un-268
der πT (·|x, y<t). Such key tokens therefore have269
a large student-to-teacher probability ratio. After270
the wrong branch is taken, later tokens are con-271
ditioned on the same mistaken preﬁx, so teacher– 272
student disagreement may shrink again. We there- 273
fore use the student-to-teacher ratio to locate the 274
local decisions where the student is conﬁdent and 275
the teacher rejects the sampled choice. 276
Token-level importance score. For each sam- 277
pled token yt in an SGO, we deﬁne the student- 278
to-teacher ratio 279
rt = πS(yt | x, y<t)
πT (yt | x, y<t) , (4) 280
and its log form 281
ℓt = log rt
= log πS(yt | x, y<t) − log πT (yt | x, y<t).
(5) 282
A large rt means that the sampled token is much 283
more likely under the student than under the 284
teacher. We treat high-ratio tokens as pivotal to- 285
4
# Page 5
(a) OPD
(b) OPSD
Figure 3: Distribution of token-level log ratios ℓt on
SGOs in the Qwen3 mathematical reasoning setting.
Both OPD and OPSD exhibit long-tailed distributions:
most tokens have small log ratios, while a small num-
ber of tokens exhibit large student–teacher disagree-
ment.
kens: local decisions where the SGO departs from286
the teacher-preferred reasoning direction.287
The log ratio also has an optimization inter-288
pretation. Under a preﬁx-level reverse-KL objec-289
tive KL(pt
S∥pt
T ), the effective gradient weight of290
a student-sampled token is log πS(yt | x, y<t) −291
log πT (yt | x, y<t) = ℓt up to a removable base-292
line (Appendix A). Thus, ℓt is both a disagreement293
signal and a token-level corrective weight. Re-294
NIO uses this preﬁx-computable token signal as295
evidence for sample-level SGO importance, pre-296
serving OPD’s ability to train on truncated preﬁxes297
without observing the ﬁnal answer.298
3.3 Selecting Key Tokens from Long-Tailed299
Log Ratios300
The previous section shows that pivotal tokens301
should have large student-to-teacher ratios. Next302
step is to identify these tokens within a SGO.303
Figure 3 shows the empirical distribution of304
ℓt in the Qwen3 mathematical reasoning setting.305
Under both OPD and OPSD, the distribution is306
strongly long-tailed: most tokens have ℓt really307
close to zero, which means student and teacher308
align well on most tokens in SGO, while only a309
small subset has much larger values. This pattern310
matches the intuition from Section 3.2

## [evaluation] offset 469 pattern `\bexperiment`

Source: https://openreview.net/pdf?id=kv6QSpUJbc
# Page 1
ReNIO: Reweighting Negative Trajectory Importance for LLM On-Policy
Distillation
Anonymous ACL submission
Abstract001
On-policy distillation (OPD) improves LLM002
reasoning by training a student model on its003
own generated outputs, but standard OPD004
treats all student-generated outputs (SGOs)005
equally regardless of their informativeness.006
We observe a consistent asymmetry in con-007
trolled ﬁltering experiments: in both OPD and008
on-policy self distillation (OPSD), training009
only on incorrect SGOs outperforms training010
only on correct ones. Our further analysis011
suggests that models trained on correct-only012
SGOs tend to generate shorter reasoning traces013
and show weaker reﬂection behavior, while014
incorrect SGOs better preserve exploratory015
reasoning near the model’s capability bound-016
ary. To exploit this signal without requiring017
full answer-containing rollouts, we introduce018
ReNIO, which Reweights Negative trajectory019
Importance for LLM On-policy distillation.020
By using the student-to-teacher probability021
ratio, ReNIO identiﬁes pivotal tokens leading022
to wrong reasoning traces and aggregates their023
information into a normalized sample weight,024
inherently assigning larger weights to likely025
negative trajectories without observing the026
correctness of ﬁnal-answer. Since ReNIO only027
uses preﬁx-conditioned token probabilities,028
it preserves OPD’s preﬁx training advantage029
over full-rollout reinforcement learning.030
Across both mathematical reasoning and031
code generation tasks, ReNIO improves both032
OPD and OPSD, with representative relative033
gains of up to 8.90% for Qwen3-1.7B and034
10.00% for R1-Distill-Qwen-7B on mathe-035
matical reasoning benchmarks. Code repo:036
https://anonymous.4open.science/r/ReNIO-037
22CDAHGKJH612038
1 Introduction039
Reinforcement learning (RL) and on-policy dis-040
tillation (OPD) are becoming two mainstream041
paradigms for post-training large language models042
(LLMs) on reasoning tasks ( Ke et al. , 2026; Chen043
et al. , 2026). RL methods sample on-policy rea- 044
soning trajectories and update the model accord- 045
ing to externally returned rewards ( Y u et al., 2025; 046
Bai et al. , 2025; Zhihong Shao , 2024; DeepSeek- 047
AI et al. , 2025). OPD, in contrast, trains on 048
student-generated outputs (SGOs) by aligning the 049
student’s token-level distributions with teacher dis- 050
tributions along the same sampled trajectories ( Lu 051
and Lab , 2025; Agarwal et al. , 2023). This gives 052
OPD a more dense supervision signal: while RL 053
typically receives sparse sequence-level rewards 054
and must address credit assignment over long tra- 055
jectories, OPD can provide token-wise feedback at 056
every visited preﬁx. 057
OPD also has a substantial training-cost advan- 058
tage because it can learn from short SGO preﬁxes 059
instead of full answer-containing rollouts with just 060
little performance degradation ( Zhang et al., 2026; 061
Zhao et al. , 2026). In comparison, reinforcement 062
learning for reasoning tasks must observe the ﬁnal 063
answer of an on-policy reasoning trajectory before 064
assigning a reward (Wen et al., 2025). For difﬁcult 065
reasoning problems, obtaining this answer may 066
require generating very long trajectories, which 067
makes RL substantially more expensive in gener- 068
ation, memory, and training time. 069
These two advantages make OPD attractive for 070
efﬁcient reasoning post-training, but they also shift 071
the bottleneck from obtaining supervision to de- 072
ciding which student-generated preﬁxes deserve 073
more training emphasis. Standard OPD and on- 074
policy self distillation(OPSD)( Zhao et al. , 2026) 075
assign equal training weight to all SGOs, even 076
though on-policy trajectories can differ greatly 077
in how much useful learning signal they con- 078
tain. Our controlled ﬁltering experiments re- 079
veal a counterintuitive but consistent asymmetry: 080
under both OPD and on-policy self-distillation 081
(OPSD) ( Zhao et al. , 2026), training only on in- 082
correct SGOs consistently outperforms training 083
only on correct SGOs. Further behavioral analy- 084
1
# Page 2
sis shows that correct-only training tends to pro-085
duce shorter responses with fewer reﬂection-style086
markers, whereas incorrect-only training better087
preserves exploratory and self-corrective reason-088
ing. These ﬁndings suggest that negative trajecto-089
ries can expose valuable process-level correction090
signals for the student’s own failure modes, and091
may therefore play a more important role in OPD.092
Hence, it’s important to emphasize incorrect tra-093
jectories during OPD. The challenge is to empha-094
size informative negative trajectories without ob-095
serving whether the ﬁnal answer is correct. A096
direct correctness-based weighting rule would re-097
quire rolling out each SGO until the answer ap-098
pears, which would r

## [related-work] offset 27866 pattern `\brelated work\b`

with truly high-disagreement to- 459
kens, they dilute the signal from pivotal decisions. 460
Consistently, removing threshold-based selection 461
still improves over OPD but only reaches 40.83, 462
below the full ReNIO result. 463
Batch-wise normalization has the largest effect 464
among the ablations. Without it, the average 465
drops to 39.54. This is expected because ReNIO’s 466
sample weights directly scale the distillation loss 467
and therefore the gradient magnitude; without nor- 468
malization, the effective objective scale can vary 469
across batches and destabilize training. 470
5 Related Work 471
Classical knowledge distillation transfers teacher 472
behavior to a student on ﬁxed data or teacher- 473
7
# Page 8
Model Math Tasks Coding Tasks
AIME24 AIME25 HMMT25 Avg HumanEval+ MBPP+ Avg
Teacher: Qwen3-8B
Qwen3-1.7B 51.33 36.00 23.33 36.89 73.63 57.21 65.42
w/ OPD 54.44 39.16 27.50 40.37 74.40 62.43 68.42
w/ OPD+ReNIO 54.72+0.51% 43.06+9.96% 28.33+3.02% 42.04+4.14% 75.00+0.81% 63.56+1.81% 69.28+1.26%
Teacher: DS-R1-Qwen-7B
DS-R1-Qwen-1.5B 27.78 22.78 14.44 21.67 49.09 41.07 45.08
w/ OPD 28.89 23.06 14.44 22.13 50.15 41.14 45.65
w/ OPD+ReNIO 29.72+2.87% 23.89+3.60% 16.67+15.44% 23.43+5.87% 50.91+1.52% 41.20+0.15% 46.06+0.90%
Table 2: Results of methods that require an additional teacher model.
Method AIME24 AIME25 HMMT25 Avg
OPSD(1024) 53.06 41.94 27.50 40.83
/w ReNIO 57.78 42.78 27.78 42.78
OPSD(4096) 53.33 37.22 25.56 38.70
/w ReNIO 53.33 43.06 25.28 40.56
OPD(1024) 54.44 39.16 27.50 40.37
/w ReNIO 54.72 43.06 28.33 42.04
OPD(4096) 56.11 42.20 25.83 41.38
/w ReNIO 56.39 41.94 28.61 42.31
Table 3: Effect of SGO preﬁx length on Qwen3-
1.7B OPSD and OPD mathematical reasoning perfor-
mance. Scores are Avg@ 12 over AIME24, AIME25,
and HMMT25. 1024 and 4096 denote the maximum
training-preﬁx length; 4096 can almost cover the ﬁnal
answer of an SGO in our setting.
generated targets ( Hinton et al. , 2015), but this of-474
ﬂine setting can suffer from exposure bias in LLM475
post-training. On-policy distillation reduces this476
mismatch by sampling trajectories from the stu-477
dent policy and applying teacher supervision on478
the visited preﬁxes ( Agarwal et al. , 2024, 2023;479
Lu and Lab , 2025; Gu et al. , 2023). Recent OPD480
studies cover self-distillation ( Zhao et al. , 2026;481
Shenfeld et al. , 2026; Hubotter et al. , 2026; Ku-482
janpää et al. , 2024; Y e et al. , 2026; Stein et al. ,483
2026), mechanism analysis ( Kim et al. , 2026a;484
Zhang et al. , 2026; Li et al. , 2026; Y ang et al. ,485
2026), training stabilization ( Ko et al. , 2026), and486
better use of student-generated outputs ( Xu et al. ,487
2024; Ko et al. , 2025; Lyu et al. , 2025; Peng488
et al. , 2025). Closest to our work, some meth-489
ods reweight tokens or samples in OPD ( Wen490
et al., 2025; Zheng et al. , 2026; Hou et al. , 2026),491
but their weighting or calibration signals require492
knowing whether an SGO reaches the correct an-493
swer. ReNIO instead c

## [limitations] offset 31747 pattern `\blimitation`

training strategy that em- 501
phasizes negative trajectories without observing 502
ﬁnal-answer correctness. We propose ReNIO, a 503
preﬁx-computable reweighting method that iden- 504
tiﬁes pivotal tokens through student-to-teacher log 505
ratios and aggregates them into normalized sample 506
weights. Because ReNIO does not require the an- 507
swer of an SGO for weighting, it preserves OPD’s 508
advantage over RL by allowing training on SGO 509
preﬁxes. Across mathematical reasoning and code 510
generation tasks, ReNIO improves both OPD and 511
OPSD while preserving short-preﬁx training. 512
Limitations 513
We evaluate ReNIO across multiple model fami- 514
lies and task domains, showing consistent gains 515
on mathematical reasoning and code generation. 516
However, due to hardware constraints, we have not 517
8
# Page 9
veriﬁed its effectiveness on larger-scale models.518
Ethics Statement519
Our experiments use publicly available models,520
public benchmark datasets, and model-generated521
on-policy trajectories. We do not collect private522
user data, conduct human-subject studies, or use523
personally identiﬁable information. To the best of524
our knowledge, our use of these resources follows525
their intended research purposes and does not in-526
troduce known intellectual-property, ethical, or le-527
gal disputes.528
Use of AI Assistants529
We use AI assistants to help enrich our writing and530
ﬁnish experiments.531
Reproducibility Statments532
To support reproducibility, we provide code and533
detailed g uidelines for running the experiments.534
We will include the code, and relevant experi-535
mental resources in a supplementary package sub-536
mitted through Ope nReview. Upon acceptance,537
we will publicly release all rel evant materials on538
GitHub.539
References540
Rishabh Agarwal, Nino Vieillard, Piotr Stanczyk,541
Sabela Ramos, Matthieu Geist, and Olivier Bachem.542
2024. On-policy distillation of language models:543
Learning from self-generated mistakes . In Proceed-544
ings of the 12th International Conference on Learn-545
ing Representations.546
Rishabh Agarwal, Nino Vieillard, Y ongchao Zhou, Pi-547
otr Staczyk, Sabela Ramos, Matthieu Geist, and548
Olivier Bachem. 2023. On-policy distillation of lan-549
guage models: Learning from self-generated mis-550
takes. In International Conference on Learning Rep-551
resentations.552
Kimi Team Yifan Bai, Yiping Bao, Guanduo Chen, Jia-553
hao Chen, Ningxin Chen, Ruijue Chen, Y anru Chen,554
Y uankun Chen, Y utian Chen, Zhuofu Chen, Jialei555
Cui, Haochen Ding, Meng xiao Dong, Angang Du,556
Chenzhuang Du, Dikang Du, Y ulun Du, Y u Fan,557
Yichen Feng, and 149 others. 2025. Kimi k2: Open558
agentic intelligence.559
Kedi Chen, Dezhao Ruan, Y uhao Dan, Y aoting Wang,560
Siyu Y an, Xuecheng Wu, Yinqi Zhang, Qin Chen,561
Jie Zhou, Liang He, Biqing Qi, Linyang Li, Qipeng562
Guo, Xiaoming Shi, and Wei Zhang. 2026. A sur-563
vey of inductive reasoning for large language mod-564
els. Preprint, arXiv

## [conclusion] offset 31003 pattern `\bconclusion\b`

.16 27.50 40.37
ReNIO Y es Y es Y es 54.72 43.06 28.33 42.04
w/o clipping Y es No Y es 53.61 42.22 24.44 40.09
w/o threshold No Y es Y es 55.28 41.94 25.28 40.83
w/o batch norm Y es Y es No 51.94 41.39 25.28 39.54
Table 4: Component ablation of ReNIO under OPD
on Qwen3-1.7B mathematical reasoning. “Key” de-
notes threshold-based key-token selection, “Clip” de-
notes log-ratio clipping, and “Norm” denotes batch-
wise weight normalization. Scores are Avg@ 12 on
AIME24, AIME25, and HMMT25.
abilities, preserving OPD’s short-preﬁx advantage 496
while emphasizing likely negative trajectories. 497
6 Conclusion 498
This paper shows that incorrect SGOs can pro- 499
vide especially useful supervision for on-policy 500
distillation, motivating a training strategy that em- 501
phasizes negative trajectories without observing 502
ﬁnal-answer correctness. We propose ReNIO, a 503
preﬁx-computable reweighting method that iden- 504
tiﬁes pivotal tokens through student-to-teacher log 505
ratios and aggregates them into normalized sample 506
weights. Because ReNIO does not require the an- 507
swer of an SGO for weighting, it preserves OPD’s 508
advantage over RL by allowing training on SGO 509
preﬁxes. Across mathematical reasoning and code 510
generation tasks, ReNIO improves both OPD and 511
OPSD while preserving short-preﬁx training. 512
Limitations 513
We evaluate ReNIO across multiple model fami- 514
lies and task domains, showing consistent gains 515
on mathematical reasoning and code generation. 516
However, due to hardware constraints, we have not 517
8
# Page 9
veriﬁed its effectiveness on larger-scale models.518
Ethics Statement519
Our experiments use publicly available models,520
public benchmark datasets, and model-generated521
on-policy trajectories. We do not collect private522
user data, conduct human-subject studies, or use523
personally identiﬁable information. To the best of524
our knowledge, our use of these resources follows525
their intended research purposes and does not in-526
troduce known intellectual-property, ethical, or le-527
gal disputes.528
Use of AI Assistants529
We use AI assistants to help enrich our writing and530
ﬁnish experiments.531
Reproducibility Statments532
To support reproducibility, we provide code and533
detailed g uidelines for running the experiments.534
We will include the code, and relevant experi-535
mental resources in a supplementary package sub-536
mitted through Ope nReview. Upon acceptance,537
we will publicly release al
