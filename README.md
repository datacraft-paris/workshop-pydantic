# Pydantic Workshop – Learn by Doing

This repository is designed to help you learn **Pydantic**, a powerful Python library for data validation and parsing.
Pydantic is widely used in modern Python projects such as FastAPI, data pipelines, and configuration management.

---

## Workshop Goals

- Understand the core principles of **Pydantic** (models, type validation, automatic parsing).
- Practice with one progressive exercise available in three levels of difficulty.
- Discover how to structure clean and robust data models in Python projects.

---

## Branch Organization

| Branch         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `main`         | Introduction to Pydantic with a mini course and simple examples.           |
| `easy`         | Guided version of the exercise: fill-in-the-blanks and code scaffolding provided. |
| `intermediate` | Moderate guidance: fewer hints, focus on nested models and custom validation. |
| `hard`         | Minimal guidance: only the exercise prompt is provided, for full autonomy. |
| `correction`   | Full solution with explanations and good practices.                         |

> Feel free to start with the `hard` branch if you're up for a challenge.
> If it gets tricky, switch to `intermediate` or `easy` for progressive hints.
> Don't forget to refer to the mini course in `main` — it covers all the key concepts you need.

---

## Setup

### Installation

Install `uv` (Python package manager with virtual environment support):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup

Then, run: `uv sync`

Finally, activate your environment using: `source .venv/bin/activate`

## Practical Session – Build and Validate Pydantic Models

This workshop offers a single exercise available in three levels of difficulty, tailored for learners of all backgrounds.

We recommend starting with the default branch (`main`) to go through the short tutorial and learn how Pydantic works.

Once you're familiar with the basics, you can move on to the other branches depending on your desired challenge level.

Each branch (`easy`, `intermediate`, `hard`) contains:

- Four sequential model files: `model_1.py`, `model_2.py`, `model_3.py`, and `model_4.py`.
  These represent progressive steps of the exercise and must be completed in order.
  Each file builds upon the previous one — serving both as a **partial correction** and a **new step** that adds complexity.
  To access the **complete final solution**, refer to the `correction` branch, which provides the full version of `model_4.py`.
- Four corresponding test files located in the `tests/` folder: `test_model_1.py`, `test_model_2.py`, etc.
  Each test file is dedicated to checking the behavior of its associated model step.

The structure is the same across all branches to ensure consistency in learning progression.

### main branch

`git checkout main`

### hard branch

`git checkout hard`

### intermediate branch

`git checkout intermediate`

### easy branch
`git checkout easy`

### Find the correction
`git checkout correction`

---

## Check Your Progress Without Spoilers

As you complete each step (`model_1.py` to `model_4.py`), you can validate your implementation by running the corresponding test file located in the `tests/` folder, for that step, such as `test_model_1.py`, `test_model_2.py`, etc., found in all branches.

These tests confirm that your code meets the core requirements of each step **without revealing the full solution**, allowing you to progress independently before consulting the `correction` branch.

Do not modify the test files.
They are designed to verify expected behavior at each stage. While they cover key elements, they do **not guarantee completeness or best practices** — for a full review, you can refer to the final implementation in the `correction` branch.

---

*You're now all set — pick your branch, open the exercise, and start modeling with Pydantic !*
