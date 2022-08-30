# gota-api

## Pre-requisites

-   Runtime (python3.10): https://www.python.org/downloads/
-   Package manager (poetry): https://python-poetry.org/

## Development

**Pre-requisites:**

1. Activate a virtual environment
    ```bash
    poetry shell
    ```
1. Install the package (and its dependencies)
    ```bash
    poetry install
    ```

### Format

```bash
./bin/format-code
```

### Test

```bash
poetry run pytest
```

### Run API locally

```bash
python3 -m uvicorn gota_api.main:app --host 0.0.0.0 --port 8080
```
