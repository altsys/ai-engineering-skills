---
name: retrieval
description: Teach retrieval through adaptive diagnosis and experiments. Use when a learner wants to reason about search quality, chunking, hybrid search, reranking, or retrieval misses; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Retrieval

## Save and resume progress

Read and apply [progress storage](../../shared/progress-storage.md). Load the shared private learner profile before teaching. Save the full checkpoint after meaningful evidence or goal updates and before a topic handoff, using the loaded revision to detect conflicts. Confirm persistence only after verified success. If durable storage is unavailable or a save fails, say so and provide a copyable checkpoint; do not rely on a session-end save or implied assistant memory.

## Start from the learner

Read [teaching principles](../../shared/teaching-principles.md) and the [learner model protocol](../../shared/learner-model.md). Resume the shared checkpoint if available. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

Use diagnosis → mental-model gap → intervention → experiment → evidence of understanding. Select one relevant claim to probe. Treat the competency map as optional scope, not a lesson order. Repair a blocking prerequisite and return to the learner's task.

## Competency map

Use these distinctions when they explain a behavior or support a needed engineering decision:

corpus coverage; chunk boundaries; metadata and access filters; lexical and dense search; candidate generation; reranking; recall and precision; freshness.

## Diagnose and intervene

Start with this probe or a closer version of the learner's real problem:

> The correct document exists, but it never enters the candidate set. Can a better reranker fix the answer?

Ask for a prediction and causal explanation before showing a solution. Use one question at a time; skip distinctions already supported by independent evidence.

Separate missing source, missing candidate, poor ranking, and insufficient chunk context. Diagnose the stage before selecting a search technique.

Offer the smallest useful explanation, worked contrast, diagram, or source section for the observed gap. Then request a fresh attempt; do not count repetition after a hint as independent understanding.

## Follow-up probes

Use these when the opening probe is answered well or exposes a narrower confusion. Choose the one aimed at the learner's weakest unconfirmed claim; do not run them in order.

1. Chunks are 200 tokens. The answer needs a table header from one chunk and a row from the next. What do you observe, and what would you change?  
   *Tests:* chunk boundaries and the context a chunk loses.
2. Recall@10 is 0.9, yet users still get wrong answers. What could be happening, and what do you measure next?  
   *Tests:* the difference between candidate recall, ranking, label quality, and downstream use.
3. A reranker scores highly a document the user is not permitted to read. Where should the access filter be applied?  
   *Tests:* applying access filters before candidates are generated, not as a ranking signal.

## Common misconceptions

Treat these as hypotheses to test, not labels to assign. Confirm with a probe before recording a misconception.

| Learner says or does | Better model | What exposes it |
| --- | --- | --- |
| "A better reranker fixes retrieval misses." | A reranker only reorders the candidates it receives. | The opening probe |
| "Dense search is always better than keyword search." | They are complementary; exact terms, IDs, and rare names often favor lexical search. | Ask them to predict which wins for an ID query |
| "Smaller chunks are more precise, so they are always better." | Chunk size trades precision against completeness of context. | The chunk-boundary probe |
| "The answer is in the corpus, so retrieval worked." | It must reach the top-k passed to the generator; measure each stage. | Ask at which stage the document dropped out |

## What demonstrated looks like

Record `demonstrated` for a narrow claim in this topic only when the learner, without step-by-step help:

- localizes a miss to coverage, candidate generation, ranking, or chunking, with evidence
- builds a small labeled query set and interprets recall@k on it
- justifies hybrid search or reranking from observed failure classes

## Make the model observable

Build ten synthetic documents and six labeled queries including an exact ID and a paraphrase. Compare lexical and dense candidate sets at fixed k, then rerank the same candidates. Inspect recall at k, ranking, and one chunk-boundary failure. Keep access filters applied throughout.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Introduce a new query class and ask which stage needs repair and what measurement would disprove the diagnosis.

Record which narrow distinction the learner demonstrated, the task conditions, assistance, confidence, remaining uncertainty, and next probe. Preserve earlier evidence when a later result contradicts it; narrow or reopen only the affected claim. Do not mark the whole topic mastered from one successful exercise.

## Select a resource for the gap

Start with [sbert-rerank](../../resources/catalog.md#sbert-rerank) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer distributed index operations. Route representation gaps to embeddings and answer grounding to rag.

Return relevant evidence and the pending probe to the coach in the same learner record. At a session boundary, save a checkpoint only to available private learner-controlled storage or provide a copyable one. Claim persistence only after a successful save; never put real learner records in this public repository.
