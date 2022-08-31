from enum import Enum

from pydantic import EmailStr

from gota_api.models.model import Model, ModelID


class UserAvailability(str, Enum):
    BIWEEKLY = "BIWEEKLY"
    ONCE_A_MONTH = "ONCE_A_MONTH"
    ONCE_A_WEEK = "ONCE_A_WEEK"
    ONE_TIME_ONLY = "ONE_TIME_ONLY"


class UserSkill(str, Enum):
    BACKEND = "BACKEND"
    FRONT_END = "FRONT_END"
    NETWORKING = "NETWORKING"
    PEOPLE_MANAGEMENT = "PEOPLE_MANAGEMENT"
    SOFTWARE_DEVELOPMENT = "SOFTWARE_DEVELOPMENT"


class User(Model):
    name: str
    email: EmailStr
    availability: UserAvailability
    skills: list[str]


UserID = ModelID
