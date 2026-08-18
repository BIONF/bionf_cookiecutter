# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

Or, for local development with conda:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
conda env create -f environment.yml
conda activate {{ cookiecutter.package_name }}
```

This creates a `{{ cookiecutter.package_name }}` environment and installs the
package in editable mode along with its dev dependencies.

## Usage

```python
from {{ cookiecutter.package_name }} import greet

print(greet("world"))
```

## Development

With the `{{ cookiecutter.package_name }}` environment activated, run the tests:

```bash
pytest
```

Lint and format:

```bash
ruff check .
ruff format .
```
{% if cookiecutter.license != "None" %}
## License

Distributed under the {{ cookiecutter.license }} license. See `LICENSE` for details.
{% endif %}