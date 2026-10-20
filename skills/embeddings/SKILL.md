---
name: embeddings
description: Teach embeddings through adaptive diagnosis and experiments. Use when a learner wants to reason about vector representations, semantic similarity, embedding models, or nearest-neighbor behavior; update evidence-based learner claims rather than deliver a fixed tutorial.
---

# Embeddings

## Start from the learner

Before teaching, read [teaching principles](../../shared/teaching-principles.md), the [learner model protocol](../../shared/learner-model.md), and [progress storage](../../shared/progress-storage.md). The last two define how to load, update, save, and hand off the shared learner record; this skill does not restate them. Infer the goal and constraints from the conversation; ask only what changes the next teaching decision.

Use diagnosis → mental-model gap → intervention → experiment → evidence of understanding. Select one relevant claim to probe. Treat the competency map as optional scope, not a lesson order. Repair a blocking prerequisite and return to the learner's task.

## Competency map

Use these distinctions when they explain a behavior or support a needed engineering decision:

representation geometry; cosine versus dot product; normalization; task and model dependence; semantic versus lexical similarity; vector compatibility.

## Diagnose and intervene

Start with this probe or a closer version of the learner's real problem:

> Two documents discuss the same topic but contradict each other. Should their embeddings be far apart? Why?

Ask for a prediction and causal explanation before showing a solution. Use one question at a time; skip distinctions already supported by independent evidence.

Distinguish similarity from truth, relevance, and entailment. Use a small ranked example before discussing vector index internals.

Offer the smallest useful explanation, worked contrast, diagram, or source section for the observed gap. Then request a fresh attempt; do not count repetition after a hint as independent understanding.

## Follow-up probes

Use these when the opening probe is answered well or exposes a narrower confusion. Choose the one aimed at the learner's weakest unconfirmed claim; do not run them in order.

1. A query for "error code E4012" returns documents about other error codes. Why might an embedding model do this, and what would you try?  
   *Tests:* how dense representations treat rare identifiers, and when lexical matching is the better tool.
2. You upgrade the embedding model and re-embed only new documents. What happens to search quality?  
   *Tests:* vectors are only comparable within one model space.
3. A query and a document have cosine similarity 0.82. Is that a good match?  
   *Tests:* scores are relative within a model and corpus, not absolute thresholds.

## Common misconceptions

Treat these as hypotheses to test, not labels to assign. Confirm with a probe before recording a misconception.

| Learner says or does | Better model | What exposes it |
| --- | --- | --- |
| "Similar embeddings mean the documents agree." | Similarity tracks topic and phrasing, not truth or entailment. | The opening contradiction probe |
| "A threshold like 0.8 works for any model." | Score distributions differ by model and domain; calibrate on labeled pairs. | The 0.82 probe |
| "Embeddings capture exact identifiers." | Dense models often blur rare tokens; lexical search handles exact matches. | The E4012 probe |
| "Vectors with the same dimension can be compared." | Only vectors from the same model, version, and preprocessing share a space. | The model-upgrade probe |

## What demonstrated looks like

Record `demonstrated` for a narrow claim in this topic only when the learner, without step-by-step help:

- predicts the rough ranking of paraphrase, contradiction, and keyword-overlap pairs before computing them
- explains a bad nearest neighbor from what the model encodes
- chooses between re-embedding, hybrid search, or a different model with a stated reason

## Make the model observable

Create a small corpus with paraphrases, contradictions, exact identifiers, and unrelated text. Predict rankings, compute similarities with one embedding model, then inspect mistakes. Change normalization or query phrasing separately; never mix vectors from different model spaces.

Have the learner predict first, change one important variable, inspect the actual result, and explain mismatches. Use local mocks and synthetic data by default. Agree on limits before paid calls; keep external writes in a sandbox. When execution is unavailable, label the exercise as a thought experiment and leave empirical claims untested. Never invent results.

## Require transfer evidence

Ask the learner to explain a high-similarity but irrelevant result and choose between a representation change and lexical search.

Update only the claim this task tested, following the learner model protocol.

## Select a resource for the gap

Start with [sbert-semantic](../../resources/catalog.md#sbert-semantic) when its stated gap matches. Use its exact sections, limitations, and follow-up experiment; select an alternative when the diagnosis calls for it.

Consult the [resource catalog](../../resources/catalog.md) and follow the [resource schema](../../shared/resource-schema.md). Prefer official documentation for implementation behavior and original papers for mechanisms; use Hugging Face material or an implementation exercise when it clarifies the diagnosed gap. Verify the source and exact section before assigning it. Never guess a chapter or URL for an unresolved catalog entry.

State why the section fits, what to focus on, what to skip, and the concrete follow-up experiment. If source access is unavailable, say so and use a clearly labeled local explanation rather than claim a resource was checked.

## Scope and handoff

Defer embedding training and vector database tuning. Route ranking and corpus design to retrieval.

Hand off through the shared learner record, as the learner model protocol describes.
