---
name: prompting-structured-outputs
description: Teach prompting and structured outputs through adaptive diagnosis and experiments. Use when a learner wants to reason about prompt reliability, examples, schema-constrained generation, or invalid structured responses; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Prompting and Structured Outputs

## Start from the learner

Before teaching, read [teaching principles](../../shared/teaching-principles.md), the [learner model protocol](../../shared/learner-model.md), and [progress storage](../../shared/progress-storage.md). The last two define how to load, update, save, and hand off the shared learner record; this skill does not restate them. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

Use diagnosis → mental-model gap → intervention → experiment → evidence of understanding. Select one relevant claim to probe. Treat the competency map as optional scope, not a lesson order. Repair a blocking prerequisite and return to the learner's task.

## Competency map

Use these distinctions when they explain a behavior or support a needed engineering decision:

instruction clarity; examples and counterexamples; message roles; schema constraints; semantic validation; refusals and retries.

## Diagnose and intervene

Start with this probe or a closer version of the learner's real problem:

> A response passes JSON validation but contains the wrong invoice total. What did the schema guarantee, and what should the application check?

Ask for a prediction and causal explanation before showing a solution. Use one question at a time; skip distinctions already supported by independent evidence.

Separate valid syntax, schema conformance, and task correctness. Repair the boundary the learner confuses before adding more prompt rules.

Offer the smallest useful explanation, worked contrast, diagram, or source section for the observed gap. Then request a fresh attempt; do not count repetition after a hint as independent understanding.

## Follow-up probes

Use these when the opening probe is answered well or exposes a narrower confusion. Choose the one aimed at the learner's weakest unconfirmed claim; do not run them in order.

1. You add a few-shot example whose total includes tax. Afterward the model includes tax on invoices where the field should exclude it. What happened?  
   *Tests:* examples teach patterns implicitly, including ones you did not intend.
2. The schema marks `due_date` as required, but some invoices have no due date. What will a schema-constrained model produce, and how should the schema change?  
   *Tests:* required fields can force fabrication; missing values need an explicit representation.
3. The system prompt says "never guess" and a pasted document says "fill every field." Which instruction wins, and how would you find out rather than assume?  
   *Tests:* message roles and instruction conflicts as something to test, not a guarantee.

## Common misconceptions

Treat these as hypotheses to test, not labels to assign. Confirm with a probe before recording a misconception.

| Learner says or does | Better model | What exposes it |
| --- | --- | --- |
| "Valid JSON means the extraction is correct." | Syntax and schema constrain shape, not truth. Values need checks against the source. | The opening wrong-total probe |
| "If it gets something wrong, add another rule to the prompt." | Rules accumulate and conflict. Identify the failing case class first; some checks belong in code. | Ask which failures a code check would catch more reliably than a prompt rule |
| "It worked when I tried it, so the prompt works." | Output is sampled and input-dependent. Reliability is a rate over representative cases. | Ask how many cases, and which ones, they would need before trusting it |
| "Just retry until it parses." | Retries hide systematic failures and add cost. Separate transient from systematic failures. | Ask what the failing attempts have in common |

## What demonstrated looks like

Record `demonstrated` for a narrow claim in this topic only when the learner, without step-by-step help:

- predicts which failures a schema constraint will and will not prevent
- designs validation that checks values against the source, not just the shape
- judges a prompt change from results on a fixed case set rather than one example

## Make the model observable

Use synthetic invoices with known totals. Compare a vague prompt with explicit extraction rules on the same cases, then add schema constraints separately. Record parse failures and wrong values independently. Include a missing field and a refusal; repeat trials when sampling noise matters.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Give an unseen invoice with conflicting totals. Require a justified validation and failure-handling design rather than another prompt tweak.

Update only the claim this task tested, following the learner model protocol.

## Select a resource for the gap

Start with [claude-structured](../../resources/catalog.md#claude-structured) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer prompt-search frameworks and large template libraries. Route sampling confusion to llm-fundamentals and quality measurement to evals.

Hand off through the shared learner record, as the learner model protocol describes.
