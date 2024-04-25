import random
import tabulate as tab

# Task 2 (Создание 3 разных видов паст)
# class PastaFactory:
#     def __init__(self, class_factory = None):
#         self.factory = class_factory()
#     def show(self):
#         print("Тип пасты:", self.factory.type_pasta())
#         print("Соус:", self.factory.sous())
#         print("Начинка:", self.factory.nachinka())
#         print("Добавки:", self.factory.dobavki(), '\n')
#
# class Kampanelle:
#     def type_pasta(self):
#         return "Кампанелле"
#     def sous(self):
#         return "Мазик"
#     def nachinka(self):
#         return "Фарш"
#     def dobavki(self):
#         return "Грибы"
#
# class Kannellony:
#     def type_pasta(self):
#         return "Каннеллони"
#     def sous(self):
#         return "Кетчуп"
#     def nachinka(self):
#         return "Колбаса"
#     def dobavki(self):
#         return "Сыр"
#
# class Kazareche:
#     def type_pasta(self):
#         return "Казаречче"
#     def sous(self):
#         return "Кетчуп"
#     def nachinka(self):
#         return "Креветки"
#     def dobavki(self):
#         return "Сыр"
#
# for i in range(5):
#     factory = PastaFactory(random.choice([Kampanelle, Kannellony, Kazareche]))
#     factory.show()


# Task 1 (Реализация паттерна Builder)


# Пицца
# class PizzaFactory:
#     def __init__(self, class_factory = None):
#         self.factory = class_factory()
#     def show(self):
#         return self.factory.get_pizza()
#
# class PizzaHome:
#     def get_pizza(self):
#         return "Пицца Домашняя\n\t- Вес: 1400 гр\n\t- Цена: 1900 р\n\t- Состав: Томатный соус, моцарелла, колбаса всех видов"
#
# class PizzaFourChees:
#     def get_pizza(self):
#         return "Пицца 4 сыра\n\t- Вес: 1200 гр\n\t- Цена: 1300 р\n\t- Состав: Томатный соус, моцарелла, пармезан, сыр горгонзола, артишоки и орегано"
#
# class PizzaKrudo:
#     def get_pizza(self):
#         return "Пицца Крудо\n\t- Вес: 700 гр\n\t- Цена: 800 р\n\t- Состав: Томатный соус, моцарелла и пармская ветчина"
#
#
# # Суши
# class SushiFactory:
#     def __init__(self, class_factory = None):
#         self.factory = class_factory()
#     def show(self):
#         return self.factory.get_sushi()
#
# class SushiDomino:
#     def get_sushi(self):
#         return "Суши Домино\n\t- Вес: 800 гр\n\t- Цена: 1500 р\n\t- Состав: рис, форель"
#
# class SushiUramaki:
#     def get_sushi(self):
#         return "Суши Урамаки\n\t- Вес: 1000 гр\n\t- Цена: 2500 р\n\t- Состав: рис, угорь"
#
# class SushiGunkanMaki:
#     def get_sushi(self):
#         return "Суши Гункан-маки\n\t- Вес: 700 гр\n\t- Цена: 1400 р\n\t- Состав: салат, икра"
#
#
#
# # Роллы
# class RollFactory:
#     def __init__(self, class_factory = None):
#         self.factory = class_factory()
#     def show(self):
#         return self.factory.get_roll()
#
# class RollBig:
#     def get_roll(self):
#         return "Роллы Big \n\t- Вес: 700 гр\n\t- Цена: 3000 р\n\t- Состав: рис, рыба"
#
# class RollMedium:
#     def get_roll(self):
#         return "Роллы Medium\n\t- Вес: 1200 гр\n\t- Цена: 980 р\n\t- Состав: рис, молюски"
#
# class RollSmall:
#     def get_roll(self):
#         return "Роллы Small\n\t- Вес: 1400 гр\n\t- Цена: 1900 р\n\t- Состав: рис, сыр, огурцы, колбаса"
#
#
# # Билдер
# class PZMilano:
#     def __init__(self):
#         self.sushi = None
#         self.pizza = None
#         self.roll = None
#
#     def __str__(self):
#         return f"Ваш заказ:\n {self.sushi if self.sushi else ''},\n" \
#                f"{self.pizza if self.pizza else ''},\n" \
#                f"{self.roll if self.roll else ''}\n"
#
# class PZMilano_Builder:
#     def __init__(self):
#         self.pzmilano = PZMilano()
#         self.choise = None
#
#     def show_menu(self):
#         print("********* МЕНЮ НА СЕГОДНЯ ********* ")
#         menu = [
#             ["Суши", "Пицца", "Роллы"],
#             ["1. Домино", "4. Домашняя", "7. Big"],
#             ["2. Урамаки", "5. 4 сыра", "8. Medium"],
#             ["3. Гункан-маки", "6. Крудо", "9. Small"]
#         ]
#         print(tab.tabulate((menu)))
#         self.choise = input("Ваш заказ (введите номер через пробел)?> ").split()
#
#         return self
#
#     def cooking(self):
#         for el in self.choise:
#             if el in ['1', '2', '3']:
#                 self.pzmilano.sushi = SushiFactory(
#                     [SushiDomino, SushiUramaki, SushiGunkanMaki][int(el)-1]
#                 ).show()
#             elif el in ['4', '5', '6']:
#                 self.pzmilano.pizza = PizzaFactory(
#                     [PizzaHome, PizzaFourChees, PizzaKrudo][int(el)-4]
#                 ).show()
#             elif el in ['7', '8', '9']:
#                 self.pzmilano.roll = RollFactory(
#                     [RollBig, RollMedium, RollSmall][int(el)-7]
#                 ).show()
#
#         return self.pzmilano
#
#
# pzm_builder = PZMilano_Builder()
# pzm = pzm_builder.show_menu().cooking()
#
# print(pzm)


# Task 3 (паттерн Prototype)
# from abc import ABCMeta, abstractmethod
# import copy
# class Courses_PJR(metaclass=ABCMeta):
#     def __init__(self):
#         self.id = None
#         self.type = None
#     @abstractmethod
#     def cource(self):
#         pass
#     def get_type(self):
#         return self.type
#     def get_id(self):
#         return self.id
#     def set_id(self, id):
#         self.id = id
#     def clone(self):
#         return copy.copy(self)
#
# class Python(Courses_PJR):
#     def __init__(self):
#         super().__init__()
#         self.type = "Python"
#     def cource(self):
#         print("Cource python method")
# class Java(Courses_PJR):
#     def __init__(self):
#         super().__init__()
#         self.type = "Java"
#     def cource(self):
#         print("Cource java method")
#
# class R(Courses_PJR):
#     def __init__(self):
#         super().__init__()
#         self.type = "R"
#     def cource(self):
#         print("Cource R method")
#
# # Класс кэш
# class Courses_cache:
#     cache = {}
#
#     @staticmethod
#     def get_course(sid):
#         COURSE = Courses_cache.cache.get(sid, None)
#         return COURSE.clone()
#
#     @staticmethod
#     def load():
#         python = Python()
#         python.set_id("1")
#         Courses_cache.cache[python.get_id()] = python
#
#         java = Java()
#         java.set_id("2")
#         Courses_cache.cache[java.get_id()] = java
#
#         r = R()
#         r.set_id("3")
#         Courses_cache.cache[r.get_id()] = r
#
#
# if __name__ == "__main__":
#     Courses_cache.load()
#
#     python_course = Courses_cache.get_course("1")
#     print(python_course.get_type())
#
#     java_course = Courses_cache.get_course("2")
#     print(java_course.get_type())
#
#     r_course = Courses_cache.get_course("3")
#     print(r_course.get_type())