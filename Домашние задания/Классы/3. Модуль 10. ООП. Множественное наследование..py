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
# class Wheel:
#     def __init__(self, wheel_radius):
#         self.wheel_radius = wheel_radius
#     def info_wheel(self):
#         return f"Радиус колес {self.wheel_radius}"
#
# class Engine:
#     def __init__(self, engincapacity):
#         self.engincapacity = engincapacity
#     def info_engine(self):
#         return f"Объем двигателя {self.engincapacity}"
#
# class Door:
#     def __init__(self, doors_count):
#         self.doors_count = doors_count
#     def info_door(self):
#         return f"Количество дверей {self.doors_count}"
#
# class Car(Wheel, Engine, Door):
#     def __init__(self, namemodel, manufactorer, wheel_radius, engincapacity, doors_count):
#         Wheel.__init__(self, wheel_radius=wheel_radius)
#         Engine.__init__(self, engincapacity=engincapacity)
#         Door.__init__(self, doors_count=doors_count)
#         self.namemodel = namemodel
#         self.manufactorer = manufactorer
#
#     def info_car(self):
#         print(f"Название модели: {self.namemodel}\n"
#               f"Производитель: {self.manufactorer}\n"
#               f"Радиус колес: {Wheel.info_wheel(self)} дюймов\n"
#               f"Объем двигателя: {Engine.info_engine(self)}\n"
#               f"Количество дверей: {Door.info_door(self)}")
#
# auto = Car(namemodel="Lada largus",
#            manufactorer="Lada",
#            wheel_radius="15",
#            engincapacity="1.6",
#            doors_count="5")
# auto.info_car()


# Task3 (Домашнее животное)
# class HomePet:
#     def __init__(self, name):
#         self.name = name
#     def Sound(self):
#         print("Звук животного")
#     def Show(self):
#         print(f"Кличка животного '{self.name}'")
#     def Type(self):
#         print(f"Подвид")
#
# class Dog(HomePet):
#     def __init__(self, name):
#         super().__init__(name=name)
#     def Sound(self):
#         print("Bark-Bark!")
#     def Show(self):
#         print(f"Кличка животного '{self.name}'")
#     def Type(self):
#         print(f"Собака домашняя")
#
# class Cat(HomePet):
#     def __init__(self, name):
#         super().__init__(name=name)
#     def Sound(self):
#         print("Meow-Meow!")
#     def Show(self):
#         print(f"Кличка животного '{self.name}'")
#     def Type(self):
#         print(f"Лесная кошка")
#
# class Parrot(HomePet):
#     def __init__(self, name):
#         super().__init__(name=name)
#     def Sound(self):
#         print("Squawk-Squawk!")
#     def Show(self):
#         print(f"Кличка животного '{self.name}'")
#     def Type(self):
#         print(f"Голубой ара")
#
# class Hamster(HomePet):
#     def __init__(self, name):
#         super().__init__(name=name)
#     def Sound(self):
#         print("Khrou-Khrou!")
#     def Show(self):
#         print(f"Кличка животного '{self.name}'")
#     def Type(self):
#         print(f"Джунгарский хомяк")
#
# my_dog = Dog(name="Барсик")
# my_cat = Cat(name="Феликс")
# my_parrot = Parrot(name="Дракоша")
# my_hamster = Hamster(name="Гигацентавр")
# for el in (my_dog, my_cat, my_parrot, my_hamster):
#     el.Show()
#     el.Sound()
#     el.Type()
#     print('*'*11)


# Task4 (сласс Employer)
# class Employer:
#     def Print(self):
#         print("This is Employer class")
#
# class President(Employer):
#     def Print(self):
#         print("The main person in the country")
#
# class Manager(Employer):
#     def Print(self):
#         print("A person who sit in a ofice")
#
# class Worker(Employer):
#     def Print(self):
#         print("A person who work hard every day")


# Task5 (сласс Employer с магическим методом str)
# class Employer:
#     def __init__(self, age):
#         self.age = age
#     def __str__(self):
#         return "This is Employer class"
#     def int(self):
#         print(f"Возраст служащего {self.age}")
#
# class President(Employer):
#     def __init__(self, age):
#         super().__init__(age=age)
#     def __str__(self):
#         return "The main person in the country"
#
# class Manager(Employer):
#     def __init__(self, age):
#         super().__init__(age=age)
#     def __str__(self):
#         return "A person who sit in a ofice"
#
# class Worker(Employer):
#     def __init__(self, age):
#         super().__init__(age=age)
#     def __str__(self):
#         return "A person who work hard every day"
#
# p = President(age=60)
# m = Manager(age=30)
# w = Worker(age=25)
# for el in (p, m, w):
#     print(el)
#     el.int()
#     print('*'*11)