from math import pi

# Task1 (Окружность вписанная в квадрат)
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return pi*self.radius**2
# class Square:
#     def __init__(self, length):
#         self.length = length
#     def area(self):
#         return self.length**2
#
# class CircleinSquare(Circle, Square):
#     def __init__(self, radius):
#         Circle.__init__(self, radius=radius)
#         Square.__init__(self, length=radius*2**0.5)
#     def display_details(self):
#         print(f"Circle radius: {self.radius}")
#         print(f"Square length: {self.length}")
#     def total_area(self):
#         circle_area = Circle.area(self)
#         square_area = Square.area(self)
#         return circle_area, square_area
#
# obj = CircleinSquare(radius=2)
# obj.display_details()
# circle_area, square_area = obj.total_area()
# print(f"Total area of circle: {circle_area}")
# print(f"Total area of square: {square_area}")


# Task2 (Класс Автомобиль)
class Wheel:
    def __init__(self, radius):
        self.radius = radius
    def info_wheel(self):
        return f"Радиус колес {self.radius}"