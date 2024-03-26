# Task1 (класс Человек)
# class Human:
#     def __init__(self):
#         self.fio = ''
#         self.date = ''
#         self.__tel = ''
#         self.city = ''
#         self.home = ''
#         self.country = ''
#
#     def getTel(self):
#         return self.__tel
#
#     def setTel(self, a):
#         self.__tel = a
#
#     def inputINFO(self):
#         self.fio = input("Введите ФИО> ")
#         self.date = input("Введите дату рождения> ")
#         self.__tel = input("Введите конт. телефон> ")
#         self.city = input("Введите город> ")
#         self.home = input("Введите домашний адрес> ")
#         self.country = input("Введите страну> ")
#
#     def __str__(self):
#         return (f"\nДанные человека:\n"
#                 f"{self.fio}\n"
#                 f"{self.city}\n"
#                 f"{self.home}\n"
#                 f"{self.__tel}\n"
#                 f"{self.date}\n"
#                 f"{self.country}")

# Task2 (класс Город)
# class City:
#     def __init__(self):
#         self.city_name = ''
#         self.region_name = ''
#         self.country_name = ''
#         self.__count_people = ''
#         self.post_index = ''
#         self.tel_code = ''
#
#     def get_count_people(self):
#         return self.__count_people
#
#     def set_count_people(self, count):
#         self.__count_people = count
#
#     def inputINFO(self):
#         self.city_name = input("Введите название города> ")
#         self.region_name = input("Введите название региона> ")
#         self.country_name = input("Введите название страны> ")
#         self.__count_people = input("Введите голичество жителей> ")
#         self.post_index = input("Введите почтовый индекс> ")
#         self.tel_code = input("Введите телефонный код города> ")
#
#     def __str__(self):
#         return (f"\nИнформация о городе:\n"
#                 f"{self.city_name}\n"
#                 f"{self.region_name}\n"
#                 f"{self.country_name}\n"
#                 f"{self.__count_people}\n"
#                 f"{self.post_index}\n"
#                 f"{self.tel_code}")


# Task3 (класс Country)
# class Country:
#     def __init__(self):
#         self.country_name = ''
#         self.continent_name = ''
#         self.count_people = ''
#         self.tel_code = ''
#         self.capital_name = ''
#         self.__cities = []
#
#     def get_cities(self):
#         return self.__cities
#
#     def set_cities(self, cities_list: list):
#         self.__cities = cities_list
#
#     def inputINFO(self):
#         self.country_name = input("Введите название страны> ")
#         self.continent_name = input("Введите название континента> ")
#         self.__count_people = input("Введите количество жителей страны> ")
#         self.tel_code = input("Введите телефонный код страны> ")
#         self.capital_name = input("Введите название столицы> ")
#         self.__cities = input("Введите названия городов страны (через пробел).> ").strip().split()
#
#     def __str__(self):
#         return (f"\nИнформация о стране:\n"
#                 f"{self.country_name}\n"
#                 f"{self.continent_name}\n"
#                 f"{self.__count_people}\n"
#                 f"{self.tel_code}\n"
#                 f"{self.capital_name}\n"
#                 f"{self.__cities}")


# Task4 (класс Fraction)
# class Fraction:
#     def __init__(self):
#         self.numirator = 0.0
#         self.denominator = 1.0
#
#     def get_numirator(self):
#         return self.numirator
#
#     def get_denominator(self):
#         return self.denominator
#
#     def sum(self, var: float):
#         return var + self.numirator/self.denominator
#
#     def minus(self, var: float):
#         return var - self.numirator/self.denominator
#
#     def multi(self, var: float):
#         return var * self.numirator/self.denominator
#
#     def division(self, var: float):
#         return var / self.numirator/self.denominator
#
#     def input_data(self):
#         self.numirator = float(input("Введите числитель> "))
#         d = float(input("Введите знаменатель> "))
#         if d == 0:
#             print("Знаменатель не может быть равным 0!")
#         else:
#             self.denominator = d
#
#     def __str__(self):
#         return f"Числитель: {self.numirator}, знаменатель: {self.denominator}"