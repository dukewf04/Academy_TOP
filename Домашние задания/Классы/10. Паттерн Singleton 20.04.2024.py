# Task 1 (Singleton)
# class DataBase:
#     """Интерфейс подключения к базе данных"""
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(DataBase, cls).__new__(cls)
#         return DataBase._instance
#
#     def __init__(self, db_name, db_user, db_password, db_host, db_port):
#         self.db_name = db_name
#         self.db_user = db_user
#         self.db_password = db_password
#         self.db_host = db_host
#         self.db_port = db_port
#
#     def connect(self):
#         print(f"Подключение к базе данных {self.db_name} прошло успешно!")
#
# db1 = DataBase(
#     db_name="HomeDB",
#     db_user="Postgres",
#     db_password="Postgres",
#     db_host="localhost",
#     db_port="5432",
# )
#
# db2 = DataBase(
#     db_name="WorkDB",
#     db_user="root",
#     db_password="herasebe",
#     db_host="localhost",
#     db_port="9999",
# )
#
# print(f"db1: {db1.__dict__}\ndb2: {db2.__dict__}")


# Task 2 (Абстрактная фабрика)
# import random
# class Factory:
#     def __init__(self, class_factory = None):
#         self.class_factory = class_factory
#
#     def show(self):
#         show_factory = self.class_factory()
#         print("name:", show_factory, "\nprice:", show_factory.price(), "\n")
#
# class DSA:
#     def price(self):
#         return 111000
#     def __str__(self):
#         return "DSA"
#
# class STL:
#     def price(self):
#         return 15000
#     def __str__(self):
#         return "STL"
#
# class SDE:
#     def price(self):
#         return 8000
#     def __str__(self):
#         return "SDE"
#
# def random_factory():
#     return random.choice([SDE, STL, DSA])()
# factory = Factory(random_factory)
#
# for i in range(5):
#     factory.show()
# sde = SDE()
# stl = STL()
# dsa = DSA()



# Task 3 (Логирование операций)
# import datetime as dt
# class Loggin:
#     """Логирование действий пользователя"""
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             Loggin._instance = super(Loggin, cls).__new__(cls)
#         return Loggin._instance
#
#     def __init__(self, path: str = "file"):
#         self.log_fle = "log.txt"
#         if path not in ("file", "screen"):
#             raise ValueError("Введено не корректное значение!")
#         self.path = path
#         self.count = 0
#
#     def log(self, data):
#         self.count += 1
#         loggin_data = f"[{self.count}] {dt.datetime.now().strftime('%d-%m-Y %H:%M')}. {data}\n"
#         if self.path == "file":
#             with open(self.log_fle, "a", encoding="utf-8") as f:
#                 f.write(loggin_data)
#         elif self.path == "screen":
#             print(loggin_data)
#
#
# loggin = Loggin(path=input("Куда будут логироваться действия (file - в файл, screen - на экран)> "))
#
# numbers = list(input("Введите числа через пробел> ").strip().split())
# loggin.log("Получен список чисел типа str")
#
# file = input("Введите путь к файлу, для сохранения данных> ")
# loggin.log("Получен путь к файлу, для сохранения данных")
#
# numbers = list(map(int, numbers))
# loggin.log("Преобразование списка str в список int")
#
# maxVal, minVal = max(numbers), min(numbers)
# loggin.log("Найдены максимум и минимум чисел")
#
# with open(file, "w", encoding="utf-8") as f:
#     data = f"Список чисел: {numbers}\nМаксимум: {maxVal}\nМинимум: {minVal}"
#     f.write(data)
#     loggin.log("Данные сохранены в файл")
#
#     print(data)
#