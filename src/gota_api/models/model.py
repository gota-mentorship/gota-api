import uuid
from typing import Optional

from pydantic import BaseModel

ModelID = uuid.UUID


class Model(BaseModel):
    id: Optional[ModelID]
    created_at: Optional[int]
    updated_at: Optional[int]
