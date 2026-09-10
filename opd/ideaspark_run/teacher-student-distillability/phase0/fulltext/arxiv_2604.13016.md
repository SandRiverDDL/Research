# Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe

paper_id: arxiv:2604.13016
tier: U
source_used: html_arxiv
warning: none

## Intro

On-policy distillation (OPD) has rapidly emerged as a core technique for large language model (LLM) post-training.
Recent industry efforts, including Qwen3
[Yang et al.,
2025
]
, MiMo
[Xiao et al.,
2026
]
and GLM-5
[Zeng et al.,
2026
]
, all adopt OPD in their post-training pipelines and report substantial gains, establishing it as a competitive complement to conventional supervised fine-tuning (SFT) and outcome-reward reinforcement learning (RL).
Thinking Machines Lab
[Lu and Lab,
2025
]
replicates the Qwen3 OPD recipe at a fraction of the RL compute cost, independently confirming that on-policy, dense supervision is a practically efficient alternative.
Unlike off-policy distillation, which trains the student on fixed teacher-generated sequences and suffers from exposure bias
[Bengio et al.,
2015
]
, OPD has the student generate its own rollouts and leverages the teacher’s per-token log-probabilities as a dense reward signal to refine behavior on states the student actually visits.
Recently, this has been extended to self-distillation settings where a single model serves as its own teacher given privileged information, demonstrating that the framework can drive continual self-improvement
[Hübotter et al.,
2026
, Zhao et al.,
2026b
, Shenfeld et al.,
2026
]
.
However, despite these successes, OPD remains poorly understood and fragile in practice.
We observe a striking failure mode: a stronger teacher can completely fail to improve a student, even when a weaker teacher succeeds from lower initial alignment.
Yet few studies have investigated why the teacher’s token-level signal steers the student distribution in the desired direction, or the conditions under which it fails.
Paper Overview
When does OPD succeed or fail?
Phenomenology (§
3
)
Two empirical patterns distinguish effective OPD:
• Thinking-pattern consistency
• Higher scores
≠
\neq
new knowledge
⇒
\boldsymbol{\Rightarrow}
Why does OPD work at token level?
Mechanism (§
4
)
Progressive alignment on high-prob tokens governs OPD.
• Overlap tokens grow steadily
• Overlap tokens alone suffice
⇒
\boldsymbol{\Rightarrow}
How to rescue failing OPD?
Recipe (§
5
)
Two strategies bridge the thinking-pattern gap:
• Off-policy cold start
• Teacher-aligned prompts
We present a systematic study of OPD training dynamics, progressing from empirical conditions through token-level mechanism to practical recipe.
Phenomenology (§
3
).
We investigate the empirical patterns that distinguish effective from ineffective OPD, and identify two governing factors.
(i) Thinking-pattern consistency
: the student and teacher should share consistent thinking patterns (e.g. higher overlap ratio in their top-
k
k
token distributions). Even when the teacher achieves higher benchmark scores, mismatched thinking patterns produce low initial overlap that training cannot fully recover.
(ii) Higher scores
≠
\neq
new knowledge
: even with consistent thinking patterns and higher benchmark scores, the teacher should offer knowledge that the student has not already acquired.
When both models are trained on the same data and recipe, they converge to similar distributions at their respective scales, leaving the teacher with little transferable signal.
Only when the teacher carries knowledge beyond what the student has already seen can OPD yield substantial gains.
We validate both conditions through reverse distillation experiments, which further reveal that OPD fundamentally learns thinking patterns rather than merely benefiting from pattern consistency, and that training dynamics can be entirely decoupled from benchmark scores.
Mechanism (§
4
).
We then investigate the token-level mechanism based on these conditions.
Across all settings studied, effective OPD exhibits a consistent signature where the student and teacher distributions become progressively more similar on student-visited states.
The high-probability tokens increasingly coincide (overlap ratio rising from 72% to 91%), the entropy gap between the two distributions narrows, and the shared top-
k
k
tokens concentrate 97–99% of the combined probability mass.
By contrast, failing runs show stagnant overlap and persistent entropy mismatch from the outset.
We further show that restricting supervision to overlap tokens alone matches full top-
k
k
performance, confirming that the overlap set is the principal locus of OPD’s gradient signal.
Recipe (§
5
).
Guided by the phenomenological analysis, we propose two complementary strategies that recover OPD in otherwise failing configurations:
(i) off-policy cold start
, a warmup SFT phase on teacher-generated rollouts before OPD that bridges the thinking-pattern gap by raising initial overlap ratio;
(ii) teacher-aligned prompt selection
, which uses prompts drawn from the teacher’s post-training data to sharpen alignment on high-probability tokens, though at the cost of substantially lower student entropy that necessitates mixing with out-of-distribution prompts.
In both cases, the recovered runs exhibit the same dynamic signature as naturally successful ones as shown in §
4
: steadily rising overlap ratio, improving token-level advantage, and a narrowing entropy gap.
Finally, we examine the cost of OPD’s dense supervision (§
6
).
We show that reward quality degrades systematically with trajectory depth and that instability originates at later tokens before propagating backward through the trajectory.
Surprisingly, even failing teachers provide reward that is globally correlated with rollout correctness, suggesting that the failure is not one of signal quality but of local optimization geometry. A larger teacher may induce a reward landscape that is locally flat around the student’s policy, making token-level gradients ineffective despite an informative global signal.
These findings reveal a fundamental tension between supervision density and supervision reliability, and point to the limitations of current OPD for long-horizon reasoning and agentic settings.

## Method

Before investigating the token-level mechanism of OPD, we first ask a broader question: what conditions govern the effectiveness of OPD?
A natural assumption is that a stronger teacher should always yield better distillation outcomes, yet we observe configurations where this fails.
We compare OPD runs under controlled settings and identify two conditions that jointly govern the outcome.
Takeaways
•
Thinking-pattern consistency.
The student and teacher should share compatible thinking patterns. Even when the teacher achieves higher benchmark scores, a large mismatch weakens the token-level distillation signal (
Section
˜
3.1
).
•
Higher scores
≠
\neq
new knowledge.
The teacher should provide knowledge beyond what the student has seen during training. Even with consistent thinking patterns and higher scores, a teacher may offer no genuinely new knowledge, leaving OPD without a driving signal (
Section
˜
3.2
).
3.1
Thinking-Pattern Consistency
Figure 2
:
OPD from two teachers with different thinking patterns into the same student (Qwen3-1.7B-Base). The GRPO teacher achieves stronger performance (left) and higher initial overlap ratio (right), suggesting that thinking pattern compatibility governs OPD effectiveness.
We first study whether OPD requires compatible thinking patterns between the student and the teacher. A stronger teacher does not guarantee better distillation: a large mismatch in reasoning pattern can weaken the distillation signal regardless of the teacher’s benchmark advantage.
Setup.
We use Qwen3-1.7B-Base
[Yang et al.,
2025
]
as the student and compare two teachers: Qwen3-4B (Non-thinking)
[Yang et al.,
2025
]
and Qwen3-4B-Base-GRPO, where the latter is obtained by applying zero-RL to Qwen3-4B-Base
[Yang et al.,
2025
]
using GRPO
[Shao et al.,
2024
]
(detailed training settings are provided in Appendix
A.1
).
Since the student is also a base model, we expect its thinking pattern to be closer to that of the GRPO-trained teacher. We conduct two OPD experiments using the DAPO-Math-17K dataset
[Yu et al.,
2025
]
, differing only in the choice of teacher model. Unless otherwise specified, all experiments use the default hyperparameters described in Appendix
A.2
and are evaluated on AIME 2024
[Li et al.,
2024
]
, AIME 2025
[Balunović et al.,
2025
]
and AMC 2023
[Li et al.,
2024
]
.
Following standard practice, we sample 16 solutions per problem with temperature 0.7 and top-
p
p
0.95, using a maximum validation response length of 31,744 tokens. We report average accuracy over 16 samples (avg@16) as the primary evaluation metric.
Figure 3
:
Validation performance of the two teachers (Qwen3-4B Non-thinking vs. Qwen3-4B-Base-GRPO) on AIME 2024, AIME 2025, and AMC 2023.
Results.
As shown in
Figure
˜
2
, distillation from Qwen3-4B-Base-GRPO consistently outperforms distillation from Qwen3-4B (Non-thinking), although the two teachers have broadly comparable performance as shown in
Figure
˜
3
.
Despite underperforming on benchmarks, the GRPO teacher exhibits a higher initial overlap ratio, suggesting that its thinking pattern aligns more closely with the student.
Although the two overlap curves converge later in training, the performance gap persists, suggesting that early-stage thinking-pattern mismatch causes a loss of distillation benefit that cannot be recovered later.
We report the validation accuracy for each benchmark individually in Appendix
A.3
, where the same overall trend holds across all datasets.
3.2
New Knowledge, Not Just Scale
Thinking-pattern consistency alone does not explain all of our observations. Even when the teacher scores higher and shares a consistent thinking pattern with the student, OPD can still fail.
Setup.
We construct two controlled comparisons across model families.
In the DeepSeek family, we use DeepSeek-R1-Distill-Qwen-1.5B (R1-Distill-1.5B)
[Guo et al.,
2025
]
as the student and compare two teachers: DeepSeek-R1-Distill-Qwen-7B (R1-Distill-7B)
[Guo et al.,
2025
]
and Skywork-OR1-Math-7B
[He et al.,
2025b
]
, where the latter is obtained by applying RL post-training to R1-Distill-7B.
In the Qwen family, we use Qwen3-1.7B (Non-thinking)
[Yang et al.,
2025
]
as the student and compare two teachers: Qwen3-4B (Non-thinking) and Qwen3-4B-Non-Thinking-RL-Math
[Yang et al.,
2026b
]
, where the latter is obtained by applying RL to Qwen3-4B (Non-thinking) on a 57K subset of DeepMath
[He et al.,
2025c
]
.
In both settings, the key contrast lies between a teacher from the same training pipeline and one that has acquired additional capabilities through further RL. All runs use the same dataset and training recipe as before.
Figure 4
:
Comparison of OPD performance with and without additional teacher RL post-training across two model families.
Left:
DeepSeek family.
Right:
Qwen family.
Post-trained teachers yield substantially stronger gains and higher teacher-student
gap recovery rate
.
Results.
As shown in
Figure
˜
4
, both families exhibit a consistent pattern.
Same-pipeline teachers
yield limited improvement, while the
post-trained teachers
produce substantially stronger gains across all benchmarks.
Importantly, the post-trained teachers not only achieve higher absolute performance but also recover a much larger fraction of the teacher-student gap, measured by the
gap recovery rate
(
Acc
after OPD
−
Acc
before OPD
)
/
(
Acc
teacher
−
Acc
before OPD
)
(\mathrm{Acc}_{\text{after OPD}}-\mathrm{Acc}_{\text{before OPD}})/(\mathrm{Acc}_{\text{teacher}}-\mathrm{Acc}_{\text{before OPD}})
.
This indicates that the additional capabilities acquired by these teachers are more transferable through OPD.
Since the post-trained teachers are derived from the same base checkpoints, their thinking patterns remain broadly aligned, which is also observed by the overlap ratio dynamic.
The improvement therefore stems from new capabilities of the teacher acquired through RL.
3.3
Validation via Reverse Distillation
We design a reverse-distillation experiment as the comparison that simultaneously validates both conditions and reveals deeper insights into the nature of OPD.
Setup.
JustRL-DeepSeek-1.5B (JustRL-1.5B)
[He et al.,
2025a
]
is obtained by RL from R1-Distill-1.5B. We now reverse this direction, using JustRL-1.5B as the student and distilling from R1-Distill-1.5B (its own pre-RL checkpoint).
We also use R1-Distill-7B as a teacher for the comparison.
Note that R1-Distill-7B achieves slightly higher benchmark scores than JustRL-1.5B, while R1-Distill-1.5B is substantially weaker.
Figure 5
:
Reverse distillation with JustRL-1.5B as the student and two same-family teachers (R1-Distill-1.5B and R1-Distill-7B). Both runs cause the student to regress to approximately the same level despite R1-Distill-7B scoring higher than JustRL-1.5B, indicating that OPD training dynamics are governed by thinking pattern rather than benchmark performance.
Results.
Figure
˜
5
reveals two striking phenomena.
First, distilling JustRL-1.5B toward R1-Distill-1.5B, its own pre-RL checkpoint, causes the student to regress almost exactly to its pre-RL performance, removing all gains acquired through RL.
Second, when we replace the teacher with R1-Distill-7B, a substantially larger and even slightly stronger model from the same family, the training trajectory is nearly indistinguishable: despite outscoring JustRL-1.5B on benchmarks, R1-Distill-7B drives the student to the same regressed level as the weaker 1.5B teacher.
Since OPD minimizes reverse KL divergence over student-generated trajectories, this convergence implies that the two teachers induce nearly identical local target distributions on student-visited states, despite their difference in scale.
These results yield several conclusions:
•
Thinking pattern matters, and OPD fundamentally learns thinking patterns.
Distilling from R1-Distill-1.5B into JustRL-1.5B causes JustRL-1.5B to regress to its pre-RL performance.
This suggests that OPD actively acquires the teacher’s thinking patterns and overwrites the student’s own. This is precisely why consistency in thinking patterns is important: if the gap is too large, the student may fail to learn effectively.
•
Benchmark performance does not predict OPD outcome.
R1-Distill-7B scores higher than JustRL-1.5B, yet the distillation produces no improvement and instead causes regression. This shows that OPD’s training dynamics can be completely independent of the teacher’s benchmark performance, and may even move in the opposite direction.
•
Higher scores do not imply new knowledge for OPD.
R1-Distill-7B and R1-Distill-1.5B are within the same model family and differ only in scale. The indistinguishable effects of the two models on the student already confirm that: (i) a higher score (R1-Distill-7B) may merely reflect a different degree of fit to the same data, rather than genuinely novel capabilities. For OPD to produce gains, the teacher should possess knowledge beyond what the student has already seen during training; and (ii) despite the difference in scale, R1-Distill-7B and 1.5B exhibit the same thinking patterns.
The reverse distillation experiments and the forward comparisons in
Sections
˜
3.1
and
3.2
consolidate the two conditions.
Thinking-pattern consistency is associated with higher initial overlap and stronger OPD outcomes, while new knowledge (such as from further post-training) enables larger transferable gains even when overlap is already high.
