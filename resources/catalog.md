# Resource Catalog

Reviewed on 2026-10-19. Select a resource after diagnosing a gap; this is a routing map, not required reading. The focus, skip choices, and follow-up exercises below are this project's teaching recommendations. They are not claims that the source author prescribes these exercises.

## Routing

| Topic skill | First resource | Alternative when the gap differs |
| --- | --- | --- |
| [llm-fundamentals](../skills/llm-fundamentals/SKILL.md) | [hf-inference](#hf-inference) | Use the alternatives field in the selected entry. |
| [prompting-structured-outputs](../skills/prompting-structured-outputs/SKILL.md) | [claude-structured](#claude-structured) | Use the alternatives field in the selected entry. |
| [embeddings](../skills/embeddings/SKILL.md) | [sbert-semantic](#sbert-semantic) | [scratch-embeddings](#scratch-embeddings) |
| [retrieval](../skills/retrieval/SKILL.md) | [sbert-rerank](#sbert-rerank) | Use the alternatives field in the selected entry. |
| [rag](../skills/rag/SKILL.md) | [scratch-rag](#scratch-rag) | Use the alternatives field in the selected entry. |
| [tool-calling](../skills/tool-calling/SKILL.md) | [claude-tools](#claude-tools) | Use the alternatives field in the selected entry. |
| [agents-workflows](../skills/agents-workflows/SKILL.md) | [anthropic-agents](#anthropic-agents) | Use the alternatives field in the selected entry. |
| [evals](../skills/evals/SKILL.md) | [anthropic-evals](#anthropic-evals) | Use the alternatives field in the selected entry. |
| [observability](../skills/observability/SKILL.md) | [otel-spans](#otel-spans) | Use the alternatives field in the selected entry. |
| [latency-cost](../skills/latency-cost/SKILL.md) | [hf-inference](#hf-inference) | [hf-streaming](#hf-streaming), [scratch-cost](#scratch-cost) |
| [model-selection](../skills/model-selection/SKILL.md) | [claude-model-choice](#claude-model-choice) | Use the alternatives field in the selected entry. |
| [serving-deployment](../skills/serving-deployment/SKILL.md) | [hf-serving](#hf-serving) | Use the alternatives field in the selected entry. |
| [safety-failure-handling](../skills/safety-failure-handling/SKILL.md) | [claude-injection](#claude-injection) | Use the alternatives field in the selected entry. |
| [production-ai-system-design](../skills/production-ai-system-design/SKILL.md) | [google-slos](#google-slos) | Use the alternatives field in the selected entry. |

## Selection and maintenance

Assign only the listed sections needed for the current gap. Explain the purpose, focus, skip boundary, and follow-up task. Use observed prediction, debugging, or transfer evidence to update the shared learner model; reading completion does not establish competence.

Check the live section and installed library/API version before use. A review date records source inspection, not successful execution of every example. Use mocks or supplied traces when credentials or hardware are unavailable; label simulation clearly. Obtain an explicit budget before paid experiments. Prices, model IDs, provider limits, and benchmark claims must be verified at use time, not copied from course tables.

Provider documentation is authoritative for that provider's behavior, not a universal interface. Match equivalent concepts to the learner's stack. The coach may choose a better primary source for the diagnosed gap; the catalog does not require switching providers.

AI Engineering from Scratch's canonical repository is [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch), linked from its [course website](https://aiengineeringfromscratch.com/). Its three selected lessons below were inspected directly. Use their implementation mechanics with the stated limitations; do not import their syllabus or install their tutor as a prerequisite. Hugging Face provides the inference and serving material; Sentence Transformers supplies the search examples.

The OpenTelemetry entry uses the new GenAI conventions repository rather than the retired website path. These conventions remain in development; record the revision used for an implementation exercise.

Each entry follows [resource-schema.md](../shared/resource-schema.md). To replace an entry, verify the new source and section, retain the teaching purpose, and check topic routing. Do not pad the catalog with duplicate general courses.

## hf-inference

[Open resource](https://huggingface.co/learn/llm-course/en/chapter1/8)

```yaml
title: 'Hugging Face LLM Course: Text Generation Inference'
type: course
url: https://huggingface.co/learn/llm-course/en/chapter1/8
author: Hugging Face
topics:
- llm-fundamentals
- latency-cost
level: beginner
use_for: Connect generation behavior to inference work.
why_this_resource: Connects probability-based token choices to the separate work of processing input and
  generating output.
specific_sections:
- The Two-Phase Inference Process
- Sampling Strategies
- Key Performance Metrics
focus_on: Distinguish prefill from decode, and sampling from learned knowledge.
skip_for_now: Beam search and cache implementation details until the goal needs them.
prerequisites:
- Basic Python; a conceptual probability distribution
follow_up_exercise: Predict how longer input and longer output affect first-token and completion time
  separately. Measure repeated trials or use labeled traces, then explain mismatches.
alternatives: hf-streaming for a visible streaming example.
```

## claude-structured

[Open resource](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

```yaml
title: Claude structured outputs
type: docs
url: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
author: Anthropic
topics:
- prompting-structured-outputs
level: intermediate
use_for: Repair confusion between format compliance and correct extraction.
why_this_resource: Documents actual schema behavior, SDK transformations, and failure cases rather than
  prompt recipes.
specific_sections:
- How it works
- JSON Schema limitations
- Invalid outputs
focus_on: Check application semantics separately from decoding constraints; handle refusal and truncation.
skip_for_now: SDK language variants and complex schemas.
prerequisites:
- JSON Schema basics; ordinary API calls
follow_up_exercise: Extract synthetic invoice totals with and without constraints. Count invalid structures
  and wrong totals separately; add an application check for conflicting totals.
alternatives: Use the installed provider's official schema documentation when the learner uses a different
  API.
```

## sbert-semantic

[Open resource](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)

```yaml
title: Sentence Transformers semantic search
type: docs
url: https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html
author: Sentence Transformers maintainers
topics:
- embeddings
level: beginner
use_for: Make embedding comparisons observable.
why_this_resource: Provides a small search implementation and distinguishes query/document tasks.
specific_sections:
- Symmetric vs. Asymmetric Semantic Search
- Manual Implementation
focus_on: Compare representations within one model space; inspect high-similarity counterexamples.
skip_for_now: Approximate indexes and search-engine integrations.
prerequisites:
- Python; vector similarity intuition
follow_up_exercise: Rank paraphrases, contradictions, identifiers, and unrelated text. Explain why a close
  vector does not establish truth, then test a new query.
alternatives: scratch-embeddings for implementing similarity math; sbert-rerank for ranking errors.
```

## sbert-rerank

[Open resource](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)

```yaml
title: Sentence Transformers retrieve and rerank
type: docs
url: https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html
author: Sentence Transformers maintainers
topics:
- retrieval
level: intermediate
use_for: Separate missing candidates from poor ordering.
why_this_resource: Shows candidate generation and pairwise relevance scoring as distinct stages.
specific_sections:
- Retrieve & Re-Rank Pipeline
- 'Retrieval: Bi-Encoder'
- 'Re-Ranker: Cross-Encoder'
focus_on: Rerankers only see supplied candidates; measure candidate recall separately.
skip_for_now: Large Wikipedia downloads and model training.
prerequisites:
- Embeddings; a small labeled query set
follow_up_exercise: Remove the relevant document before reranking, then restore it with a poor initial
  rank. Predict which failure reranking can repair and measure both stages.
alternatives: sbert-semantic for prerequisite gaps; scratch-rag for downstream context assembly.
```

## scratch-rag

[Open resource](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/06-rag/docs/en.md)

```yaml
title: 'AI Engineering from Scratch: RAG'
type: repository
url: https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/06-rag/docs/en.md
author: Rohit Ghumare and contributors
topics:
- rag
level: intermediate
use_for: Inspect a small retrieval-to-prompt pipeline without framework machinery.
why_this_resource: Makes intermediate representations and context construction visible.
specific_sections:
- The Full Pipeline
- 'Build It: Steps 1-6'
focus_on: Trace chunk IDs through search, context construction, and the answer stage. The lesson uses
  TF-IDF and simulated generation; neither demonstrates neural semantic search or actual grounded generation.
skip_for_now: Provider price comparisons and broad claims that RAG always beats fine-tuning.
prerequisites:
- Python; retrieval basics; NumPy for the implementation
follow_up_exercise: Build the local pipeline, log retrieved sources, and test a missing-answer case. Replace
  simulated generation only if available, then evaluate actual claim support separately.
alternatives: 'Contextual Retrieval article for chunk-context failures: https://www.anthropic.com/engineering/contextual-retrieval'
```

## claude-tools

[Open resource](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)

```yaml
title: Claude tool use overview
type: docs
url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
author: Anthropic
topics:
- tool-calling
level: intermediate
use_for: Identify who executes a tool and how its result returns.
why_this_resource: The client-tool round trip exposes the application execution boundary.
specific_sections:
- How tool use works
- When Claude uses tools
focus_on: Distinguish proposed calls, execution, and returned results. Add authorization and idempotency
  in the application; schema validation does not supply them.
skip_for_now: Hosted-tool catalog and pricing tables.
prerequisites:
- JSON; request/response APIs
follow_up_exercise: Implement a local fake refund executor. Inject a timeout after the write and retry
  the proposal; show that duplicate effects are prevented.
alternatives: claude-structured for schema constraints; anthropic-agents for loop control.
```

## anthropic-agents

[Open resource](https://www.anthropic.com/engineering/building-effective-agents)

```yaml
title: Building effective agents
type: article
url: https://www.anthropic.com/engineering/building-effective-agents
author: Erik Schluntz and Barry Zhang, Anthropic
topics:
- agents-workflows
level: intermediate
use_for: Choose between fixed orchestration and model-directed control.
why_this_resource: Puts simple workflow patterns and open-ended loops side by side.
specific_sections:
- When (and when not) to use agents
- 'Workflow: Prompt chaining'
- Agents
focus_on: Find where control decisions occur and how environment feedback informs the next action.
skip_for_now: Framework surveys and multi-agent expansion.
prerequisites:
- Tool-call boundaries; basic state management
follow_up_exercise: Run a fixed workflow and bounded loop against the same canned tool results. Compare
  success, calls, and stop reasons for an empty search and a repeated result.
alternatives: claude-tools when execution semantics are the blocking gap.
```

## anthropic-evals

[Open resource](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

```yaml
title: Demystifying evals for AI agents
type: article
url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
author: Anthropic Engineering
topics:
- evals
level: intermediate
use_for: Turn observed failures into task-based evaluation.
why_this_resource: Explains grader choices and the difference between an execution transcript and a useful
  outcome.
specific_sections:
- Types of graders for agents
- Capability vs. regression evals
- Collect tasks for the initial eval dataset
focus_on: Use explicit outcomes, inspect grader disagreements, and calibrate model judgments against humans.
skip_for_now: Benchmark score comparisons and large harness adoption.
prerequisites:
- A concrete task contract; basic testing
follow_up_exercise: Build a small development/held-out split from synthetic failures. Compare two variants
  with blind grading; explain a case where average quality hides a severe regression.
alternatives: google-slos for service objectives rather than answer-quality rubrics.
```

## otel-spans

[Open resource](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md)

```yaml
title: OpenTelemetry GenAI client spans
type: docs
url: https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md
author: OpenTelemetry contributors
topics:
- observability
level: intermediate
use_for: Design telemetry that can distinguish failure stages.
why_this_resource: 'Uses shared operation semantics rather than a vendor dashboard. The conventions are
  in development: pin the version used in an exercise.'
specific_sections:
- Spans
- Execute tool span
- Capturing instructions, inputs, and outputs
focus_on: Trace operation boundaries and errors. Follow the linked Client Inference page for model-call
  attributes; keep content capture deliberately limited.
skip_for_now: Full attribute catalogs and default recording of raw prompts.
prerequisites:
- Basic distributed tracing; request correlation
follow_up_exercise: Instrument a mocked retrieval-and-tool request. Inject one timeout and one slow dependency;
  diagnose them without logging sensitive content.
alternatives: google-slos for deciding which signals matter; repository docs index for changed conventions.
```

## hf-streaming

[Open resource](https://huggingface.co/docs/text-generation-inference/en/conceptual/streaming)

```yaml
title: 'Hugging Face Text Generation Inference: Streaming'
type: docs
url: https://huggingface.co/docs/text-generation-inference/en/conceptual/streaming
author: Hugging Face
topics:
- latency-cost
level: beginner
use_for: Separate responsiveness from completion time.
why_this_resource: Shows the same request consumed incrementally rather than treating streaming as less
  computation.
specific_sections:
- What is Streaming?
- How to use Streaming?
focus_on: Measure first visible output and final completion separately.
skip_for_now: Transport internals and every client language.
prerequisites:
- Python or JavaScript; HTTP requests
follow_up_exercise: Compare streaming and buffered delivery for the same workload. Record first-token
  time, completion time, and usage; explain what improved and what did not.
alternatives: hf-inference for prefill/decode mechanisms; scratch-cost for local budget simulation.
```

## scratch-cost

[Open resource](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/11-caching-cost/docs/en.md)

```yaml
title: 'AI Engineering from Scratch: Caching, Rate Limiting and Cost'
type: repository
url: https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/11-caching-cost/docs/en.md
author: Rohit Ghumare and contributors
topics:
- latency-cost
level: intermediate
use_for: Implement a local budget model and cache experiments.
why_this_resource: Exposes the accounting and cache policy in inspectable Python.
specific_sections:
- 'Build It: Step 2: Exact Cache'
- 'Build It: Step 4: Rate Limiter'
- 'Build It: Step 5: Cost Tracker'
focus_on: Use synthetic prices and label simulated latency. Include tenant, authorization, model, prompt
  version, and freshness in cache policy.
skip_for_now: Static prices, model names, savings claims, and any implication that temperature zero guarantees
  determinism.
prerequisites:
- Python; token accounting; dictionary-based caching
follow_up_exercise: Change a policy version and a user permission while keeping query text fixed. Show
  that an old or unauthorized answer is not reused, then reconcile simulated spend with the call log.
alternatives: 'Official provider caching behavior: https://platform.claude.com/docs/en/build-with-claude/prompt-caching'
```

## claude-model-choice

[Open resource](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)

```yaml
title: Choosing the right model
type: docs
url: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
author: Anthropic
topics:
- model-selection
level: intermediate
use_for: Make a workload-specific selection under constraints.
why_this_resource: Offers efficiency-first and capability-first starting strategies plus evaluation criteria.
specific_sections:
- Establish key criteria
- Choose the best model to start with
- Decide whether to upgrade or change models
focus_on: Compare task quality, speed, cost, and required capabilities. Treat vendor candidates as examples,
  not a cross-provider ranking.
skip_for_now: Model-name recommendations and pricing tables until checked for the actual environment.
prerequisites:
- A representative evaluation set; latency and cost measures
follow_up_exercise: Choose two available candidates, define a quality floor, and compare the same held-out
  cases. Change the latency ceiling and justify whether the choice changes.
alternatives: anthropic-evals when the task-quality evidence is weak.
```

## hf-serving

[Open resource](https://huggingface.co/docs/text-generation-inference/en/basic_tutorials/launcher)

```yaml
title: Text Generation Inference launcher arguments
type: docs
url: https://huggingface.co/docs/text-generation-inference/en/basic_tutorials/launcher
author: Hugging Face
topics:
- serving-deployment
level: intermediate
use_for: Connect admission limits to queueing and resource use.
why_this_resource: Documents actual serving controls for concurrency and token budgets.
specific_sections:
- MAX_CONCURRENT_REQUESTS
- MAX_TOTAL_TOKENS
- MAX_BATCH_TOTAL_TOKENS
focus_on: Reason about memory and overload together. Use as a concrete serving reference, not a default
  deployment recommendation.
skip_for_now: Sharding, quantization, kernels, and remote-code loading.
prerequisites:
- HTTP service basics; prefill/decode intuition
follow_up_exercise: Model a bounded local service and vary arrivals independently of service time. Define
  rejection and deadline behavior before considering a real GPU load test.
alternatives: google-slos for rollout criteria; installed serving engine documentation for its actual
  controls.
```

## claude-injection

[Open resource](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)

```yaml
title: Mitigate jailbreaks and prompt injections
type: docs
url: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks
author: Anthropic
topics:
- safety-failure-handling
level: intermediate
use_for: Identify untrusted content and enforce action boundaries.
why_this_resource: Separates direct adversarial requests from attacks arriving through documents and tool
  results.
specific_sections:
- Indirect prompt injection
focus_on: Apply least privilege and application authorization. Treat screening and prompting as fallible
  layers, not proof of safety.
skip_for_now: Long classifier examples until a concrete trust boundary is understood.
prerequisites:
- Tool execution; basic access control
follow_up_exercise: Put export instructions inside a synthetic retrieved document and then inside a tool
  result. Verify denied exports through recorded effects and enforce tenant filters independently of the
  model.
alternatives: claude-tools for the execution boundary; anthropic-evals for adversarial regression cases.
```

## google-slos

[Open resource](https://sre.google/sre-book/service-level-objectives/)

```yaml
title: 'Site Reliability Engineering: Service Level Objectives'
type: book
url: https://sre.google/sre-book/service-level-objectives/
author: Chris Jones, John Wilkes, and Niall Murphy; Google SRE
topics:
- production-ai-system-design
level: intermediate
use_for: Turn product promises into measurable service contracts.
why_this_resource: Explains user-centered objectives, measurement conditions, and why averages hide poor
  experience. It is a general systems reference, not an LLM quality guide.
specific_sections:
- Indicators in Practice
- Aggregation
- Objectives in Practice
focus_on: Specify correctness and user-visible latency, then add AI task-quality checks from evals.
skip_for_now: Contractual SLA details and objectives unrelated to the learner's task.
prerequisites:
- A concrete product task; basic service metrics
follow_up_exercise: Define a success contract for a synthetic assistant, including supported answers and
  denied actions. Inject a dependency timeout and propose release/rollback signals from user outcomes.
alternatives: anthropic-evals for task quality; hf-serving for concrete inference controls.
```

## scratch-embeddings

[Open resource](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/04-embeddings/docs/en.md)

```yaml
title: 'AI Engineering from Scratch: Embeddings and Vector Representations'
type: repository
url: https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/04-embeddings/docs/en.md
author: Rohit Ghumare and contributors
topics:
- embeddings
level: beginner
use_for: Implement vector comparison before choosing infrastructure.
why_this_resource: The small implementation makes normalization and search mechanics inspectable.
specific_sections:
- Similarity Metrics
- 'Build It: Steps 2-4'
focus_on: The local embedder uses TF-IDF, not a trained semantic model. Use it to study geometry and lexical
  limitations, then compare a neural model.
skip_for_now: Historical survey, model leaderboards, HNSW complexity claims, and scale tables.
prerequisites:
- Python; NumPy; dot product and vector norm
follow_up_exercise: Test a paraphrase with no shared words in TF-IDF and a neural embedder. Predict the
  difference and explain why the toy index cannot establish semantic competence.
alternatives: sbert-semantic for the neural query/document comparison.
```
