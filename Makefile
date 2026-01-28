.PHONY: help install install-dev test lint format typecheck run api clean all

# Default target
help:
	@echo "Linear Hello World - AI-Native Python Project"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install      Install production dependencies"
	@echo "  install-dev  Install development dependencies"
	@echo "  test         Run tests with pytest"
	@echo "  lint         Run linter (ruff)"
	@echo "  format       Format code with ruff"
	@echo "  typecheck    Run type checker (mypy)"
	@echo "  run          Run CLI hello world"
	@echo "  api          Start the API server"
	@echo "  clean        Remove build artifacts"
	@echo "  all          Run lint, typecheck, and test"

# Install production dependencies
install:
	pip install -e .

# Install development dependencies
install-dev:
	pip install -e ".[dev]"

# Run tests
test:
	pytest tests/ -v --cov=src/hello_world --cov-report=term-missing

# Run linter
lint:
	ruff check src/ tests/

# Format code
format:
	ruff format src/ tests/
	ruff check --fix src/ tests/

# Run type checker
typecheck:
	mypy src/

# Run CLI
run:
	python main.py --name "World"

# Start API server
api:
	uvicorn src.hello_world.api:app --reload --host 0.0.0.0 --port 8000

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf src/*.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

# Run all checks
all: lint typecheck test
