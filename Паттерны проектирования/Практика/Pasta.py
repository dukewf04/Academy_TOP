import random

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
class PizzaFactory:
    def __init__(self, class_factory = None):
        self.factory = class_factory()
    def show(self):
        self.factory.get_pizza()

class PizzaHome:
    def get_pizza(self):
        return "Пицца Домашняя\n\t- Вес: 1400 гр\n\t- Цена: 1900 р\n\t- Состав: Томатный соус, моцарелла, колбаса всех видов"

class PizzaFourChees:
    def get_pizza(self):
        return "Пицца 4 сыра\n\t- Вес: 1200 гр\n\t- Цена: 1300 р\n\t- Состав: Томатный соус, моцарелла, пармезан, сыр горгонзола, артишоки и орегано"

class PizzaKrudo:
    def get_pizza(self):
        return "Пицца Крудо\n\t- Вес: 700 гр\n\t- Цена: 800 р\n\t- Состав: Томатный соус, моцарелла и пармская ветчина"


# Суши
class SushiFactory:
    def __init__(self, class_factory = None):
        self.factory = class_factory()
    def show(self):
        self.factory.get_sushi()

class SushiDomino:
    def get_sushi(self):
        return "Суши Домино\n\t- Вес: 800 гр\n\t- Цена: 1500 р\n\t- Состав: рис, форель"

class SushiUramaki:
    def get_sushi(self):
        return "Суши Урамаки\n\t- Вес: 1000 гр\n\t- Цена: 2500 р\n\t- Состав: рис, угорь"

class SushiGunkanMaki:
    def get_sushi(self):
        return "Суши Гункан-маки\n\t- Вес: 700 гр\n\t- Цена: 1400 р\n\t- Состав: салат, икра"



# Роллы
class RollFactory:
    def __init__(self, class_factory = None):
        self.factory = class_factory()
    def show(self):
        self.factory.get_roll()

class RollBig:
    def get_roll(self):
        return "Роллы Big \n\t- Вес: 700 гр\n\t- Цена: 3000 р\n\t- Состав: рис, рыба"

class RollMedium:
    def get_shusi(self):
        return "Роллы Medium\n\t- Вес: 1200 гр\n\t- Цена: 980 р\n\t- Состав: рис, молюски"

class RollSmall:
    def get_shusi(self):
        return "Роллы Small\n\t- Вес: 1400 гр\n\t- Цена: 1900 р\n\t- Состав: рис, сыр, огурцы, колбаса"


# Билдер
class PZMilano:
    def __init__(self):
        self.sushi = None
        self.pizza = None
        self.roll = None

class PZMilano_Builder:
    def __init__(self):
        self.pzmilano = PZMilano()
        self.pzmilano.sushi = SushiFactory()
        self.pzmilano.pizza = PizzaFactory()
        self.pzmilano.roll = RollFactory()
    def set_sushi(self):
        self.pzmilano.sushi
