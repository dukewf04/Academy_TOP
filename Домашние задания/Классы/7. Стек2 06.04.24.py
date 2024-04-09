# Task 1 (список для работы с числами)
# class MyList:
#     def __init__(self, lst: list):
#         self.mylist = lst
#     def addElement(self, num):
#         if num in self.mylist:
#             print("Такое число уже есть в списке!")
#         else:
#             self.mylist.append(num)
#         print(self.mylist)
#     def delElement(self, num):
#         while num in self.mylist:
#             self.mylist.remove(num)
#         print(self.mylist)
#     def showList(self, reversed: int = 1):
#         # Протестировать, так как список может сохранить свое состояние после reverse
#         if reversed == 1:
#             print(self.mylist)
#         else:
#             for i in range(len(self.mylist)):
#                 print(self.mylist[-(i+1)], end=" ")
#             print()
#     def isElement(self, num):
#         if num in self.mylist:
#             print(f"Элемент {num} есть в списке")
#         else:
#             print(f"Элемента {num} нет в списке")
#     def replaceElement(self, old, new, all: int = 1):
#         for i in range(len(self.mylist)):
#             if self.mylist[i] == old:
#                 self.mylist[i] = new
#                 if all == 1: break
#         print(self.mylist)
#
# lst = list(map(int, input("Введите список чисел через пробел> ").strip().split()))
# lst = MyList(lst)
#
# while True:
#     print("[1] Добавить новое число в список")
#     print("[2] Удалить все вхождения числа из списка")
#     print("[3] Показать содержимое списка")
#     print("[4] Проверить есть ли значение в списке")
#     print("[5] Заменить значение в списке")
#     print("[0] Выход")
#
#     choise = int(input("> ").strip())
#     if choise == 0: break
#
#     if choise == 1:
#         num = int(input("Введите новое число> "))
#         lst.addElement(num)
#     elif choise == 2:
#         num = int(input("Введите число> "))
#         lst.delElement(num)
#     elif choise == 3:
#         r = int(input("1 - c начала, 2 - с конца списка> "))
#         lst.showList(reversed=r)
#     elif choise == 4:
#         num = int(input("Введите число> "))
#         lst.isElement(num)
#     elif choise == 5:
#         old = int(input("Введите заменяемое число> "))
#         new = int(input("Введите новое число> "))
#         b = int(input("1 - Заменить только первое вхождение, 2 - Заменить все вхождения> "))
#         lst.replaceElement(old=old, new=new, all=b)
#     print("*"*30)


# Task 2 (класс стека для работы со строками)
# class StringStack:
#     def __init__(self, maxsize: int = 20):
#         self.__stack = []
#         self.__maxsize = maxsize
#     def push(self, var):
#         if len(self.__stack) < self.__maxsize:
#             self.__stack.append(var)
#     def pop(self):
#         if len(self.__stack) > 0:
#             return self.__stack.pop()
#     def count(self):
#         return len(self.__stack)
#     def isEmpty(self):
#         return len(self.__stack) == 0
#     def isFull(self):
#         return len(self.__stack) == self.__maxsize
#     def clear(self):
#         self.__stack = []
#     def getLastItem(self):
#         return self.__stack[-1] if len(self.__stack) > 0 else None
#     def getStack(self):
#         return self.__stack
#
# stack = StringStack(maxsize=10)
#
# while True:
#     print("[1] помещение строки в стек")
#     print("[2] выталкивание строки из стека")
#     print("[3] подсчет количества строк в стеке")
#     print("[4] проверка пустой ли стек")
#     print("[5] проверка полный ли стек")
#     print("[6] очистка стека")
#     print("[7] получение значения без выталкивания верхней строки из стека")
#     print("[8] вывести стек на экран")
#     print("[0] выход")
#
#     choise = int(input("> ").strip())
#     if choise == 0: break
#
#     if choise == 1:
#         stack.push(input("Введите строку> "))
#         print(stack.getStack())
#     elif choise == 2:
#         stack.pop()
#     elif choise == 3:
#         print(f"Количество элементов в стеке {stack.count()}")
#     elif choise == 4:
#         print("Стек пустой") if stack.isEmpty() else print("Стек не пустой")
#     elif choise == 5:
#         print("Стек полный") if stack.isFull() else print("Стек не заполнен")
#     elif choise == 6:
#         stack.clear()
#         print("Стек очищен")
#     elif choise == 7:
#         print(stack.getLastItem())
#     elif choise == 8:
#         print(stack.getStack())
#     print("*"*30)


# Task 3 (Неограниченный стек)
# Реализация такая же, как в Task 2, только в конструкторе класса StringStack мы убираем параметр maxsize