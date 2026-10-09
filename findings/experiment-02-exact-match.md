# Experiment 02 — Exact-Match Scoring

## Evaluation question

Did the model's response exactly match the predefined reference answer?

## System under test

- Model: `llama3.2`
- Runtime: Ollama
- Evaluation framework: Inspect AI
- Dataset: `data/questions.json`
- Sample size: 5

## Requirement and criterion

The scorer compared the model's complete response with the reference answer after trimming surrounding whitespace. Comparison was case-insensitive.

A response passed only if the resulting strings were identical.

## Result

- Samples evaluated: 5
- Passed: 0
- Failed: 5
- Observed exact-match pass rate: 0%

## Interpretation

None of the five responses exactly matched its reference answer under the implemented scoring rule.

Inspection of the responses suggests that the model often provided elaborations or alternative wording. This makes exact string equality unsuitable as a standalone correctness measure for this dataset.

The observed 0% exact-match pass rate does not establish that all five answers were factually incorrect.

## Limitations

The experiment did not apply an independent factual-correctness rubric or verify every claim in the responses. Therefore, it cannot establish the factual accuracy rate.

Exact-match scoring may be appropriate for tasks with deterministic expected outputs, such as some arithmetic or structured extraction tasks. It is generally too restrictive as the sole correctness criterion for open-ended natural-language questions.

## Next step

Design a more appropriate scoring approach and compare its judgments with manually reviewed reference criteria before making stronger correctness claims.
