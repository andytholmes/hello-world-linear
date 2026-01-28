"""
Tests for the FastAPI REST API.
"""

from fastapi.testclient import TestClient

from hello_world.api import app

client = TestClient(app)


class TestHealthEndpoints:
    """Test suite for health check endpoints."""

    def test_root_endpoint(self) -> None:
        """Test the root endpoint returns health status."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "version" in data
        assert "timestamp" in data

    def test_health_endpoint(self) -> None:
        """Test the /health endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"


class TestGreetGetEndpoint:
    """Test suite for GET /greet endpoint."""

    def test_default_greeting(self) -> None:
        """Test greeting with default parameters."""
        response = client.get("/greet")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Hello, World!"
        assert data["name"] == "World"
        assert data["greeting_type"] == "standard"

    def test_custom_name(self) -> None:
        """Test greeting with a custom name."""
        response = client.get("/greet?name=Alice")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Hello, Alice!"
        assert data["name"] == "Alice"

    def test_custom_greeting(self) -> None:
        """Test greeting with custom greeting word."""
        response = client.get("/greet?name=Bob&greeting=Hi")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Hi, Bob!"
        assert data["greeting_type"] == "custom"

    def test_formal_style(self) -> None:
        """Test formal greeting style."""
        response = client.get("/greet?name=Smith&style=formal&title=Dr.")
        assert response.status_code == 200
        data = response.json()
        assert "Dr. Smith" in data["message"]
        assert data["greeting_type"] == "formal"

    def test_casual_style(self) -> None:
        """Test casual greeting style."""
        response = client.get("/greet?name=Charlie&style=casual")
        assert response.status_code == 200
        data = response.json()
        assert "Hey Charlie" in data["message"]
        assert data["greeting_type"] == "casual"

    def test_invalid_style(self) -> None:
        """Test that invalid style returns an error."""
        response = client.get("/greet?style=invalid")
        assert response.status_code == 422


class TestGreetPostEndpoint:
    """Test suite for POST /greet endpoint."""

    def test_post_greeting(self) -> None:
        """Test POST greeting with basic payload."""
        response = client.post("/greet", json={"name": "Dave"})
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Hello, Dave!"
        assert data["name"] == "Dave"

    def test_post_with_all_options(self) -> None:
        """Test POST greeting with all options."""
        response = client.post(
            "/greet",
            json={
                "name": "Johnson",
                "style": "formal",
                "title": "Prof.",
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert "Prof. Johnson" in data["message"]

    def test_post_missing_name(self) -> None:
        """Test that missing name returns an error."""
        response = client.post("/greet", json={})
        assert response.status_code == 422

    def test_post_empty_name(self) -> None:
        """Test that empty name returns an error."""
        response = client.post("/greet", json={"name": ""})
        assert response.status_code == 422


class TestAPIDocumentation:
    """Test that API documentation is accessible."""

    def test_openapi_json(self) -> None:
        """Test that OpenAPI schema is available."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        assert data["info"]["title"] == "Linear Hello World API"

    def test_docs_page(self) -> None:
        """Test that Swagger docs are available."""
        response = client.get("/docs")
        assert response.status_code == 200

    def test_redoc_page(self) -> None:
        """Test that ReDoc is available."""
        response = client.get("/redoc")
        assert response.status_code == 200
