# Repository guidance

This repository is an executable, adaptive AI-engineering curriculum. Preserve its central behavior: improve the learner's mental model rather than optimize for material coverage.

## Teaching behavior

- Use the shared loop: diagnosis -> mental-model gap -> intervention -> experiment -> evidence of understanding.
- Treat topic competency maps as optional scope, not fixed lesson order.
- Prefer predictions, debugging, experiments, transfer tasks, and justified engineering decisions over recall quizzes or long lectures.
- Do not mark a concept demonstrated from content consumption, confidence, vocabulary, or one assisted answer. Scope assessments to the evidence actually observed.
- Preserve contradictory evidence and reopen only the affected learner-model claim rather than erasing earlier progress.

## Shared protocols

Before changing coach or topic-skill behavior, read the relevant files in `shared/`, especially:

- `shared/teaching-principles.md`
- `shared/learner-model.md`
- `shared/progress-storage.md`
- `shared/resource-schema.md`

Coach and topic skills share one learner model. Keep their behavior aligned with the shared protocols rather than duplicating divergent rules in individual skills.

## Learner progress

- Real learner records are private data and must never be committed to this repository.
- When durable local storage is available, use `scripts/learner_progress.py` and one stable profile across topics.
- Load the current revision before teaching, save after meaningful learner-model or goal changes and before handoff, and respect revision-conflict handling.
- Claim persistence only after a verified successful save. If durable storage is unavailable, provide a portable checkpoint instead of implying memory.
- Keep the checkpoint schema and assessment labels compatible with `shared/learner-model.md`.
- Keep `scripts/learner_progress.py` Python-standard-library-only unless the repository explicitly adopts a dependency-management change.

## Resources

- `resources/catalog.md` is a routing catalog, not required reading.
- Select resources after diagnosing a learning gap.
- Verify the source and exact section before assigning it; do not invent unresolved chapters, URLs, or capabilities.
- Explain why the resource fits, what to focus on, what to skip, and what experiment or transfer task follows.

## Skill structure

Topic skills depend on `shared/` and `resources/`. Do not treat an individual topic directory as fully standalone unless those dependencies are deliberately removed or packaged.

When adding or changing a topic skill, keep its learner-model handoff, resource use, evidence rules, and progress-storage behavior consistent with the coach and sibling skills.

## Validation

Run:

```bash
python3 -m unittest discover -s tests -v
```

Run the storage tests when changing learner progress, checkpoint schema, persistence, or related shared protocols. Verify links and paths when changing the resource catalog or skill routing.
