# Работа с JSON
import json
from datetime import datetime

# data = {
#     "name": "Evgeny",
#     "age": 32,
#     "city": "Perm"
# }
#
# # Преобразование объекта Python в строку json
# #   - indent: параметр отступа в строке
# #   - sort_keys: сортировка ключей в json
# json_data = json.dumps(data, indent=4, sort_keys=True)
# print(json_data)
#
#
# # Преобразование строки в объект json
# json_data = '{"name": "Evgeny", "age": 32, "city": "Perm"}'
# data = json.loads(json_data)
# print(data, type(data))
#
#
# # Запись контейнера JSON в файл
# with open("json_data.json", "w") as file:
#     json.dump(data, file)
#
# with open("json_data.json", "r") as file:
#     data = json.load(file)
# print(data, type(data))


# Параметр default
# def datetime_serializer(x):
#     if isinstance(x, datetime):
#         return x.strftime("%d.%m.%Y %H:%M")
#
# data = {"name": "Evgeny", "age": 32, "city": "Perm", "birthday": datetime.now()}
# json_data = json.dumps(data, indent=4, default=datetime_serializer)
# print(json_data)


# Пользовательский класс
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class JSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, Person):
#             return {"name": person.name, "age": person.age}
#         return super().default(o)
#
# def person_to_dict(person):
#     return {"name": person.name, "age": person.age}
#
# person = Person("Евгений", 33)
# # person_json = json.dumps(person, default=person_to_dict)
# person_json = json.dumps(person, cls=JSONEncoder, ensure_ascii=False)
# print(person_json)


# Параметр skipkeys
class Person:
    pass

data = {(1, 2): "tuple_key", "normal_key": "value", Person: "Person class"}
print(json.dumps(data, skipkeys=True))