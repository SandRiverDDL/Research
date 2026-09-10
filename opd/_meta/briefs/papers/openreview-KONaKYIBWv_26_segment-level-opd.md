# Brief: Segment-Level On-Policy Distillation for Long-Horizon Agents

> Generated: 2026-06-15T07:32:51+00:00
> Source: `~/.arxiv-mcp-storage/openreview-KONaKYIBWv.md`
> Use this bounded brief instead of reading the full cached paper.

## [method] offset 8405 pattern `\n3\.1\b`

T 130
and q(P)
t (v) =π (P)
T (v|s t). In our implementa- 131
tion, each PI source is encoded as a rank-16 LoRA 132
adapter over a frozen teacher; Appendix B gives 133
the full notation, OPD estimators, PI protocol, and 134
standard bounds.135
3 Phenomenology: When Token-Level136
Supervision Fails137
Standard OPD fails when the teacher’s local to- 138
ken reward becomes misaligned with the sequence- 139
level return that actually determines success. We 140
make this measurable with thealignment coeffi- 141
cient, then define the two online proxies that CHOP 142
uses for routing.143
2
# Page 3
3.1 Alignment Coefficient144
The symbol α appears in three roles: per-state αt145
(Eq. (2)), the trajectory-averaged diagnostic αdiag,146
and the population-level theory parameterα in The-147
orem 1. Definitions, estimation protocols, and the148
relationships among them are in Appendix N.149
Writing gt(v) =∇ θ logπ θ(v|st) and150
RT (v|st) = logπ T (v|st)−logπ θ(v|st), the151
per-state alignment coefficient is the cosine152
between the teacher-induced and return-aligned153
gradient directions:154
αt = ⟨Ev[gtRT ],E v[gtR⋆]⟩
∥Ev[gtRT ]∥ ∥Ev[gtR⋆]∥ ,(2)155
where R⋆(st) is the optimal sequence-level return156
estimated by N=64 teacher rollouts (SE ≤0.03).157
When αt →1 , token-level OPD is aligned; when158
αt →0 , the token gradient is locally orthogonal159
to useful sequence-level signal. The trajectory-160
averaged diagnostic αdiag =E st∼πθ[αt] is taken161
over12reference states per trajectory.162
In the failing DeepSeek-R1-0528-Qwen3-163
8B→Qwen3-8B configuration, αdiag decays164
from 0.71 to 0.09 over 300 steps while sequence-165
AUROC stays at 0.75±0.01 (Figure 2a). Across166
12 student/teacher pairs (Appendix G), final αdiag167
predicts SWE-bench resolution under standard168
OPD with Spearman 0.86 (p <0.001 ); sequence-169
AUROC has Spearman 0.31.The same decay is170
observed for token-local baselines:on the failing171
configuration, final αdiag reaches 0.09 for standard172
OPD, 0.12 for full-vocabulary GKD (Agarwal173
et al., 2024), and 0.14 for Top-K LSM (Fu et al.,174
2026), versus 0.31 for CHOP (whose segment175
branch produces gradients outside the token-local176
score span and is therefore not bound by the177
SNR-collapse argument; see Theorem 2). The178
diagnostic thus both motivates CHOP and verifies179
that CHOP partially repairs the alignment decay,180
where token-local fixes do not (Appendix J.12).181
αdiag is a diagnostic correlate, not the operative182
routing variable; routing uses ρt (§3.2), read183
cheaply from logits already available during184
training.185
3.2 Operational Proxies186
The first proxy isreliability. Fors t = (x,ˆy<t),187
ρt = exp
−λ 1H(π T (· |s t))
−λ 2DTV(πT (· |s t), πθ(· |s t))
(3)188
5 10 15 20 25 30
Output position (K tokens)
0.0
0.2
0.4
0.6
0.8
1.0
Reliability ρt (median)
(a) Reliability decays with depth and training
step 50
step 100
step 150
step 200
step 250
0.0 0.2 0.4 0.6 0.8 1.0
OPD gradient norm
−0.2
0.0
0.2
0.4
0.6
0.8
1.0
Subsequent KL reduction
(b) Effective gradient decouples at low ρt
ρt > 0.7 (r = 0.78)
ρt < 0.3 (r = 0.09)
0.0 0.2 0.4 0.6 0.8 1.0
OPD gradient norm
−0.2
0.0
0.2
0.4
0.6
0.8
1.0
Subsequent KL reduction
(c) Restoring ρt recovers gradient effectiveness
reset rollout (r = 0.71)
original low-ρt (r = 0.09)
Figure 2: αdiag tracks aggregation failure indepen-
dently of teacher quality.(a)In the failing configu-
ration, αdiag decays to 0.09 while sequence-AUROC
stays at 0.75.(b)In long-horizon math, tail-state αdiag
decays monotonically with response length; its crossing
of α⋆ ≈0.32 is consistent with the Top-K LSM plateau
as atunedregime boundary, not a universal constant.
The fitted value of α⋆ varies from 0.27 to 0.38 across
the five student/teacher pairs in Appendix J.13 and de-
pends on segment length k, vocabulary size, and the PI
corpus; we report it as a hyperparameter with sensitivity
curves rather than a derived constant.(c)Across 12 stu-
dent/teacher pairs, final αdiag predicts OPD resolution
with Spearman 0.86; sequence-AUROC has Spearman
0.31.
with (λ1, λ2) calibrated once on 1024 states and 189
then frozen. Reliability tracks whether local to- 190
ken conditionals are usable: across 50K states, ρt 191
and per-state αt have Spearman correlation 0.84. 192
A reset-rollout intervention confirms causal direc- 193
tion (Appendix O); proxy validation and outcome- 194
leakage checks are in Appendix C.195
The second proxy isPI dependence. Given the 196
available PI setP,197
ˆκt =D TV
πT (· |s t), π (P)
T (· |s t)
.(4)198
This requires no learned predictor. On 12,847 held- 199
out SWE-bench states, the high-ˆκt tail aligns with200
file selection, test-versus-implementation switches, 201
and refactoring boundaries; annotators recover 202
79% of top-decile states as critical engineering 203
decisions (Appendix L). Replacing the joint-TV 204
proxy with a Shapley-style per-source decompo- 205
sition shifts SWE-bench resolution by only +0.1206
points (Appendix H).207
The two proxies are weakly correlated (Spear- 208
man 0.18 on SWE-bench states), confirming that 209
they capture independent failure modes. A regres- 210
sion αt =a+b 1ρt+b2(1−ˆκt) explains R2 = 0.71211
of per-state alignment variance, with both coeffi- 212
cients significant ( p <0.001 ). CHOP uses this 213
decomposition directly: ρt chooses token versus 214
segment aggregation, and ˆκt chooses whether to 215
condition the teacher on PI. PI source redundancy 216
is audited in Appendix H.217
3
# Page 4
4 Counterfactual Supervision Routing:218
CHOP219
CHOP operationalises supervision-object selec-220
tion as an online two-gate routing rule. The two221
load-bearing mechanisms are the reliability gate ρt222
(granularity) and the counterfactual PI gate ˆκt; the223
four-cell partition this induces is anorganising pre-224
sentation, not a separate contribution. The frame-225
work uses three fixed hyperparameters (τ, K, La)226
and streaming quantile thresholds with no task-227
specific tuning.228
4.1 The Supervision-Object Decision229
At each student-visited state st = (x,ˆy<t), CHOP230
asks two counterfactual questions:231
(i) Is the local teacher conditional reliable?If232
yes (ρt > τ ), the next-token distribution is the233
correct supervision object. If no (ρt ≤τ ), the234
teacher’s useful information is not identifiable235
in the next-token tangent space and a segment236
continuation distribution is used instead.237
(ii) Does PI counterfactually change the teacher?238
If ˆκt =D TV(πT (·|st), π(P)
T (·|st)) exceeds239
the streaming threshold κ∗, the PI-conditional240
teacher is activated for that state. Otherwise,241
the unconditional teacher is used, avoiding242
spurious adapter capacity effects.243
The PI gate is gt =⊮[ˆκt ≥κ ∗], where κ∗ is a244
streaming 70-percentile over recent ˆκt values. The245
resulting loss is246
Lt =


DKL
πθ(·|st)
π(gtP)
T (·|st)
ρt>τ
(TRUSTED)
SW2
2
e#µ(gtP)
t , e #νt
−βR(ˆτ) logπθ(ˆyt|st)
ρt≤τ
(UNTRUSTED) ,
(5)247
where π(gt

## [evaluation] offset 23005 pattern `\bexperiment`

the standard O(ϵT) DAgger bound;391
the segment branch contributes a sublinear
|TS|392
penalty on untrusted mass; the gate-error term is393
linear in T but multiplicatively small. Combining394
Eqs. (6)–(7) with the measured constants gives a395
surrogate regime boundary α⋆ ∈[0.27,0.38] across396
the five reference pairs; the matching of α⋆ ≈0.32397
to the Top-K LSM plateau in §5.2 is a consistency398
check on a single configuration, not a prediction of399
a universal constant.1 Full statements, proofs, the400
O(1/SNR2) convergence remark, and assumption401
diagnostics are in Appendix F.402
5 Experiments403
Scope of evaluation.CHOP targets regimes404
where a measurable fraction of student-visited405
states falls below ρ⋆ ≈0.32 during training:406
AIME 2024 at 30–60K tokens (sustained low- ρ407
tail) and SWE-bench Verified at 50-turn agent408
depth. In high-ρ or short-horizon regimes (tail-state409
αdiag ≥0.5), Top-K LSM (Fu et al., 2026) already410
matches CHOP within seed noise and CHOP’s seg-411
ment branch is rarely activated; we do not claim412
improvements there.413
5.1 Setup and Baselines414
Math.Student Qwen3-8B-Base (off-the-shelf415
AIME 2024 avg@ 16: 38.4); teacher R1-0528-416
Qwen3-8B (57.0); training on DAPO-Math-17K;417
evaluation on AIME 2024/2025 and AMC 2023418
at avg@16. We instantiate the anisotropic failure419
regime of Li et al. (2026) in the Qwen3 family:420
teacher AUROC 0.75, standard OPD recovers only421
1.3% of the gap—sharper than the 5.3% floor re-422
ported in their DeepSeek experiments.423
Agentic.Primary student Qwen3-4B; teacher424
Qwen3-8B with PI adapter;OpenHands v1.x425
harness, 50-turn cap, fixed 500-instance SWE-426
bench Verified list, 600 s wall-clock per instance.427
All methods share the same harness, Docker im-428
ages, and trajectory cap; off-the-shelf Qwen3-429
4B ( 11.8%) is the reference. We additionally430
report on Qwen3-1.7B →Qwen3-8B and Llama-431
3-8B→Llama-3-70B in Table 2 (full per-pair ta-432
ble with DeepSeek-R1-Distill-Qwen pairs and433
Mixtral baselines in Appendix G). Baselines on434
the same harness: SFT, sampled-token OPD435
1PI activation is also counterfactually minimal: PI should
activate iff it changes the teacher’s Bayes action class (Theo-
rem 3).
(GKD) (Agarwal et al., 2024), DistiLLM (Ko et al., 436
2024) and DistiLLM-2 SKL (Ko et al., 2025), 437
MiniLLM (Gu et al., 2026), f-DISTILL (Wen 438
et al., 2023), sequence-level KD (Kim and Rush, 439
2016), ToDi (Jung et al., 2025), Top-K LSM (Fu 440
et al., 2026), OPSD-style all-PI distillation (Zhao 441
et al., 2026), π-Distill (Penaloza et al., 2026), 442
SOD (Zhong et al., 2026), REOPOLD (Ko et al., 443
2026), RLVR (GRPO (Shao et al., 2024)), and the444
Li et al. 2026 full recipe (Li et al., 2026). Leakage 445
checks, reproducibility, the PI-removed teacher au- 446
dit, and the alignment-coefficient curves for token- 447
local baselines are in Appendices D.6, K, J.11, 448
and J.12.449
5.2 Reliability-Decile Mechanism Test450
We test the central claim—that CHOP gains specif- 451
ically in the low-reliability regime where Top- K452
LSM plateaus—by binning tokens into ρ-deciles 453
and measuring per-decile improvement over stan- 454
dard OPD.455
In the high- ρ decile, Top-K LSM and CHOP 456
differ by +0.2 pts; below ρ⋆ ≈0.32 , Top- K457
LSM drops to ≤+0.4 and eventually turns neg- 458
ative (−0.8 in D1–D3, 95% CI [−1.8,0.1] ), while 459
CHOP maintains +2.4 to +3.2 across all low- 460
reliability deciles ( p <0.01 paired bootstrap, 461
Holm–Bonferroni). The crossing occurs at D7– 462
D6 even at 15K tokens; by 60K, 37% of mass is 463
in D1–D5, explaining the aggregate divergence in 464
Table 1. Full 8-decile table and the corresponding 465
figure are in Appendix J.6.466
5.3 Long-Horizon Mathematical Reasoning467
Table 1 sweeps response length to 60K (stress cap; 468
App. M). Standard OPD collapses below the stu- 469
dent baseline ( 28.4 at 60K, −10 pts), mirroring 470
11.8%→6.5% on SWE-bench. CHOP and Top-K471
LSM differ by ≤0.4 through 15K; the gap opens 472
once tail-state αdiag crosses α⋆ ≈0.32 (significant 473
only at ≥45 K). CHOP’s decline rate is0.11pt/K , 474
slower than 0.19 (Top-K) and 0.55 (OPD); at 475
60K CHOP holds 44.9, recovering 34.9% of the 476
38.4→57.0gap.477
Tail-position entropy at step 250 is 4.8 nats for 478
standard OPD vs. 1.2 for CHOP, and untrusted- 479
state mass reaches 68% at 60K where the segment 480
branch dominates; AIME 2025 and AMC 2023 481
show the same rank order (Appendix J.1).482
6
# Page 7
Table 1:Long-horizon mathematical reasoning,
AIME 2024 avg@16.Student baseline 38.4 (Qwen3-
8B-Base), teacher 57.0 (R1-0528-Qwen3-8B). 3 seeds,
std 0.3–1.1. CHOP vs. Top-K LSM at 60K: p=0.032
paired bootstrap. Full sweep ( 1/3/7/15/30/45/60K, all
baselines, CIs) in Appendix J.1.
Method7K15K30K60K
Standard OPD 45.2 43.8 35.6 28.4
Top-KLSM 47.848.647.2 42.8
OPSD-style 45.6 44.3 38.1 32.5
RLVR (GRPO) 43.6 44.1 42.7 38.4
Li et al. 2026 full recipe 46.5 46.4 42.1 37.3
CHOP (ours)4

## [limitations] offset 36302 pattern `\blimitation`

information 611
only when a counterfactual TV test shows that it 612
changes the teacher’s policy. Across the regimes 613
where this mechanism predicts a gain, CHOP re- 614
covers 31.7% of the anisotropic-Qwen3 gap, pre- 615
vents the OPD-induced SWE-bench regression un- 616
der a fixed OpenHands harness, and remains signif- 617
icantly stronger than token-local baselines at 60K- 618
token AIME. Equally important, the negative cases 619
are part of the result: when ρ is high or horizons 620
are short, Top- K LSM is already sufficient and 621
CHOP’s segment branch is rarely used.622
8
# Page 9
Limitations623
CHOP’s claims are intentionally bounded. The624
vanishing-SNR analysis applies to the score-span625
implementation family in §4.5, and the route-626
conditional theorem controls a routed surrogate627
R(N) rather than task accuracy or token-level KL628
without further representation calibration. The em-629
pirical regime boundaryα⋆ ∈[0.27,0.38] is a tuned,630
model-pair-dependent quantity; the streaming 70-631
percentile rule is a practical replacement, but new632
student/teacher families still require calibration.633
Evaluation is also narrower than the space of possi-634
ble agents: SWE-bench results use one OpenHands635
v1.x harness with a 50-turn cap and 600 s per in-636
stance, and PI sources are domain-specific (call637
graphs and fail-to-pass manifests for code, gold638
answers for math), so open-ended chat or general639
tool-use settings would require new deployable PI640
extractors or would reduce CHOP to its reliability641
branch. Finally, ρt is a logit-side proxy that can642
misroute confidently wrong states, and the method643
adds nontrivial overhead (+11.6% wall-clock with644
deployable PI, +36.6% with oracle PI); when most645
states are already trusted, standard OPD or Top-K646
LSM is the simpler choice.647
References648
Rishabh Agarwal, Nino Vieillard, Yongchao Zhou, Pi-649
otr Stanczyk, Sabela Ramos Garea, Matthieu Geist,650
and Olivier Bachem. 2024. On-policy distillation651
of language models: Learning from self-generated652
mistakes. InThe Twelfth International Conference653
on Learning Representations.654
Samy Bengio, Oriol Vinyals, Navdeep Jaitly, and Noam655
Shazeer. 2015. Scheduled sampling for sequence656
prediction with recurrent neural networks.Preprint,657
arXiv:1506.03099.658
Nicolas Boizard, Kevin El Haddad, Céline Hudelot,659
and Pierre Colombo. 2025. Towards cross-tokenizer660
distillation: the universal logit distillation loss for661
llms.Preprint, arXiv:2402.12030.662
Justin Chih-Yao Chen, Becky Xiangyu Peng, Pra-663
fulla Kumar Choubey, Kung-Hsiang Huang, Jiaxin664
Zhang, Mohit Bansal, and Chien-Sheng Wu. 2026.665
Nudging the boundaries of llm reasoning.Preprint,666
arXiv:2509.25666.667
Liqun Chen, Dong Wang, Zhe Gan, Jingjing Liu, Ri-668
cardo Henao, and Lawrence Carin. 2021. Wasser-669
stein contrastive representation distillation.Preprint,670
arXiv:2012.08674.671
Jang Hyun Cho and Bharath Hariharan. 2019. On

## [conclusion] offset 87728 pattern `\bconclusion\b`

, so with constants depending on projection 1559
variance and the embedding distortion of A3,1560
t∈TX
L(N)
X (st)≤c X
|TX |ϵ(N)
X .(24)1561
The
|TX | factor follows from Cauchy–Schwarz 1562
on the realised centred discrepancies:1563
t∈TX
Zt ≤
|TX |
t∈TX
t .(25)1564
If A4 fails because the segment bias is systematic 1565
rather than variance-like, this step becomes a linear 1566
bound. For Cell D, A2 controls the PI-conditioned 1567
anchor distribution and the REINFORCE term 1568
contributes a bounded-variance additive constant 1569
scaled byβ 2; both are absorbed intoc D andϵ (N)
D .1570
F.9 Conclusion and Tightness1571
Substituting the four cell bounds into Eq. (21)1572
proves Theorem 4. The constants are not tight, 1573
and the result is not a worst-case improvement 1574
over OPD. In trusted cells the bound is linear, and 1575
in low-reliability cells the sublinear statement is 1576
a segment-metric accumulation claim under A4. 1577
This is why the main text states the theorem as a 1578
diagnostic surrogate-risk bound rather than as an 1579
unconditional token-level or task-accuracy guaran- 1580
tee.1581
G Alignment Coefficient Diagnostics and1582
SNR Analysis1583
G.1 SNR Bound: Connection to Theorem 11584
The proof of Theorem 1 (Appendix F) applies 1585
to the token-level OPD gradient estimator ˆGt =1586
RT (ˆyt|st)g t(ˆyt) as a special case of the token-local 1587
family Flocal. For reference, the full scalar-SNR 1588
derivation follows. Fix a state st visited by πθ 1589
and write gt(v) =∇ θ logπ θ(v|st), RT (v|st) =1590
logπ T (v|st)−logπ θ(v|st), and the optimal se- 1591
quence return R⋆(st). Define the per-token OPD 1592
gradient estimate ˆGt =R T (ˆyt|st)g t(ˆyt) for ˆyt ∼1593
πθ(·|st).1594
20
# Page 21
Decompose the local teacher reward into the1595
projection onto the optimal-return direction and an1596
orthogonal residual:1597
RT (v|st) =α t R⋆(st) +R ⊥
t (v),
gt(v)R⊥
t (v)
⊥E v[gt(v)R⋆(st)].
(26)1598
By construction αt matches the per-state alignment1599
used in Eq. (2), so α=E t[αt]. Bounded gradients1600
(∥gt∥ ≤G ) and bounded rewards (|RT |,|R ⋆| ≤R )1601
imply that the trajectory-level estimatorPT
t=1 ˆGt1602
has1603
t ˆGt
≤α T σ ⋆,(27)1604
Std
t ˆGt
T σ R + (1−α)
T σ ⋆,(28)1605
where σ⋆, σR are the bounded variance constants1606
from A1 (controlling the single-token variance of1607
gtR⋆ andg tR⊥ respectively). Dividing,1608
SNRtoken(T)≤ α
T σ ⋆√
T σR + (1−α)
T σ⋆
= α σ⋆
σR + (1−α)σ ⋆
(29)1609
which is independent of T and vanishes as α→0
