# Architectural Principles

## Overview

This document defines the core architectural principles and patterns for Python applications in our organization. These principles ensure scalability, maintainability, security, and consistency across all projects.

## Core Architectural Principles

### 1. Separation of Concerns

**Principle**: Each module, class, and function should have a single, well-defined responsibility.

**Implementation**:
- Use layered architecture (presentation, business logic, data access)
- Implement clean interfaces between layers
- Avoid tight coupling between components

```python
# Good: Clear separation
class UserRepository:
    """Handles data access for users."""
    def save(self, user: User) -> None: ...
    def find_by_id(self, user_id: int) -> Optional[User]: ...

class UserService:
    """Handles business logic for users."""
    def __init__(self, repository: UserRepository):
        self._repository = repository
    
    def create_user(self, user_data: Dict[str, str]) -> User:
        # Business logic here
        user = User(**user_data)
        return self._repository.save(user)

class UserController:
    """Handles HTTP requests for users."""
    def __init__(self, service: UserService):
        self._service = service
```

### 2. Dependency Injection

**Principle**: Dependencies should be injected rather than hard-coded, enabling testability and flexibility.

**Implementation**:
- Use constructor injection for required dependencies
- Use property injection for optional dependencies
- Consider using dependency injection containers for complex applications

```python
# Good: Dependencies injected
class OrderService:
    def __init__(
        self, 
        payment_service: PaymentService,
        notification_service: NotificationService,
        logger: logging.Logger
    ):
        self._payment_service = payment_service
        self._notification_service = notification_service
        self._logger = logger
```

### 3. Configuration Management

**Principle**: All configuration should be externalized and environment-specific.

**Implementation**:
- Use environment variables for configuration
- Use Pydantic Settings for type-safe configuration
- Never commit secrets or environment-specific values

```python
from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings."""
    database_url: str
    redis_url: str
    api_key: str
    debug: bool = False
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

## Application Patterns

### 1. Repository Pattern

**Use Case**: Abstract data access logic from business logic.

```python
from abc import ABC, abstractmethod
from typing import List, Optional

class UserRepository(ABC):
    """Abstract repository for user data access."""
    
    @abstractmethod
    def save(self, user: User) -> User: ...
    
    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]: ...
    
    @abstractmethod
    def find_all(self) -> List[User]: ...
    
    @abstractmethod
    def delete(self, user_id: int) -> bool: ...

class PostgreSQLUserRepository(UserRepository):
    """PostgreSQL implementation of user repository."""
    
    def __init__(self, connection: psycopg2.Connection):
        self._connection = connection
    
    def save(self, user: User) -> User:
        # PostgreSQL-specific implementation
        pass
```

### 2. Service Layer Pattern

**Use Case**: Encapsulate business logic and coordinate between repositories.

```python
class UserService:
    """Service layer for user business logic."""
    
    def __init__(
        self, 
        user_repo: UserRepository,
        email_service: EmailService,
        audit_service: AuditService
    ):
        self._user_repo = user_repo
        self._email_service = email_service
        self._audit_service = audit_service
    
    def register_user(self, user_data: Dict[str, str]) -> User:
        """Register a new user with business logic."""
        # Validation
        if self._user_repo.find_by_email(user_data["email"]):
            raise ValueError("Email already exists")
        
        # Create user
        user = User(**user_data)
        user = self._user_repo.save(user)
        
        # Side effects
        self._email_service.send_welcome_email(user.email)
        self._audit_service.log_user_registration(user.id)
        
        return user
```

### 3. Factory Pattern

**Use Case**: Create complex objects or choose implementations at runtime.

```python
from enum import Enum

class DatabaseType(Enum):
    POSTGRESQL = "postgresql"
    MONGODB = "mongodb"

class RepositoryFactory:
    """Factory for creating repository instances."""
    
    @staticmethod
    def create_user_repository(db_type: DatabaseType) -> UserRepository:
        match db_type:
            case DatabaseType.POSTGRESQL:
                return PostgreSQLUserRepository(get_pg_connection())
            case DatabaseType.MONGODB:
                return MongoDBUserRepository(get_mongo_connection())
            case _:
                raise ValueError(f"Unsupported database type: {db_type}")
```

## API Design Patterns

### 1. RESTful API Design

**Principles**:
- Use HTTP verbs correctly (GET, POST, PUT, DELETE, PATCH)
- Use resource-based URLs
- Return appropriate HTTP status codes
- Use consistent response formats

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

class UserCreate(BaseModel):
    name: str
    email: str

app = FastAPI()

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate):
    return user_service.create_user(user_data.dict())
```

### 2. Error Handling Pattern

**Principle**: Consistent error handling across the application.

```python
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class ApplicationError(Exception):
    """Base application error."""
    def __init__(self, message: str, error_code: str = None):
        self.message = message
        self.error_code = error_code
        super().__init__(message)

class ValidationError(ApplicationError):
    """Validation error."""
    pass

class BusinessRuleError(ApplicationError):
    """Business rule violation error."""
    pass

def handle_error(error: Exception) -> Dict[str, Any]:
    """Centralized error handler."""
    if isinstance(error, ApplicationError):
        logger.warning(f"Application error: {error.message}")
        return {
            "error": error.message,
            "error_code": error.error_code,
            "type": "application_error"
        }
    
    logger.error(f"Unexpected error: {error}", exc_info=True)
    return {
        "error": "Internal server error",
        "type": "system_error"
    }
```

## Data Architecture Patterns

### 1. Data Access Layer

**Pattern**: Separate data access from business logic.

```python
class DataAccessLayer:
    """Base data access layer."""
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self._connection = None
    
    def get_connection(self):
        if not self._connection:
            self._connection = self._create_connection()
        return self._connection
    
    def _create_connection(self):
        # Connection creation logic
        pass

class PostgreSQLDataAccess(DataAccessLayer):
    """PostgreSQL-specific data access."""
    
    def _create_connection(self):
        import psycopg2
        return psycopg2.connect(self.connection_string)
```

### 2. Data Processing Pipeline Pattern

**Use Case**: Process data through multiple stages.

```python
from abc import ABC, abstractmethod
import polars as pl

class ProcessingStage(ABC):
    """Abstract processing stage."""
    
    @abstractmethod
    def process(self, data: pl.DataFrame) -> pl.DataFrame:
        pass

class DataValidationStage(ProcessingStage):
    """Validate data quality."""
    
    def process(self, data: pl.DataFrame) -> pl.DataFrame:
        # Remove rows with null values in critical columns
        return data.filter(
            pl.col("amount").is_not_null() & 
            pl.col("timestamp").is_not_null()
        )

class DataTransformationStage(ProcessingStage):
    """Transform data for analysis."""
    
    def process(self, data: pl.DataFrame) -> pl.DataFrame:
        return data.with_columns([
            (pl.col("amount") / 100).alias("amount_dollars"),
            pl.col("timestamp").dt.date().alias("date")
        ])

class DataPipeline:
    """Orchestrates data processing stages."""
    
    def __init__(self, stages: List[ProcessingStage]):
        self.stages = stages
    
    def execute(self, data: pl.DataFrame) -> pl.DataFrame:
        for stage in self.stages:
            data = stage.process(data)
        return data
```

## Security Architecture

### 1. Authentication & Authorization

**Pattern**: Centralized authentication and role-based authorization.

```python
from functools import wraps
from typing import List, Optional
from jwt import decode, InvalidTokenError

class AuthenticationService:
    """Handles user authentication."""
    
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
    
    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        try:
            payload = decode(token, self.secret_key, algorithms=["HS256"])
            return payload
        except InvalidTokenError:
            return None

def require_auth(roles: List[str] = None):
    """Decorator for requiring authentication and roles."""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Extract token from request
            token = get_token_from_request()
            
            if not token:
                raise HTTPException(401, "Authentication required")
            
            user_data = auth_service.verify_token(token)
            if not user_data:
                raise HTTPException(401, "Invalid token")
            
            if roles and user_data.get("role") not in roles:
                raise HTTPException(403, "Insufficient permissions")
            
            return await func(*args, **kwargs)
        return wrapper
    return decorator

# Usage
@require_auth(roles=["admin", "manager"])
async def delete_user(user_id: int):
    pass
```

### 2. Data Protection

**Pattern**: Encrypt sensitive data and manage secrets securely.

```python
from cryptography.fernet import Fernet
import os

class DataProtectionService:
    """Handles data encryption and decryption."""
    
    def __init__(self):
        key = os.getenv("ENCRYPTION_KEY")
        if not key:
            raise ValueError("Encryption key not found")
        self.cipher = Fernet(key.encode())
    
    def encrypt(self, data: str) -> str:
        return self.cipher.encrypt(data.encode()).decode()
    
    def decrypt(self, encrypted_data: str) -> str:
        return self.cipher.decrypt(encrypted_data.encode()).decode()

# Usage in models
class SensitiveData(BaseModel):
    id: int
    encrypted_ssn: str
    
    def get_ssn(self, protection_service: DataProtectionService) -> str:
        return protection_service.decrypt(self.encrypted_ssn)
    
    def set_ssn(self, ssn: str, protection_service: DataProtectionService) -> None:
        self.encrypted_ssn = protection_service.encrypt(ssn)
```

## Performance Patterns

### 1. Caching Strategy

**Pattern**: Multi-level caching for performance optimization.

```python
import redis
from functools import wraps
import json
from typing import Any, Callable, Optional

class CacheService:
    """Redis-based caching service."""
    
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
    
    def get(self, key: str) -> Optional[Any]:
        value = self.redis.get(key)
        return json.loads(value) if value else None
    
    def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        self.redis.setex(key, ttl, json.dumps(value))

def cache_result(ttl: int = 3600, key_prefix: str = ""):
    """Decorator for caching function results."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate cache key
            cache_key = f"{key_prefix}:{func.__name__}:{hash(str(args) + str(kwargs))}"
            
            # Try to get from cache
            cached_result = cache_service.get(cache_key)
            if cached_result is not None:
                return cached_result
            
            # Execute function and cache result
            result = func(*args, **kwargs)
            cache_service.set(cache_key, result, ttl)
            return result
        return wrapper
    return decorator

# Usage
@cache_result(ttl=1800, key_prefix="user_data")
def get_user_profile(user_id: int) -> Dict[str, Any]:
    # Expensive database operation
    return user_repository.get_detailed_profile(user_id)
```

### 2. Async Processing Pattern

**Pattern**: Use async/await for I/O bound operations.

```python
import asyncio
import aiohttp
from typing import List

class AsyncDataProcessor:
    """Async data processing service."""
    
    def __init__(self):
        self.session = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def fetch_data(self, url: str) -> Dict[str, Any]:
        async with self.session.get(url) as response:
            return await response.json()
    
    async def process_batch(self, urls: List[str]) -> List[Dict[str, Any]]:
        """Process multiple URLs concurrently."""
        tasks = [self.fetch_data(url) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)

# Usage
async def main():
    urls = ["http://api1.com/data", "http://api2.com/data"]
    
    async with AsyncDataProcessor() as processor:
        results = await processor.process_batch(urls)
        return results
```

## Deployment Architecture

### 1. Containerization Standards

**Pattern**: Consistent Docker containerization.

```dockerfile
# Dockerfile
FROM python:3.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy application code
COPY src/ ./src/
COPY scripts/ ./scripts/

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Start application
CMD ["uv", "run", "python", "-m", "src.main"]
```

### 2. Environment-Specific Configuration

**Pattern**: Environment-aware configuration management.

```python
from enum import Enum
from pydantic import BaseSettings

class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"

class Settings(BaseSettings):
    environment: Environment = Environment.DEVELOPMENT
    database_url: str
    redis_url: str
    log_level: str = "INFO"
    debug: bool = False
    
    # Security settings
    secret_key: str
    jwt_expire_minutes: int = 60
    
    # Performance settings
    max_connections: int = 10
    timeout_seconds: int = 30
    
    class Config:
        env_file = ".env"
    
    @property
    def is_production(self) -> bool:
        return self.environment == Environment.PRODUCTION
    
    @property
    def is_development(self) -> bool:
        return self.environment == Environment.DEVELOPMENT

def get_settings() -> Settings:
    return Settings()
```

## Monitoring and Observability

### 1. Structured Logging

**Pattern**: Consistent, structured logging across applications.

```python
import structlog
from typing import Any, Dict

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

class Logger:
    """Application logger wrapper."""
    
    def __init__(self, name: str):
        self.logger = structlog.get_logger(name)
    
    def info(self, message: str, **kwargs):
        self.logger.info(message, **kwargs)
    
    def error(self, message: str, error: Exception = None, **kwargs):
        self.logger.error(message, error=str(error), **kwargs)
    
    def with_context(self, **kwargs) -> "Logger":
        """Add context to logger."""
        new_logger = Logger("context")
        new_logger.logger = self.logger.bind(**kwargs)
        return new_logger

# Usage
logger = Logger(__name__)
user_logger = logger.with_context(user_id=123, operation="create_order")
user_logger.info("Processing order", order_id=456, amount=100.50)
```

### 2. Metrics Collection

**Pattern**: Prometheus-based metrics collection.

```python
from prometheus_client import Counter, Histogram, Gauge, start_http_server
import time
from functools import wraps

# Define metrics
REQUEST_COUNT = Counter('http_requests_total', 'HTTP requests', ['method', 'endpoint', 'status'])
REQUEST_DURATION = Histogram('http_request_duration_seconds', 'HTTP request duration')
ACTIVE_CONNECTIONS = Gauge('active_connections', 'Active database connections')

def track_metrics(func):
    """Decorator to track function metrics."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            REQUEST_COUNT.labels(method='GET', endpoint='/api/users', status='200').inc()
            return result
        except Exception as e:
            REQUEST_COUNT.labels(method='GET', endpoint='/api/users', status='500').inc()
            raise
        finally:
            REQUEST_DURATION.observe(time.time() - start_time)
    
    return wrapper

# Start metrics server
def start_metrics_server(port: int = 8001):
    start_http_server(port)
```

## Documentation Standards

### 1. API Documentation

**Pattern**: Automatic API documentation with FastAPI.

```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="User Management API",
    description="API for managing user accounts and profiles",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

class User(BaseModel):
    """User model for API responses."""
    id: int = Field(..., description="Unique user identifier")
    name: str = Field(..., description="User's full name", min_length=1, max_length=100)
    email: str = Field(..., description="User's email address")
    is_active: bool = Field(True, description="Whether the user account is active")

@app.get("/users", response_model=List[User], tags=["users"])
async def list_users(
    limit: int = Field(10, ge=1, le=100, description="Maximum number of users to return"),
    offset: int = Field(0, ge=0, description="Number of users to skip")
) -> List[User]:
    """
    Retrieve a list of users.
    
    Returns a paginated list of user accounts with their basic information.
    """
    return user_service.list_users(limit=limit, offset=offset)
```

### 2. Code Documentation

**Pattern**: Comprehensive docstrings and type hints.

```python
from typing import List, Optional, Dict, Any
from datetime import datetime

class UserService:
    """
    Service for managing user accounts and operations.
    
    This service handles all business logic related to user management,
    including account creation, updates, and authentication.
    """
    
    def __init__(self, repository: UserRepository, logger: Logger):
        """
        Initialize the user service.
        
        Args:
            repository: Repository for user data access
            logger: Logger instance for service operations
        """
        self._repository = repository
        self._logger = logger
    
    def create_user(
        self, 
        user_data: Dict[str, Any], 
        send_welcome_email: bool = True
    ) -> User:
        """
        Create a new user account.
        
        Args:
            user_data: Dictionary containing user information with keys:
                - name (str): User's full name
                - email (str): User's email address
                - phone (str, optional): User's phone number
            send_welcome_email: Whether to send welcome email to new user
        
        Returns:
            Created user instance with generated ID and timestamps
        
        Raises:
            ValidationError: If user_data is invalid or incomplete
            DuplicateEmailError: If email already exists in the system
            
        Example:
            >>> service = UserService(repo, logger)
            >>> user_data = {"name": "John Doe", "email": "john@example.com"}
            >>> user = service.create_user(user_data)
            >>> print(user.id)
            123
        """
        self._logger.info("Creating new user", email=user_data.get("email"))
        
        # Validation logic here
        if not user_data.get("email"):
            raise ValidationError("Email is required")
        
        # Business logic here
        user = User(**user_data)
        user = self._repository.save(user)
        
        if send_welcome_email:
            self._send_welcome_email(user.email)
        
        self._logger.info("User created successfully", user_id=user.id)
        return user
```

These architectural principles provide a solid foundation for building maintainable, scalable, and secure Python applications. All development should follow these patterns unless there's a specific technical reason to deviate, which should be documented and approved by the architecture team.
