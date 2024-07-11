import os
from userdataloader import S3UserDataLoader, LocalUserDataLoader
from userdataupdater import UserDataUpdateDynamodb, UserDataUpdateLocal

# 環境変数を読み込む
TABLE_NAME = os.environ["TABLE_NAME"]
ENV = os.environ["ENV"]

if ENV == "local":
    FILEPATH = os.environ["FILEPATH"]
    userdataloader = LocalUserDataLoader(FILEPATH)
    userdataupdate = UserDataUpdateLocal(TABLE_NAME)
else:
    BUCKET_NAME = os.environ["BUCKET_NAME"]
    PATH = os.environ["PATH"]
    userdataloader = S3UserDataLoader(BUCKET_NAME, PATH)
    userdataupdate = UserDataUpdateDynamodb(TABLE_NAME)


def main() -> None:
    try:
        # ユーザーリストを取得する
        users = userdataloader.load_user_data()

        # ユーザーリストでdatabaseを更新する
        userdataupdate.update_users(users)

        # 更新されなかったユーザーをリストアップする
        unupdated_users = userdataupdate.list_unupdated_users()

        # リストアップしたユーザーのフラグを落とす
        userdataupdate.deactivate_unupdated_users(unupdated_users)

    except Exception as e:
        print(f"Error: {e}")
        raise e

    return


def lambda_handler(event, context):
    main()


if __name__ == "__main__":
    main()
