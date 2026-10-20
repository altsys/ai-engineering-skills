---
name: evals
description: Teach evaluations through adaptive diagnosis and experiments. Use when a learner wants to reason about LLM quality measurement, regression testing, benchmark design, or model-based judges; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Evaluations

## Start from the learner

Before teaching, read [teaching principles](../../shared/teaching-principles.md), the [learner model protocol](../../shared/learner-model.md), and [progress storage](../../shared/progress-storage.md). The last two define how to load, update, save, and hand off the shared learner record; this skill does not restate them. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

Use diagnosis → mental-model gap → intervention → experiment → evidence of understanding. Select one relevant claim to probe. Treat the competency map as optional scope, not a lesson order. Repair a blocking prerequisite and return to the learner's task.

## Competency map

Use these distinctions when they explain a behavior or support a needed engineering decision:

task contracts; representative cases; failure slices; baselines; rubrics; deterministic checks; human labels; judge calibration; leakage; uncertainty.

## Diagnose and intervene

Start with this probe or a closer version of the learner's real problem:

> A prompt scores better on the same ten examples used to rewrite it. What evidence is still missing before claiming an improvement?

Ask for a prediction and causal explanation before showing a solution. Use one question at a time; skip distinctions already supported by independent evidence.

Separate development feedback from held-out evidence and proxy scores from user outcomes. Diagnose rubric ambiguity before adding more cases.

Offer the smallest useful explanation, worked contrast, diagram, or source section for the observed gap. Then request a fresh attempt; do not count repetition after a hint as independent understanding.

## Follow-up probes

Use these when the opening probe is answered well or exposes a narrower confusion. Choose the one aimed at the learner's weakest unconfirmed claim; do not run them in order.

1. Two raters disagree on 30% of labels. What does that tell you before you compare any prompts?  
   *Tests:* rubric ambiguity as a measurement problem.
2. An LLM judge prefers the longer of two answers 80% of the time. How would you check whether that is judge bias or real quality?  
   *Tests:* judge calibration against human labels.
3. Variant B improves the mean by 2 points on 40 examples. What would make you trust or distrust that result?  
   *Tests:* noise, run-to-run variance, slices, and uncertainty.

## Common misconceptions

Treat these as hypotheses to test, not labels to assign. Confirm with a probe before recording a misconception.

| Learner says or does | Better model | What exposes it |
| --- | --- | --- |
| "The score went up, so it is better." | Scores on development cases overfit; held-out evidence is needed. | The opening probe |
| "An LLM judge is objective." | Judges have biases such as length and position preference; calibrate them. | The judge-length probe |
| "More test cases will fix a weak eval." | An unclear rubric or unrepresentative cases scale the problem. | The rater-disagreement probe |
| "The average score is what matters." | Rare critical failures can hide behind a good mean. | The transfer task below |

## What demonstrated looks like

Record `demonstrated` for a narrow claim in this topic only when the learner, without step-by-step help:

- writes a task contract and rubric that two people can apply consistently
- separates development cases from held-out cases and states uncertainty
- makes a release decision that weighs slice failures, not only the mean

## Make the model observable

Create a small synthetic dataset with normal, edge, and adversarial cases. Split development and held-out cases before tuning. Compare two variants using blind labels and explicit criteria; inspect disagreements and per-slice results instead of only the mean. Treat a tiny set as exploratory.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Give conflicting aggregate and rare-failure scores. Require a justified release decision, uncertainty statement, and next sample to collect.

Update only the claim this task tested, following the learner model protocol.

## Select a resource for the gap

Start with [anthropic-evals](../../resources/catalog.md#anthropic-evals) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer elaborate benchmark platforms. Route trace collection to observability and task tradeoffs to model-selection.

Hand off through the shared learner record, as the learner model protocol describes.
