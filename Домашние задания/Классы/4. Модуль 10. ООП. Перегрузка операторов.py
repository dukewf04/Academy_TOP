# Task1
from math import pi

# class Circle:
#     __slots__ = ["radius"]
#     def __init__(self, radius):
#         self.radius = radius
#     def __eq__(self, other):
#         return True if self.radius == other.square else False
#     def __gt__(self, other):
#         c1 = pi*2*self.radius
#         c2 = pi*2*other.radius
#         if c1 > c2:
#             return f"Длина первой окружности [{c1}] больше длины второй окружности [{c2}]"
#         elif c1 < c2:
#             return f"Длина второй окружности [{c2}] больше длины первой окружности [{c1}]"
#         else:
#             return f"Длины окружностей равны [{c1}]"
#     def __add__(self, other):
#         self.radius += other
#         return self
#     def __sub__(self, other):
#         self.radius -= other
#         return self
#     def __iadd__(self, other):
#         self.radius += other
#         return self
#     def __isub__(self, other):
#         self.radius -= other
#         return self
#
# circle1 = Circle(radius=5)
# circle2 = Circle(radius=7)
#
# circle1 += 5
# circle2 = circle2 - 1
# print(f"Радиус первой окружности: {circle1.radius}")
# print(f"Радиус второй окружности: {circle2.radius}")
#
# print(circle1 > circle2)


# Task2
# class Complex:
#     """
#     Операции над комплексными числами
#     z = a + b*i
#     """
#     __slots__ = ["a", "b"]
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __getComplexNumber(self, a, b):
#         real = str(a) if a != 0 else ''
#         if b < 0:
#             image = f"{b}i"
#         elif b > 0:
#             image = f"+{b}i"
#         else:
#             image = ''
#         result = real + image
#
#         return result if len(result) > 0 else '0'
#     def __add__(self, other):
#         real = self.a + other.a
#         image = self.b + other.b
#
#         return self.__getComplexNumber(real, image)
#
#     def __sub__(self, other):
#         real = self.a - other.a
#         image = self.b - other.b
#
#         return self.__getComplexNumber(real, image)
#
#     def __mul__(self, other):
#         real = self.a*other.a - self.b*other.b
#         image = self.a*other.b + self.b*other.a
#
#         return self.__getComplexNumber(real, image)
#     def __truediv__(self, other):
#         real = (self.a*other.a + self.b*other.b)/(other.a**2 + other.b**2)
#         image = (self.b*other.a - self.a*other.b)/(other.a**2 + other.b**2)
#
#         return self.__getComplexNumber(real, image)
#
#
# z1 = Complex(a=2, b=3)
# z2 = Complex(a=-5, b=-7)
#
# print(f"z1+z2 = {z1 + z2}")
# print(f"z1-z2 = {z1 - z2}")
# print(f"z1*z2 = {z1 * z2}")
# print(f"z1/z2 = {z1 / z2}")


# Task3
# class Airplane:
#     def __init__(self, airtype, maxpassengers):
#         self.airtype = airtype
#         self.maxpassengers = maxpassengers
#         self.currentPassengers = 0
#
#     def __eq__(self, other):
#         return "Самолеты доного типа" if self.airtype == other.airtype else "Самолеты разных типов"
#     def __add__(self, other):
#         self.currentPassengers += other
#         return self
#     def __sub__(self, other):
#         self.currentPassengers -= other
#         return self
#     def __iadd__(self, other):
#         self.currentPassengers += other
#         return self
#     def __isub__(self, other):
#         self.currentPassengers -= other
#         return self
#     def __gt__(self, other):
#         if self.maxpassengers > other.maxpassengers:
#             return (f"У самолета {self.airtype} вместимость пассажиров больше чем у {other.airtype}")
#         elif self.maxpassengers < other.maxpassengers:
#             return (f"У самолета {other.airtype} вместимость пассажиров больше чем у {self.airtype}")
#         else:
#             return ("Вместимость у обоих самолетов одинаковая")
#
# air1 = Airplane(airtype="Boeing 747", maxpassengers=524)
# air2 = Airplane(airtype="Airbus A350", maxpassengers=440)
# print(air1 == air2)
#
# air1 = air1 + 5
# print(f"Количество пассажиров в самолете {air1.airtype} -", air1.currentPassengers)
# air2 += 12
# print(f"Количество пассажиров в самолете {air2.airtype} -", air2.currentPassengers)
#
# print(air1 > air2)


# Task4
# class Flat:
#     def __init__(self, square, price):
#         self.square = square
#         self.price = price
#     def __eq__(self, other):
#         return True if self.square == other.square else False
#     def __ne__(self, other):
#         return True if self.square != other.square else False
#     def __gt__(self, other):
#         if self.price > other.price:
#             return "Первая квартира дороже второй"
#         elif self.price < other.price:
#             return "Вторая квартира дороже первой"
#         else:
#             return "У квартир цена одинаковая"
#
# flat1 = Flat(square=75, price=3000000)
# flat2 = Flat(square=84, price=4000000)
#
# print(flat1 == flat2)
# print(flat1 > flat2)