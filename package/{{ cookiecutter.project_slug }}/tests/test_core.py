"""Tests for {{ cookiecutter.package_name }}.core."""

from {{ cookiecutter.package_name }} import greet


def test_greet_returns_greeting():
    assert greet("world") == "Hello, world!"


def test_greet_uses_name():
    assert "Ada" in greet("Ada")
