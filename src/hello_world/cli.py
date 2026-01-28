"""
Command-line interface for the Hello World application.

This module provides a CLI using Typer for interacting with the greeter.
"""

import typer
from rich.console import Console
from rich.panel import Panel

from hello_world.greeter import Greeter

app = typer.Typer(
    name="hello-world",
    help="AI-Native Hello World CLI - Linear plans it. Cursor builds it.",
    add_completion=False,
    invoke_without_command=True,
)
console = Console()


@app.callback(invoke_without_command=True)
def greet(
    ctx: typer.Context,
    name: str = typer.Option(
        "World",
        "--name",
        "-n",
        help="The name to greet.",
    ),
    greeting: str | None = typer.Option(
        None,
        "--greeting",
        "-g",
        help="Custom greeting word (default: Hello).",
    ),
    style: str = typer.Option(
        "standard",
        "--style",
        "-s",
        help="Greeting style: standard, formal, or casual.",
    ),
    title: str = typer.Option(
        "Mr./Ms.",
        "--title",
        "-t",
        help="Title for formal greetings.",
    ),
) -> None:
    """
    Generate a personalized greeting.

    Examples:
        python main.py --name Andy
        python main.py --name Andy --style casual
        python main.py --name Smith --style formal --title Dr.
    """
    # If a subcommand is invoked, don't run the greeting
    if ctx.invoked_subcommand is not None:
        return

    greeter = Greeter(default_greeting=greeting or "Hello")

    if style == "formal":
        response = greeter.greet_formal(name, title=title)
    elif style == "casual":
        response = greeter.greet_casual(name)
    else:
        response = greeter.greet(name, greeting=greeting)

    panel = Panel(
        response.message,
        title="[bold blue]Hello World[/bold blue]",
        subtitle=f"[dim]{response.greeting_type} greeting[/dim]",
        border_style="green",
    )
    console.print(panel)


@app.command()
def version() -> None:
    """Display the application version."""
    from hello_world import __version__

    console.print(
        f"[bold]linear-hello-world[/bold] version [green]{__version__}[/green]"
    )


def main() -> None:
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
