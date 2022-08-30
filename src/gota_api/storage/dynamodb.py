from typing import Any, Union

import boto3

from gota_api.storage.storage import Storage
from gota_api.storage.types import StorageItem, StorageItemID


class DynamoDBStorage(Storage):
    DynamoDBClient = Any

    def __init__(
        self,
        table_name: str,
        partition_key: str,
        endpoint_url: str = None,
    ):
        self._partition_key = partition_key
        self._client = self._create_client(endpoint_url)
        self._table = self._client.Table(table_name)

    def _create_client(self, endpoint_url: str) -> DynamoDBClient:
        if endpoint_url:
            return boto3.resource("dynamodb", endpoint_url=endpoint_url)
        return boto3.resource("dynamodb")

    def get_items(self) -> list[StorageItem]:
        # TODO: add query-based filtering (which is more optimized than scan)
        response = self._table.scan()
        return response.get("Items", [])

    def get_item(self, item_id: StorageItemID) -> Union[StorageItem, None]:
        response = self._table.get_item(Key={self._partition_key: item_id})
        return response.get("Item")

    def save_item(self, item: StorageItem) -> None:
        self._table.put_item(Item=item)
