from abc import ABC, abstractmethod
from typing import Union

from gota_api.storage.types import StorageItem, StorageItemID


class Storage(ABC):
    """
    Layer to persist and retrieve data from the storage.
    """

    @abstractmethod
    def get_items(self) -> list[StorageItem]:
        """
        Get all items from the storage.

        :return: all items from the storage
        """

    @abstractmethod
    def get_item(self, id: StorageItemID) -> Union[StorageItem, None]:
        """
        Get the item for the given id.

        :param id: the identifier of the item to be retrieved from storage
        :return: item found in storage or None
        """

    @abstractmethod
    def save_item(self, item: StorageItem) -> None:
        """
        Save the given item in storage using the id as the unique identifier.

        :param item: the item to be saved in the storage
        :return: void
        """
