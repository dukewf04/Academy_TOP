# Task1 (Soda)
# class Soda:
#     def __init__(self, dobavka: str = ''):
#         self.dobavka = dobavka
#
#     def show_my_drink(self):
#         if isinstance(self.dobavka, str) == False:
#             print("Ошибка ввода данных")
#             return False
#
#         if self.dobavka:
#             print(f"Газировка и {self.dobavka}")
#         else:
#             print(f"Обычная газировка")
#
# soda1 = Soda(dobavka='Малина-лайм')
# soda2 = Soda()
# soda3 = Soda(dobavka=5)
#
# for obj in (soda1, soda2, soda3):
#     obj.show_my_drink()


# Task2 (Triangle)
# class TriangleChecker:
#     def __init__(self, a: int, b: int, c: int):
#         self.lst = (a, b, c)
#     def is_triangle(self):
#         for el in self.lst:
#             if isinstance(el, int) == False:
#                 print("Нужно вводить только числа!")
#                 return False
#             elif el < 0:
#                 print("С отрицательными числами ни чего не выйдет!")
#                 return False
#             elif el > sum(self.lst) - el:
#                 print("Жаль, но из этого треугольник не сделать")
#                 return False
#
#         print("Ура, можно построить треугольник!")
#
#
# triangle = TriangleChecker(a=5, b=7, c=9)
# triangle.is_triangle()


# Task3 (Nikola)
# class Nikola:
#     __slots__ = ["name", "age"]  # Ограничение набора свойств и методов в экземпляре
#     def __init__(self, name: str = "Николай", age: int = 20):
#         self.name = name if name == "Николай" else f"не {name}, а Николай"
#         self.age = age
#     def __str__(self):
#         return f"Я {self.name}, мне {self.age} лет"
#
# nikola = Nikola(name="Женя", age=20)
# print(nikola)


# Task4 (RealString)
# Методы оператора сравнения:
# __eq__() - для равенства
# __ne__() - для не равенства
# __lt__() - для оператора <
# __le__() - для оператора <=
# __gt__() - для оператора >
# __ge__() - для оператора >=
class RealString:
    def __init__(self, some_str: str):
        self.some_str = some_str
    def __eq__(self, other):
        return len(self.some_str) == len(other)
    def __len__(self):
        return len(self.some_str)

str1 = RealString("Шоколад")
str2 = RealString("Шоколад111")
str3 = "Шоколад"
str4 = [1, 2, 3]
print(str3 == str1)