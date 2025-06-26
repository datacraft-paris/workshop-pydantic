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

> 💡 Feel free to start with the `hard` branch if you're up for a challenge.
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

As you go through each step of the exercise, you can **validate your work** by running the corresponding test file, such as `test_easy.py`, `test_intermediate.py`, or `test_hard.py`.

These tests help confirm that you've met the key requirements of each stage **without revealing the full solution** — so you can stay focused and avoid spoilers from the `correction` branch.

> 🔒 **Do not edit the test files.**
> They are provided as-is to check the expected behavior at each step.
> While they validate important criteria, they **don’t guarantee your code is perfect** — for a full validation, you should compare your work with the final solution in the `correction` branch.
---

*You're now all set — pick your branch, open the exercise, and start modeling with Pydantic !*
