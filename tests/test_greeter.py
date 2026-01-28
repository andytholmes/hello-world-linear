"""
Tests for the greeter module.
"""

from datetime import datetime

from hello_world.greeter import Greeter, GreetingResponse, greet


class TestGreeter:
    """Test suite for the Greeter class."""

    def test_default_greeting(self, greeter: Greeter) -> None:
        """Test that the default greeting is 'Hello'."""
        response = greeter.greet("World")
        assert response.message == "Hello, World!"
        assert response.name == "World"
        assert response.greeting_type == "standard"

    def test_custom_greeting_word(self) -> None:
        """Test greeting with a custom greeting word."""
        greeter = Greeter(default_greeting="Howdy")
        response = greeter.greet("Partner")
        assert response.message == "Howdy, Partner!"
        assert response.greeting_type == "standard"

    def test_override_greeting(self, greeter: Greeter) -> None:
        """Test overriding the greeting in the greet call."""
        response = greeter.greet("Friend", greeting="Hi")
        assert response.message == "Hi, Friend!"
        assert response.greeting_type == "custom"

    def test_formal_greeting(self, greeter: Greeter) -> None:
        """Test formal greeting generation."""
        response = greeter.greet_formal("Smith", title="Dr.")
        assert response.message == "Good day, Dr. Smith. It is a pleasure to meet you."
        assert response.greeting_type == "formal"

    def test_formal_greeting_default_title(self, greeter: Greeter) -> None:
        """Test formal greeting with default title."""
        response = greeter.greet_formal("Johnson")
        assert "Mr./Ms. Johnson" in response.message
        assert response.greeting_type == "formal"

    def test_casual_greeting(self, greeter: Greeter) -> None:
        """Test casual greeting generation."""
        response = greeter.greet_casual("Alex")
        assert response.message == "Hey Alex! What's up?"
        assert response.greeting_type == "casual"

    def test_response_has_timestamp(self, greeter: Greeter) -> None:
        """Test that responses include a timestamp."""
        response = greeter.greet("World")
        assert isinstance(response.timestamp, datetime)

    def test_multiple_names(self, greeter: Greeter, sample_names: list[str]) -> None:
        """Test greeting multiple names."""
        for name in sample_names:
            response = greeter.greet(name)
            assert name in response.message
            assert response.name == name


class TestGreetingResponse:
    """Test suite for the GreetingResponse dataclass."""

    def test_create_response(self) -> None:
        """Test creating a GreetingResponse."""
        now = datetime.now()
        response = GreetingResponse(
            message="Hello, Test!",
            name="Test",
            timestamp=now,
            greeting_type="test",
        )
        assert response.message == "Hello, Test!"
        assert response.name == "Test"
        assert response.timestamp == now
        assert response.greeting_type == "test"

    def test_default_greeting_type(self) -> None:
        """Test that default greeting type is 'standard'."""
        response = GreetingResponse(
            message="Hello!",
            name="World",
            timestamp=datetime.now(),
        )
        assert response.greeting_type == "standard"


class TestGreetFunction:
    """Test suite for the greet convenience function."""

    def test_simple_greet(self) -> None:
        """Test simple greeting function."""
        result = greet("World")
        assert result == "Hello, World!"

    def test_greet_with_custom_greeting(self) -> None:
        """Test greeting function with custom greeting."""
        result = greet("Friend", greeting="Hi")
        assert result == "Hi, Friend!"

    def test_greet_returns_string(self) -> None:
        """Test that greet returns a string."""
        result = greet("Test")
        assert isinstance(result, str)
