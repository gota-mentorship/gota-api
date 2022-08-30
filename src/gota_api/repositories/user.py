import uuid
from typing import Union

import arrow

from gota_api.models.model import ModelID
from gota_api.models.user import User
from gota_api.repositories.erros import ItemNotFoundError
from gota_api.repositories.repository import Repository
from gota_api.storage.storage import Storage


class UserRepository(Repository):
    def __init__(self, storage: Storage):
        self._storage = storage

    def get_items(self) -> list[User]:
        return [User(**item) for item in self._storage.get_items()]

    def get_item(self, user_id: ModelID) -> Union[User, ItemNotFoundError]:
        item = self._storage.get_item(user_id)
        if not item:
            raise ItemNotFoundError()
        return User(**item)

    def create_item(self, user: User) -> User:
        user.id = str(uuid.uuid4())
        user.created_at = arrow.utcnow().int_timestamp

        self._storage.save_item(item=user.dict())

        return user

    def update_item(self, user_id: ModelID, user: User) -> Union[None, ItemNotFoundError]:
        existing_user = self.get_item(user_id)

        # immutable
        user.id = existing_user.id
        user.created_at = existing_user.created_at

        # auto-generated
        user.updated_at = arrow.utcnow().int_timestamp

        self._storage.save_item(item=user.dict())

        return None
