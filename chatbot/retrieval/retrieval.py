import json
import os

class Retrieval:
    def __init__(self, data_path: str = "./data/newjeans.json"):
        with open(data_path, "r") as file:
            data: dict[str, str] = json.load(file)
            self.data = data

    def retrieve(self, query: str) -> str | None:
        # ####
        for key, value in self.data.items():
            if key.lower() in query.lower():  # 대소문자 구분 없이 검색
                return f"{key}: {value}"
        return None
        # ###

        pass

    def print_data(self) -> None:
        print(self.data)
