import datetime

class User:
    def __init__(self, id: str) -> None:
        # idの整合性チェック
        if self.__is35id(id):
            raise ValueError("id is invalid")

        self.id = id
        self.date = datetime.datetime.now().strftime("%Y%m%d")
        self.flag = True

    def __is35id(self, id: str) -> bool:
        # 3文字のアルファベットと5文字の数字で構成されているか
        if len(id) != 8:
            return False
        if not id[:3].isalpha():
            return False
        if not id[3:].isdigit():
            return False
        return True