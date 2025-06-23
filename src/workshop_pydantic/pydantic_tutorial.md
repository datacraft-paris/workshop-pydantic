# Introduction to Pydantic

This document provides a concise introduction to **Pydantic**, a Python library used for data validation and parsing based on Python type annotations. Pydantic is widely used in modern Python projects such as FastAPI, data pipelines, and backend services.

---

## What is Pydantic?

Pydantic enforces type hints at runtime and provides user-friendly errors when data is invalid. It helps build reliable and clean data models, improves validation logic, and ensures better developer experience.

---

## Why Use Pydantic?

- Strong data validation with automatic error handling
- Easy integration with popular frameworks like FastAPI
- Automatic documentation generation
- Clean and readable code using type hints

---

## Key Concepts

### 1. BaseModel

A `BaseModel` is the core component of Pydantic. It defines the schema and validates incoming data.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True
```

## 2. Data Parsing

Pydantic can parse raw data (dicts, JSON, etc.) into typed Python objects.

```python
data = {'id': 1, 'name': 'Alice'}
user = User(**data)
print(user.id)  # 1
```

# 3. Validation

If data is invalid, Pydantic raises an error.

```python
invalid_data = {'id': 'abc', 'name': 'Alice'}
User(**invalid_data)  # Raises ValidationError
```

# 4. Optional Fields

Use `Optional` or default values to define optional fields.

```python
from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: Optional[str] = None
```

# 5. Validators

Custom logic can be added using validators.

```python
from pydantic import validator

class User(BaseModel):
    username: str

    @validator('username')
    def must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Username must not be empty')
        return v
```

## Common Use Cases

- Validating API requests and responses
- Structuring config files or environment variables
- Validating database inputs
- Cleaning and parsing data in data pipelines
