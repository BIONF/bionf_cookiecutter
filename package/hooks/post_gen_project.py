"""Post-generation hook.

Runs inside the freshly generated project directory. Cookiecutter renders
this script as a Jinja template before executing it, so cookiecutter values
are substituted in as literals below.
"""
from __future__ import annotations

import datetime
import pathlib
import sys

PACKAGE_NAME = "{{ cookiecutter.package_name }}"
LICENSE = "{{ cookiecutter.license }}"


def fail(message: str) -> None:
    """Print an error and abort generation with a non-zero exit code."""
    sys.stderr.write("\nERROR: " + message + "\n")
    sys.exit(1)


def validate_package_name() -> None:
    if not PACKAGE_NAME.isidentifier():
        fail(
            f"'{PACKAGE_NAME}' is not a valid Python package name. "
            "It must be a valid identifier (letters, digits, underscores; "
            "not starting with a digit). Try a different project name."
        )


def stamp_license_year() -> None:
    """Replace the __YEAR__ placeholder in LICENSE with the current year."""
    license_file = pathlib.Path("LICENSE")
    if not license_file.exists():
        return
    text = license_file.read_text(encoding="utf-8")
    year = str(datetime.datetime.now().year)
    license_file.write_text(text.replace("__YEAR__", year), encoding="utf-8")


def remove_license_if_none() -> None:
    if LICENSE == "None":
        pathlib.Path("LICENSE").unlink(missing_ok=True)


def main() -> None:
    validate_package_name()
    remove_license_if_none()
    stamp_license_year()


if __name__ == "__main__":
    main()