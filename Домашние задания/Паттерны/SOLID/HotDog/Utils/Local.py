local_storage = {
    "bun": "Булочка",
    "meat": "Мясо",
    "sausage": "Сосиски",
    "bacon": "Бекон",
    "cheese": "Сыр",
    "onion": "Лук",
    "cucumber": "Огурец",
    "tomato": "Помидор",
    "chili": "Чили",
    "avocado": "Авокадо",
    "cabbage": "Капуста",
    "jalapeno": "Хлапеньо",
    "mayonnaise": "Майонез",
    "ketchup": "Кетчуп",
    "mustard": "Горчица"
}

def local(input_string: str) -> str:
    """Локаль для трансляции с английского на русский. Возвращает перевод слова."""

    return local_storage[input_string]


def locals(input_strings: list) -> list:
    """Локаль для трансляции с английского на русский. Возвращает список слов с переводом."""

    return [local_storage[input_strings[i]] for i in range(len(input_strings))]