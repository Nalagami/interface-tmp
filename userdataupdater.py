from abc import ABC, abstractmethod
from model.user import User
import boto3

class UserDataUpdateInterface(ABC):
    @abstractmethod
    def update_user_data(self, users: list[User]) -> None:
        pass

    @abstractmethod
    def list_unupdated_users(self) -> list[User]:
        pass

    @abstractmethod
    def deactivate_unupdated_users(self) -> None:
        pass

class UserDataUpdateLocal(UserDataUpdateInterface):
    def __init__(self, table_name: str) -> None:
        self.dynamodb = boto3.client("dynamodb")
        self.table = table_name
        self.endpoint = "http://localhost:8000"

    def update_users(self, users: list[User]) -> None:
        # ユーザーリストでdatabaseを更新するロジック
        pass

    def list_unupdated_users(self) -> list[User]:
        # 更新されなかったユーザーをリストアップするロジック
        return []

    def deactivate_unupdated_users(self) -> None:
        # リストアップしたユーザーのフラグを落とすロジック
        pass

class UserDataUpdateDynamodb(UserDataUpdateInterface):
    def __init__(self, table_name: str) -> None:
        self.dynamodb = boto3.client("dynamodb")
        self.table = table_name

    def update_users(self, users: list[User]) -> None:
        # ユーザーリストでdatabaseを更新するロジック
        pass

    def list_unupdated_users(self) -> list[User]:
        # 更新されなかったユーザーをリストアップするロジック
        return []

    def deactivate_unupdated_users(self) -> None:
        # リストアップしたユーザーのフラグを落とすロジック
        pass