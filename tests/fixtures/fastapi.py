from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def api_client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True, scope='session')
def reset_dependency_overrides() -> Generator:
    yield
    app.dependency_overrides = {}
