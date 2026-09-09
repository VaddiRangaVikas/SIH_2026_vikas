from unittest.mock import MagicMock
from fastapi.testclient import TestClient
import pytest

from app.db.database import get_db
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    """Test that GET /health returns HTTP 200 and expected status/service."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "sovereign-ai-workbench"


def test_database_health_endpoint_success():
    """Test that GET /health/db returns HTTP 200 when database connection is healthy."""
    mock_db = MagicMock()
    mock_db.execute.return_value = None

    def override_get_db():
        yield mock_db

    app.dependency_overrides[get_db] = override_get_db
    try:
        response = client.get("/health/db")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["database"] == "connected"
        assert "verified" in data["detail"]
    finally:
        app.dependency_overrides.clear()


def test_database_health_endpoint_failure():
    """Test that GET /health/db returns HTTP 503 when database is unreachable."""
    mock_db = MagicMock()
    mock_db.execute.side_effect = Exception("Connection refused")

    def override_get_db():
        yield mock_db

    app.dependency_overrides[get_db] = override_get_db
    try:
        response = client.get("/health/db")
        assert response.status_code == 503
        data = response.json()
        assert data["status"] == "error"
        assert data["database"] == "disconnected"
        assert "Database health check failed" in data["detail"]
    finally:
        app.dependency_overrides.clear()
