"""
Linear Hello World - AI-Native Python Project

This package demonstrates an AI-native development workflow using:
- Linear for planning & orchestration
- Cursor for AI execution
- GitHub for source control
- Python for runtime

Linear plans it. Cursor builds it. GitHub controls it. Python runs it.
"""

__version__ = "0.1.0"
__author__ = "AI-Native Development Team"

from hello_world.greeter import Greeter, greet

__all__ = ["Greeter", "greet", "__version__"]
