import uuid
from typing import Optional

from pydantic import BaseModel


class Model(BaseModel):
    id: uuid.UUID
    created_at: int
    updated_at: Optional[int]
