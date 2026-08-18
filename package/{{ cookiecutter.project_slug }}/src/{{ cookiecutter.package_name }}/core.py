"""Core functionality for {{ cookiecutter.package_name }}."""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a friendly greeting.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.

    Example:
        >>> greet("world")
        'Hello, world!'
    """
    return f"Hello, {name}!"
