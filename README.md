# Inspect + Ollama Evaluation Lab

A hands-on lab for learning **LLM evaluation** using [Inspect AI](https://inspect.aisi.org.uk/) and a locally hosted Ollama model.

The objective is to practice the evaluation lifecycle:

**Claim → Requirement → Test → Evidence → Interpretation**

## Experiments

### Experiment 01 — Basic Response Validity

**Question:** Did the model produce a response containing at least five non-whitespace characters for every test question?

* Model: `llama3.2`
* Runtime: Ollama
* Framework: Inspect AI
* Dataset size: 5 samples
* Result: 5 passed, 0 failed
* Observed pass rate: 100%

**Interpretation:** All five responses satisfied the defined response-length criterion. This does not establish factual correctness, completeness, robustness, or safety.

Findings: `findings/experiment-01-response-validity.md`

### Experiment 02 — Exact-Match Scoring

**Question:** Did each model response exactly match its reference answer, ignoring case and surrounding whitespace?

* Model: `llama3.2`
* Runtime: Ollama
* Framework: Inspect AI
* Dataset size: 5 samples
* Result: 0 passed, 5 failed
* Observed exact-match pass rate: 0%

**Interpretation:** None of the five responses matched its reference answer under the implemented criterion. This does not establish that all five answers were factually incorrect. It demonstrates a limitation of using exact string equality as the sole correctness criterion for open-ended questions.

Findings: `findings/experiment-02-exact-match.md`

## Project Structure

```text
inspect-ollama-eval-lab/
├── README.md
├── data/
│   └── questions.json
├── evals/
│   └── basic_qa.py
├── findings/
│   ├── experiment-01-response-validity.md
│   └── experiment-02-exact-match.md
└── .gitignore
```

Evaluation logs and temporary log dumps are excluded from version control.

## Environment

* OS: Windows 11
* Python: 3.12
* Conda environment: `inspect-ai-lab`
* Evaluation framework: Inspect AI
* Model runtime: Ollama
* Model: `llama3.2`

Reproducing the experiments may require compatible software versions and the same model version.

## Learning Objectives

Learn to:

1. define an evaluation question and requirement;
2. create a test dataset;
3. execute an evaluation using Inspect AI;
4. inspect the evidence;
5. interpret scores in the context of the scoring criterion;
6. state what the evidence does and does not support.

The longer-term objective is to apply these practices to **TEVV-X / AI Assurance** using stronger test criteria, explicit limitations, and traceable evidence.
