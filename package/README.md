# cookiecutter-python-package

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template for simple,
modern Python packages. Generates a `src`-layout package with `pyproject.toml`
(PEP 621 metadata, Hatchling build backend), pytest tests, Ruff linting config,
a GitHub Actions CI workflow, and a license of your choice.

## Requirements

```bash
conda install -c conda-forge cookiecutter
# or: pip install cookiecutter
```

## Usage

From a directory where you want the new project created:

```bash
cookiecutter path/to/cookiecutter-python-package
```

Or straight from a Git URL:

```bash
cookiecutter https://github.com/yourusername/cookiecutter-python-package.git
```

You'll be prompted for each value below. Press Enter to accept the default.

## Prompts

| Variable | Description | Default |
| --- | --- | --- |
| `project_name` | Human-readable project name | `My Package` |
| `project_slug` | Distribution / repo name (derived) | `my-package` |
| `package_name` | Importable module name (derived) | `my_package` |
| `project_short_description` | One-line description | `A simple Python package.` |
| `version` | Initial version | `0.1.0` |
| `full_name` | Author name | `Your Name` |
| `email` | Author email | `you@example.com` |
| `github_username` | GitHub username for URLs | `yourusername` |
| `python_requires` | Minimum Python version spec | `>=3.9` |
| `license` | MIT / BSD-3-Clause / Apache-2.0 / None | `MIT` |

`project_slug` and `package_name` are derived automatically from
`project_name`, but you can override them at the prompt.

## Generated layout

```
my-package/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── core.py
│       └── py.typed
├── tests/
│   ├── __init__.py
│   └── test_core.py
├── .gitignore
├── environment.yml
├── LICENSE
├── README.md
└── pyproject.toml
```

## After generating

```bash
cd my-package
conda env create -f environment.yml
conda activate my_package
pytest
```

## Adding another license

Add the identifier to the `license` list in `cookiecutter.json`, then add a
matching `{% elif cookiecutter.license == "..." %}` block in
`{{ cookiecutter.project_slug }}/LICENSE`. Use `__YEAR__` where you want the
current year; the post-generation hook substitutes it automatically.
