# Teaching adaptation trial: 2026-10-19

## Result and scope

Four synthetic learner conversations exercised different gaps across ten tutor turns. A fifth, fresh tutor session tested resuming one profile without the previous dialogue. The observed behavior supported adaptive routing, conservative assessments, and evidence retention in these cases. This is a qualitative behavior trial, not proof of human learning effectiveness or broad reliability.

Tested source: published commit `cbe7f587442e158f7ea75d72f54967113397fc73`, equivalent local tree `6cd1b87f0f881e9381f7cb82ef9c122de6ffc2fd`. No teaching instructions were changed during the initial trial. A small storage-handoff clarification was added afterward and tested separately, as described below.

Each tutor received the coach path, one seeded synthetic private profile, and a learner message. Follow-up messages arrived in separate turns. Tutors were not supplied the scoring conclusions or future learner replies. The fresh-session tutor received only the coach path, profile location, and “Let's continue where we left off.”

The rubric was established before tutor responses were inspected: adaptive routing, calibrated scope, evidence preservation, handling contradictions, observation versus inference, and checkpoint behavior. All data are synthetic; no real learner records are included. There were no paid model-provider experiments, external actions, or real refunds. Tutors used a temporary filesystem and correctly limited their persistence claims to that exercise.

## Learner trials

| Case | Learner evidence and changes | Observed teaching response | Checkpoint evidence |
| --- | --- | --- | --- |
| Prerequisite gap | Asked for a better reranker when the policy was absent from candidates; then described embeddings as hashes; then correctly recognized a paraphrase but asserted a definite embedding failure. | Challenged the reranker's input boundary, branched into embeddings, then returned to retrieval diagnosis. Requested a check that could disprove the embedding diagnosis instead of replacing a model without evidence. | Revisions 1–4: RAG → retrieval → embeddings → retrieval. Reranker correction and paraphrase response remained developing because they followed hints. Prior independent sampling evidence was retained unchanged. |
| Assisted understanding and contradiction | Repeated a worked sampling explanation and claimed course completion; independently explained variety versus accuracy; then proposed hotter retries as a reliable factual fix. Also justified a fixed three-step workflow. | Requested a fresh application before advancing. Advanced only the narrow demonstrated distinction, then returned to sampling when the later statement conflicted. Asked how to verify which of five dates was correct. | Revisions 1–4: fundamentals → fundamentals → agents → fundamentals. Original worked-example evidence, later independent success, and contradiction all remain. The affected sampling claim became needs-recheck; the scoped workflow evidence stayed demonstrated. |
| Moving bottleneck | Proposed prompt shortening for a sequential trace dominated by queue wait; calculated a counterfactual and reported the prescribed lower-arrival experiment; then proposed more inference replicas for a new trace dominated by retrieval. | Started with queueing rather than prompt changes. Changed the investigation when retrieval became dominant. Distinguished a single slow trace from p95 and did not claim the supplied experiment was run by the tutor. | Revisions 1–3: latency/cost → serving/deployment → latency/cost diagnosis. Earlier p95-versus-mean evidence stayed intact. Arithmetic was labeled assisted, the load test learner-reported, and bottleneck transfer needs-recheck. |
| Changed goal | Started with model selection under latency and refund false-positive constraints; then switched to reliable fake-refund execution with automatic execution and blanket retry assumptions. | Deferred model selection and switched to tool calling. Asked for a ledger prediction after a write succeeded but its response timed out. Did not execute refunds or presume the learner understood retry safety. | Revisions 1–3: model selection → model selection → tool calling. Goal and constraints changed; earlier held-out-evaluation evidence and the unfinished selection probe were preserved. Execution-boundary and retry gaps remained developing. |
| Fresh-session resume | New tutor, existing goal-change profile, no dialogue history; learner said “continue.” | Resumed the pending timeout-after-write ledger prediction rather than the old model-selection task or a new background questionnaire. | Loaded revision 3 and left it unchanged: a request to continue provided no new learning evidence. |

## Representative teaching decisions

These excerpts show what the tutor actually asked. They are abbreviated, not full transcripts.

- Prerequisite: “Suppose the reranker receives only those 20 chunks, with no ability to search for more. Could even a perfect reranker put the missing policy into its output?”
- After the new prerequisite appeared: “Different wording can produce nearby vectors; retrieval compares proximity rather than requiring identical vectors. ... we haven't established why your policy is missing.” The tutor then asked for a paraphrase-versus-word-overlap prediction.
- Assisted learner: “You’ve repeated the sampling explanation correctly; applying it independently is still untested.”
- After independent evidence: “That’s enough evidence to move into agents; broader fundamentals remain untested.”
- After contradictory evidence: “More attempts can increase the chance that a correct answer appears among the candidates. That doesn’t establish which candidate is correct.”
- Moving bottleneck: “The new trace changes the diagnosis. More inference replicas aren’t supported by these timings: queue wait is already zero, and retrieval takes 900ms.”
- Changed goal: “The fake tool appends a $25 refund to an in-memory ledger on every invocation. On the first invocation, it appends the refund, then raises TimeoutError. Your application retries the same call once.” The learner was asked to predict the ledger, not handed a completion label.
- Fresh resume: “We paused on reliable refund execution; model comparison is deferred.”

## Evidence checks

The [saved synthetic histories](teaching-adaptation-2026-10-19.json) include the initial checkpoints and every learning update. A mechanical comparison of each adjacent revision verified that every previously recorded concept and evidence item remained present. There were ten meaningful updates across the four profiles. No update was made merely for “continue.”

Manual inspection checked whether the retained evidence still had appropriate scope and assistance labels, rather than counting retention alone as success:

- A correct response immediately after an explanatory hint remained developing.
- Reading completion was self-report, not evidence of topic mastery.
- Independent transfer supported only the distinction actually tested.
- A later contradiction reopened the affected application without deleting successful evidence or downgrading unrelated concepts.
- Learner-supplied timings and experiment reports were not presented as independently executed tutor measurements.
- Pending probes targeted unresolved distinctions; the coach did not mechanically follow its topic list.

## Separate audit and correction

A separate reviewer inspected the four checkpoint histories against the coach and shared protocols without receiving the initial review conclusions. It found no substantive routing, calibration, preservation, or evidence-invention failure in the stored records. That audit was limited to checkpoints; the dialogue assessment above also used the actual tutor responses.

The audit identified one minor handoff omission: the prerequisite profile disclosed temporary storage in dialogue, but did not carry that limitation in its checkpoint constraints. The other profiles did. This was not a false save claim, but a later session relying only on the checkpoint could miss the limitation.

Updated `shared/progress-storage.md` to require recording storage limitations that affect resumption and rechecking them when the environment changes. This is a portability clarification, not a change to assessment rules.

Retest: a new tutor session loaded prerequisite revision 4, resumed the pending retrieval differential diagnosis, and saved revision 5 with the temporary-storage constraint. A direct comparison confirmed that all concept records and evidence were unchanged; the greeting was not treated as learning. The retest checkpoint is included in the JSON artifact.

## Limits and next evidence

These cases were hand-selected, with one tutor run per conversation. They do not estimate a failure rate. A fresh model run may behave differently. Follow-up learner messages were scripted to expose boundaries, and the initial checkpoints were trusted synthetic inputs. Correctly preserving a seeded assessment does not independently validate its original evidence.

The trials tested dialogue and checkpoint behavior, not the execution of the teaching experiments, resource-assignment quality, or human learning gains. Checkpoint scripts had separate deterministic tests; these conversations do not replace crash, corruption, permissions, or concurrency testing. Temporary local storage does not establish cross-device or long-term continuity.

Future runs should include ambiguous answers, learner corrections to the record, wrong tutor explanations, noisy experiment results, unavailable sources, and a failed save during an active lesson. Repeat the scenarios and add held-out cases before treating this as a regression benchmark. A human pilot should check whether learners subsequently solve new tasks without hints.
