# AI Engineering Skills

An executable curriculum for learning AI engineering with an AI assistant.

This repository is not a tutorial, textbook, or "awesome list." It contains teaching skills whose job is to understand a learner's current mental model and help expand, repair, clarify, and solidify it.

## Core idea

**Do not optimize for covering material. Optimize for improving the learner's mental model.**

A learner does not understand a topic because they read a chapter, watched a video, or can repeat a definition. Understanding shows up when they can predict behavior, explain what happened, debug a failure, distinguish similar concepts, transfer an idea to a new situation, and make better engineering decisions.

The skills in this repository therefore use a recurring learning loop:

> **diagnosis → mental-model gap → intervention → experiment → evidence of understanding**

The loop is adaptive. It may take five minutes or several sessions. If a later exercise exposes an earlier misconception, the skill should branch backward, repair the prerequisite model, and then return.

## How a skill teaches

### Diagnose

Expose what the learner currently believes through predictions, explanations, debugging situations, and design decisions. Avoid relying mainly on vocabulary quizzes.

### Find the gap

Identify what is missing, incorrect, fuzzy, or unable to transfer to practice. Distinguish a missing concept from a memorized definition with no operational understanding.

### Choose an intervention

Use the smallest useful intervention. That might be a short explanation, diagram, book section, paper, documentation page, video, code experiment, comparison, or debugging exercise.

### Experiment

Whenever practical, make the concept observable. Ask the learner to predict first, change one important variable, inspect the result, and explain what happened.

### Require evidence

Do not count content consumption as learning. Look for evidence in explanation, prediction, debugging, transfer, implementation, and justified engineering decisions.

## Keep a revisable learner model

The coach and topic skills share a small record of the learner's goal, current beliefs, evidence, assessment confidence, unresolved gaps, and the next useful probe. They update it after meaningful interactions, using the [learner model protocol](shared/learner-model.md).

The record separates what the learner demonstrated from what the coach suspects. Assisted answers remain assisted evidence. Later contradictions narrow or reopen an assessment without erasing earlier progress. Teaching choices follow the revised model, not a fixed lesson order.

For example, explaining temperature after a hint suggests developing understanding. Independently using a token distribution to predict its effect demonstrates that specific distinction; applying it to factual reliability may still need a fresh probe.

At session boundaries, the assistant saves a compact checkpoint to available private learner-controlled storage or provides one to carry into the next conversation. The repository includes a private local checkpoint store for assistants with a persistent Linux/macOS filesystem; it does not supply hosted storage or guarantee assistant memory. Real learner records do not belong in this public repository.

## Reliable progress storage

The [storage protocol](shared/progress-storage.md) connects every skill to a shared private profile. The Python store validates checkpoints, saves atomically, detects conflicting updates, verifies saves, and retains revisions for recovery. Save after meaningful updates so an unexpected session ending does not discard the whole session.

```bash
python3 scripts/learner_progress.py --profile default load
```

By default, records live outside the repository in `~/.local/share/ai-engineering-skills/progress`. Set `AI_ENGINEERING_PROGRESS_DIR` to choose another private persistent location. Use one profile across topics and a separate profile for each learner. See the protocol for saving, conflict handling, restoring, and moving progress.

Requires Python 3 on Linux/macOS. Continuity requires the same persistent storage on later sessions. Cross-device sync and hosted accounts are not included. Assistants without durable file access must use a private storage integration or give the learner a checkpoint to carry forward.

Run storage checks with `python3 -m unittest discover -s tests -v`.

## External resources are part of the system

The AI should not replace excellent books, papers, courses, documentation, visualizations, or repositories with generated summaries. It should help the learner use the best source for the current gap.

Resources such as *AI Engineering from Scratch*, Hugging Face learning material, official documentation, papers, and strong interactive explanations can be used as teaching instruments.

A skill should select a resource **after identifying the learning need**. When assigning one, it should explain:

- why this resource fits the current gap
- the exact section or exercise when possible
- what to pay attention to
- what can be ignored for now
- what experiment or discussion follows it

The goal is not to collect links. Every resource should earn its place.

The [resource catalog](resources/catalog.md) maps all 14 topic skills to reviewed sections, prerequisites, focused exercises, and alternatives. It includes selected AI Engineering from Scratch lessons, Hugging Face material, and official engineering documentation. The catalog records where toy implementations and provider-specific behavior limit an example.

## Adaptive scope

Topic lists are competency maps, not mandatory syllabi.

A skill decides what to cover by asking:

1. Does the learner already understand this reliably?
2. Will it help explain behavior they need to reason about?
3. Will it help them make an engineering decision?
4. Is it a prerequisite for an important gap?

If none apply, the topic can wait.

This means two learners may take very different paths through the same skill. "Fundamentals" is defined partly by the learner's goal.

## Structure

```text
skills/
  ai-engineering-coach/
    SKILL.md
  llm-fundamentals/
    SKILL.md
  prompting-structured-outputs/
    SKILL.md
  embeddings/
    SKILL.md
  retrieval/
    SKILL.md
  rag/
    SKILL.md
  tool-calling/
    SKILL.md
  agents-workflows/
    SKILL.md
  evals/
    SKILL.md
  observability/
    SKILL.md
  latency-cost/
    SKILL.md
  model-selection/
    SKILL.md
  serving-deployment/
    SKILL.md
  safety-failure-handling/
    SKILL.md
  production-ai-system-design/
    SKILL.md

shared/
  teaching-principles.md
  learner-model.md
  progress-storage.md
  resource-schema.md

resources/
  catalog.md
```

The master coach helps identify the next important gap and routes learning across topic skills. Topic skills contain the competency map, diagnostic behavior, intervention strategies, experiments, resource guidance, and standards for evidence of understanding.

## Topic skills

Choose a skill directly or let the coach route from the current gap. Each topic provides a competency map, a diagnostic probe, a controlled experiment, transfer evidence, and a learner-model handoff.

| Skill | Focus |
| --- | --- |
| [LLM Fundamentals](skills/llm-fundamentals/SKILL.md) | Predict and explain model behavior |
| [Prompting and Structured Outputs](skills/prompting-structured-outputs/SKILL.md) | Prompt reliability, examples, schema-constrained generation, or invalid structured responses |
| [Embeddings](skills/embeddings/SKILL.md) | Vector representations, semantic similarity, embedding models, or nearest-neighbor behavior |
| [Retrieval](skills/retrieval/SKILL.md) | Search quality, chunking, hybrid search, reranking, or retrieval misses |
| [Retrieval-Augmented Generation](skills/rag/SKILL.md) | Grounded answers, citations, retrieved context, or RAG system failures |
| [Tool Calling](skills/tool-calling/SKILL.md) | Function calls, tool schemas, tool execution, or external actions requested by a model |
| [Agents and Workflows](skills/agents-workflows/SKILL.md) | Agent loops, planning, autonomous execution, workflow orchestration, or stopping behavior |
| [Evaluations](skills/evals/SKILL.md) | LLM quality measurement, regression testing, benchmark design, or model-based judges |
| [Observability](skills/observability/SKILL.md) | LLM tracing, production debugging, quality monitoring, or telemetry design |
| [Latency and Cost](skills/latency-cost/SKILL.md) | Token budgets, slow responses, caching, batching, or inference cost tradeoffs |
| [Model Selection](skills/model-selection/SKILL.md) | Choosing or comparing models, model routing, or deciding whether a larger model is needed |
| [Serving and Deployment](skills/serving-deployment/SKILL.md) | Deploying LLM services, inference capacity, load handling, or rollout reliability |
| [Safety and Failure Handling](skills/safety-failure-handling/SKILL.md) | Prompt injection, unsafe tool actions, data leakage, or resilient LLM failure behavior |
| [Production AI System Design](skills/production-ai-system-design/SKILL.md) | End-to-end AI architecture, production tradeoffs, or integrating quality, reliability, and operational constraints |

Keep this repository together when using the skills: topic instructions depend on `shared/` and `resources/`. Copying a topic folder alone omits the shared teaching and learner-model protocols.

## What this is not

It is not a generated textbook.

It is not a fixed course that assumes every learner starts from the same place.

It is not a checklist where "covered" means "learned."

It is not a large directory of resources with no opinion about when or why to use them.

It is not an attempt to make the AI the source of all knowledge.

## Design principles

**Mental models over material coverage.**

**Diagnosis before explanation.**

**Prediction before revelation when useful.**

**Experiments over definitions.**

**Evidence over completion.**

**Use the best source for the gap.**

The long-term goal is a set of portable skills that can run in AI assistants and behave less like digital textbooks and more like adaptive mentors for AI engineering.
