import uuid
from typing import NamedTuple

StorageItemID = uuid.UUID
StorageItem = NamedTuple(
    "StorageItem",
    [
        ("id", StorageItemID),
        ("created_at", str),
        ("updated_at", str),
    ],
)
