import uuid

from fastapi import APIRouter, HTTPException

from gota_api.models.user import User
from gota_api.repositories.erros import ItemNotFoundError
from gota_api.repositories.user import UserRepository
from gota_api.storage.memory import MemoryStorage

# storage = DynamoDBStorage(
#     table_name=environ.get("DYNAMODB_TABLE_NAME"),
#     partition_key=environ.get("DYNAMODB_PARTITION_KEY"),
#     endpoint_url=environ.get("DYNAMODB_ENDPOINT_URL"),
# )
# TODO: replace in-memory storage by DynamoDB
storage = MemoryStorage()
repository = UserRepository(storage)
router = APIRouter(prefix="/users", tags=["users"])

# TODO: drop unknown fields from model
# Reason is the fact FastAPI doesn't do this validation
# See https://github.com/tiangolo/fastapi/pull/1297
@router.post("/", response_model=User, response_model_include={"id"})
def create_user(user: User) -> User:
    return repository.create_item(user)


# TODO: drop unknown fields from model
# Reason is the fact FastAPI doesn't do this validation
# See https://github.com/tiangolo/fastapi/pull/1297
@router.put("/{user_id}")
def update_user(user_id: uuid.UUID, user: User) -> None:
    try:
        return repository.update_item(user_id, user)
    except ItemNotFoundError:
        raise HTTPException(status_code=404)


@router.get("/", response_model=list[User])
def get_users() -> list[User]:
    return repository.get_items()


@router.get("/{user_id}")
def get_user(user_id: uuid.UUID) -> User:
    try:
        return repository.get_item(user_id)
    except ItemNotFoundError:
        raise HTTPException(status_code=404)
