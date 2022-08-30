from enum import Enum
from typing import Optional

from gota_api.models.base import Model
from gota_api.models.user import UserSkill


class MentorshipRole(str, Enum):
    MENTEE = "MENTEE"
    MENTOR = "MENTOR"


class MentorshipStatus(str, Enum):
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"


class Mentorship(Model):
    mentee_id: Optional[str]
    mentor_id: Optional[str]
    role: MentorshipRole
    status: MentorshipStatus
    started_at: int
    ended_at: int
    matched_skills: list[UserSkill]
