# Introduction to Pydantic

This document provides a concise introduction to **Pydantic**, a Python library used for data validation and parsing based on Python type annotations. Pydantic is widely used in modern Python projects such as FastAPI, data pipelines, and backend services.

---

## What is Pydantic?

Pydantic enforces type hints at runtime and provides user-friendly errors when data is invalid. It helps build reliable and clean data models, improves validation logic, and ensures better developer experience.

---

## Performance and Why Pydantic?

Pydantic stands out by offering **dynamic type validation** at runtime, not just static type checking. It automatically parses and coerces input data into the correct types, catching errors early and reliably. Under the hood, it uses `pydantic-core`, a highly optimized Rust-based engine that ensures excellent performance even in high-throughput scenarios like APIs and data pipelines.

### Common Use Cases

- Validating incoming data in web APIs (e.g., FastAPI)
- Managing environment variables and application settings
- Structuring and validating inputs in data engineering pipelines
- Securing internal tools through enforced data contracts
- Ensuring clean boundaries between components in large codebases

### Why Pydantic Is Powerful

What makes Pydantic truly powerful is its seamless mix of **type hints**, **automatic validation**, and **descriptive error messages**, all without sacrificing performance. It encourages better code quality, minimizes boilerplate, and integrates effortlessly with modern Python tools, making it a top choice for robust data handling.

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

### 2. Data Parsing

Pydantic can parse raw data (dicts, JSON, etc.) into typed Python objects.

```python
data = {'id': 1, 'name': 'Alice'}
user = User(**data)
print(user.id)  # 1
```

### 3. Handling Validation Errors

When data does not match the expected schema, Pydantic raises a `ValidationError`. This exception provides detailed information about which fields failed validation and why. You can catch and handle these errors to provide meaningful feedback or logging.

However, Pydantic also attempts to **coerce input data** to the expected type when possible. For example, a string like `"123"` will be automatically converted to an integer if the field expects an `int`.

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str

try:
    user = User(id='123', name='Alice')  # '123' will be converted to 123
    print(user)
except ValidationError as e:
    print("Validation failed:", e)
```

### 4. Optional Fields

Use `Optional` or default values to define optional fields.

```python
from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: Optional[str] = None
```

### 5. Field Customization with `Field`

Pydantic allows fine-grained control over model fields using the `Field` function. It helps define metadata, default values, validation constraints, and descriptions to enrich your models.

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., max_length=50, description="The product's name", example="Smartphone")
    price: float = Field(default=0.0, ge=0, description="The product's price, must be >= 0")
    tags: list[str] = Field(default_factory=list, description="List of tags for the product", example=["electronics", "mobile"])
```

#### What can you do with `Field`?

- Set default values or mark fields as **required** using `...`
- Add **descriptions** and **examples** for documentation (useful with FastAPI)
- Define **validation constraints** like:
  - `max_length`, `min_length` (for strings)
  - `gt` (greater than), `ge` (greater or equal), `lt` (less than), `le` (less or equal) for numbers
  - `regex` to enforce a regular expression pattern
- Use `default_factory` to provide a callable for default values (e.g., empty list or dict)
- The order of the arguments in `Field()` does not affect their behavior since they are all keyword arguments.

#### About `...` (Ellipsis)

- Using `Field(...)` marks the field as **required** (no default value).
- You can omit `...` if you provide a default value.

#### Example:

```python
# Required field:
name: str = Field(...)

# Optional field with default:
count: int = Field(default=0)
```

#### Common Constraints Example

| Constraint  | Description                          | Applies to    |
|-------------|------------------------------------|---------------|
| `max_length`| Maximum length for strings          | `str`         |
| `min_length`| Minimum length for strings          | `str`         |
| `regex`     | Regular expression pattern to match| `str`         |
| `gt`        | Greater than                       | `int`, `float`|
| `ge`        | Greater than or equal to           | `int`, `float`|
| `lt`        | Less than                         | `int`, `float`|
| `le`        | Less than or equal to              | `int`, `float`|
| `multiple_of`  | Value must be a multiple of the given number | `int`, `float`|
| `allow_inf_nan`| Allow 'inf', '-inf', and 'nan' values| `float`|

### 6. Nested Models

You can nest models inside one another for complex data structures.

```python
class Address(BaseModel):
    city: str
    zip_code: str

class Person(BaseModel):
    name: str
    address: Address

person = Person(name="John", address={"city": "Paris", "zip_code": "75000"})
print(person.address.city)  # Paris
```

### 7. Field-Level Validation (`@field_validator`)

In Pydantic v2, you can use `@field_validator` to apply custom validation logic to individual fields.

```python
from pydantic import BaseModel, field_validator

class Product(BaseModel):
    name: str
    price: float

    @field_validator('name')
    @classmethod
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError('Name must not be empty')
        return value

    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Price must be greater than zero')
        return value
```
#### Why use `@classmethod` with `@field_validator`?

- Validators receive the **class** (`cls`) as the first argument, **not an instance**.
- This allows validators to access class-level information or configuration if needed.
- Without `@classmethod`, the method signature would expect an instance (`self`), which is not how Pydantic calls validators internally, causing errors.

---
> **For your information:**
> Although `before`, `after`, `plain`, and `wrap` modes provide fine-grained control over validation timing and behavior, in most cases you won’t need to specify them explicitly when using `field_validator`.

#### Using `before` and `after` hooks

You can specify whether your validator runs **before** or **after** built-in validation using:

```python
@field_validator('price', before=True)
@classmethod
def preprocess_price(cls, value):
    # modify value before core validation
    return value

@field_validator('price', after=True)
@classmethod
def postprocess_price(cls, value):
    # validate or modify after core validation
    return value
```

#### Validation modes: `plain` vs `wrap`

- **plain**: Receives raw input and terminates validation immediately, skipping all further validation including Pydantic's internal checks.

- **wrap**: Receives a handler function to control and customize the entire validation process, allowing code to run before or after standard validation or to short-circuit it.

### 8. Model-Level Validation (`@model_validator`)

The `@model_validator` decorator in Pydantic v2 allows you to perform validation on the entire model, instead of validating fields individually. This is useful when you need to validate combinations of fields, or apply logic that spans the whole model.

**There are three types of model-level validators:**

#### - Before Validator (`mode='before'`)
Runs **before** the model is instantiated.
Useful for preprocessing raw data.
Receives the raw input and should return the cleaned data.

```python
from typing import Any
from pydantic import BaseModel, model_validator

class UserModel(BaseModel):
    username: str

    @model_validator(mode='before')
    @classmethod
    def check_card_number_not_present(cls, data: Any) -> Any:
        if isinstance(data, dict) and 'card_number' in data:
            raise ValueError("'card_number' should not be included")
        return data
```

#### - After Validator (`mode='after'`)
Runs **after** all fields are validated and the model is instantiated.
Useful for post-initialization checks.
Must return `self`.

*Unlike `before` and `wrap` validators, `after` validators receive the model instance (`self`) rather than the class, so `@classmethod` is not needed.*


```python
from pydantic import BaseModel, model_validator

class User(BaseModel):
    username: str
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def passwords_match(self) -> 'User':
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self
```

#### - Wrap Validator (`mode='wrap'`)
Most flexible.
Allows you to run logic **before and after** internal validation.
Must include a `handler` parameter which you can choose to call or not.

*Less commonly used, but powerful for advanced scenarios like custom logging or dynamic correction.*

```python
import logging
from typing import Any
from typing_extensions import Self
from pydantic import BaseModel, ModelWrapValidatorHandler, ValidationError, model_validator

class UserModel(BaseModel):
    username: str

    @model_validator(mode='wrap')
    @classmethod
    def log_failed_validation(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        try:
            return handler(data)
        except ValidationError:
            logging.error('Model %s failed to validate with data %s', cls, data)
            raise
```

### 9. Lists and Sub-models

Pydantic handles lists and more complex data structures.

```python
from typing import List

class Tag(BaseModel):
    name: str

class Article(BaseModel):
    title: str
    tags: List[Tag]

article = Article(title="Hello", tags=[{"name": "tech"}, {"name": "python"}])
print(article.tags[0].name)  # tech
```

### 10. Using `default_factory` for Mutable Defaults

Pydantic provides `default_factory` to safely assign mutable default values like lists or dictionaries. This ensures that each model instance gets its own separate copy, preventing unwanted shared state.

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    tags: list[str] = Field(default_factory=list, description="A list of tags for the product")
    attributes: dict[str, str] = Field(default_factory=dict, description="Additional product attributes")

product1 = Product(name="Laptop")
product2 = Product(name="Smartphone")

print(product1.tags)        # []
print(product2.tags)        # []

print(product1.attributes)  # {}
print(product2.attributes)  # {}
```

### 11. Using Enums with Pydantic

Pydantic supports Python's built-in `Enum` types to define fields that must have a limited set of possible values. This helps ensure data integrity by restricting inputs to predefined options.

```python
from enum import Enum
from pydantic import BaseModel

class Status(str, Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'

class Task(BaseModel):
    id: int
    status: Status

task = Task(id=1, status='completed')
print(task.status)          # Status.COMPLETED
print(task.status.value)    # 'completed'
```

## Migration from Pydantic v1 to v2

Up to this point, we have focused on Pydantic v2 and its enhancements.

Pydantic v2 introduces major improvements in performance, consistency, and validation features. However, it includes some breaking changes compared to v1. For instance, the `@validator` decorator from v1 has been replaced with `@field_validator` in v2, providing a clearer and more powerful syntax. Similarly, model-level validation is now done using `@model_validator` instead of the `@root_validator` method used in v1.

If you're upgrading from v1 to v2, it's recommended to review the official migration guide, as some code adjustments may be required.

---

>For more detailed information and advanced usage, you can visit the official Pydantic documentation: [https://docs.pydantic.dev/latest/concepts/models/](https://docs.pydantic.dev/latest/concepts/models/)
