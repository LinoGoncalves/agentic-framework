# Python Coding Style Guide

## Overview

This document defines the coding standards and style guidelines for Python 3.13+ development in our organization. All code must adhere to these standards to ensure consistency, maintainability, and quality across projects.

## Python Version

- **Minimum Version**: Python 3.13+
- **Type Hints**: Mandatory for all public functions and class methods
- **Modern Python Features**: Leverage Python 3.13 features where appropriate

## Code Formatting & Style

### Primary Tools

- **Formatter**: [Ruff](https://docs.astral.sh/ruff/) (format mode)
- **Linter**: [Ruff](https://docs.astral.sh/ruff/) (lint mode)  
- **Type Checker**: [mypy](https://mypy.readthedocs.io/)
- **Security Linter**: [bandit](https://bandit.readthedocs.io/)
- **Import Sorting**: Ruff (replaces isort)

### Configuration Files

All projects must include a `pyproject.toml` file with the following configurations:

```toml
[tool.ruff]
target-version = "py313"
line-length = 88
indent-width = 4

[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # Pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "UP", # pyupgrade
    "S",  # bandit security
    "PT", # flake8-pytest-style
]
ignore = [
    "E501",  # line too long (handled by formatter)
]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"

[tool.mypy]
python_version = "3.13"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
show_error_codes = true

[tool.bandit]
exclude_dirs = ["tests", "test_*.py", "*_test.py"]
```

## Code Structure & Organization

### File Structure

```
project_name/
├── pyproject.toml
├── README.md
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── main.py
│       ├── models/
│       ├── services/
│       ├── api/
│       └── utils/
├── tests/
├── docs/
└── scripts/
```

### Import Organization

Imports must be organized in the following order (enforced by Ruff):

1. Standard library imports
2. Third-party imports
3. Local application imports

```python
# Standard library
import asyncio
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

# Third-party
import pandas as pd
import numpy as np
from pydantic import BaseModel

# Local
from .models import User
from .services.auth import AuthService
```

## Type Hints & Documentation

### Type Hints

All public functions and methods must include type hints:

```python
def process_data(
    data: pd.DataFrame, 
    filters: Dict[str, Any],
    threshold: float = 0.8
) -> pd.DataFrame:
    """Process data with specified filters and threshold."""
    pass

class UserService:
    def create_user(self, user_data: Dict[str, str]) -> User:
        """Create a new user from provided data."""
        pass
```

### Docstrings

Use Google-style docstrings for all public modules, classes, and functions:

```python
def calculate_metrics(
    data: pd.DataFrame, 
    metric_type: str,
    window_size: int = 30
) -> Dict[str, float]:
    """Calculate metrics for the given dataset.
    
    Args:
        data: Input DataFrame containing time series data
        metric_type: Type of metric to calculate ('volatility', 'returns', etc.)
        window_size: Rolling window size for calculations (default: 30)
        
    Returns:
        Dictionary containing calculated metrics with metric names as keys
        
    Raises:
        ValueError: If metric_type is not supported
        KeyError: If required columns are missing from data
        
    Examples:
        >>> data = pd.DataFrame({'price': [100, 101, 99, 102]})
        >>> metrics = calculate_metrics(data, 'returns')
        >>> print(metrics['mean_return'])
        0.0066
    """
    pass
```

## Error Handling & Logging

### Exception Handling

```python
import logging
from typing import Optional

logger = logging.getLogger(__name__)

def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers with proper error handling."""
    try:
        if b == 0:
            logger.warning(f"Division by zero attempted: {a} / {b}")
            return None
        return a / b
    except (TypeError, ValueError) as e:
        logger.error(f"Invalid input types for division: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error in division: {e}")
        raise
```

### Logging Configuration

```python
import logging

# Standard logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
```

## Performance & Best Practices

### Use Modern Python Features

```python
# Python 3.13+ features
from typing import TypedDict

class UserData(TypedDict):
    name: str
    age: int
    email: str

# Use match statements for complex conditionals
def process_status(status: str) -> str:
    match status:
        case "pending" | "waiting":
            return "In queue"
        case "processing":
            return "Active"
        case "completed":
            return "Done"
        case _:
            return "Unknown"
```

### Data Processing Best Practices

```python
# Prefer polars for large datasets
import polars as pl

# Use polars for performance-critical operations
def process_large_dataset(file_path: str) -> pl.DataFrame:
    """Process large dataset using polars for better performance."""
    return (
        pl.read_csv(file_path)
        .filter(pl.col("amount") > 0)
        .group_by("category")
        .agg(pl.col("amount").sum())
    )

# Use pandas for smaller datasets and complex operations
import pandas as pd

def analyze_small_dataset(data: pd.DataFrame) -> pd.DataFrame:
    """Analyze small dataset with pandas for rich ecosystem support."""
    return data.groupby("category").agg({
        "amount": ["sum", "mean", "std"],
        "count": "count"
    })
```

### Async Programming

```python
import asyncio
from typing import List

async def fetch_data(url: str) -> Dict[str, Any]:
    """Fetch data from URL asynchronously."""
    # Implementation here
    pass

async def process_urls(urls: List[str]) -> List[Dict[str, Any]]:
    """Process multiple URLs concurrently."""
    tasks = [fetch_data(url) for url in urls]
    return await asyncio.gather(*tasks)
```

## Security Guidelines

### Input Validation

```python
from pydantic import BaseModel, validator
import re

class UserInput(BaseModel):
    email: str
    amount: float
    
    @validator('email')
    def validate_email(cls, v):
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', v):
            raise ValueError('Invalid email format')
        return v
    
    @validator('amount')
    def validate_amount(cls, v):
        if v < 0:
            raise ValueError('Amount must be non-negative')
        return v
```

### Secret Management

```python
import os
from typing import Optional

def get_secret(key: str) -> Optional[str]:
    """Retrieve secret from environment variables."""
    value = os.getenv(key)
    if not value:
        logging.error(f"Secret '{key}' not found in environment")
    return value

# Never hardcode secrets
API_KEY = get_secret("API_KEY")
DB_PASSWORD = get_secret("DATABASE_PASSWORD")
```

## Testing Guidelines

### Test File Naming

- Test files: `test_*.py` or `*_test.py`
- Test classes: `TestClassName`
- Test methods: `test_method_name`

### Test Structure

```python
import pytest
from unittest.mock import Mock, patch
from myapp.services import UserService

class TestUserService:
    """Test suite for UserService."""
    
    @pytest.fixture
    def user_service(self):
        """Fixture for UserService instance."""
        return UserService()
    
    def test_create_user_success(self, user_service):
        """Test successful user creation."""
        # Arrange
        user_data = {"name": "John Doe", "email": "john@example.com"}
        
        # Act
        result = user_service.create_user(user_data)
        
        # Assert
        assert result.name == "John Doe"
        assert result.email == "john@example.com"
    
    def test_create_user_invalid_email(self, user_service):
        """Test user creation with invalid email."""
        user_data = {"name": "John Doe", "email": "invalid-email"}
        
        with pytest.raises(ValueError, match="Invalid email format"):
            user_service.create_user(user_data)
```

## Pre-commit Hooks

All repositories must include a `.pre-commit-config.yaml` file:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.8
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]
  
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: ["-c", "pyproject.toml"]
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Code Quality

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.13"
          
      - name: Install uv
        run: pip install uv
        
      - name: Install dependencies
        run: uv sync
        
      - name: Run Ruff
        run: uv run ruff check .
        
      - name: Run Ruff format
        run: uv run ruff format --check .
        
      - name: Run mypy
        run: uv run mypy src/
        
      - name: Run bandit
        run: uv run bandit -r src/
        
      - name: Run tests
        run: uv run pytest --cov=src --cov-report=xml
        
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

## Enforcement

All code must pass the following checks before being merged:

1. Ruff linting with zero errors
2. Ruff formatting compliance
3. mypy type checking with zero errors
4. bandit security scanning with zero high-severity issues
5. Minimum 80% test coverage for production code
6. All tests passing

These checks are enforced via:
- Pre-commit hooks (local development)
- GitHub Actions CI (pull requests)
- Branch protection rules (main/master branch)
