# Learner model protocol

Use this protocol in the coach and every topic skill. Treat the model as a revisable account of demonstrated understanding, not a verdict about the learner.

## Persist the shared record

Apply [progress storage](progress-storage.md) before teaching and after meaningful updates. Use one private learner profile across all topics, load its current revision, and save with conflict detection and verification. Keep the schema below for both JSON storage and YAML exports. Save during the session rather than relying on a final checkpoint.

## Maintain a small working model

Track only concepts relevant to the current goal, active gaps, and prerequisites. Do not populate the entire competency map with guesses.

Keep the learner's stated goal, constraints, active topic, and a short concept record:

| Field | Record |
| --- | --- |
| Concept | A narrow claim or distinction, not a whole subject such as “LLMs” |
| Current belief | What the learner appears to believe; label paraphrases as inferences |
| Evidence | A short response/action reference, task context, date or turn, and whether help was given |
| Assessment | untested, developing, demonstrated, or needs-recheck |
| Confidence | low, medium, or high confidence in this assessment, with a brief reason |
| Gap or uncertainty | Misconception, missing prerequisite, limited transfer, or what remains unknown |
| Next probe | One prediction, explanation, debugging task, or transfer task that could change the assessment |

Use `untested` when evidence is absent. Use `developing` for partial or assisted performance. Use `demonstrated` only within the conditions actually tested. Use `needs-recheck` when conflicting evidence or changed conditions make an earlier assessment uncertain. Never interpret these labels as permanent ability or a mastery percentage.

## Update after meaningful evidence

1. Observe the learner's prediction, explanation, code, debugging choice, question, or experiment interpretation. Record what actually happened separately from your inference. A question may suggest a gap without proving one.
2. Compare it with the current concept record. Add, refine, strengthen, weaken, or reopen only the claims the evidence bears on. Leave unrelated records unchanged.
3. Weigh independence and transfer. Agreement, confidence, vocabulary, and reading completion do not demonstrate understanding. A correct answer after a hint is assisted evidence; repeating your explanation is weaker than applying it to a fresh case.
4. Handle contradictions explicitly. Retain the earlier evidence, note the new counterexample, and narrow the claim or mark it `needs-recheck`. Check for a slip, ambiguous wording, missing prerequisite, or task/tool failure before inferring a misconception. Do not assume your own explanation or a noisy experiment is ground truth; verify the disputed point when needed.
5. Choose the smallest useful next action from the revised model. Repair a prerequisite if it blocks the goal; use a new example if transfer is uncertain; move ahead when evidence is sufficient for the current goal. Do not keep testing merely to fill the record.

Do not update learning status for greetings or scheduling messages. Do update stated goals and constraints when the learner changes them. Never invent an experiment result or treat an assigned task as completed.

## Calibrate and keep the learner involved

Separate confidence in the assessment from the level of understanding: you can be highly confident that understanding is still partial. Prefer independent evidence across different situations before making a broad claim. Do not infer mastery of prerequisites from success on a later task.

Make important revisions visible in one short sentence, such as “You can explain sampling now; we still need to check whether you can use it to debug an output.” Let the learner inspect and correct the record. Treat their correction as new information, preserve the distinction between self-report and demonstrated performance, and avoid arguing about labels.

Keep routine bookkeeping out of the dialogue. Do not infer personality, intelligence, motivation, or a fixed learning style from errors. Record only learning-relevant information.

## Resume and hand off

At session start, use an available learner checkpoint before asking repeated diagnostic questions. Check its goal, evidence, and unresolved probes; do not treat an old summary as fresh proof. Recheck stale or conflicting claims when they matter to the next decision, rather than automatically resetting all progress.

Maintain one learner record across coach and topic handoffs. Pass the relevant concept records and return evidence-based changes to the coach; do not create competing assessments of the same claim.

When a session ends or a handoff is useful, compact the record using the template below. Preserve decisive evidence, contradictions, and the pending probe; remove repetitive history. Use an available learner-controlled private storage mechanism, or provide a copyable checkpoint in the conversation. Do not claim cross-session persistence unless the save succeeds. Never commit a real learner's record into this public skills repository. If no record is available next time, acknowledge that and rebuild only what is needed.

```yaml
schema_version: 1
updated: "<date or session reference>"
goal: "<learner-stated outcome>"
constraints: []
active_topic: "<topic>"
concepts:
  - concept: "<narrow claim>"
    current_belief: "<observed statement or explicitly labeled inference>"
    evidence:
      - reference: "<date/turn/task>"
        observation: "<what the learner said or did>"
        assistance: "<none, hint, worked example, or unknown>"
    assessment: untested
    confidence: "low: <reason>"
    gap_or_uncertainty: "<what is unresolved>"
    next_probe: "<one useful task>"
next_action: "<resume here, including any pending experiment>"
```

## Example: revise a claim without overclaiming

- Initial evidence: learner says “temperature adds knowledge.” Record a suspected causal misconception about sampling, with medium confidence; ask what changes if the model weights stay fixed.
- After intervention: learner repeats “temperature changes probabilities” after a worked example. Record assisted, developing understanding; do not mark it demonstrated.
- Fresh task: learner independently predicts how flattening a supplied token distribution changes sampling and explains why it adds no knowledge. Mark that narrow distinction demonstrated; broader debugging transfer remains untested.
- Later contradiction: learner says raising temperature will reliably fix factual errors. Retain the successful distribution task, mark the application to factual reliability as developing, and probe the boundary. Do not erase the earlier evidence or declare all sampling knowledge lost.
