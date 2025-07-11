# Pydantic Workshop – Learn by Doing

![illustration](assets/logo_pydantic.jpg)

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/github/license/datacraft-paris/workshop-pydantic)
![Repo Size](https://img.shields.io/github/repo-size/datacraft-paris/workshop-pydantic)
![Last Commit](https://img.shields.io/github/last-commit/datacraft-paris/workshop-pydantic)



This repository is designed to help you learn **Pydantic**, a powerful Python library for data validation and parsing.
Pydantic is widely used in modern Python projects such as FastAPI, data pipelines, and configuration management.
It also enables **structured data generation from AI models**, allowing you to turn raw LLM output into clean, validated Python objects.

---

## Table of Contents
- **[Workshop Goals](#workshop-goals)**
- **[Branch Organization](#branch-organization)**
- **[Project Structure](#project-structure)**
- **[Setup](#setup)**
- **[Check Your Progress](#check-your-progress-without-spoilers)**

---

## Workshop Goals

- Understand the core principles of **Pydantic** (models, type validation, automatic parsing).
- Practice with one progressive exercise available in three levels of difficulty.
- Discover how to structure clean and robust data models in Python projects.
- Learn to integrate Pydantic with AI models for structured and validated data generation.


## Branch Organization

| Branch         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `main`         | Introduction to Pydantic with a mini course and simple examples.           |
| `easy`         | Guided version of the exercise: fill-in-the-blanks and code scaffolding provided. |
| `intermediate` | Moderate guidance: fewer hints, focus on nested models and custom validation. |
| `hard`         | Minimal guidance: only the exercise prompt is provided, for full autonomy. |
| `correction`   | Full solution with explanations and good practices.                         |

> Feel free to start with the `hard` branch if you're up for a challenge. If it gets tricky, switch to `intermediate` or `easy` for progressive hints. Don't forget to refer to the mini course in `main` — it covers all the key concepts you need.



## Project Structure

This workshop is built around a single, progressive exercise divided into five stages, designed to suit learners of all levels. We recommend starting with the default branch `main` to go through the short tutorial and learn how Pydantic works. Once you're familiar with the basics, you can move on to the other branches depending on your desired challenge level.

Each branch (`easy`, `intermediate`, `hard`) includes :

- **Four progressive model directories**:  
  `model_1`, `model_2`, `model_3`, and `model_4`  
  These stages must be completed in order, each building upon the previous one with added complexity and deeper validation logic.

- **Standard file structure in each directory**:
  - `people.py`
  - `company.py`
  - `event.py`
  - `club.py`
  - `enums.py`

- **Structured Output (final stage)** :  
  A dedicated `structured_output/` directory is included to demonstrate how Pydantic can be used to handle structured responses from LLMs.

- **Test coverage**:  
  Each step has an associated test file in the `tests/` folder:
  - `test_model_1.py`
  - `test_model_2.py`
  - `test_model_3.py`
  - `test_model_4.py`

- A `TODO.md` file at the root of the project provides instructions for each stage.

The `correction` branch contains the complete final solution, including `model_4` and the `structured_output` directory.

To switch between versions of the workshop :
```bash
git checkout <branch-name>
```

Replace `<branch-name>` with one of the following :

- `main`         → base structure  
- `easy`         → simplified version  
- `intermediate` → default level  
- `hard`         → advanced version  
- `correction`   → full solution 

---

### Final Stage : Structured Output

The `structured_output` directory showcases an advanced example of how Pydantic can be used to validate data returned from an AI model.

#### Overview

- **Purpose** : Demonstrate how to turn raw LLM output into structured, validated Python objects using Pydantic.  
- **Scope** : Brings together everything covered in the previous steps and applies it in a real-world use case.

#### Environment Setup for Structured Output :

To enable structured data generation and see results in the `structured_output` section, you need to create a `.env` file at the root of the project and add your **OpenAI API key** as follows :

```plaintext
OPENAI_API_KEY=your_api_key_here
```

This step is optional if you only want to explore the structure and validation aspects without generating data from AI models.

## Setup

You can complete this workshop in **two ways** :

### Common Instructions

Install `uv` (Python package manager with virtual environment support):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

>If the uv installation fails or you're having trouble with your virtual environment, you can try running the workshop in the cloud using GitHub Codespaces instead.

Then, run `uv sync` to install dependencies

```bash
uv sync
```

Finally, activate your environment using:

```bash
source .venv/bin/activate
```

### Option 1 — Local setup (with classic VS Code)

If you're comfortable working locally, simply clone the repository and follow the common instructions above.

### Option 2 — Run in GitHub Codespaces (cloud)

If you prefer not to set up anything locally, you can run everything directly in the browser via **GitHub Codespaces** — no installation required.

1. Go to the repository on GitHub.
2. **Select the branch you want to work on.**
3. Click on the green **Code** button → "Create codespace on `Branch's name` " 
4. In the terminal that opens in the Codespace, follow the common instructions above.

![illustration](assets/capture_3.png)

**Important** : Codespaces are tied to the branch selected when you create them.
If you want to switch branches later, go back to GitHub, select the new branch, and click on the + (plus) icon in the top right corner to create a new Codespace for that branch.
You will then need to repeat the terminal commands inside the new Codespace.

![illustration](assets/capture_4.png)

---

## Check Your Progress Without Spoilers

As you complete each stage (`model_1` to `model_4`), you can validate your implementation by running the corresponding test file located in the `tests/` folder, such as `test_model_1.py`, `test_model_2.py`, etc., found in all branches.

To validate your progress, run the test corresponding to the current model step :

```bash
pytest tests/test_model_N.py
```

*Replace `N` with the model number.*

![illustration](assets/capture_1.png)

Make sure you're in the project root (where the workshop-pydantic folder is), not inside `src/` or `tests/`.

![illustration](assets/capture_2.png)
When you run the command in your terminal, you should see an output like the image above — showing which tests failed or passed. If everything is correct, you'll see only green "passed" lines.


> **Note:** Do not modify the test files. They are designed to verify expected behavior at each stage. While they cover key elements, they do not guarantee completeness or best practices — for a full review, you can refer to the final implementation in the `correction` branch.

---

*You're now all set — pick your branch, open the exercise, and start modeling with Pydantic !*
