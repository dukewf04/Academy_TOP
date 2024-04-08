# Task 1 (Очередь)
# class Queue:
#     def __init__(self, maxsize: int = 20):
#         self.__queue = []
#         self.__maxsize = maxsize
#     def IsEmpty(self):
#         return len(self.__queue) == 0
#
#     def IsFull(self):
#         return len(self.__queue) == self.__maxsize
#
#     def Enqueue(self, var):
#         if len(self.__queue) < self.__maxsize:
#             self.__queue.append(var)
#         else:
#             print("Очередь полная!")
#
#     def Dequeue(self):
#         if len(self.__queue) > 0:
#             return self.__queue.pop(0)
#         else:
#             print("В очереди нет элементов!")
#
#     def Show(self):
#         return self.__queue
#
# queue = Queue(maxsize=20)
#
# while True:
#     print("[1] помещение элемента в очередь")
#     print("[2] удаление элемента из очереди")
#     print("[3] проверка очереди на пустоту")
#     print("[4] проверка очереди на заполнение")
#     print("[5] вывести очередь на экран")
#     print("[0] выход")
#
#     try:
#         choise = int(input("> ").strip())
#         if choise not in [i for i in range(0, 6)]:
#             raise Exception
#     except:
#         print("Выберите корректный номер из списка!")
#         continue
#
#     if choise == 0: break
#
#     if choise == 1:
#         queue.Enqueue(input("Введите символ> "))
#         print(queue.Show())
#     elif choise == 2:
#         queue.Dequeue()
#         print("Первый элемент из очереди удален")
#     elif choise == 3:
#         print("Очередь пустая") if queue.IsEmpty() else print("Очередь не пустая")
#     elif choise == 4:
#         print("Очередь полная") if queue.IsFull() else print("Очередь не полная")
#     elif choise == 5:
#         print(queue.Show())
#     print("*"*30)


# Task 2 (Очередь с приоритетами. Приоритет определяется длинной строки.)
# class Queue:
#     def __init__(self, maxsize: int = 20):
#         self.__queue = []
#         self.__maxsize = maxsize
#     def IsEmpty(self):
#         return len(self.__queue) == 0
#
#     def IsFull(self):
#         return len(self.__queue) == self.__maxsize
#
#     def InsertWithPriority(self, var):
#         if len(self.__queue) < self.__maxsize:
#             self.__queue.append(var)
#         else:
#             print("Очередь полная!")
#
#     def GetMaxPriority(self):
#         index = 0
#         max_len = 0
#         for i in range(len(self.__queue)):
#             if len(self.__queue[i]) > max_len:
#                 max_len = len(self.__queue[i])
#                 index = i
#         return index
#
#     def PullHighestPriorityElement(self):
#         if len(self.__queue) > 0:
#             index = self.GetMaxPriority()
#             print("INDEX", index)
#             print("Элемент с наивысшим приоритетом из очереди удален")
#         else:
#             print("В очереди нет элементов!")
#
#     def Peek(self):
#         if len(self.__queue) > 0:
#             index = self.GetMaxPriority()
#
#             return f"{self.__queue[index]}, приоритет - {len(self.__queue[index])}"
#         else:
#             return "В очереди нет элементов!"
#
#     def Show(self):
#         for el in self.__queue:
#             print(f"{el}, приоритет - {len(el)}")
#
#
# queue = Queue(maxsize=20)
#
# while True:
#     print("[1] помещение элемента в очередь")
#     print("[2] удаление элемента с наивысшим приоритетом из очереди")
#     print("[3] проверка очереди на пустоту")
#     print("[4] проверка очереди на заполнение")
#     print("[5] возврат самого большого по приоритету элемента без удаления")
#     print("[6] вывести очередь на экран")
#     print("[0] выход")
#
#     try:
#         choise = int(input("> ").strip())
#         if choise not in [i for i in range(0, 7)]:
#             raise Exception
#     except:
#         print("Выберите корректный номер из списка!")
#         continue
#
#     if choise == 0: break
#
#     if choise == 1:
#         queue.InsertWithPriority(input("Введите символ> "))
#         queue.Show()
#     elif choise == 2:
#         queue.PullHighestPriorityElement()
#     elif choise == 3:
#         print("Очередь пустая") if queue.IsEmpty() else print("Очередь не пустая")
#     elif choise == 4:
#         print("Очередь полная") if queue.IsFull() else print("Очередь не полная")
#     elif choise == 5:
#         print(queue.Peek())
#     elif choise == 6:
#         queue.Show()
#     print("*"*30)


# Task 3 (Логины и пароли)
# class UserData:
#     def __init__(self):
#         self.data = {}
#
#     def addUser(self, name: str, login: str, password: str):
#         if name not in self.data.keys():
#             self.data[name] = {
#                 "login": login,
#                 "password": password
#             }
#         else:
#             print("Пользователь с таким именем уже существует!")
#
#     def removeUser(self, name):
#         if name in self.data.keys():
#             del self.data[name]
#             print("Пользователь удален")
#         else:
#             print("Пользователя с таким именем не существует!")
#
#     def isUser(self, name):
#         return True if name in self.data.keys() else False
#
#     def changeLogin(self, name, login):
#         if name in self.data.keys():
#             self.data[name]["login"] = login
#             print(f"Логин пользователя {name} изменен")
#         else:
#             print("Пользователя с таким именем не существует")
#
#     def changePassword(self, name, password):
#         if name in self.data.keys():
#             self.data[name]["password"] = password
#             print(f"Пароль пользователя {name} изменен")
#         else:
#             print("Пользователя с таким именем не существует")
#
#     def show(self):
#         for i, el in enumerate(self.data.items()):
#             print(f"[{i+1}] {el[0]}\n\tЛогин: {el[1]['login']}\n\tПароль: {el[1]['password']}")
#
# userdata = UserData()
#
# while True:
#     print("[1] Добавить нового пользователя")
#     print("[2] Удалить существующего пользователя")
#     print("[3] Проверить существует ли пользователь")
#     print("[4] Изменить логин существующего пользователя")
#     print("[5] Изменить пароль существующего пользователя")
#     print("[6] Вывести всех пользователей на экран")
#     print("[0] выход")
#
#     try:
#         choise = int(input("> ").strip())
#         if choise not in [i for i in range(0, 7)]:
#             raise Exception
#     except:
#         print("Выберите корректный номер из списка!")
#         continue
#     if choise == 0: break
#
#     if choise == 1:
#         userdata.addUser(
#             name=input("Введите имя пользователя> "),
#             login=input("Введите логин> "),
#             password=input("Введите пароль> ")
#         )
#
#     elif choise == 2:
#         userdata.removeUser(name=input("Введите имя пользователя, которого нужно удалить> "))
#     elif choise == 3:
#         if userdata.isUser(name=input("Введите имя пользователя> ")):
#             print("Пользователь с таким именем существует")
#         else:
#             print("Пользователя с таким именем не существует")
#     elif choise == 4:
#         name = input("Введите имя пользователя> ")
#         if userdata.isUser(name=name):
#             login = input("Введите новый логин> ")
#             userdata.changeLogin(name=name, login=login)
#         else:
#             print("Пользователя с таким именем не существует!")
#     elif choise == 5:
#         name = input("Введите имя пользователя> ")
#         if userdata.isUser(name=name):
#             password = input("Введите новый пароль> ")
#             userdata.changePassword(name=name, password=password)
#         else:
#             print("Пользователя с таким именем не существует!")
#     elif choise == 6:
#         userdata.show()
#     print("*"*30)