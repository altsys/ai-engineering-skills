---
name: serving-deployment
description: Teach serving and deployment through adaptive diagnosis and experiments. Use when a learner wants to reason about deploying LLM services, inference capacity, load handling, or rollout reliability; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Serving and Deployment

## Save and resume progress

Read and apply [progress storage](../../shared/progress-storage.md). Load the shared private learner profile before teaching. Save the full checkpoint after meaningful evidence or goal updates and before a topic handoff, using the loaded revision to detect conflicts. Confirm persistence only after verified success. If durable storage is unavailable or a save fails, say so and provide a copyable checkpoint; do not rely on a session-end save or implied assistant memory.

## Start from the learner

Read [teaching principles](../../shared/teaching-principles.md) and the [learner model protocol](../../shared/learner-model.md). Resume the shared checkpoint if available. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

Use diagnosis → mental-model gap → intervention → experiment → evidence of understanding. Select one relevant claim to probe. Treat the competency map as optional scope, not a lesson order. Repair a blocking prerequisite and return to the learner's task.

## Competency map

Use these distinctions when they explain a behavior or support a needed engineering decision:

hosted versus self-hosted inference; resource limits; concurrency; queues; backpressure; timeouts; cancellation; readiness; versioning; canary rollout; rollback.

## Diagnose and intervene

Start with this probe or a closer version of the learner's real problem:

> Average response time looks fine at low load, but requests time out during bursts. Why might adding retries make it worse?

Ask for a prediction and causal explanation before showing a solution. Use one question at a time; skip distinctions already supported by independent evidence.

Separate model execution time from service capacity and queueing. Use a bounded queue model before teaching scaling knobs.

Offer the smallest useful explanation, worked contrast, diagram, or source section for the observed gap. Then request a fresh attempt; do not count repetition after a hint as independent understanding.

## Make the model observable

Load-test a local fake inference service with bounded concurrency. Increase arrival rate while measuring queue wait, tail latency, and rejections. Add deadlines and backpressure, then simulate a canary with a failing version and a rollback. Do not use production traffic.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Ask the learner to propose a capacity and rollout plan with explicit overload behavior and rollback signals for a new workload.

Record which narrow distinction the learner demonstrated, the task conditions, assistance, confidence, remaining uncertainty, and next probe. Preserve earlier evidence when a later result contradicts it; narrow or reopen only the affected claim. Do not mark the whole topic mastered from one successful exercise.

## Select a resource for the gap

Start with [hf-serving](../../resources/catalog.md#hf-serving) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer Kubernetes internals and multi-GPU sharding unless needed. Route token-level performance to latency-cost and tracing gaps to observability.

Return relevant evidence and the pending probe to the coach in the same learner record. At a session boundary, save a checkpoint only to available private learner-controlled storage or provide a copyable one. Claim persistence only after a successful save; never put real learner records in this public repository.
