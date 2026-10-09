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

shared/
  teaching-principles.md
  resource-schema.md

resources/
  catalog.md
```

The master coach helps identify the next important gap and routes learning across topic skills. Topic skills contain the competency map, diagnostic behavior, intervention strategies, experiments, resource guidance, and standards for evidence of understanding.

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
