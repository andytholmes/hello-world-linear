"""
Pytest configuration and fixtures for the test suite.
"""

import sys
from pathlib import Path

import pytest

# Ensure src is in path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


@pytest.fixture
def sample_names() -> list[str]:
    """Provide sample names for testing."""
    return ["Alice", "Bob", "Charlie", "World"]


@pytest.fixture
def greeter():
    """Provide a default Greeter instance."""
    from hello_world.greeter import Greeter

    return Greeter()


@pytest.fixture
def custom_greeter():
    """Provide a custom Greeter instance with a different greeting."""
    from hello_world.greeter import Greeter

    return Greeter(default_greeting="Howdy")
