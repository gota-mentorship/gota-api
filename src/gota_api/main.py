from os import environ

from fastapi import FastAPI
from mangum import Mangum

from gota_api.routers import users

app = FastAPI(root_path=environ.get("API_ROOT_PATH", ""))
app.include_router(users.router)


@app.get("/healthcheck")
def is_healthy():
    return True


# Add support to run in native aws
handler = Mangum(app)
