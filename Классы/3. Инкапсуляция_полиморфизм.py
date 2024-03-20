# public: по дефолту
# protected: _
# private: __
from math import pi


# class Phone:
#     number = "99-898-888"
#     username = "Evgeny"
#     __how_many_times_turned_on = 0  # private
#     _a = 5
#     def __init__(self):
#         pass
#     def print_number(self):
#         print("Phone number:", self.number)
#     def call(self):
#         print("Ring-Ring!")
#     def __turn_on(self):
#         self.__how_many_times_turned_on += 1
#         print("Times was turned on:", self.__how_many_times_turned_on)
#     def f(self, a: int):
#         print(a)
#     def f(self, a: int, b: str):
#         print(a, b)
#
# class Phone2(Phone):
#     def __init__(self):
#         Phone.__init__(self)
#         pass
#     def call(self):
#         print(self._a)
#
#
#
# # ****************** Полиморфизм **********************
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I'm {self.age} years old.")
#     def make_sound(self):
#         print("Meow")
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"I am a dog. My name is {self.name}. I'm {self.age} years old.")
#     def make_sound(self):
#         print("Bark")
#
# cat1 = Cat(name="Kitty", age=2.5)
# dog1 = Dog(name="Fluffy", age=3.5)
# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()
#     print()

# Example
# Перегрузка методов - создание методов с одним и тем-же именем, но с разными типами аргументов (количеством аргументов). Python не поддерживает  перегрузку методов.
# ПОЛИМОРФИЗМ - передача параметров и методов класса другого значения тела функции, что и в родительском классе.
# Для того, чтобы

class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass
    def fact(self):
        return "I am two-demensional shape"
    def __str__(self):
        return self.name

class Square(Shape):
    def __init__(self, lenght):
        super().__init__(name="Square")  # Обращение к классу-родителю
        self.lenght = lenght
    def area(self):
        return self.lenght**2
    def fact(self):
        return "Squares have each angle equal 90 degrees"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(name="Circle")  # Обращение к классу-родителю
        self.radius = radius
    def area(self):
        return pi*self.radius**2


s = Square(lenght=6)
c = Circle(radius=2)
print(c)
print(c.fact())
print(s.fact())
print(c.area())
