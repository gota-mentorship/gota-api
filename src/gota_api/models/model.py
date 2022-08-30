import uuid
from typing import Optional

from pydantic import BaseModel

ModelID = uuid.UUID


class Model(BaseModel):
    id: ModelID
    created_at: int
    updated_at: Optional[int]
