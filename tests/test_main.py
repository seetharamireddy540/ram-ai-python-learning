"""Tests for the main module."""

from my_service.main import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello, World!"
    assert hello("Python") == "Hello, Python!"