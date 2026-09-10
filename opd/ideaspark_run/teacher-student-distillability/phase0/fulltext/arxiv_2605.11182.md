# The Many Faces of On-Policy Distillation: Pitfalls, Mechanisms, and Fixes

paper_id: arxiv:2605.11182
tier: U
source_used: pdf_arxiv_pymupdf
warning: none

## Intro

On-policy distillation (OPD) [1, 2] is a promising post-training algorithm for large language models
(LLMs). Instead of training on off-policy responses, OPD trains the student on trajectories sampled
from its own policy and uses one or more teacher models to provide dense token-level supervision
along these on-policy rollouts. This makes OPD appealing as a practical mechanism for integrating
the capabilities of multiple stronger teachers into the student [3, 4], mitigating catastrophic forgetting,
and improving sample efficiency [5, 6]. A closely related topic is on-policy self-distillation (OPSD),
where the teacher is not a stronger model but the student model itself conditioned on additional
privileged information (PI) [7–9]. The PI may include ground-truth answers, system prompts or user
preferences. These methods are attractive for post-training because they can convert teacher behavior
or training-time context into supervision on the student’s own state distribution.
Despite the conceptual simplicity, the empirical behavior of OPD and OPSD remains poorly under-
stood. Prior work has reported successful applications of self-distillation for context internalization
and reasoning [7–9]. However, recent studies argue that on-policy (self) distillation can be unstable
and may degrade performance [10, 11]. These mixed results raise a basic question: when do OPD
and OPSD actually work, when do they fail, and what mechanisms explain the difference?
∗Co-second authorship
†Work done during an internship at UIUC.
Preprint.
arXiv:2605.11182v2  [cs.AI]  24 May 2026

OP(S)D Design Space
OPD Success/Failure Scenario
Teacher 
Construction
Privileged
Information
Distillation 
Loss Design
Self (OPSD)
Frozen Teacher
EMA Teacher
None
Answer Only
Full Response
System Prompt
Full-vocab KL
Sampled-Token PG
Top-K Reverse KL
Stop Grad Top-K
OPD sometimes fails in reasoning tasks.
Improvements for OPD 
OPD succeeds in prompt internalization and style learning.
Why Does OP(S)D Fail?
Figure 1: Overview. We map the OP(S)D design space (left, top) and its task-dependent success/fail-
ure behavior (left, bottom), identify three failure mechanisms—prefix-distorted teacher state, biased
Top-K reverse-KL, and PI-marginalized OPSD policy (middle), and propose practical fixes: stable
Top-K losses, SFT stabilization, and RLVR-adapted teachers (right).
In this paper, we present a comprehensive empirical study of OPD and OPSD across both successful
and failing regimes. On reasoning tasks, OPD provides only conditional benefits and can suffer from
length explosion, repetition, and teacher-student mismatch, while OPSD fails in our tested math
reasoning settings. In contrast, OPSD is effective for system-prompt internalization and alignment,
where the privileged information induces a shared latent behavior that can be compressed into a
PI-free policy at test time.
We identify three mechanisms behind these outcomes. First, student-generated prefixes can move
the teacher into states where its token-level supervision is locally incompatible with the student’s
trajectory. Second, Top-K reverse-KL approximations can introduce biased gradients and destabilize
optimization. Third, OPSD only learns a single PI-free consensus policy across PI-conditioned
teachers, which is insufficient when PI is instance-specific.
Motivated by these findings, we study practical stabilizers for OPD: a stop-gradient Top-K KL
surrogate that removes the biased gradient term, Reinforcement Learning with Verifiable Rewards
(RLVR) adaptation of the teacher to improve task performance, and Supervised Fine-Tuning (SFT)
the student to improve output format and stabilize response-length dynamics.
Our contributions are:
• We empirically study when OPD and OPSD succeed or fail in reasoning, system-prompt
internalization, and alignment.
• We identify three failure mechanisms: prefix-induced teacher-student mismatch, biased
TopK reverse-KL gradients, and OPSD’s PI-free aggregation across instance-specific PI.
• We propose practical stabilizers based on stop-gradient Top-K KL, RLVR-adapted teachers,
and student SFT for output well-formedness and response length stabilization.
2

## Method

instance-specific privileged information (PI). In contrast, OPSD is effective when
PI represents a shared latent rule, such as a system prompt or alignment preference.
We identify three failure mechanisms: (1) distribution mismatch between teacher
and student caused by conditioning on student-generated prefixes, (2) optimization
instability from biased TopK reverse-KL gradients, and (3) an OPSD-specific
