from inspect_ai import Task, task
from inspect_ai.dataset import json_dataset
from inspect_ai.scorer import Score, accuracy, scorer
from inspect_ai.solver import TaskState, generate


@scorer(metrics=[accuracy()])
def exact_match():
    async def score(state: TaskState, target):
        response = state.output.completion.strip()
        expected = target.text.strip()

        if response.lower() == expected.lower():
            return Score(
                value="C",
                answer=response,
                explanation="Response exactly matches the expected answer.",
            )

        return Score(
            value="I",
            answer=response,
            explanation=f"Expected: {expected}",
        )

    return score


@task
def basic_qa():
    return Task(
        dataset=json_dataset("../data/questions.json"),
        solver=generate(),
        scorer=exact_match(),
    )