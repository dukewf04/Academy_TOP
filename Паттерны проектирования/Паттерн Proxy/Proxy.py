# Паттерн Proxy
import abc
import random

class AbstractClass(metaclass=abc.ABCMeta):
    """Шаблон класса для Real and Proxy"""
    @abc.abstractmethod
    def sort_digits(self, reverse=False):
        pass


class RealClass(AbstractClass):
    """Реальный класс"""
    def __init__(self):
        self.digits = [random.random() for _ in range(1000000)]

    def sort_digits(self, reverse=False):
        self.digits.sort()

        if reverse:
            self.digits.reverse()

    def __str__(self):
        return "I am real RealClass"


class ProxyClass(AbstractClass):
    ref_count = 0
    def __init__(self):
        # Метод возвращает значение именованного атрибута объекта, если атрибут не найден - возвращет значение по умолчанию
        # Параметры: object, name, default. Обычно используется, когда атрибут или объект является переменной.
        if not getattr(self.__class__, "cached_object", None):
            self.__class__.cached_object = RealClass()
            print("Новый объект создан")
        else:
            print("Используется существующий")

        self.__class__.ref_count += 1
        print("Использований: ", self.__class__.ref_count)

    def sort_digits(self, reverse=False):
        print("Метод сортировки")
        print(locals().items())

        self.__class__.cached_object.sort_digits(reverse=reverse)

    def __del__(self):
        self.__class__.ref_count -= 1
        if self.__class__.ref_count == 0:
            print("Удаление копии класса")
            del self.__class__.cached_object

        print("ref_count:", self.__class__.ref_count)


if __name__ == "__main__":
    proxA = ProxyClass()
    print()
    proxB = ProxyClass()
    print()
    proxC = ProxyClass()
    print()

    proxA.sort_digits(reverse=True)
    print()

    print("Deleting proxA")
    del proxA

    print("Deleting proxB")
    del proxB

    print("Deleting proxC")
    del proxC