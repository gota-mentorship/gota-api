import uuid

import arrow
from fastapi import APIRouter

from gota_api.models.user import User, UserAvailability, UserSkill

router = APIRouter(prefix="/users", tags=["users"])


fake_user = User(
    id=uuid.uuid4(),
    name="name",
    created_at=arrow.utcnow().int_timestamp,
    updated_at=arrow.utcnow().shift(hours=1).int_timestamp,
    email="email@email.com",
    availability=UserAvailability.ONCE_A_MONTH,
    skills=[UserSkill.BACKEND, UserSkill.SOFTWARE_DEVELOPMENT],
)

# TODO: drop unknown fields from model
# Reason is the fact FastAPI doesn't do this validation
# See https://github.com/tiangolo/fastapi/pull/1297
@router.post("/", response_model=User, response_model_include={"id"})
def create_user() -> User:
    return {"id": uuid.uuid4()}


# TODO: drop unknown fields from model
# Reason is the fact FastAPI doesn't do this validation
# See https://github.com/tiangolo/fastapi/pull/1297
@router.put("/{id}")
def update_user(id: uuid.UUID, user: User) -> None:
    return None


@router.get("/", response_model=list[User])
def get_users() -> list[User]:
    return [fake_user, fake_user, fake_user]


@router.get("/{id}")
def get_user(id: uuid.UUID) -> User:
    return fake_user
