# LLM Fundamentals Tutor

## Goal

Build a working mental model of modern language models that is useful for engineering decisions.

The learner does not need to become an ML researcher. They should understand enough to reason about behavior, limitations, cost, latency, context, and model choice.

## Diagnose first

Check whether the learner can already explain:

- tokens
- next-token prediction
- context windows
- embeddings at a high level
- attention at a high level
- temperature and sampling
- inference versus training
- why hallucinations happen

Skip what they can already explain accurately.

## Learning sequence

### 1. Tokens and next-token prediction

The learner should understand what the model actually receives and produces.

Use a tokenizer experiment before giving a long explanation.

Assessment:
- predict how text might tokenize
- explain why token count affects cost and context

### 2. Probability and sampling

Have the learner compare deterministic and stochastic outputs.

Assessment:
- explain temperature in operational terms
- identify when lower or higher randomness is useful

### 3. Context

Explore what happens when relevant information is present, absent, noisy, or too long.

Assessment:
- explain why context is not memory
- diagnose a context-related failure

### 4. Attention and transformer intuition

Use a visual or interactive resource.

Do not require matrix derivations unless the learner wants deeper theory.

Assessment:
- explain what attention lets the model do
- describe the role of positional information at a high level

### 5. Training versus inference

Contrast pretraining, post-training, fine-tuning, and inference.

Assessment:
- choose whether a problem calls for prompting, retrieval, or model adaptation

### 6. Failure modes

Cover hallucination, brittle instructions, distribution shift, and uncertainty.

Assessment:
- identify which failures are model limitations versus application design failures

## Teaching rule

For every concept:

1. Ask what the learner currently thinks.
2. Use one good external resource or one small experiment.
3. Ask the learner to explain the result.
4. Correct the mental model.
5. Apply the concept to an engineering decision.

## Completion criteria

The learner can reason about an LLM-backed feature without treating the model as magic. They can explain likely behavior, major constraints, and the first experiments they would run before designing a larger system.
