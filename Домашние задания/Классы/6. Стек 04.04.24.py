# Task 1 (Односвязный список)
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def addElement(self, other):
#         if not isinstance(other, Node): return
#         if self.head == None:
#             self.head = other
#         else:
#             temp: Node = self.head
#             while temp.next != None:
#                 temp = temp.next
#             temp.next = other
#
#     def delElement(self, num):
#         """Удаление элемента из списка"""
#         temp: Node = self.head
#         if temp.data == num:
#             self.head = temp.next
#         else:
#             prev = None
#             while temp and temp.data != num:
#                 prev = temp
#                 temp = temp.next
#             if temp is None:
#                 return
#             prev.next = temp.next
#     def printList(self):
#         """Вывод всех элементов"""
#         temp: Node = self.head
#         while temp:
#             print(temp.data)
#             temp = temp.next
#
#     def isElement(self, st):
#         """Проверка существования элемента в списке"""
#         temp: Node = self.head
#         while temp:
#             if temp.data == st:
#                 return True
#             temp = temp.next
#
#         return False
#
#     def replaceElement(self, old, new):
#         """Замена элемента в списке"""
#         temp: Node = self.head
#         while temp:
#             if temp.data == old:
#                 temp.data = new
#             temp = temp.next
#
# list = LinkedList()
# for i in range(3):
#     list.addElement(Node(data=int(input(f"Введите [{i+1} из 3] число> "))))
#
# while True:
#     print("[1] Добавить элемент в список")
#     print("[2] Удалить элемент из списка")
#     print("[3] Показать содержимое списка")
#     print("[4] Проверить есть ли значение в списке")
#     print("[5] Заменить значение в списке")
#     print("[0] Выход")
#
#     choise = int(input("> ").strip())
#     if choise == 0: break
#
#     if choise == 1:
#         list.addElement(Node(data=int(input("Введите число> "))))
#     elif choise == 2:
#         list.printList()
#         number = int(input("Введите число, которое надо удалить> "))
#         list.delElement(number)
#     elif choise == 3:
#         list.printList()
#     elif choise == 4:
#         number = int(input("Введите число> "))
#         print("Это число есть в списке") if list.isElement(number) else print("Числа нет в списке")
#     elif choise == 5:
#         old = int(input("Введите число, которое нужно заменить> "))
#         if list.isElement(old):
#             list.replaceElement(old, new=int(input("Введите новое число> ")))
#         else:
#             print("Ошибка, такого числа в списке нет")
#     print("*"*30)

# Task 2 (Двусвязный список)
# class Node:
#     def __init__(self, data: str):
#         self.data = data
#         self.next = None
#         self.prev = None
#
# class DubleLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def __lt__(self, other: Node):
#         """Перегружаем оператор < Чтобы по "красивому" заносить эелементы в двусвязный список ))"""
#         if isinstance(other, Node):
#             if self.head == None:
#                 self.head = other
#             else:
#                 temp: Node = self.head
#                 while temp.next != None:
#                     temp = temp.next
#                 temp.next = other
#                 temp.next.prev = temp
#
#     def delElement(self, st):
#         """Удаление элемента из списка"""
#         temp: Node = self.head
#         while temp:
#             if temp.data == st:
#                 if temp.prev:
#                     temp.prev.next = temp.next
#                 if temp.next:
#                     temp.next.prev = temp.prev
#                 if temp == self.head:
#                     self.head = temp.next
#                 del temp
#                 break
#             temp = temp.next
#     def printList(self):
#         """Вывод всех элементов"""
#         result = []
#         count = 1
#         temp: Node = self.head
#         while temp:
#             print(count, temp.data)
#             result.append(temp.data)
#             temp = temp.next
#             count += 1
#         return result
#
#     def isElement(self, st):
#         """Проверка существования элемента в списке"""
#         temp: Node = self.head
#         while temp:
#             if temp.data == st:
#                 return True
#             temp = temp.next
#
#         return False
#
#     def replaceElement(self, old, new):
#         """Замена элемента в списке"""
#         temp: Node = self.head
#         while temp:
#             if temp.data == old:
#                 temp.data = new
#             temp = temp.next
#
#
# list = DubleLinkedList()
# for i in range(3):
#     list < Node(data=input(f"Введите [{i+1} из 3] строку> "))
#
# while True:
#     print("[1] Добавить элемент в список")
#     print("[2] Удалить элемент из списка")
#     print("[3] Показать содержимое списка")
#     print("[4] Проверить есть ли значение в списке")
#     print("[5] Заменить значение в списке")
#     print("[0] Выход")
#
#     choise = int(input("> ").strip())
#     if choise == 0: break
#
#     if choise == 1:
#         list < Node(data=input("Введите строку> "))
#     elif choise == 2:
#         str_list = list.printList()
#         str_index = int(input("Введите номер строки, которую надо удалить> "))
#         list.delElement(str_list[str_index-1])
#     elif choise == 3:
#         list.printList()
#     elif choise == 4:
#         st = input("Введите строку> ")
#         print("Строка есть в списке") if list.isElement(st) else print("Строки нет в списке")
#     elif choise == 5:
#         old = input("Введите строку, которую нужно заменить> ")
#         if list.isElement(old):
#             list.replaceElement(old, new=input("Введите новую строку> "))
#         else:
#             print("Ошибка, такой строки в списке нет")
#     print("*"*30)


# Task 3 (Ограниченный стек)
# class Stack:
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
# stack = Stack(maxsize=3)
#
# while True:
#     print("[1] помещение целого значения в стек")
#     print("[2] выталкивание целого значения из стека")
#     print("[3] подсчет количества целых в стеке")
#     print("[4] проверка пустой ли стек")
#     print("[5] проверка полный ли стек")
#     print("[6] очистка стека")
#     print("[7] получение значения без выталкивания верхнего целого в стеке")
#     print("[8] вывести стек на экран")
#     print("[0] выход")
#
#     choise = int(input("> ").strip())
#     if choise == 0: break
#
#     if choise == 1:
#         num = int(input("Введите новое число> "))
#         stack.push(num)
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


# Task 4 (Неограниченный стек)
# Реализация такая же, как в Task 3, только в конструкторе класса Stack мы убираем параметр maxsize