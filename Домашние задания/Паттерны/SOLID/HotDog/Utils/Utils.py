def counter_hotdog(lst: list, obj: dict) -> int:
    """Метод возвращающий количество одинаковых элементов в списке.
    Элемент obj является словарем.
    """
    counter = 0
    for el in lst:
        if el == obj:
            counter += 1

    return counter