---
name: ai-engineering-knowledge-systems
description: Teach embeddings, retrieval, and RAG through adaptive diagnosis and experiments. Use when a learner is building or debugging grounded AI applications.
---

# AI Engineering Knowledge Systems

Read [teaching principles](shared/teaching-principles.md), [learner model](shared/learner-model.md), and [progress storage](shared/progress-storage.md) before teaching. Use the bundled `scripts/learner_progress.py` with one stable private profile. Load before teaching, save after meaningful changes and before handoff, and verify each save. If durable storage is unavailable, provide a portable checkpoint.

Diagnose the learner's goal and current mental model, then read the relevant topic guide:

- [embeddings](topics/embeddings/TOPIC.md)
- [retrieval](topics/retrieval/TOPIC.md)
- [rag](topics/rag/TOPIC.md)

Treat these topics as a scope map, not a fixed lesson order. Use a prediction, debugging task, or experiment to find the smallest useful gap. Use the [resource catalog](resources/catalog.md) only after diagnosing that gap; verify the exact source and section before assigning it. Record observed evidence and assistance, preserve contradictions, and update only the affected learner-model claims. Keep the same learner profile when moving to another group or the coach.
