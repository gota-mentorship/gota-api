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

#### Play with sample data

##### Create User

```bash
# request
curl \
    -X "POST" \
    -d "@user_fixture.json" \
    -H "Content-Type: application/json" \
    "http://0.0.0.0:8080/users"

# response
> {"id":"159d51a3-eca3-4b23-b114-cff88e1eec7f"}
```

##### Get Users

```bash
# request
curl "http://0.0.0.0:8080/users"

# response
> [{"id":"3996c777-6322-4d7d-8455-acd73281abb1","created_at":1661942298,"updated_at":1661942366,"name":"Mario","email":"email@email.email","availability":"ONCE_A_WEEK","skills":["BACKEND","FRONT_END"]},{"id":"8c6ca891-deed-4afb-8896-9d60d0ac36d1","created_at":1661942298,"updated_at":null,"name":"Mario","email":"email@email.email","availability":"ONCE_A_WEEK","skills":["BACKEND","FRONT_END"]},{"id":"bb82c4d4-206c-42ac-967e-ffd0f2bb637b","created_at":1661942299,"updated_at":null,"name":"Mario","email":"email@email.email","availability":"ONCE_A_WEEK","skills":["BACKEND","FRONT_END"]},{"id":"159d51a3-eca3-4b23-b114-cff88e1eec7f","created_at":1661942409,"updated_at":null,"name":"Mario","email":"email@email.email","availability":"ONCE_A_WEEK","skills":["BACKEND","FRONT_END"]}]
```

##### Get User

```bash
# request
USER_ID="3996c777-6322-4d7d-8455-acd73281abb1"
curl "http://0.0.0.0:8080/users/${USER_ID}"

# response
> {"id":"3996c777-6322-4d7d-8455-acd73281abb1","created_at":1661942298,"updated_at":1661942366,"name":"Mario","email":"email@email.email","availability":"ONCE_A_WEEK","skills":["BACKEND","FRONT_END"]}
```

##### Update User

```bash
# request
USER_ID="3996c777-6322-4d7d-8455-acd73281abb1"
curl \
    -X "PUT" \
    -d "@user_fixture.json" \
    -H "Content-Type: application/json" \
    "http://0.0.0.0:8080/users/${USER_ID}"

# response
> null
```
