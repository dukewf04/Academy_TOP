import pickle, json
# Task 1, 2 (Класс Самолет. Упаковка/распаковка с помощью библиотек pickle и json)
# class Plane:
#     def __init__(self, model, manufacturer, capacity, max_speed):
#         self.data = {
#             "model": model,
#             "manufacturer": manufacturer,
#             "capacity": capacity,
#             "max_speed": max_speed
#         }
#         self.current_speed = 0
#
#     def accelerate(self, speed):
#         if speed <= self.data["max_speed"]:
#             self.current_speed = speed
#             print(f"The plane is now flying at {self.current_speed} km/h.")
#         else:
#             print("The speed exceeds the maximum speed of the plane.")
#
#     def take_off(self):
#         print(f"The plane {self.data['model']} is taking off.")
#
#     def land(self):
#         print(f"The plane {self.data['model']} is landing.")
#
#     def serialize_pickle(self):
#         """Сохраняем данные об самолете в файл с помощью модуля pickle"""
#         with open("Plane_pickle.txt", "wb") as file:
#             pickle.dump(self.data, file)
#         serialized_data = pickle.dumps(self.data)
#         print("Упакованные данные:\n", serialized_data)
#
#     def deserialize_pickle(self):
#         """Распаковываем данные об самолете из файла с помощью модуля pickle"""
#         with open("Plane_pickle.txt", "rb") as file:
#             deserialized_data = pickle.load(file)
#
#         print("Распакованные данные:\n", deserialized_data)
#
#     def serialize_json(self):
#         """Сохраняем данные об самолете в файл с помощью модуля json"""
#         with open("Plane_json.json", "w", encoding="utf-8") as file:
#             json.dump(self.data, file, indent=3)
#         serialized_data = json.dumps(self.data, indent=3, ensure_ascii=False)
#         print("Упакованные данные:\n", serialized_data)
#
#     def deserialize_json(self):
#         """Распаковываем данные об самолете из файла с помощью модуля json"""
#         with open("Plane_json.json", "r") as file:
#             deserialized_data = json.load(file)
#
#         print("Распакованные данные:\n", json.dumps(deserialized_data, indent=3, ensure_ascii=False))
#
# plane = Plane(
#     model="Boeing 747",
#     manufacturer="Boeing",
#     capacity="416-524 passengers",
#     max_speed="570 mph"
# )
#
# print("*******  С использованием модуля pickle ******* ")
# plane.serialize_pickle()
# plane.deserialize_pickle()
#
# print("\n\n******* С использованием модуля json ******* ")
# plane.serialize_json()
# plane.deserialize_json()



# Task 3 (класс Fraction)
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
#
#     def serialize_pickle(self):
#         """Сохраняем данные в файл с помощью модуля pickle"""
#         with open("Fraction_pickle.txt", "wb") as file:
#             pickle.dump(self, file)
#         serialized_data = pickle.dumps(self)
#         print("Упакованные данные:\n", serialized_data)
#
#     def deserialize_pickle(self):
#         """Распаковываем данные из файла с помощью модуля pickle"""
#         with open("Fraction_pickle.txt", "rb") as file:
#             deserialized_data = pickle.load(file)
#
#         print("Распакованные данные:\n", deserialized_data)
#
#     def serialize_json(self):
#         """Сохраняем данные в файл с помощью модуля json"""
#         data = {
#             "numirator": self.numirator,
#             "denominator": self.denominator
#         }
#         with open("Fraction_json.json", "w", encoding="utf-8") as file:
#             json.dump(data, file, indent=3)
#         serialized_data = json.dumps(data, indent=3, ensure_ascii=False)
#         print("Упакованные данные:\n", serialized_data)
#
#     def deserialize_json(self):
#         """Распаковываем данные из файла с помощью модуля json"""
#         with open("Fraction_json.json", "r") as file:
#             deserialized_data = json.load(file)
#
#         print("Распакованные данные:\n", json.dumps(deserialized_data, indent=3, ensure_ascii=False))
#
# fr = Fraction()
# fr.input_data()
#
# print("*******  С использованием модуля pickle ******* ")
# fr.serialize_pickle()
# fr.deserialize_pickle()
#
# print("\n\n******* С использованием модуля json ******* ")
# fr.serialize_json()
# fr.deserialize_json()



# Task 4 (Класс часы ...)
# Это 3 по счету однотипное задание. Описываем класс, применяем те же самые методы, что и выше, ни каких изменений не будет.
# Такое ощущение, что некоторые задания добавлены просто копипастом, чтобы были...