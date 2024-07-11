from typing import Protocol
import boto3
from model.user import User

class UserDataLoader(Protocol):
    def load_user_data(self) -> list[User]: ...

class LocalUserDataLoader(UserDataLoader):
    def __init__(self, path) -> None:
        self.path = path

    def load_user_data(self) -> list[User]:
        # ローカルファイルからユーザーリストを取得する
        with open(self.path) as f:
            content = f.read()

        # ユーザーリストをUserクラスのリストに変換する
        return [
            User(id=line.strip())
            for line in content.strip().split("\n")
        ]

class S3UserDataLoader(UserDataLoader):
    def __init__(self, bucketname, path) -> None:
        self.s3client = boto3.client("s3")
        self.bucketname = bucketname
        self.path = path

    def load_user_data(self) -> list[User]:
        # S3からユーザーリストを取得する
        response = self.s3client.get_object(Bucket=self.bucketname, Key=self.path)
        content = response["Body"].read().decode("utf-8")

        # ユーザーリストをUserクラスのリストに変換する
        return [
            User(id=line.strip())
            for line in content.strip().split("\n")
        ]