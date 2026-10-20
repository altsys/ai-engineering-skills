---
name: model-selection
description: Teach model selection through adaptive diagnosis and experiments. Use when a learner wants to reason about choosing or comparing models, model routing, or deciding whether a larger model is needed; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Model Selection

## Start from the learner

Before teaching, read [teaching principles](../../shared/teaching-principles.md), the [learner model protocol](../../shared/learner-model.md), and [progress storage](../../shared/progress-storage.md). The last two define how to load, update, save, and hand off the shared learner record; this skill does not restate them. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

Use diagnosis → mental-model gap → intervention → experiment → evidence of understanding. Select one relevant claim to probe. Treat the competency map as optional scope, not a lesson order. Repair a blocking prerequisite and return to the learner's task.

## Competency map

Use these distinctions when they explain a behavior or support a needed engineering decision:

task fit; constraints; representative evaluation; quality floors; latency and cost; context needs; tool reliability; deployment requirements; version drift.

## Diagnose and intervene

Start with this probe or a closer version of the learner's real problem:

> A larger model wins a public benchmark but fails your extraction schema more often. Which evidence should decide the choice?

Ask for a prediction and causal explanation before showing a solution. Use one question at a time; skip distinctions already supported by independent evidence.

Separate general benchmark ability from workload fit. Define non-negotiable requirements before ranking candidates.

Offer the smallest useful explanation, worked contrast, diagram, or source section for the observed gap. Then request a fresh attempt; do not count repetition after a hint as independent understanding.

## Follow-up probes

Use these when the opening probe is answered well or exposes a narrower confusion. Choose the one aimed at the learner's weakest unconfirmed claim; do not run them in order.

1. Model A is 5% more accurate and three times the cost. When is that worth it?  
   *Tests:* weighing error cost against volume and price.
2. You route easy queries to a small model and hard ones to a large model. What can go wrong with the router itself?  
   *Tests:* routing errors and how to measure them.
3. The provider updates the model behind the alias you use. What needs to be in place for you to notice?  
   *Tests:* version pinning, drift, and regression evals.

## Common misconceptions

Treat these as hypotheses to test, not labels to assign. Confirm with a probe before recording a misconception.

| Learner says or does | Better model | What exposes it |
| --- | --- | --- |
| "The top benchmark model is the best one for us." | Public benchmarks measure general ability, not fit to this workload. | The opening probe |
| "Bigger is always better." | Larger models add latency and cost and may not help easy tasks. | Ask for a task where a small model is enough |
| "Once chosen, the model is settled." | Models drift and are deprecated; the choice needs monitoring. | The alias-update probe |
| "Using the same prompt for both models is a fair comparison." | A fair comparison gives each model a reasonable configuration. | Ask how they would configure each candidate |

## What demonstrated looks like

Record `demonstrated` for a narrow claim in this topic only when the learner, without step-by-step help:

- defines non-negotiable requirements before ranking candidates
- runs or designs a held-out comparison measuring cost per successful task
- revises the choice when a constraint changes

## Make the model observable

Compare two candidates on the same small held-out workload with identical task criteria and realistic configurations. Measure critical failures, latency, and cost per successful task. If APIs are unavailable, use supplied output traces and leave unmeasured criteria unknown.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Change one constraint, such as deployment locality or a strict latency ceiling. Require a revised choice and an explanation of missing evidence.

Update only the claim this task tested, following the learner model protocol.

## Select a resource for the gap

Start with [claude-model-choice](../../resources/catalog.md#claude-model-choice) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer leaderboard surveys and model training. Route quality uncertainty to evals and deployment feasibility to serving-deployment; verify current model availability and terms before advising.

Hand off through the shared learner record, as the learner model protocol describes.
