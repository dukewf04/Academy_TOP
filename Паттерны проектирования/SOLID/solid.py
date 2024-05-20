# Паттерн SOLID
import os.path
import io
from abc import ABC, abstractmethod


# S - Принцип единой ответственности
# class User:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self._age = age
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#
# class Console:
#     @staticmethod
#     def display(obj):
#         print(f"{obj.name}, {obj.last_name}, {obj._age}")
#
#     @staticmethod
#     def input_value():
#         name = input("Input name: ")
#         last_name = input("Input last_name: ")
#         age = input("Input age: ")
#
#         return User(name, last_name, age)
#
#
# obj = User("Bill", "Ozbord", 43)
#
# Console.display(obj)
# obj = Console.input_value()
# Console.display(obj)


# O - Принцип открытости-закрытости. Объекты, классы должны быть открытыми для расширения, но закрыты для изменения
# class Output(ABC):
#     def __init__(self, data):
#         self.data = data
#
#     @abstractmethod
#     def display(self):
#         pass
#
# class ConsoleOutput(Output):
#     def display(self):
#         print(f"{self.data}")
#
# class FileOutput(Output):
#     def display(self):
#         with open("output.txt", "w", encoding="utf-8") as f:
#             f.write(self.data)
#
# obj = ConsoleOutput("some string")
# obj.display()
#
# obj2 = FileOutput("Some string file")
# obj2.display()


# L - Принцип Лисков. функции, которые используют базовый тип, должны иметь возможность использовать подтипы базового типа не зная об этом
# from typing import List
#
# class Figure(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass
#
# class Rectangle(Figure):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
# class Square(Figure):
#     def __init__(self, side):
#         self.side = side
#     def calculate_area(self):
#         return self.side * self.side
#
# def calculate_total_area(figures:List[Figure]):
#     total_area = 0
#     for obj in figures:
#         total_area += obj.calculate_area()
#     return  total_area
#
# lst = [Rectangle(5, 6), Square(10)]
# print(calculate_total_area(lst))


# I - Принцип разделения. Принцип разделения интерфейсов. Создавайте узкоспециализированные интерфейсы и не вынуждайте клиента зависеть от неиспользуемых интерфейсов
# class Walkable(ABC):
#     @abstractmethod
#     def walk(self):
#         pass
#
# class Flyable(ABC):
#     @abstractmethod
#     def fly(self):
#         pass
#
# class Ostriche(Walkable):
#     def walk(self):
#         print("Ostriche is walking")
#
# class Eagle(Walkable, Flyable):
#     def fly(self):
#         print("Eagle is flying")
#
#     def walk(self):
#         print("Eagle is walking")
#
# try:
#     obj = Eagle()
#     obj.fly()
#     obj.walk()
#
#     obj2 = Ostriche()
#     obj2.walk()
# except Exception as e:
#     print(e)


# D - принцип инверсии. Сущности должны зависеть от абстракций, а не от чего-то конкретного
class DataSource(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self):
        pass

class TextDataSource(DataSource):
    def read_data(self):
        with open(self.path, 'r') as file:
            data = file.read()
        return data

    def write_data(self, data):
        with open(self.path, 'w') as file:
            file.write(data)

class DbDataSource(DataSource):
    def read_data(self, data):
        print(f"Write {data}")
    def write_data(self, data):
        return "Data from database"

class TextOperation:
    def __init__(self, data_source):
        self.data_source = data_source
        self.data = self.data_source.read_data()

    def search_for_word(self, word):
        return word, self.data

    def count_ocurences(self, word):
        return self.data.count(word)

file = TextDataSource("D:\\data.txt")
db = DbDataSource("customers")

obj = TextOperation(file)
print(obj.search_for_word("more"))
print(obj.count_ocurences('be'))

obj = TextOperation(db)
print(obj.search_for_word('data'))
print(obj.count_ocurences('from'))