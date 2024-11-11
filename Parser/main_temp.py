from bs4 import BeautifulSoup
import requests
import pandas

# Модуль glob находит все пути, совпадающие с заданным шаблоном в соответствии с правилами, используемыми оболочкой Unix
import glob
from collections import OrderedDict

BASE_URL = "https://www.marvel.com"
URL = "https://www.marvel.com/characters"
pages_csv = "characters_pages.csv"
characters_csv = "characters_dataset.csv"


# Запись файла в csv формат
def write_csv_file(df, name):
    df.to_csv(name, index=False)
    print("Успешно выполнено!\n")


# Обратимся к полученному файлу
def read_csv_file(name):
    df = pandas.read_csv(name)
    return df


# Создание файла для записи данных из каждой карточки персонажа
def create_characters_df():
    pages = pandas.read_csv(pages_csv)
    links = pages["Links"]
    columns = []
    marvel_list = []

    # Проход по всем ссылкам, записанным в csv файл
    for link in links:
        # Данные из карточки
        marvel_characters = OrderedDict()
        # Получение данных из карточки каждого персонажа с сайта
        requests = requests.get(BASE_URL + str(link))

        content = requests.content
        soup = BeautifulSoup(content, "html.parser")

        # Поиск заголовка персонажа
        marvel_characters["Name"] = soup.find("h1").text.replace("\n", "").strip()
        marvel_characters["Link"] = link
        print(soup.find("h1").text.replace("\n", "").strip(), BASE_URL + str(link))

        # Поиск описания персонажа
        label = soup.find("p", {"class": "bioheader__label"})
        stat = soup.find_all("p", {"class": "bioheader__stat"})
        for i in range(len(label)):
            column = label[i].text.title()
            if column not in columns:
                column.append(column)

            try:
                marvel_characters[column] = stat[i].text.replace("\n", "").strip()
            except:
                marvel_characters[column] = ""

        marvel_list.append(marvel_list)
    df = pandas.DataFrame(marvel_list)
    write_csv_file(df, characters_csv)


# Получение ссылок, их обработка для передачи в csv файл
def get_all_links():
    # Запрос данных с сайта
    page = requests.get(URL)
    # Вызов конвертера данных HTML-структуры сайта
    soup = BeautifulSoup(page.content, "html.parser")

    pages = []
    # Поиск данных из файла по структуре HTML
    mvl_cards = soup.find("div", {"class": "full-content"}).find_all(
        "div", {"class": "mvl-card--explore"}
    )
    for i in range(len(mvl_cards) - 1):
        link = mvl_cards[i]
        page = link.find("a")
        # Достаем атрибут href
        print(i, page["href"], page.text)
        # Добавляем все ссылки в список
        pages.append(page["href"])
    df = pandas.DataFrame({"Link": pages})
    write_csv_file(df, pages_csv)


def main():
    files = glob.glob("*.csv")
    if characters_csv not in files:
        if pages_csv not in files:
            print("Создание файла characters_pages.csv")
            get_all_links()
        print("Создание файла characters_dataset.csv")
        create_characters_df()
    df = read_csv_file(characters_csv)
    df = df.fillna("")
    print("Колонки:", df.columns.values)
    print(df[["Link", "Eyes"]])
    # Чтение данных из файла и отображение
    df = pandas.read_csv("characters_dataset.csv")
    #  Размеры файла
    print(df.shape)


if __name__ == "__main__":
    main()
