import uuid
from typing import Union

import arrow

from gota_api.models.user import User, UserID
from gota_api.repositories.erros import ItemNotFoundError
from gota_api.repositories.repository import Repository
from gota_api.storage.storage import Storage


class UserRepository(Repository):
    def __init__(self, storage: Storage):
        self._storage = storage

    def get_items(self) -> list[User]:
        return self._storage.get_items()

    def get_item(self, id: UserID) -> Union[User, ItemNotFoundError]:
        user = self._storage.get_item(id)
        if not user:
            raise ItemNotFoundError()
        return user

    def create_item(self, user: User) -> User:
        user.id = uuid.uuid4()
        user.created_at = arrow.utcnow().int_timestamp

        self._storage.save_item(user)

        return user

    def update_item(self, user: User) -> Union[None, ItemNotFoundError]:
        existing_user = self.get_item(user.id)

        # immutable
        user.created_at = existing_user.created_at
        # auto-generated
        user.updated_at = arrow.utcnow().int_timestamp

        self._storage.save_item(user)

        return None
