---
name: evals
description: Teach evaluations through adaptive diagnosis and experiments. Use when a learner wants to reason about LLM quality measurement, regression testing, benchmark design, or model-based judges; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Evaluations

## Start from the learner

Read [teaching principles](../../shared/teaching-principles.md) and the [learner model protocol](../../shared/learner-model.md). Resume the shared checkpoint if available. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

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

## Make the model observable

Create a small synthetic dataset with normal, edge, and adversarial cases. Split development and held-out cases before tuning. Compare two variants using blind labels and explicit criteria; inspect disagreements and per-slice results instead of only the mean. Treat a tiny set as exploratory.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Give conflicting aggregate and rare-failure scores. Require a justified release decision, uncertainty statement, and next sample to collect.

Record which narrow distinction the learner demonstrated, the task conditions, assistance, confidence, remaining uncertainty, and next probe. Preserve earlier evidence when a later result contradicts it; narrow or reopen only the affected claim. Do not mark the whole topic mastered from one successful exercise.

## Select a resource for the gap

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer elaborate benchmark platforms. Route trace collection to observability and task tradeoffs to model-selection.

Return relevant evidence and the pending probe to the coach in the same learner record. At a session boundary, save a checkpoint only to available private learner-controlled storage or provide a copyable one. Claim persistence only after a successful save; never put real learner records in this public repository.
