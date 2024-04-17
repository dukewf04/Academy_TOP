from colorama import Fore, init
init(autoreset=False)
print(Fore.LIGHTCYAN_EX)

# Паттерны проектирования
# 1. Singleton (Создание только одного экземпляра класса)
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "instance"):
#             cls.instance = super(cls, Singleton).__new__(cls)
#
#         return cls.instance
#
#     def __init__(self, age):
#         self.age = age
#
# s = Singleton(20)
# print("Объект создан", s.age)
# s1 = Singleton(0)
# print("Объект создан", s1.age)
# print(s.age)


# Отложенный Singleton (Когда мы подключаем класс через импорт)
# class Singleton:
#     __instance = None
#     def __init__(self):
#         if not Singleton.__instance:
#             print("__init__ method called..")
#         else:
#             print("Instance already created:", self.getInstance())
#
#     @classmethod
#     def getInstance(cls):
#         if not cls.__instance:
#             cls.__instance = Singleton()
#         return cls.__instance
#
# s = Singleton()
# print("Object created:", Singleton.getInstance())
# s1 = Singleton()


# Моностатический Singleton ()
# class Borg:
#     __shared_state = {"1": "2"}
#     def __init__(self):
#         self.x = 1
#         self.__dict__ = self.__shared_state
#         pass
#
# b = Borg()
# b1 = Borg()
# b.x = 4
# print("Borg object 'b':", b)
# print("Borg object 'b1':", b1)
# print("Object state 'b':", b.__dict__)
# print("Object state 'b1':", b1.__dict__)


# Синглтоны и метаклассы
# Метаклассы - это классы, экземпляры которых являются классы
# class MyInt(type):
#     def __call__(cls, *args, **kwargs):
#         print("Here's my int", args)
#         print("")
#         return type.__call__(cls, *args, **kwargs)
#
# class int(metaclass=MyInt):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# i = int(4, 5)


# EXAMPLE
class HealthCheck:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck.__instance:
            HealthCheck.__instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck.__instance

    def __init__(self):
        self._servers = []
    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")
    def changeSever(self):
        self._servers.pop()
        self._servers.append("Server 5")

hc1 = HealthCheck()
hc2 = HealthCheck()
hc1.addServer()

print("Schedule health check for servers(1)..")
for i in range(4):
    print("Checking", hc1._servers[i])

hc2.changeSever()
print("Schedule health check for servers(2)..")
for i in range(4):
    print("Checking", hc2._servers[i])