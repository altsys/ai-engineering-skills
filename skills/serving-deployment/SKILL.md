---
name: serving-deployment
description: Teach serving and deployment through adaptive diagnosis and experiments. Use when a learner wants to reason about deploying LLM services, inference capacity, load handling, or rollout reliability; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Serving and Deployment

## Start from the learner

Before teaching, read [teaching principles](../../shared/teaching-principles.md), the [learner model protocol](../../shared/learner-model.md), and [progress storage](../../shared/progress-storage.md). The last two define how to load, update, save, and hand off the shared learner record; this skill does not restate them. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

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

## Follow-up probes

Use these when the opening probe is answered well or exposes a narrower confusion. Choose the one aimed at the learner's weakest unconfirmed claim; do not run them in order.

1. The service has 8 concurrent slots, and each request takes 2 seconds. What happens at 5 requests per second?  
   *Tests:* capacity arithmetic: 4 requests per second is the ceiling, so the queue grows without bound.
2. A user closes the tab mid-generation. What should happen to the request, and why does it matter at scale?  
   *Tests:* cancellation and wasted capacity.
3. The new version passes all tests, but the canary shows a 2% rise in timeouts. Roll back or continue?  
   *Tests:* rollout signals decided before release.

## Common misconceptions

Treat these as hypotheses to test, not labels to assign. Confirm with a probe before recording a misconception.

| Learner says or does | Better model | What exposes it |
| --- | --- | --- |
| "Retries improve reliability under load." | Retries amplify overload unless budgeted and backed off. | The opening probe |
| "Autoscaling handles bursts." | Scale-up lags, especially for GPU workloads; queues and backpressure are still needed. | Ask what happens in the first minute of a burst |
| "Average latency describes the service." | Near capacity, queueing makes tail latency grow sharply. | The capacity probe |
| "Deployed means done." | Releases need versioning, a canary, and rollback signals. | The canary probe |

## What demonstrated looks like

Record `demonstrated` for a narrow claim in this topic only when the learner, without step-by-step help:

- does basic capacity arithmetic and predicts where queueing starts
- specifies overload behavior (reject, shed, or degrade) explicitly
- defines rollback signals before a rollout

## Make the model observable

Load-test a local fake inference service with bounded concurrency. Increase arrival rate while measuring queue wait, tail latency, and rejections. Add deadlines and backpressure, then simulate a canary with a failing version and a rollback. Do not use production traffic.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Ask the learner to propose a capacity and rollout plan with explicit overload behavior and rollback signals for a new workload.

Update only the claim this task tested, following the learner model protocol.

## Select a resource for the gap

Start with [hf-serving](../../resources/catalog.md#hf-serving) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer Kubernetes internals and multi-GPU sharding unless needed. Route token-level performance to latency-cost and tracing gaps to observability.

Hand off through the shared learner record, as the learner model protocol describes.
