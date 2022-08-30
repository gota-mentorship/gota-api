from typing import Union

from gota_api.storage.storage import Storage
from gota_api.storage.types import StorageItem, StorageItemID


class MemoryStorage(Storage):
    """
    Dummy lightweight in-memory implementation of a storage to retrieve and save items using a
    Python dict.
    """

    def __init__(self):
        self._items = {}

    def get_items(self) -> list[StorageItem]:
        return [item for item in self._items.values()]

    def get_item(self, item_id: StorageItemID) -> Union[StorageItem, None]:
        return self._items.get(item_id)

    def save_item(self, item: StorageItem) -> None:
        self._items[item.id] = item
