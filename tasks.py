"""Invoke tasks for project automation."""

from invoke import task


@task
def test(c):
    """Run tests."""
    c.run("pytest tests/")


@task
def format(c):
    """Format code with black and isort."""
    c.run("black src/ tests/")
    c.run("isort src/ tests/")


@task
def lint(c):
    """Run linting checks."""
    c.run("black --check src/ tests/")
    c.run("isort --check-only src/ tests/")
    c.run("mypy src/")


@task
def clean(c):
    """Clean build artifacts."""
    c.run("rm -rf build/ dist/ *.egg-info/")
    c.run("find . -type d -name __pycache__ -exec rm -rf {} +", warn=True)


@task
def install(c):
    """Install package in development mode."""
    c.run("pip install -e .[dev]")