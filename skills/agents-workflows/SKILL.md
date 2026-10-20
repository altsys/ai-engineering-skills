---
name: agents-workflows
description: Teach agents and workflows through adaptive diagnosis and experiments. Use when a learner wants to reason about agent loops, planning, autonomous execution, workflow orchestration, or stopping behavior; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Agents and Workflows

## Save and resume progress

Read and apply [progress storage](../../shared/progress-storage.md). Load the shared private learner profile before teaching. Save the full checkpoint after meaningful evidence or goal updates and before a topic handoff, using the loaded revision to detect conflicts. Confirm persistence only after verified success. If durable storage is unavailable or a save fails, say so and provide a copyable checkpoint; do not rely on a session-end save or implied assistant memory.

## Start from the learner

Read [teaching principles](../../shared/teaching-principles.md) and the [learner model protocol](../../shared/learner-model.md). Resume the shared checkpoint if available. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

Use diagnosis → mental-model gap → intervention → experiment → evidence of understanding. Select one relevant claim to probe. Treat the competency map as optional scope, not a lesson order. Repair a blocking prerequisite and return to the learner's task.

## Competency map

Use these distinctions when they explain a behavior or support a needed engineering decision:

fixed workflows versus model-directed control; state; planning; tool feedback; bounded loops; checkpoints; recovery; human handoff.

## Diagnose and intervene

Start with this probe or a closer version of the learner's real problem:

> A three-step task has known dependencies. What would an agent loop add, and what new failures would it introduce?

Ask for a prediction and causal explanation before showing a solution. Use one question at a time; skip distinctions already supported by independent evidence.

Distinguish control-flow flexibility from competence. Begin with a deterministic baseline and add model decisions only where uncertainty requires them.

Offer the smallest useful explanation, worked contrast, diagram, or source section for the observed gap. Then request a fresh attempt; do not count repetition after a hint as independent understanding.

## Follow-up probes

Use these when the opening probe is answered well or exposes a narrower confusion. Choose the one aimed at the learner's weakest unconfirmed claim; do not run them in order.

1. An agent repeats the same search five times with slightly different wording and exhausts its budget. What signals could stop it earlier?  
   *Tests:* stop conditions and detecting lack of progress.
2. For this task, which steps would you make fixed code and which would you leave to the model? Justify each.  
   *Tests:* where model decisions add value and where they only add risk.
3. The agent's context grows with every tool result. What breaks first as tasks get longer, and how would you manage state?  
   *Tests:* state management and context limits.

## Common misconceptions

Treat these as hypotheses to test, not labels to assign. Confirm with a probe before recording a misconception.

| Learner says or does | Better model | What exposes it |
| --- | --- | --- |
| "An agent is a smarter workflow." | An agent loop adds flexibility, not competence, and brings new failure modes. | The opening probe |
| "Give the agent more tools and it will figure it out." | More overlapping choices raise wrong-tool and cost risk. | Ask them to predict the effect of adding ten similar tools |
| "The agent will stop when it is done." | Stopping needs explicit conditions and budgets. | The repeated-search probe |
| "A plan made upfront makes the agent reliable." | Plans go stale when tool results surprise; replanning and checkpoints are needed. | Ask what happens when step 2 returns something unexpected |

## What demonstrated looks like

Record `demonstrated` for a narrow claim in this topic only when the learner, without step-by-step help:

- chooses a fixed workflow or an agent loop for a task, with stated reasons
- specifies budgets, stop conditions, and recovery points
- reads a trace and identifies the step where control went wrong

## Make the model observable

Simulate a research task using local canned tool responses. Compare a fixed workflow with a bounded agent loop on a normal case, an empty search, and a repeating result. Track task success, calls, state transitions, and stop reasons under the same budget.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Ask the learner to design recovery from a crash between a write and its checkpoint, and justify where human review belongs.

Record which narrow distinction the learner demonstrated, the task conditions, assistance, confidence, remaining uncertainty, and next probe. Preserve earlier evidence when a later result contradicts it; narrow or reopen only the affected claim. Do not mark the whole topic mastered from one successful exercise.

## Select a resource for the gap

Start with [anthropic-agents](../../resources/catalog.md#anthropic-agents) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer multi-agent systems and elaborate planning frameworks. Route execution semantics to tool-calling and measurement to evals.

Return relevant evidence and the pending probe to the coach in the same learner record. At a session boundary, save a checkpoint only to available private learner-controlled storage or provide a copyable one. Claim persistence only after a successful save; never put real learner records in this public repository.
