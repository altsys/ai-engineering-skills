---
name: rag
description: Teach retrieval-augmented generation through adaptive diagnosis and experiments. Use when a learner wants to reason about grounded answers, citations, retrieved context, or RAG system failures; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Retrieval-Augmented Generation

## Start from the learner

Before teaching, read [teaching principles](../../shared/teaching-principles.md), the [learner model protocol](../../shared/learner-model.md), and [progress storage](../../shared/progress-storage.md). The last two define how to load, update, save, and hand off the shared learner record; this skill does not restate them. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

Use diagnosis → mental-model gap → intervention → experiment → evidence of understanding. Select one relevant claim to probe. Treat the competency map as optional scope, not a lesson order. Repair a blocking prerequisite and return to the learner's task.

## Competency map

Use these distinctions when they explain a behavior or support a needed engineering decision:

retrieval versus generation; evidence sufficiency; context assembly; source provenance; citations; conflicting and stale evidence; abstention.

## Diagnose and intervene

Start with this probe or a closer version of the learner's real problem:

> The answer cites a real retrieved document, but the cited passage does not support the claim. Which parts of the system could have failed?

Ask for a prediction and causal explanation before showing a solution. Use one question at a time; skip distinctions already supported by independent evidence.

Separate retrieval relevance, evidence support, and fluent generation. A citation is a pointer, not proof of support.

Offer the smallest useful explanation, worked contrast, diagram, or source section for the observed gap. Then request a fresh attempt; do not count repetition after a hint as independent understanding.

## Follow-up probes

Use these when the opening probe is answered well or exposes a narrower confusion. Choose the one aimed at the learner's weakest unconfirmed claim; do not run them in order.

1. Retrieved context contains a 2023 policy and a 2025 policy that disagree. What should the answer do, and what does the system need to make that possible?  
   *Tests:* conflicting and stale evidence, and the metadata needed to handle it.
2. A question is not answerable from the corpus, yet the system answers fluently. What do you change, and how do you check the change does not make it refuse answerable questions?  
   *Tests:* abstention and its cost on answerable questions.
3. You raise top-k from 5 to 10 and answer quality drops. Why could more relevant-looking context hurt?  
   *Tests:* distraction and context dilution; route to llm-fundamentals if the mechanism is missing.

## Common misconceptions

Treat these as hypotheses to test, not labels to assign. Confirm with a probe before recording a misconception.

| Learner says or does | Better model | What exposes it |
| --- | --- | --- |
| "A citation proves the answer is grounded." | A citation is a pointer. Check whether the cited passage supports the claim. | The opening probe |
| "RAG eliminates hallucination." | It supplies evidence; the model can still ignore, misread, or go beyond it. | The unanswerable-question probe |
| "More context is always safer." | Extra context can distract the model and adds cost and latency. | The top-k probe |
| "Bad answers mean we need a better LLM." | First separate retrieval failure from generation failure with a sufficient-context control. | Ask for the experiment that separates them |

## What demonstrated looks like

Record `demonstrated` for a narrow claim in this topic only when the learner, without step-by-step help:

- separates retrieval failure from generation failure with a controlled comparison
- scores claim support separately from retrieval relevance
- designs abstention behavior and states its cost on answerable questions

## Make the model observable

Use a synthetic policy corpus with answerable, unanswerable, stale, and conflicting cases. Compare normal retrieval with manually supplied sufficient context while holding the generator prompt fixed. Score retrieval coverage and claim support separately; inspect unsupported answers and abstentions.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Give a new failure trace and require an evidence-based choice between retrieval repair, context repair, and generation constraints.

Update only the claim this task tested, following the learner model protocol.

## Select a resource for the gap

Start with [scratch-rag](../../resources/catalog.md#scratch-rag) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer fine-tuning and agentic retrieval until a simple baseline is measured. Route missing candidates to retrieval and evaluation design to evals.

Hand off through the shared learner record, as the learner model protocol describes.
