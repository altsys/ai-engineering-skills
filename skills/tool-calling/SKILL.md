---
name: tool-calling
description: Teach tool calling through adaptive diagnosis and experiments. Use when a learner wants to reason about function calls, tool schemas, tool execution, or external actions requested by a model; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Tool Calling

## Start from the learner

Read [teaching principles](../../shared/teaching-principles.md) and the [learner model protocol](../../shared/learner-model.md). Resume the shared checkpoint if available. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

Use diagnosis → mental-model gap → intervention → experiment → evidence of understanding. Select one relevant claim to probe. Treat the competency map as optional scope, not a lesson order. Repair a blocking prerequisite and return to the learner's task.

## Competency map

Use these distinctions when they explain a behavior or support a needed engineering decision:

tool proposals versus execution; argument validation; authorization; tool results; call sequencing; timeouts; retries; idempotency.

## Diagnose and intervene

Start with this probe or a closer version of the learner's real problem:

> The model emits a valid refund call twice after a timeout. Who decides whether to execute it, and how do you prevent two refunds?

Ask for a prediction and causal explanation before showing a solution. Use one question at a time; skip distinctions already supported by independent evidence.

Separate model intent from application authority and external side effects. Draw the proposal, validation, execution, and result boundary only as needed.

Offer the smallest useful explanation, worked contrast, diagram, or source section for the observed gap. Then request a fresh attempt; do not count repetition after a hint as independent understanding.

## Make the model observable

Use a local fake refund tool with no external effects. Inject invalid arguments, a denied request, and a timeout after a successful write. Predict outcomes, then add validation and an idempotency key; inspect recorded effects rather than assistant wording.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Give a different write tool and require an execution policy that handles unknown outcomes without duplicate writes.

Record which narrow distinction the learner demonstrated, the task conditions, assistance, confidence, remaining uncertainty, and next probe. Preserve earlier evidence when a later result contradicts it; narrow or reopen only the affected claim. Do not mark the whole topic mastered from one successful exercise.

## Select a resource for the gap

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer framework-specific tool registries. Route multi-step control to agents-workflows and adversarial inputs to safety-failure-handling.

Return relevant evidence and the pending probe to the coach in the same learner record. At a session boundary, save a checkpoint only to available private learner-controlled storage or provide a copyable one. Claim persistence only after a successful save; never put real learner records in this public repository.
