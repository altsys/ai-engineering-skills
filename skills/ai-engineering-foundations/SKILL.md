---
name: ai-engineering-foundations
description: Teach LLM behavior, prompting, and model choice through adaptive diagnosis and experiments. Use when a learner is building a foundation for practical AI engineering.
---

# AI Engineering Foundations

Read [teaching principles](shared/teaching-principles.md), [learner model](shared/learner-model.md), and [progress storage](shared/progress-storage.md) before teaching. Use the bundled `scripts/learner_progress.py` with one stable private profile. Load before teaching, save after meaningful changes and before handoff, and verify each save. If durable storage is unavailable, provide a portable checkpoint.

Diagnose the learner's goal and current mental model, then read the relevant topic guide:

- [llm-fundamentals](topics/llm-fundamentals/TOPIC.md)
- [prompting-structured-outputs](topics/prompting-structured-outputs/TOPIC.md)
- [model-selection](topics/model-selection/TOPIC.md)

Treat these topics as a scope map, not a fixed lesson order. Use a prediction, debugging task, or experiment to find the smallest useful gap. Use the [resource catalog](resources/catalog.md) only after diagnosing that gap; verify the exact source and section before assigning it. Record observed evidence and assistance, preserve contradictions, and update only the affected learner-model claims. Keep the same learner profile when moving to another group or the coach.
