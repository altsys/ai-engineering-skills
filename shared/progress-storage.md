# Save and resume learner progress

Use one private profile across the coach and all topics. Keep the evidence rules in [learner-model.md](learner-model.md); persistence stores the assessment, it does not establish that it is correct.

## Choose storage once

For an assistant with Python and a persistent Linux/macOS filesystem, use `scripts/learner_progress.py` from the repository root. It requires only the Python standard library. Use the default root `~/.local/share/ai-engineering-skills/progress`, or set `AI_ENGINEERING_PROGRESS_DIR` to a private persistent directory outside every Git checkout. The store rejects a root inside a Git checkout.

Use a stable learner-selected profile ID. In a private single-user environment, `default` is suitable; in a shared environment, establish the correct profile before reading any progress. Never derive an ID from an email address or use one profile for multiple learners. Reuse the same root and profile across topics and sessions.

Check whether the filesystem survives the session. A successful write proves local storage, not cross-device sync or survival of a temporary container. Do not describe a temporary filesystem as durable. If no durable filesystem is available, use an already available private learner-controlled file service with version/conflict protection and read-back verification. Otherwise provide an export and explicitly say progress has not been durably saved. Do not silently switch storage or create competing copies.

## Load before teaching

Run:

```bash
python3 scripts/learner_progress.py --profile default load
```

The result contains `revision` and `checkpoint`. Revision 0 with a null checkpoint means no record exists for this profile. Retain the revision for the next save. Read the goal, constraints, evidence, and pending probe before diagnosing again. An invalid store is an error, not a new learner: preserve the file and report the problem rather than resetting it.

## Save after meaningful updates

Save after each meaningful learner-model update, a goal/constraint change, and before a topic handoff. Do not depend on a final goodbye: sessions can end abruptly. Keep routine storage steps out of the teaching dialogue.

Serialize the complete shared checkpoint as JSON with the same fields and schema version as the YAML template in `learner-model.md`. Preserve relevant concepts and evidence from other topics; the input replaces the complete current checkpoint. Do not include transcripts, secrets, or unrelated personal information. Use standard input rather than writing a temporary learner file into the repository:

```bash
python3 scripts/learner_progress.py --profile default save --expected-revision 0 < /private/path/checkpoint.json
```

The redirect above illustrates a private input file; assistants may supply JSON directly through process standard input. Replace `0` with the revision actually loaded. Never put checkpoint content in shell arguments or interpolate it as shell code. The checkpoint must include `schema_version`, `updated`, `goal`, `constraints`, `active_topic`, `concepts`, and `next_action`. Include evidence for assessed concepts.

Report a save only after a zero exit status and `saved: true`; the command validates and reads back the stored revision before reporting success. On failure, keep the unsaved checkpoint available, tell the learner, and provide a private export or copyable checkpoint. Do not advance the saved revision or claim persistence.

On a revision conflict, reload the current checkpoint, reconcile the new evidence with it, and save against the new revision. Preserve both sessions' evidence and flag contradictions. Never retry with a guessed revision or overwrite a newer record blindly.

## Inspect and recover

```bash
python3 scripts/learner_progress.py --profile default history
python3 scripts/learner_progress.py --profile default restore --revision 2 --expected-revision 5
```

History lists saved revision metadata. Restore appends the chosen checkpoint as a new revision; it does not erase later history. Use the actual revision numbers from load/history. For example, the command above restores revision 2 as revision 6 when the current revision is 5. Set a fresh `updated` reference on the next learning update; restoring does not make old evidence fresh.

Each save retains prior checkpoints in a single atomically replaced file. File locking and required revision checks prevent simultaneous writers from silently losing updates. Private profile directories use mode 0700 and store files use 0600. These permissions are not encryption and do not isolate users sharing one operating-system account. History retains old evidence, including corrected information; keep the whole profile private. A private filesystem backup is still needed for disk loss or corruption. Atomic writes and history do not provide off-device backup.

To move between machines or recover a damaged store, copy the whole profile directory from a trusted private backup while no session is writing, then load and verify it. To export only the latest checkpoint, use `load` and retain its `checkpoint` object in private storage. Import that object with `save` against the destination's loaded revision. This retains the latest learning record but not the source's full revision history. Do not save the load envelope as a checkpoint.

## Assistants without local execution

Use the same protocol and schema with a private storage tool if one is available. Read the current file/version before an update, protect against conflicting writes, then read back and verify it. Do not claim the Python store ran when it did not. If persistence cannot be verified, provide a copyable checkpoint and explain that the learner must carry it into the next session. This repository supplies a reliable local store, not a hosted user-account service.
