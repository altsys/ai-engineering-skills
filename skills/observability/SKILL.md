---
name: observability
description: Teach observability through adaptive diagnosis and experiments. Use when a learner wants to reason about LLM tracing, production debugging, quality monitoring, or telemetry design; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Observability

## Save and resume progress

Read and apply [progress storage](../../shared/progress-storage.md). Load the shared private learner profile before teaching. Save the full checkpoint after meaningful evidence or goal updates and before a topic handoff, using the loaded revision to detect conflicts. Confirm persistence only after verified success. If durable storage is unavailable or a save fails, say so and provide a copyable checkpoint; do not rely on a session-end save or implied assistant memory.

## Start from the learner

Read [teaching principles](../../shared/teaching-principles.md) and the [learner model protocol](../../shared/learner-model.md). Resume the shared checkpoint if available. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

Use diagnosis → mental-model gap → intervention → experiment → evidence of understanding. Select one relevant claim to probe. Treat the competency map as optional scope, not a lesson order. Repair a blocking prerequisite and return to the learner's task.

## Competency map

Use these distinctions when they explain a behavior or support a needed engineering decision:

request correlation; spans; prompt and model versions; retrieval provenance; tool events; usage; errors; latency decomposition; sampling; privacy.

## Diagnose and intervene

Start with this probe or a closer version of the learner's real problem:

> End-to-end latency doubled while model latency stayed flat. Which observations would distinguish queueing, retrieval, and retries?

Ask for a prediction and causal explanation before showing a solution. Use one question at a time; skip distinctions already supported by independent evidence.

Separate observed execution facts from quality judgments. Add the smallest trace that can distinguish the competing explanations.

Offer the smallest useful explanation, worked contrast, diagram, or source section for the observed gap. Then request a fresh attempt; do not count repetition after a hint as independent understanding.

## Make the model observable

Instrument a local mocked retrieval-and-tool pipeline with correlation IDs, versions, durations, and retry events. Inject a slow retriever and a tool timeout separately. Diagnose from traces, then connect a bad answer to its context and configuration without logging raw sensitive content.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Provide a partial trace with a missing span. Require the learner to state what cannot yet be concluded and propose one useful instrument.

Record which narrow distinction the learner demonstrated, the task conditions, assistance, confidence, remaining uncertainty, and next probe. Preserve earlier evidence when a later result contradicts it; narrow or reopen only the affected claim. Do not mark the whole topic mastered from one successful exercise.

## Select a resource for the gap

Start with [otel-spans](../../resources/catalog.md#otel-spans) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer vendor dashboards and logging everything. Route quality labels to evals and bottleneck remedies to latency-cost.

Return relevant evidence and the pending probe to the coach in the same learner record. At a session boundary, save a checkpoint only to available private learner-controlled storage or provide a copyable one. Claim persistence only after a successful save; never put real learner records in this public repository.
