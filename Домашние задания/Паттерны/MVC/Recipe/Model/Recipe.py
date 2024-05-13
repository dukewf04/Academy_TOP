import json


class Recipe:
    __DATA_STRUCTURE = {
        "name": "Имя",
        "author": "Автор",
        "type": "Тип рецепта",
        "title": "Описание",
        "link": "Ссылка на видео с рецептом",
        "ingredients_list": "Список ингридиентов",
        "kitchen_name": "Название кухни",
    }

    def __init__(self):
        self.__data: list[dict[str, str]] = []

    def printf(self, data: dict):
        """Структурированный вывод данных на экран"""

        for key in data.keys():
            print(f"\t\t{self.__DATA_STRUCTURE[key]}: {data[key]}")

    def add_recipe(self, data):
        self.__data.append(data)

    def get_all_recipes(self):
        count = 0
        for el in self.__data:
            count += 1
            print(f"\t[{count}]")
            self.printf(el)
            print("-" * 20)

    def find_recipie(self, name):
        if len(self.__data) == 0:
            print("Список рецептов пуст")
            return

        empty = True
        for el in self.__data:
            if el["name"].find(name) != -1:
                empty = False
                self.printf(el)

        if empty:
            print("Рецептов не найдено")
