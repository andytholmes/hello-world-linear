"""
Tests for the CLI module.
"""

from typer.testing import CliRunner

from hello_world.cli import app

runner = CliRunner()


class TestCLI:
    """Test suite for the CLI."""

    def test_default_greeting(self) -> None:
        """Test CLI with default options."""
        result = runner.invoke(app, [])
        assert result.exit_code == 0
        assert "Hello, World!" in result.output

    def test_custom_name(self) -> None:
        """Test CLI with custom name."""
        result = runner.invoke(app, ["--name", "Alice"])
        assert result.exit_code == 0
        assert "Hello, Alice!" in result.output

    def test_custom_name_short_flag(self) -> None:
        """Test CLI with short name flag."""
        result = runner.invoke(app, ["-n", "Bob"])
        assert result.exit_code == 0
        assert "Hello, Bob!" in result.output

    def test_custom_greeting(self) -> None:
        """Test CLI with custom greeting."""
        result = runner.invoke(app, ["--name", "Charlie", "--greeting", "Hi"])
        assert result.exit_code == 0
        assert "Hi, Charlie!" in result.output

    def test_formal_style(self) -> None:
        """Test CLI with formal style."""
        result = runner.invoke(app, ["--name", "Smith", "--style", "formal"])
        assert result.exit_code == 0
        assert "Mr./Ms. Smith" in result.output

    def test_formal_style_with_title(self) -> None:
        """Test CLI with formal style and custom title."""
        result = runner.invoke(
            app, ["--name", "Johnson", "--style", "formal", "--title", "Dr."]
        )
        assert result.exit_code == 0
        assert "Dr. Johnson" in result.output

    def test_casual_style(self) -> None:
        """Test CLI with casual style."""
        result = runner.invoke(app, ["--name", "Dave", "--style", "casual"])
        assert result.exit_code == 0
        assert "Hey Dave" in result.output

    def test_version_command(self) -> None:
        """Test the version command."""
        result = runner.invoke(app, ["version"])
        assert result.exit_code == 0
        assert "linear-hello-world" in result.output
        assert "0.1.0" in result.output
