import json
import os

class Article:
    def __init__(self):
        self.data = []
    def add_data(self, title, author, char_count, publisher, about):
        self.data.append({
            "title": title,
            "author": author,
            "char_count": char_count,
            "publisher": publisher,
            "about": about,
        })

    def load_data(self, filename):
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        else:
            print(f"Ошибка при загрузке данных. Файла {filename} не существует!")

    def save_data(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def print_data(self):
        if self.data:
            for el in self.data:
                print(json.dumps(el, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    FILE_NAME = "json_data.json"

    article = Article()
    article.load_data(FILE_NAME)

    while True:
        print("1 - Добавить статью и сохранить")
        print("2 - Вывести весь список статей")
        print("0 - Выход")
        choise = input("> ")

        if choise == '0':
            break
        elif choise == '1':
            article.add_data(title=input("Название статьи> "),
                             author=input("Автор> "),
                             char_count=input("Количество страниц> "),
                             publisher=input("Издатель> "),
                             about=input("Краткое описание> "))
            article.save_data(FILE_NAME)
        elif choise == "2":
            article.print_data()

        print("*"*30)