---
name: tool-calling
description: Teach tool calling through adaptive diagnosis and experiments. Use when a learner wants to reason about function calls, tool schemas, tool execution, or external actions requested by a model; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Tool Calling

## Save and resume progress

Read and apply [progress storage](../../shared/progress-storage.md). Load the shared private learner profile before teaching. Save the full checkpoint after meaningful evidence or goal updates and before a topic handoff, using the loaded revision to detect conflicts. Confirm persistence only after verified success. If durable storage is unavailable or a save fails, say so and provide a copyable checkpoint; do not rely on a session-end save or implied assistant memory.

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

## Follow-up probes

Use these when the opening probe is answered well or exposes a narrower confusion. Choose the one aimed at the learner's weakest unconfirmed claim; do not run them in order.

1. The model calls `get_weather(city="Paris")`, but the user meant Paris, Texas. Whose responsibility is that, and what can the application do?  
   *Tests:* ambiguous arguments, validation, and asking for clarification.
2. A tool returns an error as text, and the model then tells the user the action succeeded. Why might that happen, and how would you detect it?  
   *Tests:* tool results are model input; ground truth lives in system records.
3. The model chains three read calls and then a write. Which calls need authorization checks, and where are they enforced?  
   *Tests:* authorization enforced at execution, not requested in the prompt.

## Common misconceptions

Treat these as hypotheses to test, not labels to assign. Confirm with a probe before recording a misconception.

| Learner says or does | Better model | What exposes it |
| --- | --- | --- |
| "The model runs the tool." | The model proposes a call; the application decides whether to execute it. | The opening probe |
| "Arguments that match the schema are safe." | A schema checks shape; authorization and business rules are separate checks. | Ask what a valid but unauthorized call looks like |
| "Retrying a timed-out call is safe." | A timeout is an unknown outcome; writes need idempotency. | The duplicate-refund probe |
| "The assistant's final message tells me what happened." | Check recorded effects and tool logs, not assistant wording. | The error-as-text probe |

## What demonstrated looks like

Record `demonstrated` for a narrow claim in this topic only when the learner, without step-by-step help:

- draws the proposal, validation, execution, and result boundary for a new tool
- designs idempotent handling of unknown outcomes
- verifies outcomes from system records rather than assistant text

## Make the model observable

Use a local fake refund tool with no external effects. Inject invalid arguments, a denied request, and a timeout after a successful write. Predict outcomes, then add validation and an idempotency key; inspect recorded effects rather than assistant wording.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Give a different write tool and require an execution policy that handles unknown outcomes without duplicate writes.

Record which narrow distinction the learner demonstrated, the task conditions, assistance, confidence, remaining uncertainty, and next probe. Preserve earlier evidence when a later result contradicts it; narrow or reopen only the affected claim. Do not mark the whole topic mastered from one successful exercise.

## Select a resource for the gap

Start with [claude-tools](../../resources/catalog.md#claude-tools) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer framework-specific tool registries. Route multi-step control to agents-workflows and adversarial inputs to safety-failure-handling.

Return relevant evidence and the pending probe to the coach in the same learner record. At a session boundary, save a checkpoint only to available private learner-controlled storage or provide a copyable one. Claim persistence only after a successful save; never put real learner records in this public repository.
