import json
# Метод абстрактной фабрики
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



# Паттерн строитель(Builder)
class Phone:
    def __init__(self):
        self.os = None
        self.camera = None
        self.battery = None
        self.screen = None

    def __str__(self):
        return json.dumps(self.__dict__, indent=3)

class Phone_Builder:
    def __init__(self):
        self.phone = Phone()
    def set_os(self, os):
        self.phone.os = os
        return self
    def set_camera(self, camera):
        self.phone.camera = camera
        return self
    def set_battery(self, battery):
        self.phone.battery = battery
        return self
    def set_screen(self, screen):
        self.phone.screen = screen
        return self
    def get_phone(self):
        return self.phone

builder = Phone_Builder()
phone = (builder
         .set_os("Android")
         .set_camera("50 MP")
         .set_battery("6000 mA")
         .set_screen("7.7i")
         .get_phone()
         )

print(phone)