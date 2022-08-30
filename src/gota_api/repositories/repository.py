from abc import ABC, abstractmethod
from typing import Union

from gota_api.repositories.erros import ItemNotFoundError
from gota_api.storage.types import StorageItem, StorageItemID


class Repository(ABC):
    """
    Layer to manage, persist and retrieve items from storage.
    """

    @abstractmethod
    def get_items(self) -> list[StorageItem]:
        """
        Get all items from the repository.

        :return: all items from the repository
        """

    @abstractmethod
    def get_item(self, item_id: StorageItemID) -> Union[StorageItem, ItemNotFoundError]:
        """
        Get the item with the item_id from the repository.

        :param item_id: the id of the item to be retrieved from the repository
        :raises ItemNotFoundError: if the item wasn't found
        :return: the item found
        """

    @abstractmethod
    def create_item(self, item: StorageItem) -> StorageItemID:
        """
        Creates the item in the repository. An id and created at timestamp is auto-generated.

        :param item: the item to be saved
        :return: the saved item
        """

    @abstractmethod
    def update_item(
        self, item_id: StorageItemID, item: StorageItem
    ) -> Union[None, ItemNotFoundError]:
        """
        Update the item with the given id in the repository.

        :param item_id: the unique identifier of the item to be updated
        :param item: the item to be saved in the repository
        :raises ItemNotFoundError: if the item isn't present in the repository
        :return: void
        """
