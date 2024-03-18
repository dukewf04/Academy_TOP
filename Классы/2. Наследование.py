# Наследование
# class Super:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"My name is {self.name}"
#
# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)
#
# obj = Sub("Evgeny")
# print(obj)

# Пример 3х уровнего наследования
# class Level1:
#     varia1 = 100
#     def __init__(self):
#         self.var1 = 101
#     def fun1(self):
#         return 102
#
#
# class Level2(Level1):
#     varia2 = 200
#     def __init__(self):
#         Level1.__init__(self)
#         self.var2 = 201
#     def fun2(self):
#         return 202
#
# class Level3(Level2):
#     varia3 = 300
#
#     def __init__(self):
#         Level2.__init__(self)
#         self.var3 = 301
#
#     def fun3(self):
#         return 302
#
# obj = Level3()
# print(obj.varia1, obj.var1, obj.fun1())
# print(obj.varia2, obj.var2, obj.fun2())
# print(obj.varia3, obj.var3, obj.fun3())


# Множественное наследование
# class SuperA:
#     varA = 10
#     def funA(self):
#         return 11
#
# class SuperB:
#     varB = 20
#     def funB(self):
#         return 21
#
# class Sub(SuperA, SuperB):
#     pass
#
# obj = Sub()
# print(obj.varA, obj.funA())
# print(obj.varB, obj.funB())

# Одинаковые атрибуты и функции у классов-родителей
# class Left:
#     var = "L"
#     varLeft = "LL"
#     def fun(self):
#         return "Left"
#
# class Right:
#     var = "R"
#     varRight = "RR"
#     def fun(self):
#         return "Right"
#
# class Sub(Left, Right):
#     pass
#
# obj = Sub()
# print(obj.var, obj.varLeft, obj.varRight, obj.fun())


# Иерархия классов
class One:
    def doit(self):
        print("doit from One")
    def doanything(self):
        self.doit()
    def f(self):
        print("****Test One****")

class Two(One):
    def doit(self):
        print("doit from Two")
    def f(self):
        print("****Test Two****")

one = One()
two = Two()
one.doanything()
two.doanything()
two.f()