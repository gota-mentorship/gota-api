# gota-api

## Pre-requisites

-   Runtime (python3.10): https://www.python.org/downloads/
-   Package manager (poetry): https://python-poetry.org/

## Development

### Register git hooks

```bash
git config --local core.hooksPath .githooks/
```

### Test

1. Install the package (and its dependencies)
    ```bash
    poetry install
    ```
1. Activate a virtual environment
    ```bash
    poetry shell
    ```
1. Run tests:
    ```bash
    poetry run pytest
    ```
