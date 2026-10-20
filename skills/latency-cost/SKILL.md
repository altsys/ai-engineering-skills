---
name: latency-cost
description: Teach latency and cost through adaptive diagnosis and experiments. Use when a learner wants to reason about token budgets, slow responses, caching, batching, or inference cost tradeoffs; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Latency and Cost

## Save and resume progress

Read and apply [progress storage](../../shared/progress-storage.md). Load the shared private learner profile before teaching. Save the full checkpoint after meaningful evidence or goal updates and before a topic handoff, using the loaded revision to detect conflicts. Confirm persistence only after verified success. If durable storage is unavailable or a save fails, say so and provide a copyable checkpoint; do not rely on a session-end save or implied assistant memory.

## Start from the learner

Read [teaching principles](../../shared/teaching-principles.md) and the [learner model protocol](../../shared/learner-model.md). Resume the shared checkpoint if available. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

Use diagnosis → mental-model gap → intervention → experiment → evidence of understanding. Select one relevant claim to probe. Treat the competency map as optional scope, not a lesson order. Repair a blocking prerequisite and return to the learner's task.

## Competency map

Use these distinctions when they explain a behavior or support a needed engineering decision:

time to first token; total latency; tail latency; queueing; input and output tokens; caching; concurrency; batching; quality constraints.

## Diagnose and intervene

Start with this probe or a closer version of the learner's real problem:

> Streaming makes the first text appear sooner. Does it necessarily reduce completion time or token cost?

Ask for a prediction and causal explanation before showing a solution. Use one question at a time; skip distinctions already supported by independent evidence.

Separate perceived responsiveness, total work, throughput, and cost per successful task. Optimize the measured bottleneck under a quality floor.

Offer the smallest useful explanation, worked contrast, diagram, or source section for the observed gap. Then request a fresh attempt; do not count repetition after a hint as independent understanding.

## Follow-up probes

Use these when the opening probe is answered well or exposes a narrower confusion. Choose the one aimed at the learner's weakest unconfirmed claim; do not run them in order.

1. Doubling the input context barely changes latency, but doubling the output length nearly doubles it. Why?  
   *Tests:* input is processed in a parallel prefill pass while output tokens are generated one at a time.
2. Cost per request dropped 40% after switching to a smaller model, but cost per resolved ticket went up. How?  
   *Tests:* cost per successful task rather than per call.
3. Prompt caching is enabled, but the hit rate is near zero. What about the prompt structure could cause that?  
   *Tests:* caches reuse a stable prefix, so ordering matters.

## Common misconceptions

Treat these as hypotheses to test, not labels to assign. Confirm with a probe before recording a misconception.

| Learner says or does | Better model | What exposes it |
| --- | --- | --- |
| "Streaming makes responses faster." | It improves time to first token, not completion time or cost. | The opening probe |
| "Every token costs the same time." | Output length usually dominates generation time. | The context-versus-output probe |
| "A cheaper model makes the system cheaper." | Failures, retries, and escalations can cost more than the savings. | The cost-per-ticket probe |
| "Optimize the average." | Tail latency drives user experience and timeouts. | Ask what p95 shows that the mean hides |

## What demonstrated looks like

Record `demonstrated` for a narrow claim in this topic only when the learner, without step-by-step help:

- decomposes a latency measurement into stages before optimizing
- predicts which change (shorter output, caching, smaller model) moves which metric
- reports cost per successful task under a stated quality floor

## Make the model observable

Use a local latency simulator or a small approved API budget. Vary output length, context length, and concurrency separately. Measure first-token and completion latency, tail behavior, and usage. Compare one optimization against the same task-quality checks; label simulated values explicitly.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Give a workload with repeated prefixes and long outputs. Ask which optimization to try first and what could worsen at higher load.

Record which narrow distinction the learner demonstrated, the task conditions, assistance, confidence, remaining uncertainty, and next probe. Preserve earlier evidence when a later result contradicts it; narrow or reopen only the affected claim. Do not mark the whole topic mastered from one successful exercise.

## Select a resource for the gap

Start with [hf-inference](../../resources/catalog.md#hf-inference) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer GPU kernel optimization and unmeasured caching schemes. Route queueing and capacity to serving-deployment; verify current prices and provider cache behavior before real estimates.

Return relevant evidence and the pending probe to the coach in the same learner record. At a session boundary, save a checkpoint only to available private learner-controlled storage or provide a copyable one. Claim persistence only after a successful save; never put real learner records in this public repository.
