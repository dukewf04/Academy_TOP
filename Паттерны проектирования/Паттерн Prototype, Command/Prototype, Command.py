# Творческий шаблон проектирования
# Цель - сократить количество классов для приложения.
# from abc import ABCMeta, abstractmethod
# import copy
# class Courses_PJR(metaclass=ABCMeta):
#     def __init__(self):
#         self.id = None
#         self.type = None
#     @abstractmethod
#     def cource(self):
#         pass
#     def get_type(self):
#         return self.type
#     def get_id(self):
#         return self.id
#     def set_id(self, id):
#         self.id = id
#     def clone(self):
#         return copy.copy(self)
#
# class Python(Courses_PJR):
#     def __init__(self):
#         super().__init__()
#         self.type = "Python"
#     def cource(self):
#         print("Cource python method")
# class Java(Courses_PJR):
#     def __init__(self):
#         super().__init__()
#         self.type = "Java"
#     def cource(self):
#         print("Cource java method")
#
# class R(Courses_PJR):
#     def __init__(self):
#         super().__init__()
#         self.type = "R"
#     def cource(self):
#         print("Cource R method")
#
# # Класс кэш
# class Courses_cache:
#     cache = {}
#
#     @staticmethod
#     def get_course(sid):
#         COURSE = Courses_cache.cache.get(sid, None)
#         return COURSE.clone()
#
#     @staticmethod
#     def load():
#         python = Python()
#         python.set_id("1")
#         Courses_cache.cache[python.get_id()] = python
#
#         java = Java()
#         java.set_id("2")
#         Courses_cache.cache[java.get_id()] = java
#
#         r = R()
#         r.set_id("3")
#         Courses_cache.cache[r.get_id()] = r
#
#
# if __name__ == "__main__":
#     Courses_cache.load()
#
#     python_course = Courses_cache.get_course("1")
#     print(python_course.get_type())
#
#     java_course = Courses_cache.get_course("2")
#     print(java_course.get_type())
#
#     r_course = Courses_cache.get_course("3")
#     print(r_course.get_type())

# Абстрактные методы (@)
# import abc
# class Shape(abc.ABC):
#     @abc.abstractmethod
#     def area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def area(self):
#         return self.w * self.h
#
# rect = Rectangle(5, 6)
# print(rect.area())

# @staticmethod - используется для создания метода, который ничего не знает о классе или экземпляре, через который он был вызван.
# Он может передавать и получать аргументы, без неявного определения через наследование.
# По-человечески: обычный метод внутри класса, который может быть вызван без создания объекта класса.


# Паттерн Command
from sys import stdout as console

# Обработка команды exit
class SessionClosed(Exception):
    def __init__(self, value):
        self.value = value

# Интерфейс команды
class Command:
    def execute(self):
        raise NotImplementedError()
    def cancel(self):
        raise NotImplementedError()
    def name(self):
        raise NotImplementedError()

# Команда rm
class RmCommand(Command):
    def execute(self):
        console.write("you are executed \"rm \" command \n")
    def canesl(self):
        console.write("you are executed \"rm \" command \n")
    def name(self):
        return "rm"

# Команда uptime
class UpTimeCommand(Command):
    def execute(self):
        console.write("you are executed \"rm \" command \n")
    def canesl(self):
        console.write("you are executed \"rm \" command \n")
    def name(self):
        return "uptime"

# Команда undo
class UndoCommand(Command):
    def execute(self):
        try:
            cmd = HISTORY.pop()
            TRASH.append(cmd)
            console.write("Undo command \" [0] \" \n".format(cmd.name()))
            cmd.cancel()
        except IndexError:
            console.write("ERROR: HISTORY is empty \n")
    def name(self):
        return "undo"

# Команда redo
class RedoCommand(Command):
    def execute(self):
        try:
            cmd = HISTORY.pop()
            TRASH.append(cmd)
            console.write("Redo command \" [0] \" \n".format(cmd.name()))
            cmd.cancel()
        except IndexError:
            console.write("ERROR: HISTORY is empty \n")
    def name(self):
        return "undo"

# Команда History
class HistoryCommand(Command):
    def execute(self):
        i = 0
        for cmd in HISTORY:
            console.write("[0]: [1]\n".format(i, cmd.name()))
            i += 1
    def name(self):
        print("History")

# Команда exit
class ExitCommand(Command):
    def execute(self):
        raise SessionClosed("Goodbye!")

    def name(self):
        return "exit"

COMMANDS = {"rm": RmCommand(), "uptime": UpTimeCommand(), "undo": UndoCommand(), "redo": RedoCommand(), "history": HistoryCommand(), "exit": ExitCommand()}
HISTORY = list()
TRASH = list()

def main():
    try:
        while True:
            console.flush()
            console.write("pysh >> ")
            cmd = input()
            try:
                command = COMMANDS[cmd]
                command.execute()
                if not isinstance(command, UndoCommand) and not isinstance(command, RedoCommand) and not isinstance(command, HistoryCommand):
                    TRASH = list()
                    HISTORY.append(command)
            except KeyError:
                console.write("ERROR: HISTORY is empty \n")
    except SessionClosed as e:
        console.write(e.value)

if __name__ == "__main__":
    main()