"""
FastAPI REST API for the Hello World application.

This module provides a REST API for the greeter functionality.

Usage:
    uvicorn src.hello_world.api:app --reload
"""

from datetime import datetime

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

from hello_world import __version__
from hello_world.greeter import Greeter

app = FastAPI(
    title="Linear Hello World API",
    description="AI-Native Hello World API - Linear plans it. Cursor builds it. GitHub controls it. Python runs it.",
    version=__version__,
    docs_url="/docs",
    redoc_url="/redoc",
)


class GreetingRequest(BaseModel):
    """Request model for creating a greeting."""

    name: str = Field(
        ..., min_length=1, max_length=100, description="The name to greet"
    )
    greeting: str | None = Field(
        None, min_length=1, max_length=50, description="Custom greeting word"
    )
    style: str = Field(
        "standard",
        pattern="^(standard|formal|casual)$",
        description="Greeting style",
    )
    title: str = Field("Mr./Ms.", description="Title for formal greetings")


class GreetingResponse(BaseModel):
    """Response model for a greeting."""

    message: str = Field(..., description="The greeting message")
    name: str = Field(..., description="The name that was greeted")
    timestamp: datetime = Field(..., description="When the greeting was generated")
    greeting_type: str = Field(..., description="The type of greeting used")


class HealthResponse(BaseModel):
    """Response model for health check."""

    status: str = Field(..., description="Service status")
    version: str = Field(..., description="API version")
    timestamp: datetime = Field(..., description="Current server time")


@app.get("/", response_model=HealthResponse, tags=["Health"])
async def root() -> HealthResponse:
    """
    Root endpoint - returns API health status.

    Returns:
        HealthResponse with service status and version.
    """
    return HealthResponse(
        status="healthy",
        version=__version__,
        timestamp=datetime.now(),
    )


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check() -> HealthResponse:
    """
    Health check endpoint.

    Returns:
        HealthResponse with service status and version.
    """
    return HealthResponse(
        status="healthy",
        version=__version__,
        timestamp=datetime.now(),
    )


@app.get("/greet", response_model=GreetingResponse, tags=["Greeting"])
async def greet_get(
    name: str = Query(
        "World", min_length=1, max_length=100, description="The name to greet"
    ),
    greeting: str | None = Query(
        None, min_length=1, max_length=50, description="Custom greeting"
    ),
    style: str = Query(
        "standard", pattern="^(standard|formal|casual)$", description="Greeting style"
    ),
    title: str = Query("Mr./Ms.", description="Title for formal greetings"),
) -> GreetingResponse:
    """
    Generate a greeting via GET request.

    Args:
        name: The name to greet.
        greeting: Optional custom greeting word.
        style: The greeting style (standard, formal, casual).
        title: Title for formal greetings.

    Returns:
        GreetingResponse with the generated greeting.
    """
    greeter = Greeter(default_greeting=greeting or "Hello")

    if style == "formal":
        result = greeter.greet_formal(name, title=title)
    elif style == "casual":
        result = greeter.greet_casual(name)
    else:
        result = greeter.greet(name, greeting=greeting)

    return GreetingResponse(
        message=result.message,
        name=result.name,
        timestamp=result.timestamp,
        greeting_type=result.greeting_type,
    )


@app.post("/greet", response_model=GreetingResponse, tags=["Greeting"])
async def greet_post(request: GreetingRequest) -> GreetingResponse:
    """
    Generate a greeting via POST request.

    Args:
        request: GreetingRequest with name and optional parameters.

    Returns:
        GreetingResponse with the generated greeting.
    """
    greeter = Greeter(default_greeting=request.greeting or "Hello")

    if request.style == "formal":
        result = greeter.greet_formal(request.name, title=request.title)
    elif request.style == "casual":
        result = greeter.greet_casual(request.name)
    else:
        result = greeter.greet(request.name, greeting=request.greeting)

    return GreetingResponse(
        message=result.message,
        name=result.name,
        timestamp=result.timestamp,
        greeting_type=result.greeting_type,
    )
