import uuid
from typing import NamedTuple

StorageItem = NamedTuple(
    "StorageItem",
    [
        ("id", uuid.UUID),
        ("created_at", str),
        ("updated_at", str),
    ],
)

StorageItemID = uuid.UUID
