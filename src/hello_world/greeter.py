"""
Core greeter module for the Hello World application.

This module contains the main business logic for greeting functionality.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class GreetingResponse:
    """Response model for a greeting."""

    message: str
    name: str
    timestamp: datetime
    greeting_type: str = "standard"


class Greeter:
    """
    A greeter class that generates personalized greetings.

    This class demonstrates the core functionality of the hello world
    application, providing various greeting methods.

    Attributes:
        default_greeting: The default greeting template to use.
    """

    def __init__(self, default_greeting: str = "Hello") -> None:
        """
        Initialize the Greeter.

        Args:
            default_greeting: The default greeting word to use.
        """
        self.default_greeting = default_greeting

    def greet(self, name: str, greeting: str | None = None) -> GreetingResponse:
        """
        Generate a greeting for the given name.

        Args:
            name: The name to greet.
            greeting: Optional custom greeting word.

        Returns:
            A GreetingResponse containing the full greeting.
        """
        greeting_word = greeting or self.default_greeting
        message = f"{greeting_word}, {name}!"

        return GreetingResponse(
            message=message,
            name=name,
            timestamp=datetime.now(),
            greeting_type="custom" if greeting else "standard",
        )

    def greet_formal(self, name: str, title: str = "Mr./Ms.") -> GreetingResponse:
        """
        Generate a formal greeting.

        Args:
            name: The name to greet.
            title: The title to use (default: "Mr./Ms.").

        Returns:
            A GreetingResponse with a formal greeting.
        """
        message = f"Good day, {title} {name}. It is a pleasure to meet you."

        return GreetingResponse(
            message=message,
            name=name,
            timestamp=datetime.now(),
            greeting_type="formal",
        )

    def greet_casual(self, name: str) -> GreetingResponse:
        """
        Generate a casual greeting.

        Args:
            name: The name to greet.

        Returns:
            A GreetingResponse with a casual greeting.
        """
        message = f"Hey {name}! What's up?"

        return GreetingResponse(
            message=message,
            name=name,
            timestamp=datetime.now(),
            greeting_type="casual",
        )


def greet(name: str, greeting: str = "Hello") -> str:
    """
    Simple function to generate a greeting string.

    This is a convenience function for quick greetings.

    Args:
        name: The name to greet.
        greeting: The greeting word to use.

    Returns:
        A greeting string.
    """
    greeter = Greeter(default_greeting=greeting)
    response = greeter.greet(name)
    return response.message
