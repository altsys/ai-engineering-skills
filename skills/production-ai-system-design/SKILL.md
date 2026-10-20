---
name: production-ai-system-design
description: Teach production AI system design through adaptive diagnosis and experiments. Use when a learner wants to reason about end-to-end AI architecture, production tradeoffs, or integrating quality, reliability, and operational constraints; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Production AI System Design

## Save and resume progress

Read and apply [progress storage](../../shared/progress-storage.md). Load the shared private learner profile before teaching. Save the full checkpoint after meaningful evidence or goal updates and before a topic handoff, using the loaded revision to detect conflicts. Confirm persistence only after verified success. If durable storage is unavailable or a save fails, say so and provide a copyable checkpoint; do not rely on a session-end save or implied assistant memory.

## Start from the learner

Read [teaching principles](../../shared/teaching-principles.md) and the [learner model protocol](../../shared/learner-model.md). Resume the shared checkpoint if available. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

Use diagnosis → mental-model gap → intervention → experiment → evidence of understanding. Select one relevant claim to probe. Treat the competency map as optional scope, not a lesson order. Repair a blocking prerequisite and return to the learner's task.

## Competency map

Use these distinctions when they explain a behavior or support a needed engineering decision:

user task and success contract; data flow; component boundaries; retrieval and tools; quality gates; service budgets; access control; release and rollback; feedback loops.

## Diagnose and intervene

Start with this probe or a closer version of the learner's real problem:

> A demo answers correctly, but users report intermittent wrong actions and slow requests. What evidence and boundaries are missing from the design?

Ask for a prediction and causal explanation before showing a solution. Use one question at a time; skip distinctions already supported by independent evidence.

Separate a successful model call from a reliable user outcome. Diagnose the weakest system boundary rather than adding components by default.

Offer the smallest useful explanation, worked contrast, diagram, or source section for the observed gap. Then request a fresh attempt; do not count repetition after a hint as independent understanding.

## Follow-up probes

Use these when the opening probe is answered well or exposes a narrower confusion. Choose the one aimed at the learner's weakest unconfirmed claim; do not run them in order.

1. Which part of this system would you not use an LLM for, and why?  
   *Tests:* keeping deterministic parts deterministic.
2. Define what "working" means for this product in a way you could measure every week.  
   *Tests:* a measurable success contract and service objectives.
3. Traffic grows tenfold. Which component fails first, and how would you find out before users do?  
   *Tests:* bottleneck reasoning combined with observability.

## Common misconceptions

Treat these as hypotheses to test, not labels to assign. Confirm with a probe before recording a misconception.

| Learner says or does | Better model | What exposes it |
| --- | --- | --- |
| "The model call works, so the feature works." | Reliability is measured at the user outcome, not the model call. | The opening probe |
| "Each problem needs a new component." | Fix the weakest boundary; every component adds failure modes. | Ask what failures each proposed component adds |
| "Design first, then build." | Evals and traces from a thin slice should reshape the design. | Ask how the design might change after the first week of traces |
| "Quality and operations are separate concerns." | Latency and cost budgets constrain quality choices such as retrieval depth. | Ask how a 2-second budget changes the design |

## What demonstrated looks like

Record `demonstrated` for a narrow claim in this topic only when the learner, without step-by-step help:

- writes a measurable success contract and defines failure behavior
- identifies the weakest boundary from evidence and justifies keeping other parts simple
- revises the architecture when a constraint changes

## Make the model observable

Choose one narrow synthetic product task. Sketch its data and control flow, define measurable success and failure behavior, then build or simulate the smallest end-to-end slice. Inject missing evidence, an unauthorized action, and a dependency timeout. Evaluate quality and service behavior together.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Change the workload or access model and require the learner to revise the architecture, identify new failure modes, and justify what remains simple.

Record which narrow distinction the learner demonstrated, the task conditions, assistance, confidence, remaining uncertainty, and next probe. Preserve earlier evidence when a later result contradicts it; narrow or reopen only the affected claim. Do not mark the whole topic mastered from one successful exercise.

## Select a resource for the gap

Start with [google-slos](../../resources/catalog.md#google-slos) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer broad platform builds and speculative scale. Route each exposed gap to the matching topic skill and return with evidence before expanding the architecture.

Return relevant evidence and the pending probe to the coach in the same learner record. At a session boundary, save a checkpoint only to available private learner-controlled storage or provide a copyable one. Claim persistence only after a successful save; never put real learner records in this public repository.
