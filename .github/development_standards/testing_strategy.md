# Testing Strategy and Standards

## Overview

This document defines the testing strategy, standards, and practices for Python applications. Our approach emphasizes comprehensive testing with 80% minimum coverage for production code, automated testing in CI/CD, and clear testing patterns.

## Testing Philosophy

### Core Principles

1. **Test Pyramid Approach**: More unit tests, fewer integration tests, minimal E2E tests
2. **Test-Driven Development**: Write tests first when feasible, especially for complex business logic
3. **Fast Feedback**: Tests should run quickly to enable frequent execution
4. **Isolation**: Each test should be independent and repeatable
5. **Clear Intent**: Tests should clearly express what they're validating

### Coverage Requirements

- **Production Code**: Minimum 80% test coverage
- **Critical Business Logic**: 95% test coverage
- **Integration Points**: 100% test coverage for external API interactions
- **Security Functions**: 100% test coverage

## Testing Framework and Tools

### Primary Tools

- **Test Framework**: pytest (required)
- **Coverage**: pytest-cov (required)
- **Async Testing**: pytest-asyncio (for async code)
- **Mocking**: pytest-mock (built on unittest.mock)
- **Test Data**: factory-boy (for generating test data)
- **HTTP Testing**: httpx (for API testing)
- **Database Testing**: pytest-postgresql or similar

### Configuration

All projects must include a `pyproject.toml` with pytest configuration:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--cov=src",
    "--cov-report=term-missing",
    "--cov-report=html:htmlcov",
    "--cov-report=xml:coverage.xml",
    "--cov-fail-under=80",
    "--strict-markers",
    "--disable-warnings",
]
markers = [
    "unit: Unit tests",
    "integration: Integration tests", 
    "e2e: End-to-end tests",
    "slow: Slow running tests",
    "external: Tests requiring external services",
]
```

## Test Structure and Organization

### Directory Structure

```
project/
├── src/
│   └── myproject/
├── tests/
│   ├── unit/
│   │   ├── test_models.py
│   │   ├── test_services.py
│   │   └── test_utils.py
│   ├── integration/
│   │   ├── test_api.py
│   │   ├── test_database.py
│   │   └── test_external_services.py
│   ├── e2e/
│   │   └── test_user_workflows.py
│   ├── fixtures/
│   │   ├── conftest.py
│   │   └── factories.py
│   └── data/
│       ├── sample_data.json
│       └── test_files.csv
```

### Test Naming Conventions

- **Test Files**: `test_<module_name>.py` or `<module_name>_test.py`
- **Test Classes**: `TestClassName` (mirrors the class being tested)
- **Test Methods**: `test_<behavior_being_tested>`

```python
# Good test naming examples
def test_create_user_with_valid_data_returns_user():
    """Test that creating a user with valid data returns a User object."""
    pass

def test_create_user_with_duplicate_email_raises_validation_error():
    """Test that creating a user with duplicate email raises ValidationError.""" 
    pass

def test_calculate_portfolio_value_with_empty_portfolio_returns_zero():
    """Test that calculating value of empty portfolio returns zero."""
    pass
```

## Unit Testing Standards

### Test Structure (Arrange-Act-Assert)

```python
import pytest
from myproject.models import User
from myproject.services import UserService
from myproject.exceptions import ValidationError

class TestUserService:
    """Test suite for UserService."""
    
    def test_create_user_with_valid_data_returns_user(self):
        """Test user creation with valid data."""
        # Arrange
        service = UserService()
        user_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 30
        }
        
        # Act
        result = service.create_user(user_data)
        
        # Assert
        assert isinstance(result, User)
        assert result.name == "John Doe"
        assert result.email == "john@example.com"
        assert result.age == 30
        assert result.id is not None
    
    def test_create_user_with_invalid_email_raises_validation_error(self):
        """Test user creation with invalid email format."""
        # Arrange
        service = UserService()
        user_data = {
            "name": "John Doe",
            "email": "invalid-email",
            "age": 30
        }
        
        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            service.create_user(user_data)
        
        assert "Invalid email format" in str(exc_info.value)
```

### Fixtures and Test Data

Use pytest fixtures for reusable test setup:

```python
# tests/fixtures/conftest.py
import pytest
from myproject.models import User
from myproject.services import UserService
from myproject.repositories import UserRepository

@pytest.fixture
def sample_user():
    """Create a sample user for testing."""
    return User(
        id=1,
        name="John Doe",
        email="john@example.com",
        age=30
    )

@pytest.fixture
def user_service():
    """Create a UserService instance with mocked dependencies."""
    mock_repository = Mock(spec=UserRepository)
    return UserService(repository=mock_repository)

@pytest.fixture
def user_data():
    """Valid user data for testing."""
    return {
        "name": "Jane Smith",
        "email": "jane@example.com", 
        "age": 25
    }
```

### Factory Pattern for Test Data

Use factory-boy for generating test data:

```python
# tests/fixtures/factories.py
import factory
from factory import SubFactory
from myproject.models import User, Order

class UserFactory(factory.Factory):
    """Factory for creating User instances."""
    class Meta:
        model = User
    
    name = factory.Sequence(lambda n: f"User {n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.name.lower().replace(' ', '.')}@example.com")
    age = factory.Faker('random_int', min=18, max=80)
    is_active = True

class OrderFactory(factory.Factory):
    """Factory for creating Order instances."""
    class Meta:
        model = Order
    
    user = SubFactory(UserFactory)
    amount = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    status = "pending"
    created_at = factory.Faker('date_time_this_year')

# Usage in tests
def test_order_calculation():
    """Test order total calculation."""
    order = OrderFactory(amount=Decimal("100.50"))
    assert order.calculate_total() == Decimal("100.50")
```

## Mocking and Test Doubles

### Mocking External Dependencies

```python
import pytest
from unittest.mock import Mock, patch
from myproject.services import PaymentService
from myproject.external import PaymentGateway

class TestPaymentService:
    """Test suite for PaymentService."""
    
    def test_process_payment_success(self):
        """Test successful payment processing."""
        # Arrange
        mock_gateway = Mock(spec=PaymentGateway)
        mock_gateway.charge.return_value = {"transaction_id": "txn_123", "status": "success"}
        
        service = PaymentService(gateway=mock_gateway)
        
        # Act
        result = service.process_payment(amount=100.50, card_token="card_123")
        
        # Assert
        assert result["status"] == "success"
        assert result["transaction_id"] == "txn_123"
        mock_gateway.charge.assert_called_once_with(
            amount=100.50,
            card_token="card_123"
        )
    
    @patch('myproject.external.EmailService.send')
    def test_send_confirmation_email(self, mock_send):
        """Test sending confirmation email."""
        # Arrange
        service = PaymentService()
        
        # Act
        service.send_confirmation("user@example.com", "txn_123")
        
        # Assert
        mock_send.assert_called_once()
        args, kwargs = mock_send.call_args
        assert "user@example.com" in args
        assert "txn_123" in str(kwargs)
```

### Async Testing

```python
import pytest
import pytest_asyncio
from unittest.mock import AsyncMock
from myproject.services import AsyncUserService

class TestAsyncUserService:
    """Test suite for AsyncUserService."""
    
    @pytest.mark.asyncio
    async def test_fetch_user_data_success(self):
        """Test successful async user data fetching."""
        # Arrange
        mock_client = AsyncMock()
        mock_client.get_user.return_value = {"id": 1, "name": "John Doe"}
        
        service = AsyncUserService(client=mock_client)
        
        # Act
        result = await service.fetch_user_data(user_id=1)
        
        # Assert
        assert result["name"] == "John Doe"
        mock_client.get_user.assert_called_once_with(1)
```

## Integration Testing

### Database Testing

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from myproject.database import Base
from myproject.repositories import UserRepository

@pytest.fixture(scope="function")
def db_session():
    """Create a test database session."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
    
    session.close()

class TestUserRepository:
    """Integration tests for UserRepository."""
    
    def test_save_and_retrieve_user(self, db_session):
        """Test saving and retrieving a user from database."""
        # Arrange
        repository = UserRepository(session=db_session)
        user_data = {"name": "John Doe", "email": "john@example.com"}
        
        # Act
        saved_user = repository.save(User(**user_data))
        retrieved_user = repository.find_by_id(saved_user.id)
        
        # Assert
        assert retrieved_user is not None
        assert retrieved_user.name == "John Doe"
        assert retrieved_user.email == "john@example.com"
```

### API Testing

```python
import pytest
from httpx import AsyncClient
from myproject.main import app

@pytest.mark.asyncio
async def test_create_user_endpoint():
    """Test user creation API endpoint."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Arrange
        user_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 30
        }
        
        # Act
        response = await client.post("/users", json=user_data)
        
        # Assert
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "John Doe"
        assert data["email"] == "john@example.com"
        assert "id" in data

@pytest.mark.asyncio
async def test_get_user_not_found():
    """Test getting non-existent user returns 404."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/users/999")
        assert response.status_code == 404
```

## Performance Testing

### Load Testing with Locust

```python
# tests/performance/locustfile.py
from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    """Simulate user behavior for load testing."""
    
    wait_time = between(1, 3)
    
    def on_start(self):
        """Execute when user starts."""
        self.login()
    
    def login(self):
        """Login user for testing."""
        response = self.client.post("/auth/login", json={
            "email": "test@example.com",
            "password": "password123"
        })
        self.token = response.json().get("token")
    
    @task(3)
    def view_users(self):
        """View users list."""
        self.client.get("/users", headers={"Authorization": f"Bearer {self.token}"})
    
    @task(1) 
    def create_user(self):
        """Create a new user."""
        user_data = {
            "name": "Test User",
            "email": f"test{self.random_id()}@example.com"
        }
        self.client.post("/users", json=user_data, headers={"Authorization": f"Bearer {self.token}"})
    
    def random_id(self):
        """Generate random ID."""
        import random
        return random.randint(1000, 9999)
```

### Performance Benchmarks

```python
import pytest
import time
from myproject.services import DataProcessingService

class TestPerformance:
    """Performance tests for critical functions."""
    
    @pytest.mark.slow
    def test_data_processing_performance(self):
        """Test that data processing meets performance requirements."""
        # Arrange
        service = DataProcessingService()
        large_dataset = generate_test_data(rows=10000)
        
        # Act
        start_time = time.time()
        result = service.process_data(large_dataset)
        end_time = time.time()
        
        # Assert
        processing_time = end_time - start_time
        assert processing_time < 2.0, f"Processing took {processing_time:.2f}s, should be < 2.0s"
        assert len(result) > 0
```

## Test Execution and CI/CD

### Local Development

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=html

# Run specific test types
uv run pytest -m unit
uv run pytest -m integration
uv run pytest -m "not slow"

# Run tests in parallel
uv run pytest -n auto
```

### GitHub Actions Configuration

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.13"]
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install uv
      run: pip install uv
    
    - name: Install dependencies
      run: uv sync
    
    - name: Run unit tests
      run: uv run pytest tests/unit/ -v
    
    - name: Run integration tests
      run: uv run pytest tests/integration/ -v
    
    - name: Check coverage
      run: uv run pytest --cov=src --cov-fail-under=80 --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: unittests
```

## Test Data Management

### Test Database Setup

```python
# tests/fixtures/database.py
import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from myproject.database import Base, get_db_session
from myproject.main import app

@pytest.fixture(scope="session")
def test_engine():
    """Create test database engine."""
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)
    return engine

@pytest.fixture(scope="function")
def db_session(test_engine):
    """Create database session for tests."""
    connection = test_engine.connect()
    transaction = connection.begin()
    
    Session = sessionmaker(bind=connection)
    session = Session()
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def client(db_session):
    """Create test client with database session."""
    def override_get_db():
        yield db_session
    
    app.dependency_overrides[get_db_session] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides.clear()
```

### Test Data Files

```python
# tests/fixtures/data.py
import json
import csv
from pathlib import Path

TEST_DATA_DIR = Path(__file__).parent.parent / "data"

def load_json_data(filename: str) -> dict:
    """Load test data from JSON file."""
    with open(TEST_DATA_DIR / filename) as f:
        return json.load(f)

def load_csv_data(filename: str) -> list:
    """Load test data from CSV file.""" 
    with open(TEST_DATA_DIR / filename) as f:
        return list(csv.DictReader(f))

# Usage in tests
def test_process_market_data():
    """Test processing market data from file."""
    market_data = load_json_data("sample_market_data.json")
    result = process_market_data(market_data)
    assert len(result) > 0
```

## Security Testing

### Authentication Testing

```python
import pytest
from myproject.auth import AuthService
from myproject.exceptions import UnauthorizedError

class TestAuthService:
    """Security tests for authentication."""
    
    def test_login_with_valid_credentials_returns_token(self):
        """Test login with valid credentials."""
        # Arrange
        auth_service = AuthService()
        
        # Act
        token = auth_service.login("user@example.com", "correct_password")
        
        # Assert
        assert token is not None
        assert auth_service.verify_token(token) is not None
    
    def test_login_with_invalid_password_raises_unauthorized(self):
        """Test login with invalid password."""
        auth_service = AuthService()
        
        with pytest.raises(UnauthorizedError):
            auth_service.login("user@example.com", "wrong_password")
    
    def test_verify_expired_token_raises_unauthorized(self):
        """Test that expired tokens are rejected."""
        auth_service = AuthService()
        expired_token = "expired.jwt.token"
        
        with pytest.raises(UnauthorizedError):
            auth_service.verify_token(expired_token)
```

### Input Validation Testing

```python
import pytest
from myproject.validators import validate_email, validate_amount

class TestInputValidation:
    """Security tests for input validation."""
    
    @pytest.mark.parametrize("email,expected", [
        ("valid@example.com", True),
        ("user.name+tag@domain.co.uk", True),
        ("invalid.email", False),
        ("@invalid.com", False),
        ("valid@", False),
        ("", False),
        (None, False),
    ])
    def test_email_validation(self, email, expected):
        """Test email validation with various inputs."""
        result = validate_email(email)
        assert result == expected
    
    @pytest.mark.parametrize("amount,should_raise", [
        (100.50, False),
        (0, False),
        (-50.00, True),
        ("not_a_number", True),
        (None, True),
    ])
    def test_amount_validation(self, amount, should_raise):
        """Test amount validation prevents negative values."""
        if should_raise:
            with pytest.raises(ValueError):
                validate_amount(amount)
        else:
            assert validate_amount(amount) == amount
```

## Test Documentation

### Test Case Documentation

```python
def test_portfolio_rebalancing_with_market_volatility():
    """
    Test portfolio rebalancing during high market volatility.
    
    This test verifies that the portfolio rebalancing algorithm:
    1. Correctly identifies when volatility exceeds threshold (>20%)
    2. Applies appropriate risk adjustments to asset allocation
    3. Maintains portfolio within risk tolerance bounds
    4. Generates appropriate trade orders for rebalancing
    
    Test Data:
    - Portfolio with $100,000 across 5 assets
    - Historical volatility data showing 25% volatility spike
    - Risk tolerance set to moderate (15% max allocation per asset)
    
    Expected Behavior:
    - Risk adjustment factor should be applied (0.8x normal allocation)
    - No single asset should exceed 12% allocation (15% * 0.8)
    - Total portfolio value should remain stable
    """
    # Test implementation here
    pass
```

## Continuous Testing

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: pytest-unit
        name: Run unit tests
        entry: uv run pytest tests/unit/ -v
        language: system
        pass_filenames: false
        always_run: true
      
      - id: pytest-coverage
        name: Check test coverage
        entry: uv run pytest --cov=src --cov-fail-under=80
        language: system
        pass_filenames: false
        always_run: true
```

### Test Metrics Tracking

Track and monitor key testing metrics:

- **Coverage Percentage**: Maintain >80% overall, >95% for critical paths
- **Test Execution Time**: Keep unit tests under 30s total runtime
- **Test Reliability**: <1% flaky test rate
- **Bug Detection Rate**: Tests should catch >90% of regressions

### Test Environment Management

```python
# tests/conftest.py
import os
import pytest

def pytest_configure(config):
    """Configure pytest environment."""
    os.environ["ENVIRONMENT"] = "test"
    os.environ["DATABASE_URL"] = "sqlite:///:memory:"
    os.environ["REDIS_URL"] = "redis://localhost:6379/15"  # Test DB

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Automatically set up test environment for all tests."""
    # Reset any global state
    clear_caches()
    reset_counters()
    
    yield
    
    # Clean up after test
    cleanup_test_data()
```

This comprehensive testing strategy ensures high-quality, reliable code that meets our 80% coverage requirement and follows industry best practices for Python development.
